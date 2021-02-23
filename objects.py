
from pygame import transform, sprite, Rect
from random import randint
from numpy import sin, deg2rad, sqrt

class Entity:
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rotate = 0
        self.padding = (sqrt(self.w * self.w + self.h * self.h) - self.w) / 2
        
    def draw(self, screen, img, local_area = None):
        img = transform.scale(img, (self.w, self.h))
        if self.rotate:
            img = transform.rotate(img, self.rotate)

        screen.blit(img, (self.x - sin(deg2rad(self.rotate)) * self.padding, self.y - sin(deg2rad(self.rotate)) * self.padding ), local_area)
        
        # return screen


    def showInfor(self):
        print(self.x, self.y, self.w, self.h)
    
    def collide_with(self, e, fix = 0):
        horizontial = False
        vertical = False
        if self.x <= e.x:
            horizontial = e.x < self.x + self.w - 7 - fix
        else:
            horizontial = self.x < e.x + e.w - 7 - fix
        
        if not horizontial:
            return False
        
        if self.y < e.y:
            vertical = e.y < self.y + self.h - fix
        else:
            vertical = self.y < e.y + e.h - fix

        return horizontial and vertical

    
    def move(self, x, y):
        self.x += x
        self.y += y

class Bird(Entity):
    def __init__(self, x = 0, y = 0, w = 0, h = 0, speedU = 0, speedD = 0):
        super().__init__(x, y, w, h)
        self.speedUp = speedU
        self.speedDown = speedD
        

class Column(Entity):
    def __init__(self, x = 0, y = 0,w = 0, h = 0, margin = 80):
        super().__init__(x, y, w, h)
        self.margin = margin
        height_top = randint(50, 550 - self.margin)
        height_bottom = 600 - height_top - self.margin

        self.top = Entity(x, 0, w, height_top)
        self.bottom = Entity(x, height_top + margin, w, height_bottom)
        
    def draw(self, screen, surface):
        rect = Rect((0, 0), (100, self.bottom.h))
        subsurface = surface.subsurface(rect)
        self.bottom.draw(screen, subsurface)

        rect = Rect((0, 600 - self.top.h), (100, self.top.h))
        subsurface = surface.subsurface(rect)
        self.top.draw(screen, subsurface)
        
    
    def collide_with(self, e, fix = 0):
        return self.top.collide_with(e, fix + 5) or self.bottom.collide_with(e, fix)

    def move(self, x, y):
        self.x += x
        self.y += y
        self.top.x += x
        self.top.y += y
        self.bottom.x += x
        self.bottom.y += y
    
    # def setX(self, x):
    #     self.top.x = x
    #     self.bottom.y = y
    #     self.x = x
    
    def refresh(self, x, margin):
        self.margin = margin
        print("Margin", margin)
        self.top.x = x
        self.bottom.x = x
        self.x = x
        height_top = randint(50, 550 - self.margin)
        height_bottom = 600 - height_top - self.margin
        self.top.h = height_top # = Entity(x, 0, w, height_top)
        self.top.y= 0
        self.bottom.y = height_top + self.margin
        self.bottom.h = height_bottom # = Entity(x, height_top + margin, w, height_bottom)





if __name__ == "__main__":
    b = Bird(0, 0, 20, 20)
    c = Column(10, 19, 30, 30)
    
    print(dir(c))
    

