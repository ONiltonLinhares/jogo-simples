import pygame
import time

# inicialize o Pygame
pygame.init()

# Definir as dimensões da janela
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

# Definir as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Crie a janela
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Movendo o quadrado")
screen.fill(WHITE)  

# Defina as propriedades do quadrado
square_size = 25
square_color = BLACK
square_position = [(WINDOW_WIDTH - square_size) / 2, (WINDOW_HEIGHT - square_size) / 2]

# Defina a velocidade de movimento do quadrado
movement_speed = 1.2

# Defina a opção de tela cheia
fullscreen = False

# Variável para controlar o tempo de duração da velocidade aumentada
speed_up_duration = 2  # segundos

# Variável para armazenar o tempo em que a velocidade foi aumentada
speed_up_start_time = None

# Crie o loop principal do jogo
while True:
    # Trate os eventos
    for event in pygame.event.get():
        # Se o usuário clicar no botão "X" da janela, saia do jogo
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Se uma tecla for pressionada
        elif event.type == pygame.KEYDOWN:
            # Adicione a opção de tela cheia
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                    
            # Se a tecla de espaço for pressionada, aumente a velocidade do movimento do quadrado
            elif event.key == pygame.K_SPACE:
                movement_speed = 2.5
                speed_up_start_time = time.time()
                pygame.time.set_timer(pygame.USEREVENT, int(speed_up_duration * 1000)) # timer para voltar a velocidade normal depois de 2 segundos

        # Se o temporizador expirar, volte a velocidade do movimento do quadrado para 1.2
        elif event.type == pygame.USEREVENT:
            movement_speed = 1.2

    # Obtenha as teclas pressionadas
    keys = pygame.key.get_pressed()
    
    # Verifique se a tecla de seta correspondente está pressionada e mova o quadrado naquela direção
    speed_multiplier = 1  # multiplicador de velocidade padrão
    if keys[pygame.K_LEFT]:
        square_position[0] -= movement_speed * speed_multiplier
        if square_position[0] < -square_size:
            square_position[0] = WINDOW_WIDTH
    if keys[pygame.K_RIGHT]:
        square_position[0] += movement_speed * speed_multiplier
        if square_position[0] > WINDOW_WIDTH:
            square_position[0] = -square_size
    if keys[pygame.K_UP]:
        square_position[1] -= movement_speed * speed_multiplier
        if square_position[1] < -square_size:
            square_position[1] = WINDOW_HEIGHT
    if keys[pygame.K_DOWN]:
        square_position[1] += movement_speed * speed_multiplier
        if square_position[1] > WINDOW_HEIGHT:
            square_position[1] = -square_size
    
    # Limpe a tela
    screen.fill(WHITE)

    # Desenhe o quadrado
    pygame.draw.rect(screen, square_color, (square_position[0], square_position[1], square_size, square_size))

    # Atualize a janela
    pygame.display.update()