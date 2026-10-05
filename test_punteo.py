from config import FS
from guitarra.acordes import ACORDES
from guitarra.evento import EventoMusical
from guitarra.tecnicas import TipoTecnica
from guitarra.sintetizador import reproducir_evento
from audio.reproductor import reproducir


evento = EventoMusical(
    notas=ACORDES["A"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)

evento = EventoMusical(
    notas=ACORDES["G"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)

evento = EventoMusical(
    notas=ACORDES["A"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)

evento = EventoMusical(
    notas=ACORDES["G"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)

evento = EventoMusical(
    notas=ACORDES["G"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)

evento = EventoMusical(
    notas=ACORDES["F"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)

evento = EventoMusical(
    notas=ACORDES["E"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)

evento = EventoMusical(
    notas=ACORDES["E2"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)

evento = EventoMusical(
    notas=ACORDES["G2"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)

evento = EventoMusical(
    notas=ACORDES["A2"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)

evento = EventoMusical(
    notas=ACORDES["C"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)

evento = EventoMusical(
    notas=ACORDES["A2"],
    tecnica=TipoTecnica.PUNTEO,
    tiempos=1
)

audio = reproducir_evento(
    evento,
    180
)

reproducir(audio, FS)