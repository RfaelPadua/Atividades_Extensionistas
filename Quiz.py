import pygame
import sys
import json
from random import shuffle
from Questoes import *
from os import path


questions = questao
shuffle(questions[0])
shuffle(questions[1])
shuffle(questions[2])
enter = False


materia_cont_perguntas = [0, 0, 0, 0]
materia_cont_rodadas = [0, 0, 0, 0]
points = 0
materia = 0
user_name = ''



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
                clicou = False
                pygame.time.delay(100)

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

		#desenhar o botão
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

# Classe para criar os botões das respostas
class Quiz(pygame.sprite.Sprite):
    global questions, materia_cont_perguntas, materia_cont_rodadas, materia

    


    def __init__(self):
        super().__init__()


    def draw_text_quiz(text, color, x, y):
        global fonte_alternativa
        
        img = fonte_alternativa.render(text, True,color)
        img_rect = img.get_rect(midleft=(x, y))
        tela.blit(img, img_rect)


    def pergunta(self):
        
        palavras_pergunta = [palavra.split(' ') for palavra in questions[materia][materia_cont_perguntas[materia]][0].splitlines()]
        espaco = fonte2.size(' ')[0]
        x, y = 250,190

        for linha in palavras_pergunta:
            for palavra in linha:
                palavra_superficie = fonte2.render(palavra, True, (255, 255, 255))
                palavra_largura, palavra_altura = palavra_superficie.get_size()
                palavra_altura = 50
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

    def alternativas_certas_erradas(self, x, y, image, scale, questions, alternativa):
        
        string_alternativas = ['A. ', 'B. ', 'C. ', 'D. ']
        self.botao_alternativa(self, x, y, image, scale)
        self.draw_text_quiz(string_alternativas[alternativa-1], (0, 0, 0), x-175, y+10)
        self.draw_text_quiz(questions[materia][materia_cont_perguntas[materia]][alternativa], (0, 0, 0), x-135, y+10)
        pygame.display.update()

    
    def alternativa(self):
        global materia_cont_perguntas, points, materia
        
        clicou_alternativa = False
        
        A = [350, 480]  # Coordenadas alteradas
        B = [850, 480]  # Coordenadas alteradas
        C = [350, 580]  # Coordenadas alteradas
        D = [850, 580]  # Coordenadas alteradas

        

        if self.botao_alternativa(self, A[0], A[1], alternativa_botao, 0.7):
            certo = questions[materia][materia_cont_perguntas[materia]][5] == 1
            clicou_alternativa = True
            if certo:
                som_acertou.play()
                points += 1
                certo = True
            else:
                som_erro.play()
            
                

        self.draw_text_quiz('A. ', (0, 0, 0), A[0]-175, A[1]+10)
        self.draw_text_quiz(questions[materia][materia_cont_perguntas[materia]][1], (0, 0, 0), A[0]-135, A[1]+10)

        if self.botao_alternativa(self, B[0], B[1], alternativa_botao, 0.7):  # Coordenadas alteradas
            certo = questions[materia][materia_cont_perguntas[materia]][5] == 2
            clicou_alternativa = True
            if certo:
                som_acertou.play()
                points += 1
            else:
                som_erro.play()

        self.draw_text_quiz('B. ', (0, 0, 0), B[0]-175, B[1]+10)  # Coordenadas alteradas
        self.draw_text_quiz(questions[materia][materia_cont_perguntas[materia]][2], (0, 0, 0), B[0]-135, B[1]+10)  # Coordenadas alteradas

        if self.botao_alternativa(self, C[0], C[1], alternativa_botao, 0.7):  # Coordenadas alteradas
            clicou_alternativa = True
            if questions[materia][materia_cont_perguntas[materia]][5] == 3:
                som_acertou.play()
                points += 1
            else:
                som_erro.play()

        self.draw_text_quiz('C. ', (0, 0, 0), C[0]-175, C[1]+10)  # Coordenadas alteradas
        self.draw_text_quiz(questions[materia][materia_cont_perguntas[materia]][3], (0, 0, 0), C[0]-135, C[1]+10)  # Coordenadas alteradas

        if self.botao_alternativa(self, D[0], D[1], alternativa_botao, 0.7):  # Coordenadas alteradas
            clicou_alternativa = True
            if questions[materia][materia_cont_perguntas[materia]][5] == 4:
                som_acertou.play()
                points += 1
            else:
                som_erro.play()

        self.draw_text_quiz('D. ', (0, 0, 0), D[0]-175, D[1]+10)  # Coordenadas alteradas
        self.draw_text_quiz(questions[materia][materia_cont_perguntas[materia]][4], (0, 0, 0), D[0]-135, D[1]+10)  # Coordenadas alteradas

        if clicou_alternativa:
            if questions[materia][materia_cont_perguntas[materia]][5] == 1:
                self.alternativas_certas_erradas(self, A[0], A[1], alternativa_certa, 0.7, questions, 1)
            else:
                self.alternativas_certas_erradas(self, A[0], A[1], alternativa_errada, 0.7, questions, 1)
            
            if questions[materia][materia_cont_perguntas[materia]][5] == 2:
                self.alternativas_certas_erradas(self, B[0], B[1], alternativa_certa, 0.7, questions, 2)
            else:
                self.alternativas_certas_erradas(self, B[0], B[1], alternativa_errada, 0.7, questions, 2)
            
            if questions[materia][materia_cont_perguntas[materia]][5] == 3:
                self.alternativas_certas_erradas(self, C[0], C[1], alternativa_certa, 0.7, questions, 3)
            else:
                self.alternativas_certas_erradas(self, C[0], C[1], alternativa_errada, 0.7, questions, 3)
            
            if questions[materia][materia_cont_perguntas[materia]][5] == 4:
                self.alternativas_certas_erradas(self, D[0], D[1], alternativa_certa, 0.7, questions, 4)
            else:
                self.alternativas_certas_erradas(self, D[0], D[1], alternativa_errada, 0.7, questions, 4)
            
            
            materia_cont_perguntas[materia] += 1

            pygame.time.delay(1500)


    def pontuacao(self):
        global points
        # self.draw_text_quiz('Pontuação: ' + str(points), (0, 0, 0), 0, 600)

    def update(self):
        global status_jogo, points, materia_cont_perguntas, materia_cont_rodadas
        
        
        
        if materia_cont_perguntas[materia] > 50:
            materia_cont_perguntas[materia] = 0
            materia_cont_rodadas[materia] = 0
            shuffle(questions[materia])

        if materia_cont_perguntas[materia] - materia_cont_rodadas[materia]*10 == 10:
            materia_cont_rodadas[materia] += 1
            status_jogo = 'fim'

        
        
        self.pergunta(self=Quiz)
        self.alternativa(self=Quiz)
        self.pontuacao(self=Quiz)

class Data():
    def __init__(self):
        super().__init__()
    
    def save(self, score, HS_FILE):
        try:
            with open(HS_FILE, 'w') as f:
                json.dump(score, f)
        except:
            return 0
    
    def load(self, HS_FILE):
            with open(HS_FILE, 'r') as f:
                score = json.load(f)
                return score
    
    def sort_score(self, score):
        if len(score) > 0:

                score.sort(key=lambda x: x[1], reverse=True)

                if len(score) > 5:
                    score.pop()
                
        return score

        
def draw_text(text, color, x, y):
    global fonte_outline
    img = fonte.render(text, True, color)
    img_rect = img.get_rect(center=(x, y))
    tela.blit(img, img_rect)

def draw_text_placar_score(text, color, x, y):
    global fonte_ranking
    img = fonte_ranking.render(text, True, color)
    img_rect = img.get_rect(midleft=(x, y))
    tela.blit(img, img_rect)

def draw_text_placar(text, color, x, y):
    global fonte_placar
    img = fonte_placar.render(text, True, color)
    img_rect = img.get_rect(center=(x, y))
    tela.blit(img, img_rect)





# Inicializando o pygame
pygame.init()
pygame.mixer.init()
tela = pygame.display.set_mode((1200, 675))
pygame.mixer.music.load('audios/Quiz_Background_Music.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


hit_sound = pygame.mixer.Sound('audios/hit.wav')
som_acertou = pygame.mixer.Sound('audios/Som_acerto.mp3')
# som_acertou.set_volume(0)
som_erro = pygame.mixer.Sound('audios/Som_erro.mp3')
# som_erro.set_volume(0)
pygame.display.set_caption('Quiz')
relogio = pygame.time.Clock()
status_jogo = 'inicio'




try:
    score = Data.load(self=Data, HS_FILE='score.json')
except:
    score = [[], [], []]










points = 0
clicou = False
fonte = pygame.font.Font('font/Silkscreen-Regular.ttf', 48)
fonte_ranking = pygame.font.Font('font/Chalk Board.ttf', 35)
fonte2 = pygame.font.Font('font/Chalk Board.ttf',52)
fonte_placar = pygame.font.Font('font/Fonte_placar.TTF', 47)
fonte_alternativa = pygame.font.Font('font/Chalk Board.ttf', 43)

background_placar = pygame.image.load('imagens/Placar_background.png').convert()
background_placar = pygame.transform.scale(background_placar, (1200, 675))

background_inicio = pygame.image.load('imagens/Tela_Inicial.jpg').convert()
background_inicio = pygame.transform.scale(background_inicio, (1200, 675))
background_quiz = pygame.image.load('imagens/Quiz.jpg').convert()
background_quiz = pygame.transform.scale(background_quiz, (1200, 675))
botao = pygame.image.load('imagens/botao_menu_transparente.png').convert_alpha()
alternativa_botao = pygame.image.load('imagens/botao_alternativa.png').convert_alpha()
alternativa_certa = pygame.image.load('imagens/botao_certo.png').convert_alpha()
alternativa_errada = pygame.image.load('imagens/botao_errado.png').convert_alpha()

botao_menu = Botao_menu(600, 380, botao, 0.93, 0)
botao_voltar = Botao_menu(175, 610, botao, 0.7, 0)
botao_voltar_placar = Botao_menu(175, 610, botao, 0.7, 0)
botao_matematica = Botao_menu(600, 280, botao, 0.93, 0)
botao_geografia = Botao_menu(600, 385, botao, 0.93, 1)
botao_ciencias = Botao_menu(600, 490, botao, 0.93, 2)
botao_placar = Botao_menu(600, 500, botao, 0.93, 0)

botao_nome = pygame.transform.scale(botao, (340, 80))
input_rect = botao_nome.get_rect(center = (600, 380))

largura, altura = botao.get_size()



while True:
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicou = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicou = False
        
        if status_jogo == 'fim':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                elif event.key == pygame.K_RETURN:
                    enter = True
                elif len(user_name) < 9 and event.key != pygame.K_TAB:
                    user_name += event.unicode


    if status_jogo == 'inicio':
        tela.blit(background_inicio, (0, 0))
    
        if botao_menu.draw(tela):
            hit_sound.play()
            status_jogo = 'menu'

        if botao_placar.draw(tela):
            hit_sound.play()
            status_jogo = 'placar'       

        draw_text('Jogar', (0 ,0 , 0), 600, 380)
        draw_text('Placar', (0 ,0 , 0), 600, 500)
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
        if botao_ciencias.draw(tela):
            hit_sound.play()
            status_jogo = 'jogando'
            materia = 2
        if botao_voltar.draw(tela):
            hit_sound.play()
            status_jogo = 'inicio'
        
        draw_text('Matemática', (0, 0, 0), 600, 280)
        draw_text('Geografia', (0, 0, 0), 600, 385)
        draw_text('Ciências', (0, 0, 0), 600, 490)
        draw_text('Voltar', (0, 0, 0), 175, 608)
        pygame.display.update()

    elif status_jogo == 'placar':
        tela.blit(background_placar, (0, 0))

        
        if len(score[0]) > 0:
            for i in range(len(score[0])):
                draw_text_placar_score(f'{i+1}º- ', (255,255,255), 110, 335 + 40*i)
                score[0][i][0] = score[0][i][0].upper()
                nome = list(score[0][i][0])
                x = 145
                for letra in nome:
                    letra_surface = fonte_ranking.render(letra, True, (255, 255, 255))
                    letra_largura, letra_altura = letra_surface.get_size()

                    if letra_largura + x < 350:
                            
                        draw_text_placar_score(letra, (255, 255, 255), x, 335 + 40*i)
                        x += letra_largura

                            
                draw_text_placar_score(f'{score[0][i][1]}', (255,255,255), 350, 335 + 40*i)
        
        if len(score[1]) > 0:
            for i in range(len(score[1])):
                draw_text_placar_score(f'{i+1}º- ', (255,255,255), 475, 335 + 40*i)
                score[1][i][0] = score[1][i][0].upper()
                nome = list(score[1][i][0])
                x = 510
                for letra in nome:
                    letra_surface = fonte_ranking.render(letra, True, (255, 255, 255))
                    letra_largura, letra_altura = letra_surface.get_size()

                    if letra_largura + x < 715:
                            
                        draw_text_placar_score(letra, (255, 255, 255), x, 335 + 40*i)
                        x += letra_largura
                   
                            
                draw_text_placar_score(f'{score[1][i][1]}', (255,255,255), 715, 335 + 40*i)
        
        if len(score[2]) > 0:
            for i in range(len(score[2])):
                draw_text_placar_score(f'{i+1}º- ', (255,255,255), 840, 335 + 40*i)
                score[2][i][0] = score[2][i][0].upper()
                nome = list(score[2][i][0])
                x = 875
                for letra in nome:
                    letra_surface = fonte_ranking.render(letra, True, (255, 255, 255))
                    letra_largura, letra_altura = letra_surface.get_size()

                    if letra_largura + x < 1080:
                            
                        draw_text_placar_score(letra, (255, 255, 255), x, 335 + 40*i)
                        x += letra_largura
                            
                draw_text_placar_score(f'{score[2][i][1]}', (255,255,255), 1080, 335 + 40*i)
 

        if botao_voltar.draw(tela)and status_jogo == 'placar':
            hit_sound.play()
            status_jogo = 'inicio'
            points = 0
        draw_text('Voltar', (0, 0, 0), 175, 608)
        pygame.display.update()
    
    elif status_jogo == 'jogando':
        tela.blit(background_quiz, (0, 0))
        
        for materias in materia_cont_perguntas:
            if materia >= 50:
                materia = 0
        
        Quiz.update(self=Quiz)
        pygame.display.update()
        
    elif status_jogo == 'fim':

        tela.blit(background_inicio, (0, 0))

        
        
        text_surface = fonte.render(user_name, True, (0, 0, 0))
        text_surface2 = fonte.render(user_name + '|', True, (0, 0, 0))
        tela.blit(botao_nome, input_rect)
        ticks = 0
        ticks += pygame.time.get_ticks()
        if int(ticks/600) % 2 == 0:
            tela.blit(text_surface , input_rect.move(20, 7))
        else:
            tela.blit(text_surface2, input_rect.move(20, 7))

        
        draw_text('Fim de jogo', (0, 0, 0), 600, 200)
        draw_text('Escreva seu nome:', (0, 0, 0), 600, 300)
        draw_text('Pontuação: ' + str(points)+'/10', (0, 0, 0), 600, 485)



        if (botao_voltar.draw(tela) or enter == True) and len(user_name) > 0:
            hit_sound.play()

            
            score[materia].append([user_name, points])


            score[materia] = Data.sort_score(self=Data.sort_score, score=score[materia])

            
            Data.save(self=Data, score=score, HS_FILE='score.json')
            points = 0
            user_name = ''
            status_jogo = 'inicio'
            
            
        
        draw_text('Voltar', (0, 0, 0), 175, 608)
        enter = False
        pygame.display.update()

    
    pygame.display.update()
    relogio.tick(60)
    

    
