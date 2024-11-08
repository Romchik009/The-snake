import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
red = (255, 0, 0)
black = (0, 0, 0)
green = (137, 172, 118)
blue = (0, 255, 255)

dis_widht = 600
dis_height = 500
dis = pygame.display.set_mode((dis_widht, dis_height))

pygame.display.set_capcion('Snake')
clock = pygame.time.Clock()
snake_block = 10
snack_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Ваш счет:" + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_List):
    for x in snake_List: 
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def messege(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_widht / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_widht / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Lenght_of_snake = 1
    foodx = round(random.randrange(0, dis_widht - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 
    while not game_over: 
        while game_close == True: 
            dis.fill(blue)
            messege("Вы проиграли нажмите Q для выхода или C для повторной игры", red)
            Your_score(Lenght_of_snake - 1)
pygame.display.update()
for event in pygame.event.get(): 
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q: 
            game_over = True
            game_close = False
        if event.key == pygame.K_c: 
            gameLoop()
for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
        game_over = True
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_LEFT: 
            x1_change = -snake_block
            y1_change = 0
        elif event.key == pygame.K_RIGHT: 
            x1_change = snake_block
            y1_change = 0
        elif event.key == pygame.K_UP: 
            x1_change = -snake_block
            y1_change = 0
        elif event.key == pygame.K_DOWN: 
            x1_change = snake_block
            y1_change = 0
    if x1 >= dis_widht or x1_change < 0 or y1_change >= dis_height or y1_change < 0: 
        game_close = True
        x1_change += x1_change
        y1_change += y1_change
        dis.fill(blue)
pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) 
snake_Head = [] 
snake_Head.append(x1_change) 
snake_Head.append(y1_change) 
snake_List.append(snake_Head) 
if len(snake_List) > Length_of_snake: 
    del snake_List[0]
for x in snake_List[:-1]: 
    if x == snake_Head: 
        game_close = True
our_snake(snake_block, snake_List)
Your_score(Lenght_of_snake - 1)
pygame.display.update()
if x1_change == foodx and y1_change == foody: 
    foodx = round(random.randrange(0, dis_widht - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 
    Lenght_of_snake += 1
clock.tick(snack_speed)
pygame.quit()
quit()
gameLoop()


*это конечный код*

