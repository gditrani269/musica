1 - Silencios (muy fácil y mejora mucho el resultado).
2 - Rasgueos por acorde (empieza la parte realmente "guitarrística").
3 - Compás (4/4, 3/4, etc.).
4 - Patrones completos de rasgueo (↓ ↓ ↑ ↑ ↓ ↑).
5 - Capo/transposición.
6 - Lectura de tablaturas.

musica/
│
├── guitarra/
    ├── acordes.py
    ├── notas.py
    ├── sintetizador.py
    ├── envolventes.py
    ├── evento.py
    |       └── EventoMusical
    ├── tecnicas.py
    |       └── TipoTecnica
    └── rasgueos.py
            └── TipoRasgueo
|    
├── audio/
|
├── lectura/
|      └── lector
|
├── canciones/
│
├── config.py
|       ├── FS
|       ├── DURACION
|       ├── VELOCIDAD_RASGUEO
|       └── etc.
├── main.py
└── README.md

main.py
    │
    ▼
reproducir_evento()
    │
    ├──────────────┐
    ▼              ▼
ACORDE         MELODÍA
    │              │
    ▼              ▼
_generar_patron() generar_nota()
    │              │
    └──────┬───────┘
           ▼
      aplicar_envolvente()