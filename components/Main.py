import pygame # importação da biblioteca para a criação dos games
# a biblioteca pygame contém todos as estruturas necessáras para fazer o game funcionar.

import random # importação da biblioteca responsável pela criação de números aleatórios

pygame.init() # comando para iniciar a biblioteca para acesso aos comandos.

#definição do tamanho da tela do game utilizando pixels
x = 1280
y = 720
#preparando a tela para receber o background
screen = pygame.display.set_mode((x,y)) # passando o tamanho da tela para a criação da janela.
pygame.display.set_caption('Meu Jogo em Python')# título da janela
#carregando os "plano de fundo".
bg = pygame.image.load('images/bg.jpg').convert_alpha() # carregando o background (fundo)
bg = pygame.transform.scale(bg,(x,y))# padronizando o background com o mesmo tamanho da janela.
#carregando as naves - personagens
nave1 = pygame.image.load('images/nave1.png').convert_alpha()# carregando a nave1 
nave1 = pygame.transform.scale(nave1,(50,50))# ajustando o tamanho da nave1
nave2 = pygame.image.load('images/nave2.png').convert_alpha() # carregando a nave2 
nave2 = pygame.transform.scale(nave2,(50,50))# ajustando o tamanho da nave2
#carregando a imagem do missil
missil = pygame.image.load('images/missil.png').convert_alpha()# carregando a imagem do míssil.
missil = pygame.transform.scale(missil,(25,25))# ajustando o tamanho do míssil

#posicionando as naves de acordo com o plano cartesiano.
#Poscionando a nave1 em relação ao eixo x e y 
pos_nave1_x = 500
pos_nave1_y = 360
#Poscionando a nave2 em relação ao eixo x e y
pos_nave2_x = 200
pos_nave2_y = 300
#Poscionando  o míssil em relação ao eixo x e y
vel_x_missil = 0 #ajustando a velocidade do míssil para 0
pos_x_missil = 220
pos_y_missil = 311

#Definição das funções que irão controlar:
#disparo do missil - triggered
#execução do jogo - rodando
triggered = False
rodando = True

#funções

#função para posicionar a nave2 aleatoriamente.
def respawn(): #o comando def cria uma função, no caso chamada aqui de respawn
  x = 1350 # dentro dessa função o x recebe o valor de 1350 representando o limite da tela
  y = random.randint(1,640) # y recebe um número entre 1 e 640 criando o mecanismo de 
  #permitir que a nave1 apareça em lugares diferentes
  return [x,y]

#Função para recarregar o míssil
def respawn_missil():# criação da função
  triggered = False #disparo recebe o valor falso
  respawn_missil_x = pos_nave2_x +20 #ajuste da posição em x
  respawn_missil_y = pos_nave2_y +11 #ajuste da posição em y
  vel_x_missil = 0 #ajuste da velocidade para 0
  return[respawn_missil_x,respawn_missil_y,triggered, vel_x_missil] #retorno dos valores


#trecho abaixo responsável pela execução do jogo.
while rodando: #mantém a janela aberta
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      rodando = False
  screen.blit(bg,(0,0))#inicia o background

  rel_x = x % bg.get_rect().width
  screen.blit(bg,(rel_x - bg.get_rect().width,0))# cria background
  if rel_x < 1280:
    screen.blit(bg, (rel_x,0))

  #teclas de movimentação
  tecla = pygame.key.get_pressed()
  if tecla[pygame.K_UP] and pos_nave2_y > 1:
    pos_nave2_y -= 1
    if not triggered:
      pos_y_missil -=1
  if tecla[pygame.K_DOWN] and pos_nave2_y < 665:
    pos_nave2_y += 1
    if not triggered:
      pos_y_missil +=1  
  #movimentação do missil
  if tecla[pygame.K_SPACE]:
    triggered = True
    vel_x_missil = 1


  #condicional para o respawn
  if pos_nave1_x == 50:
    pos_nave1_x = respawn()[0]
    pos_nave1_y = respawn()[1]
  
  #Condicional para recarregar o missil
  if pos_x_missil == 1300:
      pos_x_missil, pos_y_missil, triggered, vel_x_missil = respawn_missil() 
  

  #movimento
  x-=0.5
  #posicionamento da nave1
  pos_nave1_x -=1
  #posicionamento do missil
  pos_x_missil += vel_x_missil
  #posiciona os personagens 
  screen.blit(nave1,(pos_nave1_x,pos_nave1_y))
  screen.blit(missil,(pos_x_missil,pos_y_missil))
  screen.blit(nave2,(pos_nave2_x,pos_nave2_y))

  pygame.display.update()