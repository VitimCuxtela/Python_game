import pygame,time

#definindo cores
preto = (0,0,0)
amarelo = (255,255,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

#definindo outras constantes do jogo

largurajanela = 500
alturajanela = 400 

#definindo a função mover
def mover (figura,dim_janela):
  borda_esquerda = 0
  borda_superior = 0
  borda_direita = dim_janela[0]
  borda_inferior = dim_janela[1]
  if figura['objRect'].top < borda_superior or figura['objRect'].bottom > borda_inferior:
    figura['vel'][1] = -figura['vel'][1]
  if figura['objRect'].left < borda_esquerda or figura['objRect'].right > borda_direita:
    figura['vel'][0] = -figura['vel'][0]
  figura['objRect'].x += figura['vel'][0]
  figura['objRect'].y += figura['vel'][1]

pygame.init()

janela = pygame.display.set_mode((largurajanela,alturajanela))
pygame.display.set_caption("animação")

#figuras

f1 = {'objRect':pygame.Rect(300,80,40,80),'cor':vermelho,'vel':[0,-5],'forma':'ELIPSE'}
f2 = {'objRect':pygame.Rect(200,200,20,20),'cor':verde,'vel':[5,5],'forma':'ELIPSE'}
f3 = {'objRect':pygame.Rect(100,150,60,60),'cor':azul,'vel':[-5,5],'forma':'RETANGULO'}
f4 = {'objRect':pygame.Rect(200,150,80,40),'cor':amarelo,'vel':[5,0],'forma':'ELIPSE'}
figuras = [f1,f2,f3,f4]

deve_continuar = True
while deve_continuar:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      deve_continuar = False

#preenchendo a cor do fundo
  janela.fill(preto)

  for figura in figuras:
    #posicionando a figura
    mover(figura,(largurajanela,alturajanela))

  #desenhando a figura na janela
    if figura['forma'] == 'RETANGULO':
      pygame.draw.rect(janela,figura['cor'],figura['objRect'])
    elif figura['forma'] == 'ELIPSE':
       pygame.draw.ellipse(janela,figura['cor'],figura['objRect'])
  
  #atualizando a tela
    pygame.display.update()

  #esperando 2 segundos
    time.sleep(0.02)
pygame.quit()