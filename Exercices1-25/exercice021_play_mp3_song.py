"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

import pygame
import os

pygame.mixer.init()

def play_mp3(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
# Obtendo o caminho absoluto para a pasta "MP3_musics" usando o caminho atual do script    
current_path = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(current_path, "MP3_musics")

# caminho absoluto para a pasta de música
file_path = os.path.join(folder_path, "Herman - Vibe.mp3")
play_mp3(file_path)

# Mantenha o programa em execução para reproduzir a música completa
while pygame.mixer.music.get_busy():
    pass
