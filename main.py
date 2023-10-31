#Library
import pygame
from pygame import Vector2
import random
import sys
#Snake
class Snake:
    def __init__(self):
        #Body
        self.body = [Vector2(0, 0), Vector2(40, 0), Vector2(80, 0)]
        self.direction = Vector2(40,0)
        self.eat = False
        #Snake Images
        #Head
        self.head_up = pygame.image.load("./snake/graphics/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("./snake/graphics/head_down.png").convert_alpha()
        self.head_left = pygame.image.load("./snake/graphics/head_left.png").convert_alpha()
        self.head_right = pygame.image.load("./snake/graphics/head_right.png").convert_alpha()
        #Tail
        self.tail_up = pygame.image.load("./snake/graphics/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("./snake/graphics/tail_down.png").convert_alpha()
        self.tail_left = pygame.image.load("./snake/graphics/tail_left.png").convert_alpha()
        self.tail_right = pygame.image.load("./snake/graphics/tail_right.png").convert_alpha()
        #Body
        self.body_vertical = pygame.image.load("./snake/graphics/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("./snake/graphics/body_horizontal.png").convert_alpha()
        #Body Movements
        self.body_bl = pygame.image.load("./snake/graphics/body_bl.png").convert_alpha()
        self.body_br = pygame.image.load("./snake/graphics/body_br.png").convert_alpha()
        self.body_tl = pygame.image.load("./snake/graphics/body_tl.png").convert_alpha()
        self.body_tr = pygame.image.load("./snake/graphics/body_tr.png").convert_alpha()
    def drawSnake(self):
        for index in range(len(self.body) - 1, -1, -1):
            #Rectangle
            rectangle = pygame.Rect(self.body[index].x, self.body[index].y, CELL_SIZE, CELL_SIZE)
            #Image
            if index == len(self.body) - 1:
                #Direction
                if self.direction == Vector2(40, 0):
                    screen.blit(self.head_right, rectangle)
                elif self.direction == Vector2(0, 40):
                    screen.blit(self.head_down, rectangle)
                elif self.direction == Vector2(-40, 0):
                    screen.blit(self.head_left, rectangle)
                else:
                    screen.blit(self.head_up, rectangle)
            elif index == 0:
                #Direction
                if self.body[1] == self.body[0] + Vector2(40, 0):
                    screen.blit(self.tail_left, rectangle)
                elif self.body[1] == self.body[0] + Vector2(0, 40):
                    screen.blit(self.tail_up, rectangle)
                elif self.body[1] == self.body[0] + Vector2(-40, 0):
                    screen.blit(self.tail_right, rectangle)
                else:
                    screen.blit(self.tail_down, rectangle)
            else:
                #Direction
                if self.body[index] == self.body[index - 1] + Vector2(40, 0):
                    if self.body[index] == self.body[index + 1] - Vector2(40, 0):
                        screen.blit(self.body_horizontal, rectangle)
                    elif self.body[index] == self.body[index + 1] - Vector2(0, 40):
                        screen.blit(self.body_bl, rectangle)
                    elif self.body[index] == self.body[index + 1] - Vector2(0, -40):
                        screen.blit(self.body_tl, rectangle)
                elif self.body[index] == self.body[index - 1] + Vector2(-40, 0):
                    if self.body[index] == self.body[index + 1] - Vector2(-40, 0):
                        screen.blit(self.body_horizontal, rectangle)
                    elif self.body[index] == self.body[index + 1] - Vector2(0, 40):
                        screen.blit(self.body_br, rectangle)
                    elif self.body[index] == self.body[index + 1] - Vector2(0, -40):
                        screen.blit(self.body_tr, rectangle)
                elif self.body[index] == self.body[index - 1] + Vector2(0, 40):
                    if self.body[index] == self.body[index + 1] - Vector2(0, 40):
                        screen.blit(self.body_vertical, rectangle)
                    elif self.body[index] == self.body[index + 1] - Vector2(40, 0):
                        screen.blit(self.body_tr, rectangle)
                    elif self.body[index] == self.body[index + 1] - Vector2(-40, 0):
                        screen.blit(self.body_tl, rectangle)
                else:
                    if self.body[index] == self.body[index + 1] - Vector2(0, -40):
                        screen.blit(self.body_vertical, rectangle)
                    elif self.body[index] == self.body[index + 1] - Vector2(40, 0):
                        screen.blit(self.body_br, rectangle)
                    elif self.body[index] == self.body[index + 1] - Vector2(-40, 0):
                        screen.blit(self.body_bl, rectangle)
    def moveSnake(self):
        if self.eat:
            newBody = self.body[:]
            self.eat = False
        else:
            newBody = self.body[1:]
        newBody.append(newBody[-1] + self.direction)
        self.body = newBody[:]

#Fruit
class Fruit:
    def __init__(self):
        #Starting Position
        self.x = 600
        self.y = 600
        self.position = Vector2(self.x, self.y)
        #Fruit Image
        self.FRUIT_IMAGE = pygame.image.load("./snake/graphics/fruit.png").convert_alpha()
    def generate(self):
        #Generate Fruit
        self.x = CELL_SIZE * random.randint(0, CELL_NUMBER - 1)
        self.y = CELL_SIZE * random.randint(0, CELL_NUMBER - 1)
        self.position = Vector2(self.x, self.y)
    def drawFruit(self):
        #Rectangle
        rectangle = pygame.Rect(self.position.x, self.position.y, CELL_SIZE, CELL_SIZE)
        #Draw
        screen.blit(self.FRUIT_IMAGE, rectangle)
#Logic
class Logic:
    def __init__(self):
        #Snake Object
        self.snake = Snake()
        #Fruit Object
        self.fruit = Fruit()
    def update(self):
        #Fail
        game.fail()
        #Move Snake
        self.snake.moveSnake()
        #Check Collision
        self.collision()
    def draw(self):
        #Grass
        self.grass()
        #Draw Objects
        self.snake.drawSnake()
        self.fruit.drawFruit()
    def grass(self):
        GRASS_COLOR = (167, 209, 69)
        for column in range(CELL_NUMBER):
            for row in range(CELL_NUMBER):
                if (column + row) % 2 == 0:
                    rectangle = pygame.Rect(column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, GRASS_COLOR, rectangle)
    def collision(self):
        if self.fruit.position == self.snake.body[-1]:
            #New fruit
            while self.fruit.position in self.snake.body:
                self.fruit.generate()
            #Add new cell
            self.snake.eat = True
    def fail(self):
        #Walls
        if not (0 <= self.snake.body[-1].x <= 760 and 0 <= self.snake.body[-1].y <= 760):
            self.gameOver()
        #Body
        for cell in self.snake.body[:-1]:
            if cell == self.snake.body[-1]:
                self.gameOver()
    def gameOver(self):
        pygame.quit()
        sys.exit()
#Pygame Init
pygame.init()
#Title
SCREEN_TITLE = "SNAKE"
pygame.display.set_caption(SCREEN_TITLE)
#Grid
CELL_SIZE = 40
CELL_NUMBER = 20
#Screen
SCREEN_WIDTH = CELL_SIZE * CELL_NUMBER
SCREEN_HEIGHT = CELL_SIZE * CELL_NUMBER
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Screen Color
SCREEN_COLOR = (175, 215, 70)
screen.fill(SCREEN_COLOR)
#Clock
FRAMERATE = 60
clock = pygame.time.Clock()
#Game Logic Object
game = Logic()
#User Timer
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
#Main
def main():
    running = True
    #Game Loop
    while running:
        #Events
        for event in pygame.event.get():
            #Quit
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == SCREEN_UPDATE:
                game.update()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and game.snake.direction != Vector2(0, 40):
                    game.snake.direction = Vector2(0, -40)
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and game.snake.direction != Vector2(0, -40):
                    game.snake.direction = Vector2(0, 40)
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and game.snake.direction != Vector2(-40, 0):
                    game.snake.direction = Vector2(40, 0)
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and game.snake.direction != Vector2(40, 0):
                    game.snake.direction = Vector2(-40, 0)
        #Screen Update
        screen.fill(SCREEN_COLOR)
        game.draw()
        pygame.display.update() 
        clock.tick(FRAMERATE)
    #Exit
    pygame.quit()
    sys.exit()
#Execution
if __name__ == "__main__":
    main()