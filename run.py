import json
import random
import htpy as h
from flask import Flask, url_for, Response, request
import urllib
from components import (
    ratio_html,
    finished_dialog_html,
    header_html,
    statistics_html,
    timer_html,
)
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


@app.route("/target")
def target():
    random_county = random.choice(COUNTIES)
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

    return Response(
        h.span(
            {
                "x-init": f'$.notify("{selected_county} är rätt!", "success");'
                "statCorrect++;"
                "statTries++"
            }
        ),
        headers={"HX-Trigger": "setNewTarget"},
    )


@app.route("/")
def index():
    return Response(
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
                    h.h2[
                        "Klicka på: ",
                        h.span(
                            hx_get=url_for("target"),
                            hx_trigger="load, setNewTarget from:body",
                        ),
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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
