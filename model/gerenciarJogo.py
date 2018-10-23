"""
Created on jun de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""
import pygame
from .motorJogo import Jogo

helicoptero = 'static/img/aeronave/helicopteroNPC.gif'
aviaoNPC = 'static/img/aeronave/aviaoNPC.gif'
aviao = 'static/img/aeronave/aviaoJogador.gif'


def iniciar_jogo(jogador):
    """
    Funcao para ligar o jogo
    """
    print("DEBUG: jogo iniciado")
    jogo = Jogo(pygame, "DESTROYER AIRPLANES", (1280, 720), [], 32, pygame.RESIZABLE)
    jogo.adicionar_jogador(jogador[1])
    jogo.iniciar_jogo()
    print("DEBUG: jogo finalizado")
