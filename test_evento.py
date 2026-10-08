import numpy as np

from lectura.lector import leer_eventos
from guitarra.sintetizador import reproducir_evento
from audio.reproductor import reproducir
from config import FS
from guitarra.evento import EventoMusical
from guitarra.tecnicas import TipoTecnica
from guitarra.instrumentos import TipoGuitarra


eventos, tempo_bpm = leer_eventos(
    "canciones/prueba2.txt"
)


audio_total = np.array([])


for evento in eventos:

    print(evento)
    print("Velocidad:", evento.velocidad_rasgueo)
    print(evento.instrumento)

    audio = reproducir_evento(
        evento,
        tempo_bpm
    )

    audio_total = np.concatenate(
        (audio_total, audio)
    )


reproducir(audio_total, FS)
"""
evento_acustica = EventoMusical(
    notas=["A3"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=2,
    instrumento=TipoGuitarra.ACUSTICA
)

evento_electrica = EventoMusical(
    notas=["A3"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=2,
    instrumento=TipoGuitarra.ELECTRICA_LIMPIA
)

print("Generando audio acústico...")
audio_acustica = reproducir_evento(
    evento_acustica,
    tempo_bpm
)
print("Audio acústico:", len(audio_acustica), "muestras")

print("Generando audio eléctrico...")
audio_electrica = reproducir_evento(
    evento_electrica,
    tempo_bpm
)
print("Audio eléctrico:", len(audio_electrica), "muestras")

print("Reproduciendo acústica...")
reproducir(audio_acustica, FS)

print("Reproduciendo eléctrica...")
reproducir(audio_electrica, FS)

print("Fin de la prueba")
"""