import numpy as np


def aplicar_distorsion(
    senal: np.ndarray,
    ganancia: float = 3.0
) -> np.ndarray:

    senal_distorsionada = np.tanh(
        ganancia * senal
    )

    return senal_distorsionada