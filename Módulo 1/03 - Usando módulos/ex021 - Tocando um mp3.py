# escreva um programa que toque uma música .mp3

import pygame

pygame.init()
pygame.mixer.music.load('Mighty Morphin Power Rangers.mp3')
pygame.mixer.music.play(-1)
while True:
    # Seu código aqui
    pass
pygame.mixer.music.stop()
pygame.quit()
