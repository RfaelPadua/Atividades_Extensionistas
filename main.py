# coding: latin1
import pygame
import pygame.gfxdraw
import sys
import time
import random
# the Label class is this module below
from label import *

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

pygame.init()
pygame.mixer.init()
hit = pygame.mixer.Sound("sounds/hit.wav")
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
test_font = pygame.font.SysFont("calibri", 25)
game_state = "menu"
materia = "none"

menu_botao_surf = pygame.image.load('graficos/botao_menu1.png').convert_alpha()
background_surf = pygame.image.load('graficos/background.png').convert()
background_surf = pygame.transform.scale(background_surf, (1200, 600))

botao_matematica = Botao_menu(150, 295, menu_botao_surf, 0.4, "Matematica")
botao_geografia = Botao_menu(450, 295, menu_botao_surf, 0.4, "Geografia")
botao_historia = Botao_menu(750, 295, menu_botao_surf, 0.4, "Historia")
botao_programacao = Botao_menu(1050, 295, menu_botao_surf, 0.4, "Programacao")
botao_menu = Botao_menu(600, 500, menu_botao_surf, 0.4, "Menu")

while True:
    screen.fill(0)
    screen.blit(background_surf, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

    

    if game_state == "menu":
        
        

        if botao_matematica.draw(screen):
            hit.play()
            game_state = "matematica"
        if botao_geografia.draw(screen):
            hit.play()
            game_state = "geografia"
        if botao_historia.draw(screen):
            hit.play()
            game_state = "historia"
        if botao_programacao.draw(screen):
            hit.play()
            game_state = "programacao"
        
        draw_text('Escolha  uma  Materia', test_font, (255, 255, 255), 600, 150)
        draw_text('Matematica', test_font, (255, 255, 255), 150, 295)
        draw_text('Geografia', test_font, (255, 255, 255), 450, 295)
        draw_text('Historia', test_font, (255, 255, 255), 750, 295)
        draw_text('Programacao', test_font, (255, 255, 255), 1050, 295)

    elif game_state == "matematica":
        screen.blit(background_surf, (0, 0))
        draw_text('Matematica', test_font, (255, 255, 255), 600, 150)
        if botao_menu.draw(screen):
            hit.play()
            game_state = "menu"
    elif game_state == "geografia":
        screen.blit(background_surf, (0, 0))
        draw_text('Geografia', test_font, (255, 255, 255), 600, 150)
        if botao_menu.draw(screen):
            hit.play()
            game_state = "menu"
    elif game_state == "historia":
        screen.blit(background_surf, (0, 0))
        draw_text('Historia', test_font, (255, 255, 255), 600, 150)
        if botao_menu.draw(screen):
            hit.play()
            game_state = "menu"
    elif game_state == "programacao":
        screen.blit(background_surf, (0, 0))
        draw_text('Programacao', test_font, (255, 255, 255), 600, 150)
        if botao_menu.draw(screen):
            hit.play()
            game_state = "menu"

    pygame.display.update()