import sounddevice as sd

def reproducir(audio, fs):

    sd.play(audio, fs)
    sd.wait()