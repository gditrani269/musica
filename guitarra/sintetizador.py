import numpy as np
from config import FS, TipoEnvolvente
from guitarra.rasgueos import TipoRasgueo
from .notas import NOTAS

from guitarra.evento import EventoMusical
from guitarra.tecnicas import TipoTecnica
from guitarra.envolventes import aplicar_envolvente
from config import FS, VELOCIDAD_RASGUEO

# ============================================
# Generador de una nota
# ============================================

def generar_nota(frecuencia, t, vibrato=False):

    if vibrato:
        mod = 0.003 * np.sin(2*np.pi*5*t)
        f = frecuencia * (1 + mod)
    else:
        f = frecuencia

    nota = (
        1.00 * np.sin(2*np.pi*1*f*t) +
        0.50 * np.sin(2*np.pi*2*f*t) +
        0.30 * np.sin(2*np.pi*3*f*t) +
        0.20 * np.sin(2*np.pi*4*f*t) +
        0.10 * np.sin(2*np.pi*5*f*t)
    )

    return nota

# ============================================
# Generar un acorde basico
# ============================================
def generar_acorde(
    lista_notas,
    vibrato=False,
    rasgueo=TipoRasgueo.DOWN,
    patron=None,
    velocidad_rasgueo=VELOCIDAD_RASGUEO,
    duracion=2.0
):

    if not patron:
        patron = [rasgueo]

    return _generar_patron(
        lista_notas,
        patron,
        vibrato=vibrato,
        velocidad_rasgueo=velocidad_rasgueo,
        duracion=duracion
    )

# ============================================
# Generar un acorde basico
# ============================================

def _generar_rasgueo(lista_notas,
                   vibrato=False,
                   rasgueo=TipoRasgueo.DOWN,
                   velocidad_rasgueo=VELOCIDAD_RASGUEO,
                   duracion=2.0):
    t = np.linspace(
        0,
        duracion,
        int(FS*duracion),
        endpoint=False
    )
    acorde = np.zeros_like(t)
    delay = int(velocidad_rasgueo * FS / 1000)
    # Dirección del rasgueo
    if rasgueo == TipoRasgueo.UP:
        notas = list(reversed(lista_notas))
    else:
        notas = lista_notas
    for i, nombre_nota in enumerate(notas):
        frecuencia = NOTAS[nombre_nota]
        nota = generar_nota(
            frecuencia,
            t,
            vibrato
        )
        volumen = 1.0 - (i * 0.15)
        inicio = i * delay
        if inicio >= len(acorde):
            break
        acorde[inicio:] += volumen * nota[:len(acorde)-inicio]
    acorde /= np.max(np.abs(acorde))
    return acorde

def _generar_punteo(
    lista_notas,
    vibrato=False,
    duracion=2.0
):

    t = np.linspace(
        0,
        duracion,
        int(FS * duracion),
        endpoint=False
    )

    frecuencia = NOTAS[lista_notas[0]]

    nota = generar_nota(
        frecuencia,
        t,
        vibrato
    )

    nota = aplicar_envolvente(
        nota,
        TipoEnvolvente.GUITARRA,
        duracion,
        FS
    )

    return nota

def _generar_patron(
    lista_notas,
    patron,
    vibrato=False,
    velocidad_rasgueo=VELOCIDAD_RASGUEO,
    duracion=2.0
):

    audio = []

    if not patron:

        return np.array([])

    duracion_paso = duracion / len(patron)

    for accion in patron:

        if accion in (TipoRasgueo.DOWN, TipoRasgueo.UP):

            segmento = _generar_rasgueo(
                lista_notas,
                vibrato=vibrato,
                rasgueo=accion,
                velocidad_rasgueo=velocidad_rasgueo,
                duracion=duracion_paso
            )

            audio.append(segmento)


    return np.concatenate(audio)

def reproducir_evento(evento: EventoMusical, tempo_bpm):

    if evento.tecnica == TipoTecnica.RASGUEO:

        return generar_acorde(
            lista_notas=evento.notas,
            vibrato=evento.vibrato,
            patron=evento.patron,
            velocidad_rasgueo=evento.velocidad_rasgueo,
            duracion=evento.tiempos * (60 / tempo_bpm)
        )

    elif evento.tecnica == TipoTecnica.PUNTEO:

        duracion = evento.tiempos * (60 / tempo_bpm)

        return _generar_punteo(
            lista_notas=evento.notas,
            vibrato=evento.vibrato,
            duracion=duracion
        )

    elif evento.tecnica == TipoTecnica.SILENCIO:

        duracion = evento.tiempos * (60 / tempo_bpm)

        return np.zeros(
            int(FS * duracion)
        )

    raise NotImplementedError(
        f"Técnica no soportada: {evento.tecnica}"
    )