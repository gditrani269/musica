from guitarra.evento import EventoMusical
from guitarra.tecnicas import TipoTecnica
from guitarra.rasgueos import TipoRasgueo
from guitarra.acordes import ACORDES


evento = EventoMusical(
    notas=ACORDES["Am"],
    tecnica=TipoTecnica.RASGUEO,
    patron=[
        TipoRasgueo.DOWN,
        TipoRasgueo.DOWN,
        TipoRasgueo.UP,
        TipoRasgueo.UP,
        TipoRasgueo.DOWN,
        TipoRasgueo.UP
    ],
    duracion=2
)


print(evento)