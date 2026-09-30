from dataclasses import dataclass, field

from guitarra.tecnicas import TipoTecnica
from guitarra.rasgueos import TipoRasgueo


@dataclass
class EventoMusical:
    """
    Representa un evento musical.

    Un evento musical es un conjunto de notas más la técnica
    con la que deben interpretarse.
    """

    notas: list[str]

    tecnica: TipoTecnica

    duracion: float

    patron: list[TipoRasgueo] = field(default_factory=list)

    vibrato: bool = False

    velocidad_rasgueo: int = 15