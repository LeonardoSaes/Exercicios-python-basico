# toca nave espacial quando dá o play
import pygame
pygame.init()
pygame.mixer.music.load('nave espacial.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
