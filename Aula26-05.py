import pygame

screen = pygame.display.set_mode((600,600))

# trabalhando com os objetos
# inserindo a imagem
nave1 = pygame.image.load('nave1.png')
# convertendo a imagem para um retangulo
nave1_rect = nave1.get_rect()
# variavel de velocidade de movimento
vel = 10
# criar um obstaculo
obstaculo = pygame.Rect(400,200,80,80)

#looping do jogo

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.fill((255,255,255))

    # movimentação
    controle = pygame.key.get_pressed()

    if controle[pygame.K_LEFT]:
        nave1_rect.x -= vel
    if controle[pygame.K_RIGHT];
        nave1_rect.x += vel
    if controle[pygame.UP]:
        nave1_rect.y -= vel
    if controle[pygame.K_DOWN]:
        nave1_rect.y += vel

    # posicionar os objetos
    screen.blit(nave1,nave1_rect)
    pygame.draw.rect(screen, (255,0,0), obstaculo,4)

    