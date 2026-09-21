FS = 44100

DURACION = 3

VIBRATO = False

#TIPO_ENVOLVENTE = "adsr"
from enum import Enum

class TipoEnvolvente(Enum):

    ADSR = 1

    GUITARRA = 2

RASGUEO = "down"

VELOCIDAD_RASGUEO = 15