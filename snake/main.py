#Library
import pygame
from pygame import Vector2
import random
import time
import sys
#Snake
class Snake:
    def __init__(self):
        #Body
        self.body = [Vector2(40, 120), Vector2(80, 120), Vector2(120, 120)]
        self.direction = Vector2(0,0)
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
                if self.body[len(self.body) - 1] == self.body[len(self.body) - 2] + Vector2(40, 0):
                    screen.blit(self.head_right, rectangle)
                elif self.body[len(self.body) - 1] == self.body[len(self.body) - 2] + Vector2(0, 40):
                    screen.blit(self.head_down, rectangle)
                elif self.body[len(self.body) - 1] == self.body[len(self.body) - 2] + Vector2(-40, 0):
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
        if self.direction == Vector2(0, 0):
            return
        if self.eat:
            newBody = self.body[:]
            self.eat = False
        else:
            newBody = self.body[1:]
        newBody.append(newBody[-1] + self.direction)
        self.body = newBody[:]
    def reset(self):
        self.direction = Vector2(0,0)
        self.body = [Vector2(40, 120), Vector2(80, 120), Vector2(120, 120)]
        self.eat = False

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
        #Initial Score
        self.score = 0
        #Initial High Score
        self.high_score = 0
    def highScore(self):
        file = open("./snake/score/score.txt", "r")
        self.high_score = int(file.read())
        file.close()
    def updateScore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("./snake/score/score.txt", "w")
            file.write(str(self.high_score))
            file.close()
    def drawScore(self):
        #Adapt
        x = 30
        x1 = 0
        if self.score >= 100 or self.high_score >= 100:
            x = 45
            x1 = 10
        #Current Score
        score_surface = FONT.render(str(self.score), True, (56, 74, 12))
        new_score_surface = FONT.render(str(self.high_score), True, (56, 74, 12))
        position = Vector2(CELL_SIZE * CELL_NUMBER - 60 + x1, CELL_SIZE * CELL_NUMBER - 40)
        rectangle = score_surface.get_rect(center = (position))
        apple_rectangle = self.fruit.FRUIT_IMAGE.get_rect(midright = Vector2(CELL_SIZE * CELL_NUMBER - 70, CELL_SIZE * CELL_NUMBER - 40))
        bg_rectangle = pygame.Rect(apple_rectangle.left, apple_rectangle.top, apple_rectangle.width + x, apple_rectangle.height)
        pygame.draw.rect(screen, (56, 74, 12), bg_rectangle, 2)
        screen.blit(score_surface, rectangle)
        screen.blit(self.fruit.FRUIT_IMAGE, apple_rectangle)
        #Best Score
        new_position = Vector2(CELL_SIZE * CELL_NUMBER - 60 + x1, CELL_SIZE * CELL_NUMBER - 40 - apple_rectangle.height)
        new_rectangle = new_score_surface.get_rect(center = new_position)
        new_apple_rectangle = self.fruit.FRUIT_IMAGE.get_rect(midright = Vector2(CELL_SIZE * CELL_NUMBER - 70, CELL_SIZE * CELL_NUMBER - 40 - apple_rectangle.height - 1))
        new_bg_rectangle = pygame.Rect(new_apple_rectangle.left, new_apple_rectangle.top, new_apple_rectangle.width + x, new_apple_rectangle.height)
        pygame.draw.rect(screen, (56, 74, 12), new_bg_rectangle, 2)
        screen.blit(new_score_surface, new_rectangle)
        screen.blit(self.fruit.FRUIT_IMAGE, new_apple_rectangle)
        #Letter
        letter = FONT.render("B", True, (56, 74, 12))
        letter_rectangle = self.fruit.FRUIT_IMAGE.get_rect(center = Vector2(CELL_SIZE * CELL_NUMBER - 76, CELL_SIZE * CELL_NUMBER - 35 - apple_rectangle.height))
        screen.blit(letter, letter_rectangle) 
    def update(self):
        self.highScore()
        #Fail
        game.fail()
        #Move Snake
        self.snake.moveSnake()
        #Check Collision
        self.collision()
        #Score
        self.updateScore()
    def draw(self):
        #Grass
        self.grass()
        #Draw Objects
        self.snake.drawSnake()
        self.fruit.drawFruit()
        #Score
        self.drawScore()
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
            self.score += 1
            #High Score
            self.updateScore()
            self.snake.eat = True
            sound = pygame.mixer.Sound(EAT_SOUND)
            sound.play()
    def fail(self):
        #Walls
        if not (0 <= self.snake.body[-1].x + self.snake.direction[0] <= 760 and 0 <= self.snake.body[-1].y + self.snake.direction[1] <= 760):
            sound = pygame.mixer.Sound(WALL_COLLISION_SOUND)
            sound.play()
            self.gameOver()
        #Body
        for cell in self.snake.body[:-1]:
            if self.snake.body[-1] + self.snake.direction == cell:
                sound = pygame.mixer.Sound(STEP_SOUND)
                sound.play()
                self.gameOver()
                break
    def gameOver(self):
        self.score = 0
        self.snake.reset()
#Pygame Init
pygame.init()
#Mixer
pygame.mixer.init()
#Font
FONT_SOURCE = "./snake/fonts/font.ttf"
#Font Object
FONT = pygame.font.Font(FONT_SOURCE, 25)
#Sounds
EAT_SOUND = "./snake/sounds/crunch.wav"
WALL_COLLISION_SOUND = "./snake/sounds/wall_collision.wav"
STEP_SOUND = "./snake/sounds/step.wav"
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
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and game.snake.body[-1] + Vector2(0, -40) != game.snake.body[-2]:
                    game.snake.direction = Vector2(0, -40)
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and game.snake.body[-1] + Vector2(0, 40) != game.snake.body[-2]:
                    game.snake.direction = Vector2(0, 40)
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and game.snake.body[-1] + Vector2(40, 0) != game.snake.body[-2]:
                    game.snake.direction = Vector2(40, 0)
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and game.snake.body[-1] + Vector2(-40, 0) != game.snake.body[-2]:
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