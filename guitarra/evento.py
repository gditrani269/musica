from dataclasses import dataclass, field

from guitarra.tecnicas import TipoTecnica
from guitarra.rasgueos import TipoRasgueo


@dataclass
class EventoMusical:
    """
    Representa un evento musical.

    Un evento musical es un conjunto de notas más la técnica
    con la que deben interpretarse.
    """

    notas: list[str]

    tecnica: TipoTecnica

    tiempos: int

    patron: list[TipoRasgueo] = field(default_factory=list)

    vibrato: bool = False

    velocidad_rasgueo: int = 15

    def __str__(self):

        if self.patron:
            patron = " ".join(
                golpe.name
                for golpe in self.patron
            )
        else:
            patron = "-"
        
        notas = " ".join(self.notas)

        return (
            f"{self.tecnica.name:8} | "
            f"{notas} | "
            f"{self.tiempos} tiempos | "
            f"{patron}"
        )

