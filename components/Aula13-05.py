import pygame # importação da biblioteca para a criação dos games
# a biblioteca pygame contém todos as estruturas necessáras para fazer o game funcionar.



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
nave1 = pygame.image.load('images/jato.png').convert_alpha()# carregando a nave1 
nave1 = pygame.transform.scale(nave1,(50,50))# ajustando o tamanho da nave1

nave2 = pygame.image.load('images/nave1.png').convert_alpha() # carregando a nave2 
nave2 = pygame.transform.scale(nave2,(50,50))# ajustando o tamanho da nave1


#posicionando as naves de acordo com o plano cartesiano.
#Poscionando a nave1 em relação ao eixo x e y 
pos_nave1_x = 500
pos_nave1_y = 360

pos_nave2_y = 500
pos_nave2_x = 360

#execução do jogo - rodando
rodando = True
#funções
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
  if tecla[pygame.K_UP] and pos_nave1_y > 1:
    pos_nave1_y -= 1    
  if tecla[pygame.K_DOWN] and pos_nave1_y < 665:
    pos_nave1_y += 1
  if tecla[pygame.K_LEFT] and pos_nave1_x > 1:
    pos_nave1_x -= 1
  if tecla[pygame.K_RIGHT] and pos_nave1_x < 1230:
    pos_nave1_x += 1
 
  if tecla[pygame.K_w] and pos_nave2_y > 1:
    pos_nave2_y -= 1    
  if tecla[pygame.K_s] and pos_nave2_y < 665:
    pos_nave2_y += 1
  
  if tecla[pygame.K_a] and pos_nave2_x > 1:
    pos_nave2_x -= 1
  if tecla[pygame.K_d] and pos_nave2_x < 1230:
    pos_nave2_x += 1
  
  #posiciona os personagens 
  screen.blit(nave1,(pos_nave1_x,pos_nave1_y))
  screen.blit(nave2,(pos_nave2_x,pos_nave2_y))
  

  pygame.display.update()