import json
import random
import htpy as h
from flask import Flask, url_for, Response, request
import urllib
from components import finished_dialog_html, header_html
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
                {"@sl-request-close": "$event.preventDefault()"},
                x_data="{statTries: 0, statWrong: 0, statCorrect: 0, statRatio: 0.00}",
            )[
                h.header[
                    h.h2[
                        "Klicka på: ",
                        h.span(
                            hx_get=url_for("target"),
                            hx_trigger="load, setNewTarget from:body",
                        ),
                    ],
                    h.div(".statistics")[
                        h.div[
                            f"Försök: ", h.span(x_text="statTries"), "/", len(COUNTIES)
                        ],
                        h.div["Rätt: ", h.span(x_text="statCorrect")],
                        h.div["Fel: ", h.span(x_text="statWrong")],
                        h.div[
                            "Ratio: ",
                            h.span(
                                x_text="statCorrect > 0 ? (statCorrect / statTries).toFixed(2): 0"
                            ),
                        ],
                    ],
                ],
            ],
            h.div("#map", x_show=f"statTries != {len(COUNTIES)}"),
            h.span(".notifier"),
            h.div(x_show=f"statTries == {len(COUNTIES)}")[finished_dialog_html(),],
            h.script(src="https://unpkg.com/leaflet/dist/leaflet.js"),
            h.script(src=url_for("static", filename="map.js")),
        ],
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
