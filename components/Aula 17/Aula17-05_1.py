from asyncio import events
from turtle import Screen, position
import pygame #sumonando a biblioteca pygame

#definição de cores

black = (0, 0, 0)
red = (250, 0, 0)

#iniciando o código
pygame.init()

altura = 480
largura = 640

screen = pygame.display.set_mode((largura,altura)) #Criando a tela
pygame.display.set_caption("Bolinha") #Nome do aplicativo
#posição de bolinha
posicao_x = 300
posicao_y = 200
velocidade_x = 1
velocidade_y = 1

#Iniciando o jogo
rodando = True #Variável segura o jogo aberto

#Cria o loop que mantém o game aberto
while rodando:
    event = pygame.event.poll() #comando que guarda a  interação do usuário
    if event.type == pygame.QUIT: #confere se o usuário clicou no X para fechar
        break #Sair do jogo
    #movimentação da bolinha
    posicao_x += velocidade_x
    posicao_y += velocidade_y

    #mudanddo a direção da bolinha em X
    if posicao_x > 600:
        velocidade_x =- 1
    elif posicao_x < 0:
        velocidade_x =+ 1

    #mudanddo a direção da bolinha em Y
    if posicao_y > 440:
        velocidade_y =- 1
    elif posicao_y < 0:
        velocidade_y =+ 1

    screen.fill(black) #comando que preenche a tela com a cor escolhida

    pygame.draw.ellipse(screen,red,(posicao_x,posicao_y,40,40))

    pygame.display.flip() #mantém a tela do jogo atualizada