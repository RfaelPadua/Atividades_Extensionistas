import pygame
import sys
import random
import time
from Questoes import *


materia_cont_perguntas = [0, 0]
materia_cont_rodadas = [0, 0]
points = 0

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
    global questions, materia_cont_perguntas, materia_cont_rodadas

    def __init__(self):
        super().__init__()


    def draw_text_quiz(text, color, x, y):
        global fonte2
        
        img = fonte2.render(text, True,color)
        img_rect = img.get_rect(midleft=(x, y))
        tela.blit(img, img_rect)


    def pergunta(self):

        palavras_pergunta = [palavra.split(' ') for palavra in questions[materia][materia_cont_perguntas[materia]][0].splitlines()]
        espaco = fonte.size(' ')[0]
        x, y = 250,190

        for linha in palavras_pergunta:
            for palavra in linha:
                palavra_superficie = fonte2.render(palavra, True, (255, 255, 255))
                palavra_largura, palavra_altura = palavra_superficie.get_size()
                if x + palavra_largura >= 950:
                    x = 250
                    y += palavra_altura
                palavra_rect = palavra_superficie.get_rect()
                palavra_rect.midleft = (x, y)
                tela.blit(palavra_superficie, palavra_rect)
                x += palavra_rect.width + espaco


        

    def botao_alternativa(self, x, y, image, scale):
        global clicou, materia
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect(center = (x, y))
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if clicou and self.clicked == False:
                self.clicked = True
                action = True
                clicou = False
    
                    
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        tela.blit(self.image, (self.rect.x, self.rect.y))
        
        return action

    
    def alternativa(self):
        global materia_cont_perguntas, points, materia
        A = [350, 450]  # Coordenadas alteradas
        B = [850, 450]  # Coordenadas alteradas
        C = [350, 625]  # Coordenadas alteradas
        D = [850, 625]  # Coordenadas alteradas

        if self.botao_alternativa(self, A[0], A[1], botao, 0.7):
            if questions[materia][materia_cont_perguntas[materia]][5] == 1:
                som_acertou.play()
                materia_cont_perguntas[materia] += 1
                points += 1
                print(points)
            else:
                materia_cont_perguntas[materia] += 1
                som_erro.play()
                

        self.draw_text_quiz('A. ', (0, 0, 0), A[0]-130, A[1])
        self.draw_text_quiz(questions[materia][materia_cont_perguntas[materia]][1], (0, 0, 0), A[0]-90, A[1])

        if self.botao_alternativa(self, B[0], B[1], botao, 0.7):  # Coordenadas alteradas
            if questions[materia][materia_cont_perguntas[materia]][5] == 2:
                som_acertou.play()
                materia_cont_perguntas[materia] += 1
                points += 1
                print(points)
            else:
                materia_cont_perguntas[materia] += 1
                print(points)
                som_erro.play()


        self.draw_text_quiz('B. ', (0, 0, 0), B[0]-130, B[1])  # Coordenadas alteradas
        self.draw_text_quiz(questions[materia][materia_cont_perguntas[materia]][2], (0, 0, 0), B[0]-90, B[1])  # Coordenadas alteradas

        if self.botao_alternativa(self, C[0], C[1], botao, 0.7):  # Coordenadas alteradas
            if questions[materia][materia_cont_perguntas[materia]][5] == 3:
                som_acertou.play()
                materia_cont_perguntas[materia] += 1
                points += 1
                print(points)
            else:
                materia_cont_perguntas[materia] += 1
                print(points)
                som_erro.play()

        self.draw_text_quiz('C. ', (0, 0, 0), C[0]-130, C[1])  # Coordenadas alteradas
        self.draw_text_quiz(questions[materia][materia_cont_perguntas[materia]][3], (0, 0, 0), C[0]-90, C[1])  # Coordenadas alteradas

        if self.botao_alternativa(self, D[0], D[1], botao, 0.7):  # Coordenadas alteradas
            if questions[materia][materia_cont_perguntas[materia]][5] == 4:
                som_acertou.play()
                materia_cont_perguntas[materia] += 1
                points += 1
                print(points)
            else:
                materia_cont_perguntas[materia] += 1
                print(points)
                som_erro.play()

        self.draw_text_quiz('D. ', (0, 0, 0), D[0]-130, D[1])  # Coordenadas alteradas
        self.draw_text_quiz(questions[materia][materia_cont_perguntas[materia]][4], (0, 0, 0), D[0]-90, D[1])  # Coordenadas alteradas

       

    def pontuacao(self):
        global points
        # self.draw_text_quiz('Pontuação: ' + str(points), (0, 0, 0), 0, 600)

    def update(self):
        global status_jogo, points, materia_cont_perguntas, materia_cont_rodadas

        if materia_cont_perguntas[materia] - materia_cont_rodadas[materia]*10 == 10:
            materia_cont_rodadas[materia] += 1
            status_jogo = 'fim'
        
        
        self.pergunta(self=Quiz)
        self.alternativa(self=Quiz)
        self.pontuacao(self=Quiz)


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
som_acertou = pygame.mixer.Sound('audios/Som_acerto.mp3')
som_erro = pygame.mixer.Sound('audios/Som_erro.mp3')
pygame.display.set_caption('Quiz')
relogio = pygame.time.Clock()
status_jogo = 'inicio'
materia = 0

points = 0
clicou = False
fonte = pygame.font.Font('font/Silkscreen-Regular.ttf', 48)
fonte_outline = pygame.font.Font('font/Silkscreen-Regular.ttf', 48)
fonte2 = pygame.font.Font('font/Chalk Board.ttf',52)

background_inicio = pygame.image.load('imagens/Tela_Inicial.jpg').convert()
background_inicio = pygame.transform.scale(background_inicio, (1200, 675))
background_quiz = pygame.image.load('imagens/Quiz.jpg').convert()
background_quiz = pygame.transform.scale(background_quiz, (1200, 675))
botao = pygame.image.load('imagens/botao_menu2.png').convert_alpha()

botao_menu = Botao_menu(600, 380, botao, 0.93, 0)
botao_voltar = Botao_menu(150, 600, botao, 0.7, 0)
botao_matematica = Botao_menu(600, 380, botao, 0.93, 0)
botao_geografia = Botao_menu(600, 485, botao, 0.93, 1)

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
            materia = 0
        if botao_geografia.draw(tela):
            hit_sound.play()
            status_jogo = 'jogando'
            materia = 1
        if botao_voltar.draw(tela):
            hit_sound.play()
            status_jogo = 'inicio'
        
        draw_text('Matemática', (0, 0, 0), 600, 380)
        draw_text('Geografia', (0, 0, 0), 600, 485)
        draw_text('Voltar', (0, 0, 0), 150, 600)
        pygame.display.update()
    
    elif status_jogo == 'jogando':
        tela.blit(background_quiz, (0, 0))
        
        print(materia)
        for materias in materia_cont_perguntas:
            if materia >= 50:
                materia = 0
        
        Quiz.update(self=Quiz)
        pygame.display.update()
        
    elif status_jogo == 'fim':
        tela.blit(background_inicio, (0, 0))
        draw_text('Fim de jogo', (0, 0, 0), 600, 380)
        draw_text('Pontuação: ' + str(points), (0, 0, 0), 600, 485)
        
        if botao_voltar.draw(tela):
            hit_sound.play()
            status_jogo = 'inicio'
            points = 0
        draw_text('Voltar', (0, 0, 0), 150, 600)
        pygame.display.update()
    