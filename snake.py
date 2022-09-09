import time
import pygame
import random
import os

pygame.init()
pygame.mixer.init()

screen_width = 640
screen_height = 460
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snakes")
pygame.display.update()

clock = pygame.time.Clock()
fps = 30


red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)


def text(window, message, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    rendered_text = font.render(message, True, color)
    window.blit(rendered_text, [x, y])


def snake_plot(snk_list, snake_size, color):
    for x, y in snk_list:
        pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])


def tutorial():
    exitGame = False
    img = pygame.image.load('Data/Images/tutorial.jpg')
    img = pygame.transform.scale(
        img, (screen_width, screen_height)).convert_alpha()
    while(exitGame == False):
        screen.blit(img, [0, 0])
        mouse = pygame.mouse.get_pos()
        if 10 <= mouse[0] <= 10+80 and 410 <= mouse[1] <= 410+40:
            pygame.draw.rect(screen, red, [10, 410, 80, 40])

        else:
            pygame.draw.rect(screen, black, [10, 410, 80, 40])

        text(screen, "BACK", 35, white, 15, 420)
        pygame.display.update()
        clock.tick(fps)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exitGame = True
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_BACKSPACE):
                    pygame.mixer.music.load('Data/Sounds/click.mp3')
                    pygame.mixer.music.play()
                    time.sleep(0.2)
                    welcome_screen()
                    exitGame = True
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if 10 <= mouse[0] <= 10+80 and 410 <= mouse[1] <= 410+40:
                    pygame.mixer.music.load('Data/Sounds/click.mp3')
                    pygame.mixer.music.play()
                    time.sleep(0.2)
                    welcome_screen()
                    exitGame = True


def cheats():
    exitGame = False
    img = pygame.image.load('Data/Images/cheats.jpg')
    img = pygame.transform.scale(
        img, (screen_width, screen_height)).convert_alpha()
    while(exitGame == False):
        screen.blit(img, [0, 0])
        mouse = pygame.mouse.get_pos()
        if 540 <= mouse[0] <= 540+80 and 410 <= mouse[1] <= 410+40:
            pygame.draw.rect(screen, red, [540, 410, 80, 40])

        else:
            pygame.draw.rect(screen, black, [540, 410, 80, 40])

        text(screen, "BACK", 35, white, 545, 420)
        pygame.display.update()
        clock.tick(fps)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exitGame = True
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_BACKSPACE):
                    pygame.mixer.music.load('Data/Sounds/click.mp3')
                    pygame.mixer.music.play()
                    time.sleep(0.2)
                    welcome_screen()
                    exitGame = True
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if 540 <= mouse[0] <= 540+80 and 410 <= mouse[1] <= 410+40:
                    pygame.mixer.music.load('Data/Sounds/click.mp3')
                    pygame.mixer.music.play()
                    time.sleep(0.2)
                    welcome_screen()
                    exitGame = True


def welcome_screen():
    exitGame = False
    img = pygame.image.load('Data/Images/homescreen.png')
    img = pygame.transform.scale(
        img, (screen_width, screen_height)).convert_alpha()
    while(exitGame == False):
        screen.blit(img, [0, 0])
        mouse = pygame.mouse.get_pos()
        if screen_width/2 - 65 <= mouse[0] <= screen_width/2 - 65 + 120 and 320 <= mouse[1] <= 320+40:
            pygame.draw.rect(screen, red, [screen_width/2 - 65, 320, 120, 40])

        else:
            pygame.draw.rect(
                screen, black, [screen_width/2 - 65, 320, 120, 40])
        if 530 <= mouse[0] <= 530 + 100 and 410 <= mouse[1] <= 410+40:
            pygame.draw.rect(screen, red, [530, 410, 100, 40])

        else:
            pygame.draw.rect(screen, black, [530, 410, 100, 40])

        text(screen, "TUTORIAL", 32, white, screen_width/2 - 62, 330)
        text(screen, "CHEATS!", 31, white, 532, 420)
        pygame.display.update()
        clock.tick(fps)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exitGame = True
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_RETURN):
                    pygame.mixer.music.load('Data/Sounds/click.mp3')
                    pygame.mixer.music.play()
                    time.sleep(0.2)
                    pygame.mixer.music.load('Data/Sounds/eot.mp3')
                    pygame.mixer.music.play(-1)
                    gameloop()
                    exitGame = True
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if screen_width/2 - 65 <= mouse[0] <= screen_width/2 - 65 + 120 and 320 <= mouse[1] <= 320+40:
                    pygame.mixer.music.load('Data/Sounds/click.mp3')
                    pygame.mixer.music.play()
                    time.sleep(0.2)
                    tutorial()
                    exitGame = True
                if 530 <= mouse[0] <= 530 + 100 and 410 <= mouse[1] <= 410+40:
                    pygame.mixer.music.load('Data/Sounds/click.mp3')
                    pygame.mixer.music.play()
                    time.sleep(0.2)
                    cheats()
                    exitGame = True


def gameloop():
    gameOver = False
    exitGame = False
    position_x = 200
    position_y = 300
    direction_x = 0
    direction_y = 0
    snake_velocity = 5
    snake_size = 10
    score = 0
    colour = yellow
    fruit = "apple"
    snake_length = 1
    snake_positional_list = []
    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)
    snk_img = pygame.image.load('Data/Images/snakeplayback.png')
    snk_img = pygame.transform.scale(
        snk_img, (screen_width, screen_height)).convert_alpha()

    if(not os.path.exists("Data/hiscore.txt")):
        with open("Data/hiscore.txt", "w") as f:
            f.write("0")
            hiscore = "0"
            content = "0"
    else:
        with open("Data/hiscore.txt") as f:
            hiscore = f.read()
        with open("Data/hiscore.txt") as f:
            content = f.read()

    while(exitGame == False):

        if(gameOver == True):
            with open("Data/hiscore.txt", "w") as f:
                f.write(f"{str(hiscore)}")
            screen.fill(white)
            if(score > int(content)):
                gameover = pygame.image.load('Data/Images/gameover_alt.jpg')
            else:
                gameover = pygame.image.load('Data/Images/gameover.jpg')
            gameover = pygame.transform.scale(
                gameover, (screen_width, screen_height)).convert_alpha()
            screen.blit(gameover, [0, 0])
            text(screen, f"{score}", 45, black, 330, 330)
            mouse = pygame.mouse.get_pos()
            if 35 <= mouse[0] <= 35+100 and 400 <= mouse[1] <= 400+40:
                pygame.draw.rect(screen, red, [35, 400, 100, 40])

            else:
                pygame.draw.rect(screen, black, [35, 400, 100, 40])
            if 500 <= mouse[0] <= 500+100 and 400 <= mouse[1] <= 400+40:
                pygame.draw.rect(screen, red, [500, 400, 100, 40])

            else:
                pygame.draw.rect(screen, black, [500, 400, 100, 40])
            text(screen, "RETRY!", 35, white, 505, 410)
            text(screen, "MENU", 35, white, 50, 410)
            pygame.display.update()
            clock.tick(fps)
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    exitGame = True
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_RETURN):
                        pygame.mixer.music.load('Data/Sounds/click.mp3')
                        pygame.mixer.music.play()
                        time.sleep(0.2)
                        pygame.mixer.music.load('Data/Sounds/eot.mp3')
                        pygame.mixer.music.play(-1)
                        gameloop()
                        exitGame = True
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if 500 <= mouse[0] <= 500+100 and 400 <= mouse[1] <= 400+40:
                        pygame.mixer.music.load('Data/Sounds/click.mp3')
                        pygame.mixer.music.play()
                        time.sleep(0.2)
                        pygame.mixer.music.load('Data/Sounds/eot.mp3')
                        pygame.mixer.music.play(-1)
                        gameloop()
                        exitGame = True
                    if 35 <= mouse[0] <= 35+100 and 400 <= mouse[1] <= 400+40:
                        pygame.mixer.music.load('Data/Sounds/click.mp3')
                        pygame.mixer.music.play()
                        time.sleep(0.2)
                        welcome_screen()
                        exitGame = True

        else:

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    exitGame = True

                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_UP or event.key == pygame.K_w):
                        direction_y = -snake_velocity
                        direction_x = 0
                    if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                        direction_y = snake_velocity
                        direction_x = 0
                    if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                        direction_x = -snake_velocity
                        direction_y = 0
                    if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                        direction_x = snake_velocity
                        direction_y = 0
                    if(event.key == pygame.K_c):
                        num = random.randint(0, 4)
                        if(num == 0):
                            if(colour != red):
                                colour = red
                            else:
                                colour = cyan
                        if(num == 1):
                            if(colour != black):
                                colour = black
                            else:
                                colour = magenta
                        if(num == 2):
                            if(colour != cyan):
                                colour = cyan
                            else:
                                colour = red
                        if(num == 3):
                            if(colour != magenta):
                                colour = magenta
                            else:
                                colour = yellow
                        if(num == 4):
                            if(colour != yellow):
                                colour = yellow
                            else:
                                colour = black
                    if(event.key == pygame.K_f):
                        num = random.randint(0, 5)
                        if(num == 0):
                            if(fruit != "banana"):
                                fruit = "banana"
                            else:
                                fruit = "watermelon"
                        if(num == 1):
                            if(fruit != "grapes"):
                                fruit = "grapes"
                            else:
                                fruit = "orange"
                        if(num == 2):
                            if(fruit != "orange"):
                                fruit = "orange"
                            else:
                                fruit = "banana"
                        if(num == 3):
                            if(fruit != "watermelon"):
                                fruit = "watermelon"
                            else:
                                fruit = "pineapple"
                        if(num == 4):
                            if(fruit != "pineapple"):
                                fruit = "pineapple"
                            else:
                                fruit = "apple"
                        if(num == 5):
                            if(fruit != "apple"):
                                fruit = "apple"
                            else:
                                fruit = "grapes"
                    if(event.key == pygame.K_v):
                        if(snake_velocity < 10):
                            snake_velocity += 1

            position_x += direction_x
            position_y += direction_y

            if(abs(position_x - food_x) < 8 and abs(position_y - food_y) < 8):
                score += 1
                snake_length += 3
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(20, screen_height - 20)
                if(score > int(hiscore)):
                    hiscore = score

            head = []
            head.append(position_x)
            head.append(position_y)
            snake_positional_list.append(head)

            if(len(snake_positional_list) > snake_length):
                del snake_positional_list[0]

            if(position_x > screen_width or position_x < 0 or position_y > screen_height or position_y < 0):
                gameOver = True
                pygame.mixer.music.load('Data/Sounds/crash.mp3')
                pygame.mixer.music.play()

            if(head in snake_positional_list[:-1]):
                gameOver = True
                pygame.mixer.music.load('Data/Sounds/crash.mp3')
                pygame.mixer.music.play()

            screen.fill(white)
            screen.blit(snk_img, [0, 0])
            text(
                screen, f'Score : {score}   HiScore : {hiscore}', 45, black, 15, 0)
            snake_plot(snake_positional_list, snake_size, colour)
            apple_img = pygame.image.load(f'Data/Images/{fruit}.png')
            apple_img = pygame.transform.scale(
                apple_img, (20, 20)).convert_alpha()
            screen.blit(apple_img, [food_x, food_y])
            pygame.display.update()
            clock.tick(fps)


welcome_screen()

pygame.quit()

