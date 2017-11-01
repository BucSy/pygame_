import pygame
import random

class Worm:

    def __init__(self, surface, x, y, length):
        self.surface = surface
        self.x = x
        self.y = y
        self.length = length
        self.grow_to = 50
        self.dir_x = 0
        self.dir_y = -1
        self.body = []
        self.crashed = False

    def eat(self):
        self.grow_to += 25

    def canGoUp(self):
        if self.dir_x == 0 and self.dir_y == 1:
            print("Nem mehet fel")
            return False
        else:
            return True

    def canGoDown(self):
        if self.dir_x == 0 and self.dir_y == -1:
            print("Nem mehet fel")
            return False
        else:
            return True

    def canGoLeft(self):
        if self.dir_x == 1 and self.dir_y == 0:
            print("Nem mehet fel")
            return False
        else:
            return True

    def canGoRight(self):
        if self.dir_x == -1 and self.dir_y == 0:
            print("Nem mehet fel")
            return False
        else:
            return True

    def key_event(self, event):
        if event.key == pygame.K_UP and w.canGoUp():
            self.dir_x = 0
            self.dir_y = -1
        elif event.key == pygame.K_DOWN and w.canGoDown():
            self.dir_x = 0
            self.dir_y = 1
        elif event.key == pygame.K_LEFT and w.canGoLeft():
            self.dir_x = -1
            self.dir_y = 0
        elif event.key == pygame.K_RIGHT and w.canGoRight():
            self.dir_x = 1
            self.dir_y = 0

    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y

        if (self.x, self.y) in self.body:
            self.crashed = True

        self.body.insert(0, (self.x, self.y))

        if len(self.body) > self.length:
            self.body.pop()

    def draw(self):
        for x, y in self.body:
            self.surface.set_at((x, y), (255, 255, 255))

    def position(self):
        return self.x, self.y


class Food:
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(1, surface.get_width())
        self.y = random.randint(1, surface.get_height())
        self.color = 255, 255, 255

    def draw(self):
        self.surface.set_at((self.x, self.y), self.color)
    def position(self):
        return self.x, self.y


width = 640
height = 400

score = 0
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
food = Food(screen)
running = True

roundedWidth = int(round(width / 2))
roundedHeight = int(round(height / 2))

w = Worm(screen, roundedWidth, roundedHeight, 200)

while running:
    screen.fill((0, 0, 0))
    w.move()
    w.draw()
    food.draw()

    if w.crashed:
        print ("Crash!")
        running = False
    if w.x <= 0:
        print("kisebb mint 0")
        w.x = width - 2
    if w.x >= width - 1:
        w.x = 1
    if w.y <= 0:
        w.y = height - 2
    if w.y >= height - 1:
        w.y = 1

    elif w.position() == food.position():
         score += 1
         w.eat()
         print ("Score: %d" % score)
         food = Food(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            w.key_event(event)


    pygame.display.flip()
    clock.tick(240)
