#generar_nota()
#generar_acorde()

import numpy as np
from config import FS, DURACION, TipoEnvolvente
from .notas import NOTAS

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
                   velocidad_rasgueo=15):

    t = np.linspace(
        0,
        DURACION,
        int(FS*DURACION),
        endpoint=False
    )

    acorde = np.zeros_like(t)

    delay = int(velocidad_rasgueo * FS / 1000)

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