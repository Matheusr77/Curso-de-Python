#Atividade 21
#Tocando um MP3
#OBS: NÃO RODOU

import pygame

pygame.init()
pygame.mixer.music.load('Atividade 21.mp3') #O arquivo de áudio foi deletado
pygame.mixer.music.play()
input()
pygame.event.wait()