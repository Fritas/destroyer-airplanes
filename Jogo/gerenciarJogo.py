import sys
sys.path.append("..")
import pygame
from Jogo.motorJogo import Jogo

helicoptero = '../img/aeronave/helicopteroNPC.gif'
aviaoNPC = '../img/aeronave/aviaoNPC.gif'
aviao = '../img/aeronave/aviaoJogador.gif'


def iniciar_jogo(jogador):
    """
    Funcao para ligar o jogo
    """
    print("DEBUG: jogo iniciado")
    jogo = Jogo(pygame, "DESTROYER AIRPLANES", (1280, 720), [], 32, pygame.RESIZABLE)
    jogo.adicionar_jogador(jogador[1])
    jogo.iniciar_jogo()
    print("DEBUG: jogo finalizado")
