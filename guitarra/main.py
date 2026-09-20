from config import (
    FS,
    DURACION,
    VIBRATO,
    RASGUEO,
    VELOCIDAD_RASGUEO,
    TipoEnvolvente
)

from sintetizador import generar_acorde

from envolventes import aplicar_envolvente

from reproductor import reproducir

from acordes import ACORDES


audio = generar_acorde(
    ACORDES["C"],
    vibrato=VIBRATO,
    rasgueo=RASGUEO,
    velocidad_rasgueo=VELOCIDAD_RASGUEO
)

audio = aplicar_envolvente(
    audio,
    TipoEnvolvente.GUITARRA,
    DURACION,
    FS
)

reproducir(audio, FS)

######################

audio = generar_acorde(
    ACORDES["Am"],
    vibrato=VIBRATO,
    rasgueo=RASGUEO,
    velocidad_rasgueo=VELOCIDAD_RASGUEO
)

audio = aplicar_envolvente(
    audio,
    TipoEnvolvente.GUITARRA,
    DURACION,
    FS
)

reproducir(audio, FS)