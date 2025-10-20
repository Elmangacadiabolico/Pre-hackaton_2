# Proyecto Pygame Simple

Este proyecto es un ejemplo básico de cómo usar la librería `pygame` en Python para crear una ventana con imágenes.

## Descripción

El script `main.py` inicializa una ventana de Pygame, carga una imagen de fondo, un personaje (jugador) y un objeto que cae desde la parte superior de la pantalla.

Este proyecto es ideal para principiantes que están aprendiendo a:
- Configurar una ventana de Pygame.
- Cargar y mostrar imágenes.
- Implementar un bucle de juego básico.
- Manejar eventos simples.

## Requisitos

- Python 3.x
- Pygame

Puedes instalar Pygame con pip:
```bash
pip install pygame
```

## Estructura de Archivos

```
.
├── main.py
├── assets
│   └── img
│       ├── fondo.png       (¡Necesaria!)
│       ├── jugador.png     (¡Necesaria!)
│       └── objeto.png      (¡Necesaria!)
└── README.md
```

## Uso

1.  **Asegúrate de tener las imágenes:**
    El programa necesita tres archivos de imagen para funcionar:
    - `fondo.png`
    - `jugador.png`
    - `objeto.png`

    Debes colocarlos dentro de la carpeta `assets/img/`. Como no se encontraron imágenes, el programa mostrará un error.

2.  **Ejecuta el script:**
    Una vez que tengas las imágenes en su lugar, puedes ejecutar el juego con el siguiente comando:
    ```bash
    python main.py
    ```

## Visuales

Aquí hay una idea de cómo se vería el programa si las imágenes estuvieran presentes.

**Fondo de pantalla:**
*(Aquí iría una captura de la pantalla con el fondo)*
![Fondo](https://via.placeholder.com/800x600.png?text=Fondo+del+Juego)

**Jugador y Objeto:**
*(Aquí iría una captura del jugador y el objeto cayendo)*
![Jugador y Objeto](https://via.placeholder.com/800x600.png?text=Jugador+y+Objeto)
