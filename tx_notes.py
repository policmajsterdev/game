import pygame
from pygame.locals import *
import db_save
import pisak
import sys
import delete_db
import graph
import os
import tk_box

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(32)

screen = pygame.display.set_mode((1280, 720))
filepath = os.path.dirname(__file__)
mainClock = pygame.time.Clock()

pygame.display.set_caption("Policmajster: Początek")

pygame.display.set_icon(graph.icon)
loadingSound = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\load.ogg"))

black = (0, 0, 0)
dyellow = (115, 115, 0)


# ZAPISKI


def ostatnia_strona():
    pygame.mouse.set_visible(True)
    tomek_quest = db_save.search_data("quest_tomek", "dane_quest_tomek")
    while True:
        click = False

        screen.fill(black)
        screen.blit(graph.zapisky_bg, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        mx, my = pygame.mouse.get_pos()

        mx, my = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                loadingSound.play()
                break

        if len(tomek_quest) > 0:
            tomek_x = screen.blit(graph.strona_tomek[0], (30, 30))
            if tomek_x.collidepoint((mx, my)):
                screen.blit(graph.strona_tomek[1], (30, 30))
                if click:
                    loadingSound.play()
                    tk_box.zapiski("Tomka", "dane_quest_tomek")



        pisak.pisz("wers", "Wybierz zapiski by przeczytać.", 20, 655, dyellow)

        pygame.display.update()
        mainClock.tick(30)


