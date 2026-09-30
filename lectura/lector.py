from dataclasses import dataclass
from guitarra.rasgueos import TipoRasgueo

@dataclass
class AcordeCancion:
    nombre: str
    tiempos: int
    rasgueo: TipoRasgueo
    patron: list[TipoRasgueo]


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

            rasgueo = TipoRasgueo.DOWN
            patron = []

            if len(partes) > 2:

                if partes[2].lower() in ("down", "up"):

                    try:
                        rasgueo = TipoRasgueo(
                            partes[2].lower()
                        )

                    except ValueError:
                        raise ValueError(
                            f"Tipo de rasgueo desconocido: {partes[2]}"
                        )

                else:

                    for golpe in partes[2:]:
                        print("golpe leído:", golpe)

                        if golpe.upper() == "D":

                            patron.append(
                                TipoRasgueo.DOWN
                            )

                        elif golpe.upper() == "U":

                            patron.append(
                                TipoRasgueo.UP
                            )

                        else:

                            raise ValueError(
                                f"Golpe de rasgueo desconocido: {golpe}"
                            )

            acordes.append(
                AcordeCancion(
                    nombre,
                    tiempos,
                    rasgueo,
                    patron
                )
            )

    return Cancion(
        tempo_bpm=tempo_bpm,
        acordes=acordes
    )