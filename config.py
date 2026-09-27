FS = 44100

#SEGUNDOS_POR_TIEMPO = 0.5
VIBRATO = False

#TIPO_ENVOLVENTE = "adsr"
from enum import Enum

class TipoEnvolvente(Enum):
    ADSR = 1
    GUITARRA = 2

class TipoRasgueo(Enum):
    DOWN = "down"
    UP = "up"

RASGUEO = TipoRasgueo.DOWN

VELOCIDAD_RASGUEO = 15

SILENCIO = "-"