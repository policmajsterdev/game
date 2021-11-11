import os.path
import pygame

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
filepath = os.path.dirname(__file__)

# Moduł wypisywania tekstu
controlVol = 0.5
screen = pygame.display.set_mode((1280, 720))
loadingSound = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\load.ogg"))
siren = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\norma.ogg"))
szum = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\szumszkolny.ogg"))
silowniaOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\silownia.ogg"))
progOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\prog.ogg"))
barSound = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\barSound.ogg"))


def pisz(wers, tekst, szerokosc, wysokosc, kolor, rozmiar=18):
    my_font = pygame.font.SysFont("monospace", rozmiar, bold=True)
    wers = my_font.render(tekst, 1, kolor)
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
    pygame.mixer.Sound.set_volume(loadingSound, 0.2)
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
