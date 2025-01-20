import json
import random
import htpy as h
from flask import Flask, url_for, Response, request
import urllib
from constants import COUNTIES, COUNTIES_DICT_BY_REAL_NAME

app = Flask(
    __name__,
    static_url_path="",
    static_folder="static",
)


def _parse_data(data) -> str:
    decoded_data = urllib.parse.unquote(request.data.decode())
    parsed_data = urllib.parse.parse_qs(decoded_data)
    return json.loads(parsed_data["data"][0])


@app.route("/target")
def target():
    random_county = random.choice(COUNTIES)
    return Response(random_county.html)


@app.route("/target/verify", methods=["POST"])
def verify_target():
    data = _parse_data(request.data)

    selected_county = data["selected_county"]
    current_target = data["current_target"]
    selected_target = COUNTIES_DICT_BY_REAL_NAME[selected_county]

    if selected_target != current_target:
        return Response(
            h.span({"x-init": f'$.notify("{selected_county} är fel!", "error")'}),
        )

    return Response(
        h.span({"x-init": f'$.notify("{selected_county} är rätt!", "success")'}),
        headers={"HX-Trigger": "setNewTarget"},
    )


@app.route("/")
def index():
    return Response(
        h.html(lang="en")[
            h.head[
                h.meta(charset="UTF-8"),
                h.meta(
                    name="viewport", content="width=device-width, initial-scale=1.0"
                ),
                h.title["🇸🇪 Swärje 🇸🇪 "],
                h.link(
                    rel="stylesheet", href="https://unpkg.com/leaflet/dist/leaflet.css"
                ),
                h.link(rel="stylesheet", href=url_for("static", filename="styles.css")),
                h.script(src="https://unpkg.com/htmx.org@2.0.4"),
                h.script(
                    src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.js"
                ),
                h.script(src="https://unpkg.com/alpinejs", defer=""),
                h.script(src=url_for("static", filename="notify.js")),
            ],
            h.body[
                h.h1[
                    "Klicka på: ",
                    h.span(
                        hx_get=url_for("target"),
                        hx_trigger="load, setNewTarget from:body",
                    ),
                ],
                h.span(".result"),
                h.div("#map"),
                h.script(src="https://unpkg.com/leaflet/dist/leaflet.js"),
                h.script(src=url_for("static", filename="map.js")),
            ],
        ]
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
