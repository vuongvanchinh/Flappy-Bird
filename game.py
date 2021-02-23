
from objects import Bird, Column
import pygame
from time import sleep
from random import randint


WIDTH_SCREEN = 500
HEIGHT_SCREEN = 600
COLUMN_WIDTH = 100
NUMBER_COLUMNS = 2
SPACE_BETWEEN_COLUMNS = 300

########### COLOR ###########
TEXT_COLOR = (0, 153, 204)

FPS = 60
fpsClock = pygame.time.Clock()

bird = Bird(150, 100, 60, 44)
columns = [Column(WIDTH_SCREEN + i * 250, 0, 100, HEIGHT_SCREEN, margin = 100) for i in range(NUMBER_COLUMNS)]

pygame.init()

BACKGROUND_IMG = pygame.image.load("data/background.jpg")
BIRD_IMG = pygame.image.load("data/bird.png")
COLUMN_IMG = pygame.transform.scale(pygame.image.load("data/column.png"), (COLUMN_WIDTH, HEIGHT_SCREEN))
MUSIC = pygame.mixer.Sound("data/click.wav")
MUSIC_TING = pygame.mixer.Sound("data/ting.wav")
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("Flappy Bird")

def draw_image(img, x, y, w, h):
    global screen
    img = pygame.transform.scale(img, (w, h))
    screen.blit(img, (x, y))

def draw_text(screen, font_letter, content, x = 0, y = 0, size = 40, color = (255, 255, 255)):
    l_font = pygame.font.SysFont(font_letter, size)
    suface = l_font.render(content, True, color)
    screen.blit(suface, (x, y))

def play_music(music):
    music.play()

def new_game():
    global scores, speedUp, speedDown, game_speed, bird, column

    bird.x = 150
    bird.y = 150
    for i in range(NUMBER_COLUMNS):
        columns[i].refresh(WIDTH_SCREEN + i* SPACE_BETWEEN_COLUMNS, randint(90, 100))

    speedUp = 50
    speedDown = SPEED_FALL_DEFAULT
    game_speed = 2
    bird.rotate = 0
    scores = 0

SPEED_FALL_DEFAULT = 1
running = True
speedUp = 40
speedDown = SPEED_FALL_DEFAULT
game_speed = 2

G = 9.8
time = 0.0
lost_game = False
scores = 0

if __name__ == "__main__":
    while running:
        screen.blit(BACKGROUND_IMG, (0, 0))
    
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                break
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    bird.move(0, -speedUp)
                    play_music(MUSIC)
                    bird.rotate = 45
                    speedDown = SPEED_FALL_DEFAULT
                    time = 0.0

            elif e.type == pygame.MOUSEBUTTONDOWN:
                bird.move(0, - speedUp)
                play_music(MUSIC)
                speedDown = 0
                bird.rotate = 45
                speedDown = SPEED_FALL_DEFAULT
                time = 0.0
       
        
        for column in columns:
            if (column.x <= WIDTH_SCREEN):
                column.draw(screen, COLUMN_IMG)
        bird.draw(screen, BIRD_IMG)
        draw_text(screen, "Arial", "Scores: {}".format(scores),20, 20, 30, color= TEXT_COLOR)
        
        bird.move(0, speedDown)
        for col in columns:
            col.move(-game_speed, 0)

        time += 0.01 
        speedDown = G * time
        
        if bird.rotate > -30:
            bird.rotate -= 1
        ##********************* handel lost game
        while lost_game:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                    lost_game = False
                    print("exit")
                    break
                
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        new_game()
                        lost_game = False
                        break
            draw_text(screen, "Arial","GAME OVER", 180, 180, color = TEXT_COLOR)
            draw_text(screen, "Arial", "Scores:{}".format(scores), 190, 240, color = TEXT_COLOR)
            draw_text(screen, "Arial", "Press Enter key to play new game!", 100,HEIGHT_SCREEN - 40, 20, color = TEXT_COLOR)


            pygame.display.update()

        pygame.display.update()
         #  handel logic game
        if bird.y >= HEIGHT_SCREEN - bird.h: #reach to the ground
            speedDown = 0
            lost_game = True
            game_speed = 0
        for column in columns:
            if column.x < -column.w:
                column.refresh(WIDTH_SCREEN, randint(90, 110))
                scores += 1
                play_music(MUSIC_TING)
                game_speed += 0.001

            if column.collide_with(bird, 10): # column must be the instance call not bird.collide_with(column) 
                column.top.showInfor()
                column.bottom.showInfor()
                bird.showInfor()
                speedDown = 0
                lost_game = True
                game_speed = 0
                break

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++
        fpsClock.tick(FPS)





