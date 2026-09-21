from config import (
    FS,
    DURACION,
    SEGUNDOS_POR_TIEMPO,
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
    if acorde.nombre not in ACORDES:
        print(
            f"Acorde desconocido: {acorde.nombre}"
        )
        continue
    notas = ACORDES[acorde.nombre]
    duracion = acorde.tiempos * SEGUNDOS_POR_TIEMPO
    audio = generar_acorde(
        notas,
        vibrato=VIBRATO,
        rasgueo=RASGUEO,
        velocidad_rasgueo=VELOCIDAD_RASGUEO,
        duracion=duracion
    )
    audio = aplicar_envolvente(
        audio,
        TipoEnvolvente.GUITARRA,
        duracion,
        FS
    )
    reproducir(
        audio,
        FS
    )