import os.path
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
filepath = os.path.dirname(__file__)
#Moduł wypisywania tekstu
controlVol = 0.5
screen = pygame.display.set_mode((1280, 720))
loadingSound = pygame.mixer.Sound("data\\sound\\load.wav")
siren = pygame.mixer.Sound("data\\sound\\norma.wav")
szum = pygame.mixer.Sound("data\\sound\\szumszkolny.wav")
silowniaOGG = pygame.mixer.Sound("data\\sound\\silownia.wav")
progOGG = pygame.mixer.Sound("data\\sound\\prog.wav")
barSound = pygame.mixer.Sound("data\\sound\\barSound.wav")

def pisz(wers, tekst, szerokosc, wysokosc, kolor):
    myFont = pygame.font.SysFont("monospace", 18, bold = True)
    wers = myFont.render(tekst, 1, kolor)
    screen.blit(wers, (szerokosc, wysokosc))

def volume_low():
    global controlVol
    pygame.mixer.music.pause()
    controlVol = 0.1
    pygame.mixer.music.set_volume(controlVol)
    pygame.mixer.Sound.set_volume(siren, 0.1)
    pygame.mixer.Sound.set_volume(szum, 0.1)
    pygame.mixer.Sound.set_volume(silowniaOGG, 0.1)
    pygame.mixer.Sound.set_volume(progOGG, 0.1)
    pygame.mixer.Sound.set_volume(loadingSound, 0.3)
    pygame.mixer.Sound.set_volume(barSound, 0.1)
    pygame.mixer.music.play(-1)

def volume_normal():
    global controlVol
    pygame.mixer.music.pause()
    controlVol = 0.4
    pygame.mixer.music.set_volume(controlVol)
    pygame.mixer.Sound.set_volume(siren, 0.4)
    pygame.mixer.Sound.set_volume(szum, 0.4)
    pygame.mixer.Sound.set_volume(silowniaOGG, 0.4)
    pygame.mixer.Sound.set_volume(progOGG, 0.4)
    pygame.mixer.Sound.set_volume(loadingSound, 0.4)
    pygame.mixer.Sound.set_volume(barSound, 0.4)
    pygame.mixer.music.play(-1)

def volume_hi():
    global controlVol
    pygame.mixer.music.pause()
    controlVol = 0.8
    pygame.mixer.music.set_volume(controlVol)
    pygame.mixer.Sound.set_volume(siren, 0.8)
    pygame.mixer.Sound.set_volume(szum, 0.8)
    pygame.mixer.Sound.set_volume(silowniaOGG, 0.8)
    pygame.mixer.Sound.set_volume(progOGG, 0.8)
    pygame.mixer.Sound.set_volume(loadingSound, 0.8)
    pygame.mixer.Sound.set_volume(barSound, 0.8)
    pygame.mixer.music.play(-1)

    
