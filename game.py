import pygame

class Worm:

    def __init__(self, surface, x, y, length):
        self.surface = surface
        self.x = x
        self.y = y
        self.length = length
        self.dir_x = 0
        self.dir_y = -1
        self.body = []
        self.crashed = False

    def currentDirection(self, dir_xx, dir_yy):
        self.dir_xx = dir_xx
        self.dir_yy = dir_yy
        print(dir_xx, dir_yy)

    def key_event(self, event):
        if event.key == pygame.K_UP:
            self.dir_x = 0
            self.dir_y = -1
            w.currentDirection(0, -1)
        elif event.key == pygame.K_DOWN:
            self.dir_x = 0
            self.dir_y = 1
            w.currentDirection(0, 1)
        elif event.key == pygame.K_LEFT:
            self.dir_x = -1
            self.dir_y = 0
            w.currentDirection(-1, 0)
        elif event.key == pygame.K_RIGHT:
            self.dir_x = 1
            self.dir_y = 0
            w.currentDirection(1, 0)

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


width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

roundedWidth = int(round(width / 2))
roundedHeight = int(round(height / 2))

w = Worm(screen, roundedWidth, roundedHeight, 200)

while running:
    screen.fill((0, 0, 0))
    w.move()
    w.draw()

    if w.crashed or w.x <= 0 or w.x >= width -1 or w.y <= 0 or w.y >= height - 1:
        print ("Crash!")
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            w.key_event(event)

    pygame.display.flip()
    clock.tick(240)
