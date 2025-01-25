from flask import url_for
import htpy as h


def header_html() -> h.Element:
    return h.head[
        h.meta(charset="UTF-8"),
        h.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        h.title["🇸🇪 Swärje 🇸🇪 "],
        h.link(rel="stylesheet", href="https://unpkg.com/leaflet/dist/leaflet.css"),
        h.link(rel="stylesheet", href=url_for("static", filename="styles.css")),
        h.link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.19.1/cdn/themes/light.css",
        ),
        h.script(
            src="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.19.1/cdn/shoelace-autoloader.js",
            type="module",
        ),
        h.script(src="https://unpkg.com/htmx.org@2.0.4"),
        h.script(src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.js"),
        h.script(src="https://unpkg.com/alpinejs", defer=""),
        h.script(src=url_for("static", filename="notify.js")),
    ]


def calc_ratio() -> h.Element:
    return h.span(
        x_text="statCorrect > 0 ? `${(statCorrect / statTries * 100).toFixed(0)}%`: '0%'"
    )


def finished_dialog_html() -> h.Element:
    return h.sl_dialog(".finished-dialog", no_header="", open="")[
        "Statistik",
        h.ul(".stats-ul")[
            h.li[calc_ratio(), " rätt!"],
            h.li["Antal rätt: ", h.span(x_text="statCorrect")],
            h.li["Antal fel: ", h.span(x_text="statWrong")],
        ],
        h.sl_button(
            {"@click": "window.location.reload()"}, slot="footer", variant="primary"
        )["Börja om"],
    ]
