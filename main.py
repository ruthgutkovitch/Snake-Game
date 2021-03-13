import pygame
import time
import random

class Apple:
    food_x = 0
    food_y = 0

    def __init__(self, screen_width, screen_height):
        self.food_x = round(random.randrange(0, screen_width))
        self.food_y = round(random.randrange(0, screen_height))

    def change(self, screen_width, screen_height):
        self.food_x = round(random.randrange(0, screen_width))
        self.food_y = round(random.randrange(0, screen_height))

    def draw(self, screen,image):
        screen.blit(image,(self.food_x, self.food_y))

class Player:
    x = []
    y = []
    move = 10
    len = 1
    score = 0
    str = None

    def __init__(self, screen_width, screen_height):
        self.x.append(screen_width/2)
        self.y.append(screen_height/2)

    def updateSnakeHead(self):
        if self.str == "Right":
            self.x[0] += self.move
        if self.str == "Left":
            self.x[0] -= self.move
        if self.str == "Up":
            self.y[0] -= self.move
        if self.str == "Down":
            self.y[0] += self.move

    def updatePrev(self):
        for i in range(len(self.x)-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

    def updatePlayerPosition(self):
        self.updatePrev()
        self.updateSnakeHead()

    def moveRight(self):
        self.str = "Right"

    def moveLeft(self):
        self.str = "Left"

    def moveUp(self):
        self.str = "Up"

    def moveDown(self):
        self.str = "Down"

    def draw(self, screen, image):
        for i in range(self.len):
            screen.blit(image, (self.x[i], self.y[i]))

class Screen:
    orange_color = (245, 155, 22)
    yellow_color = (248, 255, 3)
    white_color = (255, 255, 255)
    screen_width = 800
    screen_height = 600
    score = 0
    screen = None
    clock = None

    def __init__(self):
        self._running = False
        self._snake_surf = None
        self._apple_surf = None
        self.player = Player(self.screen_width, self.screen_height)
        self.apple = Apple(self.screen_width, self.screen_height)

    def endGame(self):
        len = self.player.len
        for i in range(len):
            if self.player.x[i] >= self.screen_width or self.player.x[i] <= 0:
                return True
            if self.player.y[i] >= self.screen_height or self.player.y[i] <= 0:
                return True

        return False

    def createScreen(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self._running = True
        self._snake_surf = pygame.image.load("block.png").convert()
        self._apple_surf = pygame.image.load("apple").convert()
        self.screen.fill(self.white_color)
        self.clock = pygame.time.Clock()
        pygame.display.update()
        pygame.display.set_caption("Snake Game")


    def printMessage(self, str, num):
        font = pygame.font.SysFont(None, num)
        message = font.render(str, True, self.orange_color)
        self.screen.blit(message, [self.screen_width / 3, self.screen_height / 3])
        pygame.display.update()
        time.sleep(2)

    def Score(self):
        font = pygame.font.SysFont(None, 40)
        value = font.render("Your score is " + str(self.player.score), True, self.yellow_color)
        self.screen.blit(value, [0,0])

    def displayScreen(self):
        self.screen.fill(self.white_color)
        self.player.draw(self.screen, self._snake_surf)
        self.apple.draw(self.screen, self._apple_surf)
        self.Score()
        pygame.display.update()

    def play(self):
        self.createScreen()
        while(self._running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    self.printMessage("You Ended The Game", 50)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.moveRight()
                    if event.key == pygame.K_LEFT:
                        self.player.moveLeft()
                    if event.key == pygame.K_UP:
                        self.player.moveUp()
                    if event.key == pygame.K_DOWN:
                        self.player.moveDown()
                self.player.updatePlayerPosition()

            if self.endGame() == True:
                self._running = False
                self.printMessage("You lost ", 100)

            self.displayScreen()
            if self.apple.food_x == self.player.x[0] and self.apple.food_y == self.player.y[0]:
                self.score += 1
                self.player.len += 1
                self.apple.change(self.screen_width, self.screen_height)

            self.clock.tick(self.player.move)

        pygame.quit()

if __name__ == '__main__':
    Screen = Screen()
    Screen.play()