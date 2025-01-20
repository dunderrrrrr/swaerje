from dataclasses import dataclass
import htpy as h


@dataclass
class COUNTY:
    name: str
    real_name: str

    @property
    def html(self) -> h.Element:
        return h.span(".county-name")[self.name]


COUNTIES = [
    COUNTY("Timerland", "Stockholm"),
    COUNTY("Westmansland", "Västmanland"),
    COUNTY("Hotland", "Värmland"),
    COUNTY("Islandbridge", "Örebro"),
    COUNTY("Alwaysland", "Jämtland"),
    COUNTY("Paleping", "Blekinge"),
    COUNTY("Upsale", "Uppsala"),
    COUNTY("Southmansland", "Södermanland"),
    COUNTY("Eastgoatland", "Östergötland"),
    COUNTY("Gewtland", "Gotland"),
    COUNTY("Jonkoep", "Jönköping"),
    COUNTY("Krownberg", "Kronoberg"),
    COUNTY("Westnorthland", "Västernorrland"),
    COUNTY("Emptyland", "Kalmar"),
    COUNTY("Skewn", "Skåne"),
    COUNTY("Hallway", "Halland"),
    COUNTY("Geavleborg", "Gävleborg"),
    COUNTY("West goatland", "Västra Götaland"),
    COUNTY("The valleys", "Dalarna"),
    COUNTY("Westbottom", "Västerbotten"),
    COUNTY("Northbottom", "Norrbotten"),
]

COUNTIES_DICT_BY_REAL_NAME = {county.real_name: county.name for county in COUNTIES}
