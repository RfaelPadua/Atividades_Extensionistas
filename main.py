import pygame
import sys
import time 
import random

pygame.init()
tela = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Quiz')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()