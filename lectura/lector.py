from dataclasses import dataclass
from guitarra.rasgueos import TipoRasgueo
from guitarra.evento import EventoMusical
from guitarra.tecnicas import TipoTecnica
from guitarra.acordes import ACORDES
from guitarra.tipos_evento import TipoEvento
from guitarra.instrumentos import TipoGuitarra

@dataclass
class AcordeCancion:
    tipo: TipoEvento
    nombre: str
    tiempos: int
    rasgueo: TipoRasgueo
    patron: list[TipoRasgueo]
    instrumento: TipoGuitarra = TipoGuitarra.ACUSTICA


@dataclass
class Cancion:
    tempo_bpm: int
    acordes: list[AcordeCancion]


def leer_cancion(archivo):

    tempo_bpm = 120          # valor por defecto
    acordes = []
    instrumento_actual = TipoGuitarra.ACUSTICA

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
            
            if linea.upper().startswith("G="):

                nombre_instrumento = linea.split("=", 1)[1].strip().upper()

                try:
                    instrumento_actual = TipoGuitarra[nombre_instrumento]
                except KeyError:
                    raise ValueError(
                        f"Instrumento desconocido: {nombre_instrumento}"
                    )

                continue

            partes = linea.split()

            #---------------------------------
            # Compatibilidad con el formato nuevo
            if partes[0] == "A":
                tipo = TipoEvento.ACORDE
                partes = partes[1:]

            elif partes[0] == "P":
                tipo = TipoEvento.PUNTEO
                partes = partes[1:]

            # Compatibilidad con el formato viejo
            else:

                tipo = TipoEvento.ACORDE
            #---------------------------------
            
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
                    tipo,
                    nombre,
                    tiempos,
                    rasgueo,
                    patron,
                    instrumento_actual
                )
            )

    return Cancion(
        tempo_bpm=tempo_bpm,
        acordes=acordes
    )

def crear_eventos(cancion):

    eventos = []

    for acorde in cancion.acordes:

        if acorde.nombre == "-":

            evento = EventoMusical(
                notas=[],
                tecnica=TipoTecnica.SILENCIO,
                tiempos=acorde.tiempos,
                patron=[],
                instrumento=acorde.instrumento
            )

            eventos.append(evento)

            continue

        if acorde.tipo == TipoEvento.ACORDE:

            notas = ACORDES[acorde.nombre]
            tecnica = TipoTecnica.RASGUEO

        elif acorde.tipo == TipoEvento.PUNTEO:

            notas = [acorde.nombre]
            tecnica = TipoTecnica.PUNTEO


        evento = EventoMusical(
            notas=notas,
            tecnica=tecnica,
            tiempos=acorde.tiempos,
            patron=acorde.patron,
            instrumento=acorde.instrumento
        )

        eventos.append(evento)

    return eventos

def leer_eventos(archivo):

    cancion = leer_cancion(archivo)

    eventos = crear_eventos(cancion)

    return eventos, cancion.tempo_bpm