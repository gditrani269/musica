import numpy as np

from config import (
    FS,
    #SEGUNDOS_POR_TIEMPO,
    VIBRATO,
    RASGUEO,
    VELOCIDAD_RASGUEO,
    TipoEnvolvente,
    SILENCIO
)
from guitarra.sintetizador import generar_acorde
from guitarra.envolventes import aplicar_envolvente
from audio.reproductor import reproducir
from guitarra.acordes import ACORDES
from lectura.lector import leer_cancion

cancion = leer_cancion(
    "canciones/prueba.txt"
)

duracion_tiempo = 60 / cancion.tempo_bpm

for acorde in cancion.acordes:
    duracion = acorde.tiempos * duracion_tiempo
    if acorde.nombre == "-":

    #    duracion = acorde.tiempos * duracion_tiempo

        silencio = np.zeros(
            int(FS * duracion)
        )

        reproducir(
            silencio,
            FS
        )

        continue
    if acorde.nombre not in ACORDES:
        print(
            f"Acorde desconocido: {acorde.nombre}"
        )
        continue
    notas = ACORDES[acorde.nombre]
#    duracion = acorde.tiempos * duracion_tiempo
    audio = generar_acorde(
        notas,
        vibrato=VIBRATO,
        rasgueo=acorde.rasgueo,
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