import pygame

#definindo cores
preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
verde =(0,255,0)
azul = (0,0,255)

#definindo pi 
pi = 3.1416
pygame.init()

#criando a janela
janela = pygame.display.set_mode((500,400))
pygame.display.set_caption("Figuras e Textos")

#preenchendo a janela com uma cor
janela.fill(branco)
#trabalhando com texto
fonte = pygame.font.Font(None,48)
texto = fonte.render("Olá, mundo!",True,branco,azul)
janela.blit(texto,[30,150])
#figuras
pygame.draw.line(janela,verde,(60,260),(420,260),10)
pygame.draw.polygon(janela,preto,((191,206),(236,277),(156,277)),0)
pygame.draw.circle(janela,azul,(300,50),20,0)
pygame.draw.ellipse(janela,vermelho,(400,250,40,80),1)
pygame.draw.rect(janela,verde,(20,20,60,40),0)
pygame.draw.arc(janela,vermelho,[250,75,150,125],pi/2,3*pi/2,2)
pygame.draw.arc(janela,preto,[250,75,150,125],-pi/2.-pi/2,2)


#mostrando a tela
pygame.display.update()

deve_continuar = True
while deve_continuar:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      deve_continuar = False
    
  
pygame.quit()