from flask import url_for
import htpy as h


def header_html() -> h.Element:
    return h.head[
        h.meta(charset="UTF-8"),
        h.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        h.title["🇸🇪 Swärje 🇸🇪 "],
        h.link(rel="stylesheet", href="https://unpkg.com/leaflet/dist/leaflet.css"),
        h.link(rel="stylesheet", href=url_for("static", filename="styles.css")),
        h.script(src="https://unpkg.com/htmx.org@2.0.4"),
        h.script(src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.js"),
        h.script(src="https://unpkg.com/alpinejs", defer=""),
        h.script(src=url_for("static", filename="notify.js")),
    ]
