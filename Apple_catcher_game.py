import pygame
import random
import math
from pygame import mixer


def game_loop():
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

    def print_apple(x, y, i):
        screen.blit(apple[i], (x, y))

    def print_bowl():
        screen.blit(bowl, (bowlX, bowlY))

    def collision_cheak(appleX, appleY, bowlX, bowlY):
        distance = math.sqrt((math.pow(appleX - bowlX, 2) + (math.pow(appleY - bowlY, 2))))

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

    game_over = pygame.font.Font('freesansbold.ttf', 45)
    fontX = 5
    fontY = 270

    def print_game_over():
        game_over_ = game_over.render("GAME OVER! Press Enter to restart", True, (0, 0, 0))
        screen.blit(game_over_, (fontX, fontY))

    hiscore_font = pygame.font.Font('freesansbold.ttf', 32)
    hiscore_fontX = 610
    hiscore_fontY = 10

    def print_hiscore():
        hiscore_render = hiscore_font.render("Hiscore: " + str(hiscore), True, (255, 255, 255))
        screen.blit(hiscore_render, (hiscore_fontX, hiscore_fontY))

    with open("Hiscore_Manager_Apple_Catcher.txt", "r") as f:
        hiscore = f.read()
    running = True
    game__over = False

    while running:
        if game__over:
            with open("Hiscore_Manager_Apple_Catcher.txt", "w") as f:
                f.write(str(hiscore))
            screen.blit(bg, (0, 0))
            print_game_over()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
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
                        game__over = True

                collision = collision_cheak(appleX[i], appleY[i], bowlX, bowlY)
                if collision:
                    score += 1
                    appleY[i] = random.choice([-110, -120])
                    appleX[i] = random.randint(300, 600)
                    apple_bite = mixer.Sound('bite_apple.wav')
                    apple_bite.play()

                print_apple(appleX[i], appleY[i], i)

                appleY[i] += appleY_change[i]
            if score > int(hiscore):
                hiscore = score
            print_hiscore()
            print_score()
            print_bowl()
            bowlX += bowlX_change

        pygame.display.update()


game_loop()
