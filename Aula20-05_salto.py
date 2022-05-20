# iniciando o projeto jump

import pygame
janela = pygame.display.set_mode((500,500))

x = 250
y = 250
raio = 15
vel_x = 10
vel_y = 10
jump = False

rodando = True
while rodando:
    janela.fill((0,0,0))
    pygame.draw.circle(janela,(255,255,255),(x,y),raio)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            rodando = False
    # movimentação
        controle = pygame.key.get_pressed()
    if controle[pygame.K_LEFT] and x > 0:
            x -= vel_x
    if controle[pygame.K_RIGHT] and x < 500:
            x += vel_x

    # jump - controle de salto
    if jump is False and controle[pygame.K_SPACE]:
            jump = True # ativa o salto
    if jump is True:
            y -= vel_y * 4
            vel_y -= 1
            if vel_y < -10:
                jump = False
                vel_y = 10
    pygame.time.delay(30)
    pygame.display.update()