#crear_adsr()
#crear_envolvente_guitarra()
#aplicar_envolvente()
import numpy as np
from config import TipoEnvolvente

def crear_adsr(
        duracion,
        fs,
        ataque=0.02,
        decay=0.15,
        sustain=0.60,
        release=0.30):

    n = int(duracion * fs)

    envolvente = np.zeros(n)

    na = int(ataque * fs)
    nd = int(decay * fs)
    nr = int(release * fs)

    ns = n - na - nd - nr

    # Attack
    envolvente[:na] = np.linspace(
        0,
        1,
        na,
        endpoint=False
    )

    # Decay
    envolvente[na:na+nd] = np.linspace(
        1,
        sustain,
        nd,
        endpoint=False
    )

    # Sustain
    envolvente[na+nd:na+nd+ns] = sustain

    # Release
    envolvente[na+nd+ns:] = np.linspace(
        sustain,
        0,
        nr
    )

    return envolvente

def crear_envolvente_guitarra(
        duracion,
        fs):

    n = int(duracion * fs)

    t = np.linspace(
        0,
        duracion,
        n
    )

    ataque = 1 - np.exp(-80*t)
    decay = np.exp(-2*t)
    env = ataque * decay
    env /= np.max(env)

    return env

def aplicar_envolvente(audio, tipo, duracion, fs):

    if tipo == TipoEnvolvente.ADSR:

        env = crear_adsr(
            duracion,
            fs
        )

    elif tipo == TipoEnvolvente.GUITARRA:

        env = crear_envolvente_guitarra(
            duracion,
            fs
        )

    else:

        raise ValueError(
            f"Tipo de envolvente desconocido: {tipo}"
        )

    return audio * env