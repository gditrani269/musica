from dataclasses import dataclass
from config import TipoRasgueo

@dataclass
class AcordeCancion:
    nombre: str
    tiempos: int
    rasgueo: TipoRasgueo


@dataclass
class Cancion:
    tempo_bpm: int
    acordes: list[AcordeCancion]


def leer_cancion(archivo):

    tempo_bpm = 120          # valor por defecto
    acordes = []

    with open(archivo, "r", encoding="utf-8") as f:

        for linea in f:

            linea = linea.strip()

            # Ignorar líneas vacías
            if not linea:
                continue

            # Ignorar comentarios
            if linea.startswith("#"):
                continue

            # Leer el tempo_bpm
            if linea.upper().startswith("TEMPO="):

                tempo_bpm = int(
                    linea.split("=")[1].strip()
                )

                continue

            partes = linea.split()

            nombre = partes[0]

            if len(partes) > 1:
                tiempos = int(partes[1])
            else:
                tiempos = 4

            if len(partes) > 2:
                try:
                    rasgueo = TipoRasgueo(partes[2].lower())
                except ValueError:
                    raise ValueError(
                        f"Tipo de rasgueo desconocido: {partes[2]}"
                    )
            else:
                rasgueo = TipoRasgueo.DOWN

            acordes.append(
                AcordeCancion(
                    nombre,
                    tiempos,
                    rasgueo
                )
            )

    return Cancion(
        tempo_bpm=tempo_bpm,
        acordes=acordes
    )