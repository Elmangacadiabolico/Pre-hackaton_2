import pygame
import random
import sys

def main():
    """
    Juego simple de Pygame con un jugador que captura objetos.
    """
    # Inicializa pygame
    pygame.init()

    # --- Configuración de la Pantalla ---
    ANCHO, ALTO = 800, 600
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Captura el Objeto")

    # --- Colores ---
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)
    AZUL = (0, 0, 255)
    VERDE_LIMA = (50, 205, 50) # Color para la animación de captura

    # --- Jugador ---
    # Se crea un rectángulo para el jugador en lugar de cargar una imagen
    jugador_ancho, jugador_alto = 50, 50
    # pygame.Rect(pos_x, pos_y, ancho, alto)
    jugador_rect = pygame.Rect(ANCHO // 2 - jugador_ancho // 2, ALTO - jugador_alto - 10, jugador_ancho, jugador_alto)
    jugador_color = ROJO
    jugador_velocidad = 7

    # --- Objeto ---
    # Se crea un rectángulo para el objeto
    objeto_ancho, objeto_alto = 30, 30
    objeto_rect = pygame.Rect(random.randint(0, ANCHO - objeto_ancho), 0, objeto_ancho, objeto_alto)
    objeto_velocidad = 5

    # --- Animación de Captura ---
    # Contador para controlar la duración del cambio de color
    animacion_captura_contador = 0

    # --- Control de FPS y Bucle Principal ---
    clock = pygame.time.Clock()
    ejecutando = True

    # --- Bucle del Juego ---
    while ejecutando:
        # --- Manejo de Eventos ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False

        # --- Movimiento del Jugador ---
        # Captura las teclas presionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jugador_rect.left > 0:
            jugador_rect.x -= jugador_velocidad
        if teclas[pygame.K_RIGHT] and jugador_rect.right < ANCHO:
            jugador_rect.x += jugador_velocidad
        if teclas[pygame.K_UP] and jugador_rect.top > 0:
            jugador_rect.y -= jugador_velocidad
        if teclas[pygame.K_DOWN] and jugador_rect.bottom < ALTO:
            jugador_rect.y += jugador_velocidad

        # --- Lógica del Juego ---
        # Mover el objeto hacia abajo
        objeto_rect.y += objeto_velocidad
        # Si el objeto sale de la pantalla, reposicionarlo arriba
        if objeto_rect.top > ALTO:
            objeto_rect.y = -objeto_alto
            objeto_rect.x = random.randint(0, ANCHO - objeto_ancho)

        # --- Detección de Colisiones ---
        # Comprueba si el rectángulo del jugador colisiona con el del objeto
        if jugador_rect.colliderect(objeto_rect):
            # Inicia la animación de captura
            jugador_color = VERDE_LIMA
            animacion_captura_contador = 10 # Duración de 10 frames

            # Reposiciona el objeto en la parte superior en un lugar aleatorio
            objeto_rect.y = -objeto_alto
            objeto_rect.x = random.randint(0, ANCHO - objeto_ancho)

        # --- Manejo de la Animación ---
        if animacion_captura_contador > 0:
            animacion_captura_contador -= 1
        else:
            # Restaura el color original del jugador
            jugador_color = ROJO

        # --- Dibujado en Pantalla ---
        # 1. Rellenar el fondo de color blanco
        pantalla.fill(BLANCO)

        # 2. Dibujar el jugador
        pygame.draw.rect(pantalla, jugador_color, jugador_rect)

        # 3. Dibujar el objeto
        pygame.draw.rect(pantalla, AZUL, objeto_rect)

        # --- Actualizar la Pantalla ---
        pygame.display.flip()

        # --- Controlar FPS ---
        # Limita el bucle a 60 fotogramas por segundo
        clock.tick(60)

    # --- Fin de Pygame ---
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()