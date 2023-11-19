import pygame
import sys
import random
import time
from Questoes import questions




# Classe para criar os botões do menu
class Botao_menu(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale, type):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.type = type
    
    def draw(self, surface):
        global materia, clicou
        action = False
		#posição do mouse
        pos = pygame.mouse.get_pos()

		#checar se o mouse está em cima do botão e se foi clicado
        if self.rect.collidepoint(pos):
            if clicou and self.clicked == False:
                self.clicked = True
                action = True
                materia = type
                clicou = False
                pygame.time.delay(100)

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

		#desenhar o botão
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

# Classe para criar os botões das respostas
class Quiz(pygame.sprite.Sprite):
    global alternativas_ordem, questions, questao_atual
    questao_atual = random.randint(0,len(questions))

    alternativas_ordem = [0, 1, 2, 3]
    # random.shuffle(alternativas_ordem)
    def __init__(self):
        super().__init__()
    def draw_text_quiz(text, color, x, y):
        global fonte
        img = fonte.render(text, True, color)
        img_rect = img.get_rect(midleft=(x, y))
        tela.blit(img, img_rect)


    def pergunta(self):
        self.draw_text_quiz(questions[questao_atual][0], (0, 0, 0), 0, 40)

    # def botao_alternativa(self):
        
    def alternativa(self):
       
        botao_alternativa = Botao_menu(40, 300, botao, 0.93, 'Matematica')
        
        self.draw_text_quiz('A. ', (0, 0, 0), 0, 300)
        self.draw_text_quiz(questions[questao_atual][1], (0, 0, 0), 40, 300)

        self.draw_text_quiz('B. ', (0, 0, 0), 0, 350)
        self.draw_text_quiz(questions[questao_atual][2], (0, 0, 0), 40, 350)

        self.draw_text_quiz('C. ', (0, 0, 0), 0, 400)
        self.draw_text_quiz(questions[questao_atual][3], (0, 0, 0), 40, 400)

        self.draw_text_quiz('D. ', (0, 0, 0), 0, 450)
        self.draw_text_quiz(questions[questao_atual][4], (0, 0, 0), 40, 450)


    def update(self): 
        self.pergunta(self=Quiz)
        self.alternativa(self=Quiz)

        
        


def draw_text(text, color, x, y):
    global fonte_outline
    img = fonte.render(text, True, color)
    img_rect = img.get_rect(center=(x, y))
    img_sombra = fonte_outline.render(text, True, (0,0,0))
    img_rect_sombra = img.get_rect(center=(x, y))
    tela.blit(img_sombra, img_rect_sombra)
    tela.blit(img, img_rect)

# Inicializando o pygame
pygame.init()
pygame.mixer.init()
tela = pygame.display.set_mode((1200, 675))
hit_sound = pygame.mixer.Sound('audios/hit.wav')
pygame.display.set_caption('Quiz')
relogio = pygame.time.Clock()
status_jogo = 'inicio'
materia = ''
clicou = False
fonte = pygame.font.SysFont('Calibri Bold', 48)
fonte_outline = pygame.font.SysFont('Calibri Bold', 48)

background_inicio = pygame.image.load('imagens/background1.png').convert()
background_inicio = pygame.transform.scale(background_inicio, (1200, 675))
background_quiz = pygame.image.load('imagens/background.png').convert()
background_quiz = pygame.transform.scale(background_quiz, (1200, 675))
botao = pygame.image.load('imagens/botao_menu2.png').convert_alpha()

botao_menu = Botao_menu(600, 380, botao, 0.93, '')
botao_voltar = Botao_menu(150, 600, botao, 0.5, '')
botao_matematica = Botao_menu(600, 380, botao, 0.93, 'Matematica')
botao_geografia = Botao_menu(600, 485, botao, 0.93, 'Geografia')

while True:
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicou = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicou = False


    if status_jogo == 'inicio':
        tela.blit(background_inicio, (0, 0))
    
        if botao_menu.draw(tela):
            hit_sound.play()
            status_jogo = 'menu'


        draw_text('Jogar', (0 ,0 , 0), 600, 380)
        pygame.display.update()
        
    elif status_jogo == 'menu':
        tela.blit(background_inicio, (0, 0))

        if botao_matematica.draw(tela):
            hit_sound.play()
            status_jogo = 'jogando'
            materia = 'Matematica'
        if botao_geografia.draw(tela):
            hit_sound.play()
            status_jogo = 'jogando'
            materia = 'Geografia'
        if botao_voltar.draw(tela):
            hit_sound.play()
            status_jogo = 'inicio'
        
        draw_text('Matemática', (0, 0, 0), 600, 380)
        draw_text('Geografia', (0, 0, 0), 600, 485)
        draw_text('Voltar', (0, 0, 0), 150, 600)
        pygame.display.update()
    
    elif status_jogo == 'jogando':
        tela.blit(background_quiz, (0, 0))



        Quiz.update(self=Quiz)

        pygame.display.update()