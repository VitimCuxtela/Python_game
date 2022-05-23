import pygame #sumonando a biblioteca pygame
import random

black = (0, 0, 0) 
red = (255, 0, 0)
blue = (0, 0, 200)

pygame.init()

x = 1280
y = 720
pontos = 0

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Colisão")

pos_x = 500
pos_y = 360

pos_r_x = 600
pos_r_y = 400

pos_r_x = random.randint(100,1000)
pos_r_y = random.randint(100,680)

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.fill(black)
    fonte = pygame.font.Font(None,48)
    texto = fonte.render("Pontos:"+str(pontos),True,red,blue)
    screen.blit(texto,[30,150])

    tecla = pygame.key.get_pressed()
    if tecla [pygame.K_UP] and pos_y > 1:
        pos_y -= 1
    if tecla [pygame.K_DOWN] and pos_y < 620:
        pos_y += 1
    if tecla [pygame.K_LEFT] and pos_x > 1:
        pos_x -= 1
    if tecla [pygame.K_RIGHT] and pos_x < 1180:
        pos_x += 1

    if tecla [pygame.K_w] and pos_r_y > 1:
        pos_r_y -= 1
    if tecla [pygame.K_s] and pos_r_y < 620:
        pos_r_y += 1
    if tecla [pygame.K_a] and pos_r_x > 1:
        pos_r_x -= 1
    if tecla [pygame.K_d] and pos_r_x < 1180:
        pos_r_x += 1

    ret1 = pygame.draw.rect(screen,red,(pos_x,pos_y,100,100))
    ret2 = pygame.draw.rect(screen,blue,(pos_r_x,pos_r_y,100,100))

    if ret1.colliderect(ret2):
        pos_r_x = random.randint(100,1100)
        pos_r_y = random.randint(100,680)
        pontos +=1

        print("Colidiu")

    pygame.display.update()