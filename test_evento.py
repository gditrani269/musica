import numpy as np

from lectura.lector import leer_eventos
from guitarra.sintetizador import reproducir_evento
from audio.reproductor import reproducir
from config import FS


eventos, tempo_bpm = leer_eventos(
    "canciones/prueba2.txt"
)


audio_total = np.array([])


for evento in eventos:

    print(evento)

    audio = reproducir_evento(
        evento,
        tempo_bpm
    )

    audio_total = np.concatenate(
        (audio_total, audio)
    )


reproducir(audio_total, FS)