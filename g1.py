import numpy as np
import sounddevice as sd

fs = 44100
duracion = 3

t = np.linspace(0, duracion, int(fs*duracion), endpoint=False)

frecuencias = [
    261.63,
    329.63,
    392.00
]

onda = np.zeros_like(t)

for f in frecuencias:
    onda += np.sin(2*np.pi*f*t)

onda /= np.max(np.abs(onda))

sd.play(onda, fs)
sd.wait()