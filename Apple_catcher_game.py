import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('forest.png')
bg = pygame.transform.scale(background, (800, 600))

pygame.display.set_caption('Apple catcher')

icon = pygame.image.load('physics.png')
pygame.display.set_icon(icon)

mixer.music.load('background.wav')
mixer.music.play(-1)

bowl = pygame.image.load('bowl.png')
# bowl = pygame.transform.scale(bowlnor, (128, 100))
bowlX = 380
bowlY = 480
bowlX_change = 0

apple = []
appleX = []
appleY = []
appleX_change = []
appleY_change = []
num_of_apple = 1

for i in range(num_of_apple):
    apple.append(pygame.image.load('bigapple.png'))
    appleX.append(380)
    appleY.append(-10)
    appleX_change.append(0)
    appleY_change.append(4)


def print_space_ship(x, y, i):
    screen.blit(apple[i], (x, y))


def print_bowl():
    screen.blit(bowl, (bowlX, bowlY))


def collision_cheak(space_shipX, space_shipY, bowlX, bowlY):
    distance = math.sqrt((math.pow(space_shipX - bowlX, 2) + (math.pow(space_shipY - bowlY, 2))))

    if distance <= 10:
        return True
    else:
        return False


score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
score_fontX = 10
score_fontY = 10


def print_score():
    score_render = score_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_render, (score_fontX, score_fontY))


game_over = pygame.font.Font('freesansbold.ttf', 64)
fontX = 200
fontY = 270


def print_game_over():
    game_over_ = game_over.render("GAME OVER", True, (0, 0, 0))
    screen.blit(game_over_, (fontX, fontY))


running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bowlX_change = -3
            elif event.key == pygame.K_RIGHT:
                bowlX_change = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                bowlX_change = 0
            elif event.key == pygame.K_RIGHT:
                bowlX_change = 0
    for i in range(num_of_apple):
        if appleY[i] >= 536:
            for j in range(num_of_apple):
                appleX[j] = 2000
                appleY[j] = 2000
                print_game_over()
                appleY_change[j] = 0

        collision = collision_cheak(appleX[i], appleY[i], bowlX, bowlY)
        if collision:
            score += 1
            appleY[i] = random.choice([-110, -120])
            appleX[i] = random.randint(300, 600)
            apple_bite = mixer.Sound('bite_apple.wav')
            apple_bite.play()

        print_space_ship(appleX[i], appleY[i], i)

        appleY[i] += appleY_change[i]
    print_score()
    print_bowl()
    bowlX += bowlX_change
    pygame.display.update()
