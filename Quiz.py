import pygame
import sys
import random
import time

questions = [
    ["Qual bicho transmite Doença de Chagas?", ["Barbeiro", "Barata", "Pulga", "Abelha"]],
    ["Qual fruto ? conhecido no Norte e Nordeste como jerimum", ["Ab?bora", "Caju", "Chuchu", "C?co"]],
    ["Qual ? o coletivo de c?es?", ["Matilha", "Rebanho", "Alcateia", "Manada"]],
    ["Qual ? o tri?ngulo que tem todos os lados diferentes?", ["Escaleno", "Is?sceles", "Equil?tero", "Trap?zio"]],
    ["Quem comp?s o Hino Nacional?", ["Manoel da Silva", "Manuel Bandeira", "Castro Alvez", "Dom Pedro I"]],
    ["Qual ? o ant?nimo de malograr?", ["Conseguir", "Fracassar", "Perder", "Desprezar"]],
    ["Em que pa?s nasceu Carmem Miranda?", ["Portugal", "Espanha", "Brasil", "Argentina"]],
    ["Qual foi o ?ltimo Presidente do per?odo da ditadura militar no Brasil?", ["Jo?o figueiredo", "Costa e silva", "Ernesto Geisel", "Em?lio Medici"]],
    ["Seguindo a sequ?ncia do baralho, qual carta vem depois do dez", ["Valete", "Rainha", "Rei", "11"]],
    ["O adjetivo venoso est? relacionado a:", ["Veia", "Vento", "Veneno", "Venom"]],
]

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
    global alternativas_ordem, questions, fonte

    alternativas_ordem = [0, 1, 2, 3]
    # random.shuffle(alternativas_ordem)
    def __init__(self):
        super().__init__()
    
    

    def pergunta():
        draw_text(questions[0][0], fonte, (255, 255, 255), 0, 40)

    def alternativa():
        draw_text('A. ', fonte, (255, 255, 255), 0, 300)
        draw_text(questions[0][1][0], fonte, (255, 255, 255), 25, 300)

        draw_text('B. ', fonte, (255, 255, 255), 0, 350)
        draw_text(questions[1][1][1], fonte, (255, 255, 255), 25, 350)

        draw_text('C. ', fonte, (255, 255, 255), 0, 400)
        draw_text(questions[1][1][2], fonte, (255, 255, 255), 25, 400)

        draw_text('D. ', fonte, (255, 255, 255), 0, 450)
        draw_text(questions[1][1][3], fonte, (255, 255, 255), 25, 450)
    
    def update(self):
        self.pergunta()
        self.alternativa()

        
        


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    img_rect = img.get_rect(center=(x, y))
    img_sombra = font.render(text, True, (0,0,0))
    img_rect_sombra = img.get_rect(center=(x+2, y+2))
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
fonte = pygame.font.SysFont('Arial', 30)

background_inicio = pygame.image.load('imagens/background1.png').convert()
background_inicio = pygame.transform.scale(background_inicio, (1200, 675))
botao = pygame.image.load('imagens/botao_menu2.png').convert_alpha()

botao_menu = Botao_menu(600, 380, botao, 0.93, '')
botao_voltar = Botao_menu(150, 570, botao, 0.5, '')
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


        draw_text('Jogar', fonte, (255, 255, 255), 600, 300)
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
        
        draw_text('Matematica', fonte, (255, 255, 255), 600, 380)
        draw_text('Geografia', fonte, (255, 255, 255), 600, 485)
        draw_text('Voltar', fonte, (255, 255, 255), 150, 570)
        pygame.display.update()
    
    elif status_jogo == 'jogando':
        tela.blit(background_inicio, (0, 0))


        Quiz.update(self=Quiz)

        

        pygame.display.update()