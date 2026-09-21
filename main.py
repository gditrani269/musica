from config import (
    FS,
    DURACION,
    VIBRATO,
    RASGUEO,
    VELOCIDAD_RASGUEO,
    TipoEnvolvente
)
from guitarra.sintetizador import generar_acorde
from guitarra.envolventes import aplicar_envolvente
from audio.reproductor import reproducir
from guitarra.acordes import ACORDES
from lectura.lector import leer_cancion

cancion = leer_cancion(
    "canciones/prueba.txt"
)
"""
for acorde in cancion:

    print(
        acorde.nombre,
        acorde.tiempos
    )
"""
for acorde in cancion:
    notas = ACORDES[acorde.nombre]
    audio = generar_acorde(
        notas,
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
    reproducir(
        audio,
        FS
    )