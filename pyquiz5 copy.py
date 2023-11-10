# coding: latin1
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
import pygame
import pygame.gfxdraw
import sys
import time
import random
# the Label class is this module below
from label import *


pygame.init()
pygame.mixer.init()
hit = pygame.mixer.Sound("sounds/hit.wav")
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
# test_font = pygame.font.SysFont("Arial", 40)
test_font = pygame.font.Font("font/Pixeltype.ttf", 40)
background_surf = pygame.image.load('graficos/Tela_Inicial.png').convert()
background_surf = pygame.transform.scale(background_surf, (1200, 600))
game_state = "menu"
materia = "none"



buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    ''' A button treated like a Sprite... and killed too '''
    
    def __init__(self, position, text, size,
        colors="white on blue",
        hover_colors="red on green",
        style="button1",
        borderc=(255,255,255),
        command=lambda: print("No command activated for this button")):

        # the hover_colors attribute needs to be fixed
        super().__init__()
        global num

        self.text = text
        self.command = command
        # --- colors ---
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        # hover_colors
        if hover_colors == "red on green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors
        # styles can be button1 or button2 (more simple this one)
        self.style = style
        self.borderc = borderc # for the style2
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render(self.text)
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, 500, self.h)
        self.position = position
        self.pressed = 1
        # the groups with all the buttons
        buttons.add(self)

    def render(self, text):
        # we have a surface
        self.text_render = self.font.render(text, 1, self.fg)
        # memorize the surface in the image attributes
        self.image = self.text_render

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == "button1":
            self.draw_button1()
        elif self.style == "button2":
            self.draw_button2()
        if self.command != None:
            self.hover()
            self.click()

    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        lcolor = (150, 150, 150)
        lcolor2 = (50, 50, 50)
        pygame.draw.line(screen, lcolor, self.position,
            (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, lcolor, (self.x, self.y - 2),
            (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(screen, lcolor2, (self.x, self.y + self.h),
            (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, lcolor2, (self.x + self.w , self.y + self.h),
            [self.x + self.w , self.y], 5)
        # background of the button
        pygame.draw.rect(screen, self.bg, self.rect)  

    def draw_button2(self):
        ''' a linear border '''
        # the width is set to 500 to have the same size not depending on the text size
        pygame.draw.rect(screen, self.bg, (self.x  -50, self.y, 600 , self.h))
        pygame.gfxdraw.rectangle(screen, (self.x  -50, self.y, 600 , self.h), self.borderc)

    def check_collision(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # you can change the colors when the pointer is on the button if you want
            self.colors = self.hover_colors
            # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            self.colors = self.original_colors
            # pygame.mouse.set_cursor(*pygame.cursors.arrow)


    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''

        self.check_collision()

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("The answer is:'" + self.text + "'")
                self.command()
                self.pressed = 0

            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1

class Botao_menu():
    def __init__(self, x, y, image, scale, type):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        global materia
        action = False
		#get mouse position
        pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                materia = type

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

		#draw Botao_menu on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    img_rect = img.get_rect(center=(x, y))
    img_sombra = font.render(text, True, (0,0,0))
    img_rect_sombra = img.get_rect(center=(x+2, y+2))
    screen.blit(img_sombra, img_rect_sombra)
    screen.blit(img, img_rect)

menu_botao_surf = pygame.image.load('graficos/botao_menu1.png').convert_alpha()
background_surf = pygame.transform.scale(background_surf, (1200, 600))

botao_matematica = Botao_menu(150, 295, menu_botao_surf, 0.4, "Matematica")
botao_geografia = Botao_menu(450, 295, menu_botao_surf, 0.4, "Geografia")
botao_historia = Botao_menu(750, 295, menu_botao_surf, 0.4, "Historia")
botao_programacao = Botao_menu(1050, 295, menu_botao_surf, 0.4, "Programacao")
botao_menu = Botao_menu(600, 500, menu_botao_surf, 0.4, "Menu")
# ACTION FOR BUTTON CLICK ================

def on_click():
    print("Click on one answer")

def on_right():
    check_score("right")

def on_false():
    ''' if there is no 'right' as arg it means it's false '''
    check_score()

def check_score(answered="wrong"):
    ''' here we check if the answer is right '''
    global qnum, points
    
    # until there are questions (before last)
    hit.play() # click sound
    if qnum < len(questions):
        print(qnum, len(questions))
        if answered == "right":
            time.sleep(.1) # to avoid adding more point when pressing too much
            points += 1
            # Show the score text
        qnum += 1 # counter for next question in the list
        score.change_text("Pontos: " + str(points), color="black")
        # Change the text of the question
        title.change_text(questions[qnum-1][0], color="black")
        # change the question number
        num_question.change_text(str(qnum))
        show_question(qnum) # delete old buttons and show new
        

    # for the last question...
    elif qnum == len(questions):
        print(qnum, len(questions))
        if answered == "right":
            kill()
            time.sleep(.1)
            points +=1
        score.change_text("Voc? pontuou " + str(points))
    time.sleep(.5)




questions = [
    ["Qual bicho transmite Doen?a de Chagas?", ["Barbeiro", "Barata", "Pulga", "Abelha"]],
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




def show_question(qnum):
    ''' put your buttons here '''

    # Kills the previous buttons/sprites
    kill()

    
    # The 4 position of the buttons
    pos = [100, 200, 300, 400]
    random.shuffle(pos)

    Button((10, 100), "A. ", 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)
    Button((10, 200), "B. ", 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)
    Button((10, 300), "C. ", 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)
    Button((10, 400), "D. ", 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)


    # ============== TEXT: question and answers ====================
    Button((50, pos[0]), questions[qnum-1][1][0], 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_right)
    Button((50, pos[1]), questions[qnum-1][1][1], 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_false)
    Button((50, pos[2]), questions[qnum-1][1][2], 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_false)
    Button((50, pos[3]), questions[qnum-1][1][3], 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_false)


def kill():
    for _ in buttons:
        _.kill()

qnum = 1
points = 0
# ================= SOME LABELS ==========================
num_question = Label(screen, str(qnum), 0, 0)
score = Label(screen, "Pontos:", 50, 500, 40, color="black")
title = Label(screen, questions[qnum-1][0], 10, 10, 40, color="black")

def start_again():
    pass

def loop():
    global game_on, game_state, materia

    show_question(qnum)

    while True:
        screen.fill(0)
        screen.blit(background_surf, (0, 0))
        for event in pygame.event.get(): # ====== quit / exit
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        if game_state == "menu":
            if botao_matematica.draw(screen):
                hit.play()
                materia = "matematica"
                game_state = "Perguntas"
            if botao_geografia.draw(screen):
                hit.play()
                materia = "geografia"
                game_state = "Perguntas"
            if botao_historia.draw(screen):
                hit.play()
                materia = "historia"
                game_state = "Perguntas"
            if botao_programacao.draw(screen):
                hit.play()
                materia = "programacao"
                game_state = "Perguntas"
            
            draw_text('Escolha  uma  Matéria', test_font, (255, 255, 255), 600, 150)
            draw_text('Matematica', test_font, (255, 255, 255), 150, 295)
            draw_text('Geografia', test_font, (255, 255, 255), 450, 295)
            draw_text('Historia', test_font, (255, 255, 255), 750, 295)
            draw_text('Programacao', test_font, (255, 255, 255), 1050, 295)

        elif game_state == "Perguntas":
            buttons.update() #                     update buttons
            buttons.draw(screen)
            show_labels()        #                 update labels
            clock.tick(60)
            
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    game_on = 1
    loop()