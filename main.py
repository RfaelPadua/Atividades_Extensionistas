import pygame
import sys
import time 
import random

pygame.init()
tela = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Quiz')
fonte = pygame.font.SysFont('Arial', 30, True, True)
game_ativo = True

background_surf = pygame.image.load('graficos/background.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

    
    if game_ativo:
        tela.blit(background_surf, (0, 0))
        pygame.display.update()