import pygame
import os

pygame.init()


pygame.mixer.music.load('call.mp3')
pygame.mixer.play()
pygame.event.wait()
    