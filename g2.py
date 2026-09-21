import numpy as np
import sounddevice as sd

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

# ============================================
# Configuración
# ============================================

FS = 44100          # Frecuencia de muestreo
DURACION = 3        # segundos

# ============================================
# Frecuencias de las notas
# ============================================

NOTAS = {
    "C4":261.63,
    "C#4":277.18,
    "D4":293.66,
    "D#4":311.13,
    "E4":329.63,
    "F4":349.23,
    "F#4":369.99,
    "G4":392.00,
    "G#4":415.30,
    "A4":440.00,
    "A#4":466.16,
    "B4":493.88
}

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
# Generar un acorde
# ============================================

def generar_acorde(lista_notas,
                   vibrato=False,
                   rasgueo="down",
                   retardo_ms=15):

    t = np.linspace(
        0,
        DURACION,
        int(FS*DURACION),
        endpoint=False
    )

    acorde = np.zeros_like(t)

    delay = int(retardo_ms * FS / 1000)

    # Dirección del rasgueo
    if rasgueo == "up":
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

        inicio = i * delay

        acorde[inicio:] += nota[:len(acorde)-inicio]

    acorde /= np.max(np.abs(acorde))

    return acorde

# ============================================
# Programa principal
# ============================================

do_mayor = [
    "C4",
    "E4",
    "G4"
]

#audio = generar_acorde(do_mayor)
audio = generar_acorde(do_mayor, vibrato=False)

adsr = crear_adsr(
    DURACION,
    FS
)

audio *= adsr

sd.play(audio, FS)
sd.wait()


audio = generar_acorde(do_mayor, rasgueo="down")

audio *= crear_envolvente_guitarra(
    DURACION,
    FS
)

sd.play(audio, FS)
sd.wait()

audio = generar_acorde(do_mayor, rasgueo="up")

audio *= crear_envolvente_guitarra(
    DURACION,
    FS
)

sd.play(audio, FS)
sd.wait()
