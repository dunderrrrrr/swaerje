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
    COUNTY("Log Islet County", "Stockholms län"),
    COUNTY("Wheeze Man's County", "Västmanlands län"),
    COUNTY("Hot County", "Värmlands län"),
    COUNTY("Penny Bridge County", "Örebro län"),
    COUNTY("Always County", "Jämtlands län"),
    COUNTY("Pale County", "Blekinge län"),
    COUNTY("Up Said Put County", "Uppsala län"),
    COUNTY("Sir M's County", "Södermanlands län"),
    COUNTY("Eastern Goat County", "Östergötlands län"),
    COUNTY("Tasty County", "Gotlands län"),
    COUNTY("J Island Buy County", "Jönköpings län"),
    COUNTY("Crown o' Mountain County", "Kronobergs län"),
    COUNTY("West Northern Land County", "Västernorrlands län"),
    COUNTY("Cold Sea County", "Kalmar län"),
    COUNTY("Scoon County", "Skåne län"),
    COUNTY("Entrance County", "Hallands län"),
    COUNTY("Buck Castle County", "Gävleborgs län"),
    COUNTY("Western Goat County", "Västra Götalands län"),
    COUNTY("Valley County", "Dalarnas län"),
    COUNTY("Western Bottom County", "Västerbottens län"),
    COUNTY("Northern Bottom County", "Norrbottens län"),
]

COUNTIES_DICT_BY_REAL_NAME = {county.real_name: county.name for county in COUNTIES}
