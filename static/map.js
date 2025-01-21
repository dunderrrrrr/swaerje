var map = L.map('map').setView([63, 15], 6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

fetch('https://raw.githubusercontent.com/dunderrrrrr/sweden-counties/refs/heads/main/sweden-counties.geojson')
    .then(response => response.json())
    .then(data => {
        L.geoJSON(data, {
            style: function (feature) {
                return {
                    color: '#000',
                    weight: 2,
                    fillColor: '#30f',
                    fillOpacity: 0.0
                };
            },
            onEachFeature: function (feature, layer) {
                layer.on('mouseover', function () {
                    layer.setStyle({ fillColor: 'yellow', fillOpacity: 0.8 });
                });
                layer.on('mouseout', function () {
                    layer.setStyle({  fillOpacity: 0.0 });
                });
                layer.bindTooltip(feature.properties.name);

                layer.on('click', function () {
                    htmx.ajax("POST", "/target/verify", {
                        target: '.notifier',
                        swap: 'innerHTML',
                        headers: { 'Content-Type': 'application/json' },
                        values: {
                            "data": JSON.stringify(
                                {
                                    "selected_county": feature.properties.name,
                                    "current_target": document.querySelector(".county-name").innerHTML
                                }
                            )
                        }
                    });
                });
            }
        }).addTo(map);
    });
