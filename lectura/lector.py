from dataclasses import dataclass

@dataclass
class AcordeCancion:
    nombre: str
    tiempos: int

def leer_cancion(archivo):
    acordes = []
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            # Ignorar líneas vacías y comentarios
            if not linea or linea.startswith("#"):
                continue
            partes = linea.split()
            nombre = partes[0]
            if len(partes) > 1:
                tiempos = int(partes[1])
            else:
                tiempos = 4   # valor por defecto
            acordes.append(
                AcordeCancion(
                    nombre,
                    tiempos
                )
            )
    return acordes