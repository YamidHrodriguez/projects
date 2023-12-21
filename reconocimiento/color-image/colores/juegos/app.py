import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Nave")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Jugador
player_width = 50
player_height = 50
player_x = width // 2 - player_width // 2
player_y = height - 2 * player_height

# Obstáculos
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []

# Reloj
clock = pygame.time.Clock()

# Puntuación
score = 0

# Música de fondo
pygame.mixer.music.load('rutinas\human-tetris.wav')  # Reemplaza 'tu_cancion.mp3' con la ruta de tu propia canción
pygame.mixer.music.play(-1)  # -1 para reproducir la música en bucle

# Función principal del juego
def game():
    global player_x, player_y, obstacles, score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player_x -= (keys[pygame.K_LEFT] - keys[pygame.K_RIGHT]) * 5
        player_x = max(0, min(width - player_width, player_x))

        # Crear obstáculos
        if random.randint(1, obstacle_frequency) == 1:
            obstacle_x = random.randint(0, width - obstacle_width)
            obstacle_y = -obstacle_height
            obstacles.append((obstacle_x, obstacle_y))

        # Mover y dibujar obstáculos
        new_obstacles = []
        for obstacle in obstacles:
            obstacle_x, obstacle_y = obstacle
            obstacle_y += obstacle_speed
            if obstacle_y < height:
                new_obstacles.append((obstacle_x, obstacle_y))
                pygame.draw.rect(screen, white, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
            else:
                score += 1
        obstacles = new_obstacles

        # Dibujar jugador
        pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))

        # Dibujar puntuación
        font = pygame.font.Font(None, 36)
        score_text = font.render("Puntuación: {}".format(score), True, white)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        screen.fill(black)
        clock.tick(30)

if __name__ == "__main__":
    game()
