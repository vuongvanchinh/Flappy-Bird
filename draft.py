import pygame
import random
from pygame import mixer
from time import sleep

pygame.init()
CLICK_SOUND = mixer.Sound("data/click.wav")
IMAGE_COLLUMN = pygame.image.load("data/column.png")
IMAGE_BIRD = pygame.image.load("data/bird.png")
IMAGE_BACKGROUND = pygame.image.load("data/background.jpg")

class Bird:
    def __init__(self):
        self.xScreen, self.yScreen = 500, 600
        
        self.screen = pygame.display.set_mode(
            (self.xScreen, self.yScreen))

        pygame.display.set_caption("Flappy Bird")

        self.gamerunning = True
        pygame.display.set_icon(IMAGE_BIRD)
        #********************************************
        self.xSizeBird = 80
        self.ySizeBird = 60
        self.xBird = self.xScreen / 3
        self.yBird = self.yScreen / 2
        self.vBirdUp = 80
        self.vBirdDown = 7
        #*********************************************
        self.xColumn = self.xScreen + 250
        self.yColumn = 0
        self.xSizeColumn = 100
        self.ySizeColumn = self.yScreen
        self.vColumn = 6
        self.columnChange = 0

        self.scores = 0
        self.checkLost = False
    
    def music(self, sound):
        sound.play()
    

    def draw_image(self, img, xLocal, yLocal, xImg, yImg):
        img = pygame.transform.scale(
            img, (xImg, yImg)
        )
        self.screen.blit(img, (xLocal, yLocal))
    
    def show_score(self, x, y, scores, size):
        font = pygame.font.SysFont("Arial", size)
        score = font.render(str(scores), True, (255, 255, 255))
        self.screen.blit(score, (x, y))

    def column(self):
        marginColumn = 80
        yColumnChangeTop = -self.ySizeColumn/2 - marginColumn + self.columnChange
        yColumnChangeBotton = self.ySizeColumn/2 + marginColumn + self.columnChange

        self.draw_image(IMAGE_COLLUMN, self.xColumn, yColumnChangeTop, self.xSizeColumn, self.ySizeColumn)
        self.draw_image(IMAGE_COLLUMN, self.xColumn, yColumnChangeBotton, self.xSizeColumn, self.ySizeColumn)
        
        self.xColumn = self.xColumn - self.vColumn

        if self.xColumn < -100:
            self.xColumn = self.xScreen
            self.columnChange = random.randint(-150, 150)
            self.scores += 1
        return yColumnChangeTop + self.ySizeColumn, yColumnChangeBotton


    def run(self):
        while self.gamerunning:
            self.screen.blit(IMAGE_BACKGROUND, (0, 0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.gamerunning = False
                if e.type == pygame.MOUSEBUTTONDOWN or (e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE):
                    self.yBird -= self.vBirdUp
                    self.music(CLICK_SOUND)
            
            self.yBird += self.vBirdDown
            yColumnChangeTop, yColumnChangeBotton = self.column()

            if self.yBird < yColumnChangeTop and (self.xColumn+self.xSizeColumn - 5 > self.xBird+self.xSizeBird > self.xColumn + 5 or self.xColumn+self.xSizeColumn > self.xBird > self.xColumn):
                self.checkLost = True
            if self.yBird+self.ySizeBird > yColumnChangeBotton and (self.xColumn+self.xSizeColumn - 5 > self.xBird+self.xSizeBird > self.xColumn + 5 or self.xColumn+self.xSizeColumn > self.xBird > self.xColumn):
                self.checkLost = True
             # ---------Check xem bird có chạm tường-----------------------------
            if (self.yBird + self.ySizeBird > self.yScreen) or self.yBird < 0:
                self.yBird = self.yScreen/2
                self.checkLost = True
            self.vColunm = 6 if self.scores < 1 else 6 + self.scores/5  # Tốc độ tăng dần
            self.vBirdDown = 7 if self.scores < 1 else 7 + self.scores/10  # Bird rơi nhanh dần
            #==================== cham dat =============
            if self.yBird >= self.yScreen - self.ySizeBird:
                self.vBirdDown = 0
            print(self.vColunm)
            while self.checkLost:
                self.xColumn = self.xScreen + 100
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        self.gamerunning = False
                        self.checkLost = False
                        break

                    if e.type == pygame.KEYDOWN or e.type == pygame.MOUSEBUTTONDOWN:
                        self.checkLost = False
                        self.scores = 0
                    
                self.show_score(100, 100 ,"Scores:{}".format(self.scores), 40)
                self.show_score(self.xScreen / 2 - 100, self.yScreen/ 2 -100, "Game Over", 50)
                self.vColunm = 6
                self.vBirdDown = 7
                pygame.display.update()
            self.draw_image(IMAGE_BIRD, self.xBird, self.yBird, self.xSizeBird, self.ySizeBird)
            self.show_score(10, 10, "Scores:{}".format(self.scores), 35)

            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(80)

bird = Bird()
bird.run()


    