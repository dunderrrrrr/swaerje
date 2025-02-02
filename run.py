import json
import random
import htpy as h
from flask import Flask, url_for, Response, request
import urllib
from components import finished_dialog_html, header_html, statistics_html
from constants import COUNTIES, COUNTIES_DICT_BY_REAL_NAME

app = Flask(
    __name__,
    static_url_path="",
    static_folder="static",
)


def _parse_data() -> str:
    decoded_data = urllib.parse.unquote(request.data.decode())
    parsed_data = urllib.parse.parse_qs(decoded_data)
    return json.loads(parsed_data["data"][0])


@app.route("/target", methods=["GET"])
def target():
    completed = request.cookies.getlist("completed")
    if not completed:
        random_county = random.choice(COUNTIES)
        return Response(random_county.html)

    completed = completed[0].split(",")
    while True:
        random_county = random.choice(COUNTIES)
        if random_county.name not in completed:
            return Response(random_county.html)


@app.route("/target/verify", methods=["POST"])
def verify_target():
    data = _parse_data()

    selected_county = data["selected_county"]
    current_target = data["current_target"]
    selected_target = COUNTIES_DICT_BY_REAL_NAME[selected_county]

    if selected_target != current_target:
        return Response(
            h.span(
                {
                    "x-init": f'$.notify("{selected_county} är fel!", "error");'
                    "statWrong++;"
                    "statTries++"
                }
            ),
        )

    response = Response(
        h.span(
            {
                "x-init": f'$.notify("{selected_county} är rätt!", "success");'
                "statCorrect++;"
                "statTries++"
            }
        ),
        headers={"HX-Trigger": "setNewTarget"},
    )

    existing_completed = request.cookies.getlist("completed")
    existing_completed.append(current_target)
    response.set_cookie("completed", ",".join(existing_completed))
    return response


@app.route("/")
def index():
    response = Response(
        h.html(lang="en")[
            header_html(),
            h.body(
                {
                    "x-init": "start = Date.now();stop = 0;interval = setInterval(() => { now = Date.now() }, 10)",
                    "@sl-request-close": "$event.preventDefault()",
                },
                x_data="""{
                    statTries: 0,
                    statWrong: 0,
                    statCorrect: 0,
                    statRatio: 0.00,
                    interval: 0,
                    now: 0,
                    start: 0,
                    stop: 0
                }""",
            )[
                h.header[
                    h.p(".click")["Klicka på rätt län på kartan!"],
                    h.h3[
                        h.span(
                            hx_get=url_for("target"),
                            hx_trigger="load, setNewTarget from:body",
                        )[h.span(".county-name")["Laddar..."]],
                    ],
                    statistics_html(),
                ],
            ],
            h.div("#map", x_show=f"statCorrect != {len(COUNTIES)}"),
            h.span(".notifier"),
            h.div(
                x_show=f"statCorrect == {len(COUNTIES)}",
                x_effect="if (%s) { clearInterval(interval);stop = Date.now();interval = 0;now = 0; }"
                % f"statCorrect == {len(COUNTIES)}",
            )[finished_dialog_html()],
            h.script(src="https://unpkg.com/leaflet/dist/leaflet.js"),
            h.script(src=url_for("static", filename="map.js")),
        ],
    )
    response.set_cookie("completed", "")
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
