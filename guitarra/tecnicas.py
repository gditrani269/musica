# tecnicas.py

from enum import Enum


class TipoTecnica(Enum):
    """
    Técnicas disponibles para interpretar un conjunto de notas.
    """

    RASGUEO = "rasgueo"

    PUNTEO = "punteo"

    ARPEGIO = "arpegio"

    SILENCIO = "silencio"