
import pygame

pygame.mixer.init()
pygame.mixer.music.load('metal_pipe.mp3')

def play_mp3():
    pygame.mixer.music.play()
    