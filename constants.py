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
    COUNTY("Log Islet County", "Stockholm"),
    COUNTY("Wheeze Man's County", "Västmanland"),
    COUNTY("Hot County", "Värmland"),
    COUNTY("Penny Bridge County", "Örebro"),
    COUNTY("Always County", "Jämtland"),
    COUNTY("Pale County", "Blekinge"),
    COUNTY("Up Said Put County", "Uppsala"),
    COUNTY("Sir M's County", "Södermanland"),
    COUNTY("Eastern Goat County", "Östergötland"),
    COUNTY("Tasty County", "Gotland"),
    COUNTY("J Island Buy County", "Jönköping"),
    COUNTY("Crown o' Mountain County", "Kronoberg"),
    COUNTY("West Northern Land County", "Västernorrland"),
    COUNTY("Cold Sea County", "Kalmar"),
    COUNTY("Scoon County", "Skåne"),
    COUNTY("Entrance County", "Halland"),
    COUNTY("Buck Castle County", "Gävleborg"),
    COUNTY("Western Goat County", "Västra Götaland"),
    COUNTY("Valley County", "Dalarna"),
    COUNTY("Western Bottom County", "Västerbotten"),
    COUNTY("Northern Bottom County", "Norrbotten"),
]

COUNTIES_DICT_BY_REAL_NAME = {county.real_name: county.name for county in COUNTIES}
