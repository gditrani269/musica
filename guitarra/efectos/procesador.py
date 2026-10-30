import numpy as np

from guitarra.efectos.distorsion import aplicar_distorsion


def aplicar_efectos(
    senal: np.ndarray,
    efectos
) -> np.ndarray:

    audio = senal.copy()

    if efectos.distorsion > 0:

        audio = aplicar_distorsion(
            audio,
            ganancia=efectos.distorsion
        )

    return audio