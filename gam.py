import pygame
from pygame.locals import *
import sys
import random
import os.path
import pisak
import graph
import check_file_save
import experience
import tk_box
import db_save
import delete_db
import tx_notes
import dialogs

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(32)

mainClock = pygame.time.Clock()
filepath = os.path.dirname(__file__)

# Rozmiar_okna

xw = 1
xh = 1
screen = pygame.display.set_mode((1280, 720))

# Nazwa_okna_gry/Ikona

pygame.display.set_caption("Policmajster: Początek")
pygame.display.set_icon(graph.icon)

# Muzyka w tle \\ reszta w module

controlVol = 0.5
pygame.mixer.music.load(os.path.join(filepath, "data\\sound\\horror2.ogg"))
pygame.mixer.music.set_volume(controlVol)

# Dźwięki

loadingSound = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\load.ogg"))
loadingSoundDEV = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\loading1.wav"))
siren = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\norma.ogg"))
szum = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\szumszkolny.ogg"))
silowniaOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\silownia.ogg"))
progOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\prog.ogg"))
barSound = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\barSound.ogg"))
korytarzSound = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\korytarz.ogg"))
spacerOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\spacer.ogg"))
strzelnicaOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\strzelnicaglucha.ogg"))
shot = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\shot.wav"))
shotgun = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\shotgun.wav"))
saveOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\save.ogg"))
stolowkaOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\stolowka.ogg"))
salawfOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\salawf.ogg"))
klik = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\klik.wav"))
pen = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\pen.wav"))
scream_girl = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\scream.wav"))
ricochet = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\ricochet.ogg"))
rain_wav = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\rain.ogg"))
beep = [pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\beep1.wav")),
        pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\beep2.wav")),
        pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\beep3.wav"))]
pin_open = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\pin_open.ogg"))
pin_closed = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\pin_closed.ogg"))
door_close = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\closed_door.wav"))
door_open = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\open_door.ogg"))
radios = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\radiostacja.ogg"))
move = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\move.wav"))
sektor_i_wav = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\sektori.ogg"))
warsztat_wav = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\warsztat.ogg"))
eq_wav = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\hiteq.ogg"))
cashpaid = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\cashpaid.wav"))

# Tekst

myFont = pygame.font.SysFont("monospace", 18)

# Kolory

blue = (0, 0, 255)
black = (0, 0, 0)
white = (170, 170, 170)
red = (220, 0, 0)
green = (0, 140, 0)
dyellow = (115, 115, 0)
brown = (153, 102, 51)
dark_blue = (0, 51, 102)

# Strzelnica

gun = pygame.image.load(os.path.join(filepath, "data\\tarcze\\gun.png")).convert_alpha()
gun2 = pygame.image.load(os.path.join(filepath, "data\\tarcze\\gun1.png")).convert_alpha()
efe = [pygame.image.load(os.path.join(filepath, "data\\tarcze\\efe.png")).convert_alpha(),
       pygame.image.load(os.path.join(filepath, "data\\tarcze\\efe1.png")).convert_alpha(),
       pygame.image.load(os.path.join(filepath, "data\\tarcze\\efe2.png")).convert_alpha(),
       pygame.image.load(os.path.join(filepath, "data\\tarcze\\efe3.png")).convert_alpha(),
       pygame.image.load(os.path.join(filepath, "data\\tarcze\\efe4.png")).convert_alpha(),
       pygame.image.load(os.path.join(filepath, "data\\tarcze\\efe5.png")).convert_alpha(),
       pygame.image.load(os.path.join(filepath, "data\\tarcze\\efe6.png")).convert_alpha()]
francuzIMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\francuz.png")).convert_alpha()
francuz_mask = pygame.mask.from_surface(francuzIMG)
francuz1IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\francuz1.png")).convert_alpha()
francuz1_mask = pygame.mask.from_surface(francuz1IMG)
tifaIMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tifa.png")).convert_alpha()
tifa_mask = pygame.mask.from_surface(tifaIMG)
blood_IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\blood.png")).convert_alpha()
blood_mask = pygame.mask.from_surface(blood_IMG)
tarczaIMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tarcza1.png")).convert_alpha()
tarcza_mask = pygame.mask.from_surface(tarczaIMG)
tarcza_rect = tarczaIMG.get_rect()
tarcza9IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tarcza9.png")).convert_alpha()
tarcza9_mask = pygame.mask.from_surface(tarcza9IMG)
tarcza9_rect = tarcza9IMG.get_rect()
tarcza8IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tarcza8.png")).convert_alpha()
tarcza8_mask = pygame.mask.from_surface(tarcza8IMG)
tarcza8_rect = tarcza8IMG.get_rect()
tarcza7IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tarcza7.png")).convert_alpha()
tarcza7_mask = pygame.mask.from_surface(tarcza7IMG)
tarcza7_rect = tarcza7IMG.get_rect()
tarcza6IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tarcza6.png")).convert_alpha()
tarcza6_mask = pygame.mask.from_surface(tarcza6IMG)
tarcza6_rect = tarcza6IMG.get_rect()
tarcza5IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tarcza5.png")).convert_alpha()
tarcza5_mask = pygame.mask.from_surface(tarcza5IMG)
tarcza5_rect = tarcza5IMG.get_rect()
tarcza4IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tarcza4.png")).convert_alpha()
tarcza4_mask = pygame.mask.from_surface(tarcza4IMG)
tarcza4_rect = tarcza4IMG.get_rect()
tarcza3IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tarcza3.png")).convert_alpha()
tarcza3_mask = pygame.mask.from_surface(tarcza3IMG)
tarcza3_rect = tarcza3IMG.get_rect()
tarcza2IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tarcza2.png")).convert_alpha()
tarcza2_mask = pygame.mask.from_surface(tarcza2IMG)
tarcza2_rect = tarcza2IMG.get_rect()
tarcza1IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tarcza10.png")).convert_alpha()
tarcza1_mask = pygame.mask.from_surface(tarcza1IMG)
tarcza1_rect = tarcza1IMG.get_rect()
tarcza0IMG = pygame.image.load(os.path.join(filepath, "data\\tarcze\\tarcza0.png")).convert_alpha()
green_blob = pygame.image.load(os.path.join(filepath, "data\\tarcze\\aim1.png")).convert_alpha()  # celownik czerwony
orange_blob = pygame.image.load(os.path.join(filepath, "data\\tarcze\\aim2.png")).convert_alpha()  # celownik zielony
blob_mask = pygame.mask.from_surface(green_blob)
blob_rect = green_blob.get_rect()
blob_color = green_blob

# Aktywne eq

active = None


# Akta_osobowe


def akta_osobowe():
    pygame.mouse.set_visible(True)
    running = True
    dane_konta = experience.aktualny_stan_konta()
    dane_gracza = db_save.pobierz_dane("dane_gracza")
    ramka_exp = Rect(110, 295, 300, 20)
    block_exp = Rect(111, 296, dane_konta[0], 18)
    ramka_ang = Rect(110, 345, 300, 20)
    block_ang = Rect(111, 346, dane_konta[1], 18)
    baretki = db_save.search_data("baretki", "dane_baretki")
    while running:
        poz_y = 0
        click = False
        screen.fill(black)
        screen.blit(graph.teczka_osobowa, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        screen.blit(graph.odznaka, (1080, 10))
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

        # Stopnie służbowe

        if dane_gracza[0][1] == "posterunkowy":
            screen.blit(graph.post, (340, 197))
        elif dane_gracza[0][1] == "starszy posterunkowy":
            screen.blit(graph.st_post, (340, 197))

        # Wyróżnienia
        for i in baretki:
            if i == "p99":
                barteka_p99_x = screen.blit(graph.odznaka_p99[1], (730, 160 + poz_y))
                if barteka_p99_x.collidepoint((mx, my)):
                    screen.blit(graph.odznaka_p99[0], (730, 160 + poz_y))
                    pisak.pisz("wers1a", "Ponad 200 pkt na strzelnicy z P99", 730, 140 + poz_y, red)
                poz_y += 50
            if i == "mosberg":
                baretka_mosberg_x = screen.blit(graph.odznaka_mosberg[1], (730, 160 + poz_y))
                if baretka_mosberg_x.collidepoint((mx, my)):
                    screen.blit(graph.odznaka_mosberg[0], (730, 160 + poz_y))
                    pisak.pisz("wers1b", "Ponad 200 pkt na strzelnicy z Mossberg 590", 730, 140 + poz_y, red)
                poz_y += 50

        pisak.pisz("wers2", "Dane funkcjonariusza:", 110, 153, black)
        pisak.pisz("wers2", dane_gracza[0][0], 340, 153, black)
        pisak.pisz("wers3", "Stopień sł.:", 110, 175, black)
        pisak.pisz("wers33", dane_gracza[0][1], 340, 175, blue)
        pisak.pisz("wers8", "Numer odznaki:       997187", 110, 250, black)
        pisak.pisz("wers9", "Doświadczenie:", 110, 270, black)
        pisak.pisz("wers91", str(dane_konta[0]), 340, 270, blue)
        pisak.pisz("wers92", "/300", 378, 270, black)
        pisak.pisz("wers99", "Grupa zaszeregowania:", 110, 375, black)
        pisak.pisz("wers99", dane_gracza[0][2], 340, 375, brown)
        pisak.pisz("wers22", "Dodatek służbowy:", 110, 395, black)
        pisak.pisz("wers23", str(dane_konta[2]), 340, 395, brown)
        pisak.pisz("wers2a", "Składniki uposażenia:", 110, 435, black)
        pisak.pisz("wers2a", "- kwota bazowa", 120, 450, black)
        pisak.pisz("wers2b", str(dane_konta[3]), 340, 450, black)
        pisak.pisz("wers2c", "- mnożnik", 120, 470, black)
        pisak.pisz("wers2d", str(dane_konta[4]), 340, 470, brown)
        pisak.pisz("wers2e", "- dodatek służbowy", 120, 490, black)
        pisak.pisz("wers2f", str(dane_konta[2]), 340, 490, brown)
        pisak.pisz("wers2g", "- dodatek stopień", 120, 510, black)
        pisak.pisz("wers2h", str(dane_konta[5]), 340, 510, blue)
        pisak.pisz("wers2i", "- wysługa lat", 120, 530, black)
        pisak.pisz("wers2j", dane_konta[6], 340, 530, black)
        pisak.pisz("wers2k", "Uposażenie netto :", 120, 560, black)
        pisak.pisz("wers2l", str(dane_konta[8]), 340, 560, black)
        pisak.pisz("wers2o", "Wypłata za    dni.", 120, 580, black)
        pisak.pisz("wers2p", str(dane_konta[9]), 250, 580, black)
        pisak.pisz("wers2k", "Stan konta", 190, 605, black)
        pisak.pisz("wers2k", str(dane_konta[7]), 205, 635, white)
        pisak.pisz("wers4", "Zaangażowanie:", 110, 320, black)
        pisak.pisz("wers4", str(dane_konta[1]), 340, 320, brown)
        pisak.pisz("wers41", "/300", 378, 320, black)

        pygame.draw.rect(screen, black, ramka_exp, 1)
        pygame.draw.rect(screen, dark_blue, block_exp)
        pygame.draw.rect(screen, black, ramka_ang, 1)
        pygame.draw.rect(screen, brown, block_ang)

        pygame.display.update()
        mainClock.tick()


def intro_dev():
    pygame.mixer.music.play(-1)
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(black)
        screen.blit(graph.intro, (0, 0))
        pisak.pisz("wers1", "Kliknij by kontynuować..", 1000, 650, white)
        kaf_1 = screen.blit(graph.kafel[0], (507, 453))
        kaf_2 = screen.blit(graph.kafel_2[0], (630, 382))
        kaf_3 = screen.blit(graph.kafel_3[0], (644, 124))
        kaf_4 = screen.blit(graph.kafel_4[0], (440, 218))
        kaf_5 = screen.blit(graph.kafel_5[0], (762, 265))
        kaf_6 = screen.blit(graph.kafel_6[0], (479, 116))
        kaf_7 = screen.blit(graph.kafel_7[0], (868, 391))
        kaf_8 = screen.blit(graph.kafel_8[0], (640, 44))
        if kaf_1.collidepoint((mx, my)):
            screen.blit(graph.kafel[1], (507, 453))
        if kaf_2.collidepoint((mx, my)):
            screen.blit(graph.kafel_2[1], (630, 382))
        if kaf_3.collidepoint((mx, my)):
            screen.blit(graph.kafel_3[1], (644, 124))
        if kaf_4.collidepoint((mx, my)):
            screen.blit(graph.kafel_4[1], (440, 218))
        if kaf_5.collidepoint((mx, my)):
            screen.blit(graph.kafel_5[1], (762, 265))
        if kaf_6.collidepoint((mx, my)):
            screen.blit(graph.kafel_6[1], (479, 116))
        if kaf_7.collidepoint((mx, my)):
            screen.blit(graph.kafel_7[1], (868, 391))
            if click:
                loadingSound.play()
                wejsciedogry()
        if kaf_8.collidepoint((mx, my)):
            screen.blit(graph.kafel_8[1], (640, 44))
        pygame.display.update()
        mainClock.tick()


# Wejście do gry


def wejsciedogry():
    bg_x = 0
    bg_x2 = graph.bg.get_width()
    starter = 0
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        bg_x -= 1
        bg_x2 -= 1
        if bg_x < graph.bg.get_width() * -1:
            bg_x = graph.bg.get_width()
        if bg_x2 < graph.bg.get_width() * -1:
            bg_x = graph.bg.get_width()

        screen.fill(black)
        screen.blit(graph.bg, (bg_x, 0))
        screen.blit(graph.bg, (bg_x2, 0))
        if starter != 29:
            screen.blit(graph.animated_Logo[starter], (490 * xw, 430 * xh))
            starter += 1
        if starter == 29:
            starter = 0

        button = screen.blit(graph.press_Enter[0], (450 * xw, 570 * xh))
        button_x = screen.blit(graph.press_Option[0], (680 * xw, 570 * xh))
        screen.blit(graph.kajdanki[0], (900 * xw, 500 * xh))
        screen.blit(graph.pistol[0], (0 * xw, 500 * xh))
        screen.blit(graph.nakladka_bg, (0 * xw, 0 * xh))

        mx, my = pygame.mouse.get_pos()

        if button_x.collidepoint((mx, my)):
            screen.blit(graph.press_Option[1], (680 * xw, 570 * xh))
            screen.blit(graph.kajdanki[1], (900 * xw, 500 * xh))
            if click:
                loadingSound.play()
                info()

        if button.collidepoint((mx, my)):
            screen.blit(graph.press_Enter[1], (450 * xw, 570 * xh))
            screen.blit(graph.pistol[1], (0 * xw, 500 * xh))
            if click:
                loadingSoundDEV.play()
                kontynuacja_gry()

        pygame.display.update()
        mainClock.tick(30)


# Kontynuacja gry


def kontynuacja_gry():
    running = True
    scena_save = None
    check_presave = check_file_save.checking_presave()
    if check_presave == 1:
        delete_db.delete_db_0_save()
    check_save = check_file_save.checking_save()
    if check_save == 1:
        scena_save = db_save.search_dane_save()
        if scena_save != "save_1":
            delete_db.delete_db_continue()
            check_save = check_file_save.checking_save()
    while running:

        click = False
        screen.fill(black)
        screen.blit(graph.kontynuacja_bg, (200, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        drzwi_x = screen.blit(graph.drzwi_nowa_gra[0], (608, 228))

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

        if check_save == 1:
            pisak.pisz("w0", "[INFO]", 620, 500, white)
            pisak.pisz("w1", "Posiadasz już zapisaną grę.", 510, 530, white)
            pisak.pisz("w1", "Jeżeli wybierzesz nową grę, stracisz dotychczasowy postęp.", 360, 560, white)
            dalej_x = screen.blit(graph.okno_kontynuacja[0], (875, 177))
            if dalej_x.collidepoint((mx, my)):
                screen.blit(graph.okno_kontynuacja[1], (875, 177))
                if click:
                    pygame.mixer.music.stop()
                    loadingSoundDEV.play()
                    if scena_save == "save_1":
                        scena_prog_3()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                loadingSound.play()
                break

        if drzwi_x.collidepoint((mx, my)):
            screen.blit(graph.drzwi_nowa_gra[1], (608, 228))
            if click:
                loadingSound.play()
                if check_save == 1:
                    delete_db.delete_db_continue()
                start()

        pygame.display.update()
        mainClock.tick()


# Start


def start():
    nazwa_gracza = []
    running = True
    imie_gracza = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.maszyna_bg, (0, 0))
        screen.blit(graph.key_enter[1], (565, 570))

        pisak.pisz("wers1", "Podaj imię. Zatwierdź        a następnie naciśnij 'Dalej'", 330, 600, white)

        for i, litera in enumerate(nazwa_gracza):
            pisak.pisz("wers2", litera, 620 + i * 12, 150, white)

        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

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

        q_nopress = screen.blit(graph.key_q[0], (315, 400))
        if q_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_q[1], (315, 400))
            if click:
                klik.play()
                nazwa_gracza.append("Q")

        w_nopress = screen.blit(graph.key_w[0], (365, 390))
        if w_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_w[1], (365, 390))
            if click:
                klik.play()
                nazwa_gracza.append("W")

        e_nopress = screen.blit(graph.key_e[0], (427, 388))
        if e_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_e[1], (427, 388))
            if click:
                klik.play()
                nazwa_gracza.append("E")

        r_nopress = screen.blit(graph.key_r[0], (487, 388))
        if r_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_r[1], (487, 388))
            if click:
                klik.play()
                nazwa_gracza.append("R")

        t_nopress = screen.blit(graph.key_t[0], (547, 388))
        if t_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_t[1], (547, 388))
            if click:
                klik.play()
                nazwa_gracza.append("T")

        z_nopress = screen.blit(graph.key_z[0], (610, 388))
        if z_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_z[1], (610, 388))
            if click:
                klik.play()
                nazwa_gracza.append("Z")

        u_nopress = screen.blit(graph.key_u[0], (670, 390))
        if u_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_u[1], (670, 390))
            if click:
                klik.play()
                nazwa_gracza.append("U")

        i_nopress = screen.blit(graph.key_i[0], (730, 390))
        if i_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_i[1], (730, 390))
            if click:
                klik.play()
                nazwa_gracza.append("I")

        o_nopress = screen.blit(graph.key_o[0], (790, 390))
        if o_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_o[1], (790, 390))
            if click:
                klik.play()
                nazwa_gracza.append("O")

        p_nopress = screen.blit(graph.key_p[0], (862, 399))
        if p_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_p[1], (862, 399))
            if click:
                klik.play()
                nazwa_gracza.append("P")

        os_nopress = screen.blit(graph.key_os[0], (922, 402))
        if os_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_os[1], (922, 402))
            if click:
                klik.play()
                nazwa_gracza.append("O")

        a_nopress = screen.blit(graph.key_a[0], (328, 459))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (328, 459))
            if click:
                klik.play()
                nazwa_gracza.append("A")

        s_nopress = screen.blit(graph.key_s[0], (393, 460))
        if s_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_s[1], (393, 460))
            if click:
                klik.play()
                nazwa_gracza.append("S")

        d_nopress = screen.blit(graph.key_d[0], (455, 459))
        if d_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_d[1], (455, 459))
            if click:
                klik.play()
                nazwa_gracza.append("D")

        f_nopress = screen.blit(graph.key_f[0], (510, 460))
        if f_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_f[1], (510, 460))
            if click:
                klik.play()
                nazwa_gracza.append("F")

        g_nopress = screen.blit(graph.key_g[0], (575, 460))
        if g_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_g[1], (575, 460))
            if click:
                klik.play()
                nazwa_gracza.append("G")

        h_nopress = screen.blit(graph.key_h[0], (635, 460))
        if h_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_h[1], (635, 460))
            if click:
                klik.play()
                nazwa_gracza.append("H")

        j_nopress = screen.blit(graph.key_j[0], (695, 460))
        if j_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_j[1], (695, 460))
            if click:
                klik.play()
                nazwa_gracza.append("J")

        k_nopress = screen.blit(graph.key_k[0], (755, 460))
        if k_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_k[1], (755, 460))
            if click:
                klik.play()
                nazwa_gracza.append("K")

        l_nopress = screen.blit(graph.key_l[0], (815, 460))
        if l_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_l[1], (815, 460))
            if click:
                klik.play()
                nazwa_gracza.append("L")

        es_nopress = screen.blit(graph.key_es[0], (875, 460))
        if es_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_es[1], (875, 460))
            if click:
                klik.play()
                nazwa_gracza.append("E")

        as_nopress = screen.blit(graph.key_as[0], (932, 460))
        if as_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_as[1], (932, 460))
            if click:
                klik.play()
                nazwa_gracza.append("A")

        y_nopress = screen.blit(graph.key_y[0], (357, 516))
        if y_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_y[1], (357, 516))
            if click:
                klik.play()
                nazwa_gracza.append("Y")

        x_nopress = screen.blit(graph.key_x[0], (421, 516))
        if x_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_x[1], (421, 516))
            if click:
                klik.play()
                nazwa_gracza.append("X")

        c_nopress = screen.blit(graph.key_c[0], (481, 516))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (481, 516))
            if click:
                klik.play()
                nazwa_gracza.append("C")

        v_nopress = screen.blit(graph.key_v[0], (542, 516))
        if v_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_v[1], (542, 516))
            if click:
                klik.play()
                nazwa_gracza.append("V")

        b_nopress = screen.blit(graph.key_b[0], (600, 516))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (600, 516))
            if click:
                klik.play()
                nazwa_gracza.append("B")

        n_nopress = screen.blit(graph.key_n[0], (660, 516))
        if n_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_n[1], (660, 516))
            if click:
                klik.play()
                nazwa_gracza.append("N")

        m_nopress = screen.blit(graph.key_m[0], (720, 516))
        if m_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_m[1], (720, 516))
            if click:
                klik.play()
                nazwa_gracza.append("M")

        del_nopress = screen.blit(graph.key_kasuj[0], (275, 510))
        if del_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_kasuj[1], (275, 510))
            if click:
                klik.play()
                nazwa_gracza.clear()
                imie_gracza = "".join(str(x) for x in nazwa_gracza)

        if not nazwa_gracza:
            pisak.pisz("wersa1", "Wpisz imię.", 600, 150, red)

        if nazwa_gracza:
            enter_nopress = screen.blit(graph.key_enter[0], (965, 503))
            if enter_nopress.collidepoint((mx, my)):
                screen.blit(graph.key_enter[1], (965, 503))
                if click:
                    klik.play()
                    imie_gracza = "".join(str(x) for x in nazwa_gracza)

        if imie_gracza:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    objasnienie(imie_gracza)

        pygame.display.update()
        mainClock.tick()


# Objaśnienie


def objasnienie(imie_gracza):
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.bgankieta, (200, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        dalej = screen.blit(graph.press_Kariera[0], (1100, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Kariera[1], (1100, 570))
            if click:
                db_save.create_db_account()
                db_save.aktualizuj_dane_gracza("dane_gracza", "imie_gracza", imie_gracza)
                db_save.aktualizuj_dane_gracza("dane_gracza", "stopien_sluzbowy", "posterunkowy")
                db_save.aktualizuj_dane_gracza("dane_gracza", "grupa_zaszeregowania", "kursant")
                pygame.mixer.music.stop()
                loadingSoundDEV.play()
                scena1()

        pisak.pisz("wers", "[ AKTA OSOBOWE ]", 30, 120, white)
        pisak.pisz("wers1", "Dane funkcjonariusza :", 30, 150, white)
        pisak.pisz("wers1a", imie_gracza, 280, 150, white)
        pisak.pisz("wers3", "Stopień : Posterunkowy", 30, 180, white)
        screen.blit(graph.post, (30, 210))
        pisak.pisz("wers4", "Data i miejsce urodzenia : 26.05.1988r Warszawa", 30, 340, white)
        pisak.pisz("wers5", "Postępowanie kwalifikacyjne : POZYTYWNIE", 30, 370, white)
        pisak.pisz("wers6", "Ankieta bezpieczeństwa : POZYTYWNIE", 30, 400, white)
        pisak.pisz("wers7", "Przydział : (brak) *kurs podstawowy od 06 października 2008r.", 30, 430, white)
        pisak.pisz("wers8", "NUMER ODZNAKI : 997187", 30, 460, white)
        pisak.pisz("wers9", "**Posterunkowy(-a)! Jeśli jesteś gotowy(-a) na szkolenie, naciśnij 'Kariera'**",
                   260, 500, dyellow)
        screen.blit(graph.odznaka, (40, 490))

        pygame.display.update()
        mainClock.tick()


# Scena 1


def scena1():
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    text = dialogs.text_scena_1
    siren.play(-1)
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.wspol, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                experience.check_exp()
                loadingSound.play()
                scena2()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 30, 120 + poz_y, white)
            poz_y += 30

        pisak.pisz("x", "**Możesz najechać myszką na słowa na niebieskim tle i podejrzeć co się tam kryje.", 30, 580, dyellow)

        akademik_poj = screen.blit(graph.akademik[0], (510, 177))
        mundurx = screen.blit(graph.czarnuch[0], (885, 212))

        if mundurx.collidepoint((mx, my)):
            screen.blit(graph.czarnuch[1], (895, 230))

        if akademik_poj.collidepoint((mx, my)):
            screen.blit(graph.akademik[1], (500, 195))

        pygame.display.update()
        mainClock.tick()


# Scena 2


def scena2():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    text = dialogs.text_scena_2
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.wspol, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena3()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 30, 120 + poz_y, white)
            poz_y += 30

        pygame.display.update()
        mainClock.tick()


# Scena 3


def scena3():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    text = dialogs.text_scena_3
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                experience.check_exp()
                loadingSound.play()
                scena4()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 30, 120 + poz_y, white)
            poz_y += 30

        pygame.display.update()
        mainClock.tick()


# Scena 4


def scena4():
    db_save.update_exp_ang_dni("exp", "dane_konta", 2)
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 2)
    text = dialogs.text_scena_4
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.strzelnica, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                experience.check_exp()
                loadingSound.play()
                scena5()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 30, 120 + poz_y, white)
            poz_y += 30

        spluwa = screen.blit(graph.p99[0], (819, 211))

        if spluwa.collidepoint((mx, my)):
            screen.blit(graph.p99[1], (820, 238))

        pygame.display.update()
        mainClock.tick(60)


# Scena 5


def scena5():
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 5)
    db_save.update_exp_ang_dni("exp", "dane_konta", 5)
    text = dialogs.text_scena_5
    dane_konta = experience.aktualny_stan_konta()
    stan_portfela = round(dane_konta[7], 2)
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.wspol, (0, 0))
        button_nie = screen.blit(graph.nie[0], (470, 600))
        button_tak = screen.blit(graph.tak[0], (660, 600))
        screen.blit(graph.portfel, (1115, 530))

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

        if button_nie.collidepoint((mx, my)):
            screen.blit(graph.nie[1], (470, 600))
            if click:
                loadingSound.play()
                scena_prog()

        if button_tak.collidepoint((mx, my)):
            screen.blit(graph.tak[1], (660, 600))
            if click:
                cashpaid.play()
                db_save.update_exp_ang_dni("stan_konta", "dane_konta", -60)
                experience.check_exp()
                silownia()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 30, 120 + poz_y, white)
            poz_y += 30

        pisak.pisz("wers12", "--> Idziesz z Tomkiem na siłownię ? (Koszt 60zł)", 20, 530, dyellow)
        pisak.pisz("wers2k", str(stan_portfela), 1135, 603, white)

        kulka = screen.blit(graph.kulkamocy[0], (700, 298))

        if kulka.collidepoint((mx, my)):
            screen.blit(graph.kulkamocy[1], (800, 320))

        pygame.display.update()
        mainClock.tick(60)


# Siłownia


def silownia():
    siren.stop()
    silowniaOGG.play(-1)
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    db_save.add_1_value("dane_ekwipunek", "usb")
    db_save.add_2_value("dane_quest_tomek", "silownia", "Przyszedł ze mną ale gdzieś poszedł..")
    text = dialogs.text_silownia_1
    dane_konta = experience.aktualny_stan_konta()
    stan_portfela = round(dane_konta[7], 2)
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.silka, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        screen.blit(graph.portfel, (1115, 530))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                eq_wav.play()
                tk_box.informacja("Pendrive ze starymi testami", graph.pendrive_src)
                loadingSound.play()
                scena_prog()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 30, 120 + poz_y, white)
            poz_y += 30

        pisak.pisz("wers2k", str(stan_portfela), 1135, 603, white)

        pygame.display.update()
        mainClock.tick(60)


# ScenaProg


def scena_prog():
    siren.stop()
    silowniaOGG.stop()
    progOGG.play(-1)
    text = dialogs.text_scena_prog
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.prog, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena6()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 30, 320 + poz_y, white)
            poz_y += 30

        pygame.display.update()
        mainClock.tick()


# Scena 6


def scena6():
    progOGG.stop()
    siren.play(-1)
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 2)
    db_save.update_exp_ang_dni("exp", "dane_konta", 2)
    db_save.add_1_value("dane_notatki", "legitymowanie")
    dane_konta = experience.aktualny_stan_konta()
    stan_portfela = round(dane_konta[7], 2)
    text = dialogs.text_scena_6
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        button_nie = screen.blit(graph.nie[0], (470, 600))
        button_tak = screen.blit(graph.tak[0], (660, 600))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        screen.blit(graph.portfel, (1115, 530))

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

        if button_nie.collidepoint((mx, my)):
            screen.blit(graph.nie[1], (470, 600))
            if click:
                loadingSound.play()
                scena7()

        if button_tak.collidepoint((mx, my)):
            screen.blit(graph.tak[1], (660, 600))
            if click:
                cashpaid.play()
                db_save.update_exp_ang_dni("stan_konta", "dane_konta", -60)
                experience.check_exp()
                silownia1()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 20, 150 + poz_y, white)
            poz_y += 30

        pisak.pisz("wers7", "--> Idziesz z Tomkiem na siłownię ? (Koszt 60zł)", 20, 530, dyellow)
        pisak.pisz("wers2k", str(stan_portfela), 1135, 603, white)
        pygame.display.update()
        mainClock.tick(60)


# Siłownia 1


def silownia1():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    db_save.add_2_value("dane_quest_tomek", "silownia_2", "Wyszedł z sali i wrócił po 20 minutach..")
    dane_konta = experience.aktualny_stan_konta()
    stan_portfela = round(dane_konta[7], 2)
    siren.stop()
    silowniaOGG.play(-1)
    text = dialogs.text_silownia_2
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.silka, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        screen.blit(graph.portfel, (1115, 530))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                silowniaOGG.stop()
                siren.play()
                loadingSound.play()
                scena7()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 20, 150 + poz_y, white)
            poz_y += 30

        pisak.pisz("wers2k", str(stan_portfela), 1135, 603, white)
        pygame.display.update()
        mainClock.tick(60)


# Scena 7


def scena7():
    db_save.update_exp_ang_dni("exp", "dane_konta", 6)
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 6)
    text = dialogs.text_scena_7
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.wspol, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena8()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 20, 150 + poz_y, white)
            poz_y += 30

        pygame.display.update()
        mainClock.tick(60)


# Scena 8


def scena8():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    text = dialogs.text_scena_8
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena9()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 30, 120 + poz_y, white)
            poz_y += 30

        pygame.display.update()
        mainClock.tick(60)


# Scena 9


def scena9():
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    text = dialogs.text_scena_9
    running = True
    while running:
        poz_y = 30
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena10()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for ver in text:
            pisak.pisz("w", ver, 30, 120 + poz_y, white)
            poz_y += 30

        pygame.display.update()
        mainClock.tick(60)


# Scena 10


def scena10():
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 3)
    db_save.update_exp_ang_dni("exp", "dane_konta", 3)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                egzamin_leg()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Minął weekend.. Kurde.. powroty są fajne.. ale najfajniejsze są - wyjazdy na powroty"
                           " do domu..", 20, 150, white)
        pisak.pisz("wers1", "Po kompanii chodzi plotka, że jutro wszystkie plutony mają 'niezapowiedzianą' wejściówkę"
                            " z legitymowania.", 20, 180, white)
        pisak.pisz("wers2", "Wejściówka czyli kartkówka. O kurdę nic się nie uczyłeś(-aś) w weekend!", 20, 210, white)
        pisak.pisz("wers3", "Chyba warto sobie przypomnieć co ostatnio było na zajęciach..", 20, 240, white)

        pygame.display.update()
        mainClock.tick(60)


# Egzamin z legitymowania ---------------


def egzamin_leg():
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    siren.stop()
    szum.play(-1)
    running = True
    odp1 = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        if active == "usb":
            pisak.pisz("wers5", "[Podpowiedź z USB] - A", 455, 550, brown)

        pisak.pisz("wers", "Czemu służy legitymowanie?", 450, 100, red)
        pisak.pisz("wers1", "Żeby potwierdzić tożsamość osoby", 450, 130, white)
        if odp1 == "a":
            pisak.pisz("wers1", "Żeby potwierdzić tożsamość osoby", 450, 130, dyellow)
        pisak.pisz("wers2", "Żeby wykazać, że coś robię na służbie", 450, 190, white)
        if odp1 == "b":
            pisak.pisz("wers2", "Żeby wykazać, że coś robię na służbie", 450, 190, dyellow)
        pisak.pisz("wers3", "Legitymowanie jest zbędne, służy statystyce", 450, 250, white)
        if odp1 == "c":
            pisak.pisz("wers3", "Legitymowanie jest zbędne, służy statystyce", 450, 250, dyellow)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp1:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp1 = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp1 = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp1 = "c"

        if odp1:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_leg2(odp1)
        pygame.display.update()
        mainClock.tick(60)


# Pytanie 2----------------------


def egzamin_leg2(odp1):
    odp2 = None
    running = True
    while running:
        click = False
        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        if active == "usb":
            pisak.pisz("wers5", "[Podpowiedź z USB] - B", 455, 550, brown)

        pisak.pisz("wers", "Przy legitymowaniu warto zachować..", 450, 100, red)
        pisak.pisz("wers1", "Kółko bezpieczeństwa", 450, 130, white)
        if odp2 == "a":
            pisak.pisz("wers1", "Kółko bezpieczeństwa", 450, 130, dyellow)
        pisak.pisz("wers2", "Trójkąt bezpieczeństwa", 450, 190, white)
        if odp2 == "b":
            pisak.pisz("wers2", "Trójkąt bezpieczeństwa", 450, 190, dyellow)
        pisak.pisz("wers3", "pół litra na czarną godzinę", 450, 250, white)
        if odp2 == "c":
            pisak.pisz("wers3", "pół litra na czarną godzinę", 450, 250, dyellow)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp2:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp2 = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp2 = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp2 = "c"

        if odp2:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_leg3(odp1, odp2)
        pygame.display.update()
        mainClock.tick(60)


# Pytanie 3----------------------


def egzamin_leg3(odp1, odp2):
    odp3 = None
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        if active == "usb":
            pisak.pisz("wers5", "[Podpowiedź z USB] - B lub C", 455, 550, brown)

        pisak.pisz("wers", "Podstawą prawną legitymowania jest:", 450, 100, red)
        pisak.pisz("wers1", "Moje widzi mi się", 450, 130, white)
        if odp3 == "a":
            pisak.pisz("wers1", "Moje widzi mi się", 450, 130, dyellow)
        pisak.pisz("wers2", "art. 515 Ustawy o broni i amunicji", 450, 190, white)
        if odp3 == "b":
            pisak.pisz("wers2", "art. 515 Ustawy o broni i amunicji", 450, 190, dyellow)
        pisak.pisz("wers3", "art. 15 Ustawy o Policji", 450, 250, white)
        if odp3 == "c":
            pisak.pisz("wers3", "art. 15 Ustawy o Policji", 450, 250, dyellow)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp3:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp3 = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp3 = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp3 = "c"

        if odp3:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_leg4(odp1, odp2, odp3)

        pygame.display.update()
        mainClock.tick(60)


# Pytanie 4----------------------


def egzamin_leg4(odp1, odp2, odp3):
    odp4 = None
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        if active == "usb":
            pisak.pisz("wers5", "[Podpowiedź z USB] - A lub C", 455, 550, brown)

        pisak.pisz("wers", "W przypadku odmowy okazania dokumentu tożsamości, ma zastasowanie:", 450, 100, red)
        pisak.pisz("wers1", "art.65 par. 2 Kodeksu Wykroczeń", 450, 130, white)
        if odp4 == "a":
            pisak.pisz("wers1", "art.65 par. 2 Kodeksu Wykroczeń", 450, 130, dyellow)
        pisak.pisz("wers2", "Pałka służbowa", 450, 190, white)
        if odp4 == "b":
            pisak.pisz("wers2", "Pałka służbowa", 450, 190, dyellow)
        pisak.pisz("wers3", "art. 15 Ustawy o Policji", 450, 250, white)
        if odp4 == "c":
            pisak.pisz("wers3", "art. 15 Ustawy o Policji", 450, 250, dyellow)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp4:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp4 = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp4 = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp4 = "c"

        if odp4:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    wyniki_leg(odp1, odp2, odp3, odp4)
        pygame.display.update()
        mainClock.tick(60)


# Wyniki z legitymowania


def wyniki_leg(odp1, odp2, odp3, odp4):
    dane_gracza = db_save.pobierz_dane("dane_gracza")
    jeden = 1
    if odp1 == "a":
        odp1x = 1
    else:
        odp1x = 0

    if odp2 == "b":
        odp2x = 1
    else:
        odp2x = 0

    if odp3 == "c":
        odp3x = 1
    else:
        odp3x = 0

    if odp4 == "a":
        odp4x = 1
    else:
        odp4x = 0
    ocena = jeden + odp1x + odp2x + odp3x + odp4x
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                eq_wav.play()
                if ocena == 5:
                    tk_box.informacja("+10 doświadczenia, +10 zaangażowania ", graph.zaang_up)
                    db_save.update_exp_ang_dni("exp", "dane_konta", 10)
                    db_save.update_exp_ang_dni("ang", "dane_konta", 10)
                    db_save.add_1_value("dane_indeks", 5)
                elif ocena == 4:
                    tk_box.informacja("+7 doświadczenia", graph.zaang_up)
                    db_save.update_exp_ang_dni("exp", "dane_konta", 7)
                    db_save.add_1_value("dane_indeks", 4)
                elif ocena == 3:
                    tk_box.informacja("+3 doświadczenia", graph.zaang_up)
                    db_save.update_exp_ang_dni("exp", "dane_konta", 3)
                    db_save.add_1_value("dane_indeks", 3)
                elif ocena == 2:
                    db_save.update_exp_ang_dni("exp", "dane_konta", 2)
                    db_save.add_1_value("dane_indeks", 2)
                else:
                    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                    db_save.add_1_value("dane_indeks", 1)
                siren.stop()
                loadingSound.play()
                scena_prog1()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wersX", dane_gracza[0][0], 600, 220, white)
        pisak.pisz("wers", "Twoja ocena z testu LEGITYMOWANIA!", 450, 250, white)

        try:
            if ocena == 5:
                pisak.pisz("wers1", "Gratulacje kujonie! Dostałeś 5!", 450, 510, dyellow)
                screen.blit(graph.cyfra5, (580, 300))
            if ocena == 4:
                pisak.pisz("wers2", "Całkiem, całkiem. Dostałeś 4!", 450, 510, dyellow)
                screen.blit(graph.cyfra4, (580, 300))
            if ocena == 3:
                pisak.pisz("wers3", "Mogło pójść lepiej.. Tylko 3?", 450, 510, dyellow)
                screen.blit(graph.cyfra3, (580, 300))
            if ocena == 2:
                pisak.pisz("wers4", "Jak chcesz skończyć kurs to weź się do nauki miernoto. Dostałeś(-aś) 2!",
                           250, 510, dyellow)
                screen.blit(graph.cyfra2, (580, 300))
            if ocena == 1:
                pisak.pisz("wers5", "Głowa pusta jak kapusta. Dostałeś pałę..", 400, 510, dyellow)
                screen.blit(graph.cyfra1, (580, 300))
        except ValueError:
            pisak.pisz("wersX", "Jeśli to widzisz - to jest to nieoczekiwany błąd gry (Zgłoś mi to)", 300, 510, red)

        pygame.display.update()
        mainClock.tick(60)


# SCENA PROG1


def scena_prog1():
    szum.stop()
    progOGG.play()
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.prog, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                progOGG.stop()
                loadingSound.play()
                scena11()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Jako młody adept otrzymujesz od szefa kompanii indeks!", 20, 490, dyellow)
        pisak.pisz("wers1", "W indeksie znajduje się spis przedmiotów do zaliczenia i Twoje dotychczasowe oceny.",
                   20, 520, dyellow)

        pygame.display.update()
        mainClock.tick(60)


# Scena 11


def scena11():
    siren.play()
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    dane_konta = experience.aktualny_stan_konta()
    stan_portfela = round(dane_konta[7], 2)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        button_nie = screen.blit(graph.nie[0], (470, 600))
        button_tak = screen.blit(graph.tak[0], (660, 600))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        screen.blit(graph.portfel, (1115, 530))

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

        if button_nie.collidepoint((mx, my)):
            screen.blit(graph.nie[1], (470, 600))
            if click:
                loadingSound.play()
                scena12()

        if button_tak.collidepoint((mx, my)):
            screen.blit(graph.tak[1], (660, 600))
            if click:
                siren.stop()
                cashpaid.play()
                db_save.update_exp_ang_dni("stan_konta", "dane_konta", -200)
                experience.check_exp()
                bar()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Pierwsze koty za płoty, pierwszy test za Tobą, chyba czas na jakieś odreagowanie.",
                   20, 150, white)
        pisak.pisz("wers1", "Jutro większość dnia to zajęcia na strzelnicy to za bardzo nie ma z czego się uczyć.",
                   20, 180, white)
        pisak.pisz("wers2", "Dowódca po zajęciach zrobił apel dla całej kompanii i powiedział, że od dziś może"
                            " wydawać przepustki.", 20, 210, white)
        pisak.pisz("wers3", "Przepustka umożliwia wyjście za teren szkoły do określonej godziny.", 20, 240, white)
        pisak.pisz("wers4", "Dowódca Twojego plutonu - Jacek - rzucił hasło by wyjść na jakieś piwo całym plutonem.",
                   20, 270, white)
        pisak.pisz("wers5", "Podobno przy szkole jest jakiś bar, który nazywa się - 'CELA'.", 20, 300, white)
        pisak.pisz("wers6", "--> Idziesz na piwo? (Koszt 200zł)", 20, 530, dyellow)
        pisak.pisz("wers2k", str(stan_portfela), 1135, 603, white)

        cela_bar = screen.blit(graph.cela[0], (627, 302))

        if cela_bar.collidepoint((mx, my)):
            screen.blit(graph.cela[1], (630, 320))

        pygame.display.update()
        mainClock.tick()


# Bar


def bar():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    dane_konta = experience.aktualny_stan_konta()
    stan_portfela = round(dane_konta[7], 2)
    barSound.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.barBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        screen.blit(graph.portfel, (1115, 530))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                bar1()

        pisak.pisz("wers", "Nie jesteś outsiderem i idziesz się trochę rozerwać. Na wyjście do ludzi, wkładasz"
                           " lepsze ciuchy.", 20, 150, white)
        pisak.pisz("wers1", "Bar, knajpa, klub - jak zwał tak zwał - schodzisz do piwnicy i już słyszysz odgłosy"
                            " ludzi i stłumiony dźwięk basu.", 20, 180, white)
        pisak.pisz("wers2", "Rozglądasz się i zdajesz sobie sprawę, że kojarzysz każdą mordę ze szkolnych korytarzy.",
                   20, 210, white)
        pisak.pisz("wers3", "- Co to policyjny pub? - pytasz się Anki ale jest tak głośno, że chyba nic nie słyszała.",
                   20, 240, white)
        pisak.pisz("wers4", "Iwona macha do Ciebie ręką i pokazuje palcem pusty stoilik, idziecie i zajmujecie"
                            " miejsce.", 20, 270, white)
        pisak.pisz("wers5", "- Dobra to co kto pije?! - krzyczy Tomek. Ustalacie, że zaczynacie od piwa.",
                   20, 300, white)
        pisak.pisz("wers6", "- Jak tam! - do stolika podchodzi dowódca Waszego plutonu, Jacek Wilczek.", 20, 330, white)
        pisak.pisz("wers7", "- Spoko! Dużo ludu! A Wy gdzie siedzicie!? - próbujesz przebić się przez odgłos muzyki.",
                   20, 360, white)
        pisak.pisz("wers8", "- Wszędzie! - odpowiada. - Chodzę i szukam ludzi od nas, bo każdy porozsiadał się tam",
                   20, 390, white)
        pisak.pisz("wers9", "gdzie było jakieś wolne miejsce! Jak skończycie piweczko to zapraszam do nas! Jesteśmy",
                   20, 420, white)
        pisak.pisz("wers10", "W drugim końcu sali! - pokazuje Wam kierunek. - Dobra, zawitamy! - odpowiada Tomek.",
                   20, 450, white)
        pisak.pisz("wers11", "'Mniam ale to piwo dobre' - myślisz. Jednak miesiąc bez wyjścia robi swoje.. ",
                   20, 480, white)

        pisak.pisz("wers2k", str(stan_portfela), 1135, 603, white)

        pygame.display.update()
        mainClock.tick()


# Bar1


def bar1():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    dane_konta = experience.aktualny_stan_konta()
    stan_portfela = round(dane_konta[7], 2)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.barBG, (0, 0))
        button_nie = screen.blit(graph.nie[0], (470, 600))
        button_tak = screen.blit(graph.tak[0], (660, 600))
        screen.blit(graph.portfel, (1115, 530))

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

        if button_nie.collidepoint((mx, my)):
            screen.blit(graph.nie[1], (470, 600))
            if click:
                loadingSound.play()
                scena_bar_iwona()

        if button_tak.collidepoint((mx, my)):
            screen.blit(graph.tak[1], (660, 600))
            if click:
                if dane_konta[7] > 100:
                    cashpaid.play()
                    db_save.update_exp_ang_dni("stan_konta", "dane_konta", -100)
                    bar2()
                else:
                    pisak.pisz("wers11", "--> Nie masz tyle pieniędzy.. ", 20, 580, red)

        pisak.pisz("wers", "Po piwie, a właściwie dwóch - bo tak fajnie się Wam rozmawiało - idziecie do stolika"
                           " Jacka.", 20, 150, white)
        pisak.pisz("wers1", "- Elo! Siedem, dwa, zero - zarymował Jacek widząc Was przy stoliku. - Siadajcie."
                            " Stolik baczność!", 20, 180, white)
        pisak.pisz("wers2", "Zauważasz, że Jacek jest wstawiony. - To co? Wódżitsu? - pokazuje Wam butelkę Żołądkowej.",
                   20, 210, white)
        pisak.pisz("wers3", "- Dawaj - odpowiada Tomek. Jacek przelewa kieliszek, a reszta alkoholu ląduje na stoliku.",
                   20, 240, white)
        pisak.pisz("wers4", "- Słuchajcie, miesiąc za nami i oby tak dalej. Wykładowcy się na nas poznają i trochę nam"
                            " odpuszczą.", 20, 270, white)
        pisak.pisz("wers5", "Musimy trzymać się razem a wszystko będzie dobrze - mówi Jacek.", 20, 300, white)
        pisak.pisz("wers6", "- No zrozumiałe - wtóruje mu Anka, która przysiada się do niego nieco bliżej.",
                   20, 330, white)
        pisak.pisz("wers7", "Atmosfera zaczyna się zagęszczać a w pubie jakby coraz więcej osób.", 20, 360, white)
        pisak.pisz("wers8", "Proponujesz powrót do akademika ale Anka oświadcza, że wróci z Jackiem. Iwona jest za"
                            " powrotem.", 20, 390, white)
        pisak.pisz("wers9", "Tomka gdzieś wcieło, postaliście jeszcze 10 minut ale nigdzie go nie ma.", 20, 420, white)
        pisak.pisz("wers10", "--> Zostajesz jeszcze chwilę? (Koszt 100zł)", 20, 550, dyellow)

        pisak.pisz("wers2k", str(stan_portfela), 1135, 603, white)

        wodka_poj = screen.blit(graph.wodka[0], (880, 210))
        if wodka_poj.collidepoint((mx, my)):
            screen.blit(graph.wodka[1], (1000, 210))

        pygame.display.update()
        mainClock.tick(60)


# Bar2 + info do questu Tomka


def bar2():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    running = True
    dane_konta = experience.aktualny_stan_konta()
    stan_portfela = round(dane_konta[7], 2)
    db_save.add_2_value("dane_quest_tomek", "bar", "W 'CELI' wychodził z drzwi dla personelu")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.barBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        screen.blit(graph.portfel, (1115, 530))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena_bar_iwona()

        pisak.pisz("wers",
                   "Zostajecie jeszcze chwilę.. ", 20,
                   150, white)
        pisak.pisz("wers1",
                   "Pęcherz ciśnie niemiłosiernie, dlatego idziesz w kierunku łazienki.",
                   20, 180, white)
        pisak.pisz("wers2", "Z kilku metrów zauważasz Tomka, który wychodzi obok baru z drzwi oznaczonych"
                            " 'Tylko dla personelu'",
                   20, 210, white)
        pisak.pisz("wers3", "Nie zauważył Cię.. ",
                   20, 240, white)
        pisak.pisz("wers4",
                   "Tomek kieruje się w stronę wyjścia, wchodzi po schodach.", 20,
                   270, white)
        pisak.pisz("wers5", "Chcesz śledzić Tomka ale natura jednak daje o sobie znać -  lecisz do kibelka.",
                   20, 300, white)
        pisak.pisz("wers6", "Po 5 minutach idziesz w stronę wyjścia, gdzie czeka na Ciebie Iwona.", 20, 330,
                   white)
        pisak.pisz("wers7", "- No już myślałam, że wróciłeś(-aś) sam(-a).. ", 20, 360, white)
        pisak.pisz("wers8",
                   "**Wracacie do pokoju.. ",
                   20, 390, white)

        pisak.pisz("wers2k", str(stan_portfela), 1135, 603, white)

        pygame.display.update()
        mainClock.tick(60)


# ScenaBarIwona


def scena_bar_iwona():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    siren.stop()
    barSound.stop()
    siren.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokojnocBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena12()

        pisak.pisz("wers", "Pokój.. cisza, spokój.. w uszach jeszcze słyszysz rytm muzyki z pubu. Otwierasz okno"
                           " by przewietrzyć lokum.", 20, 150, white)
        pisak.pisz("wers1", "Anki nie ma - no tak została z Jackiem, ale gdzie Tomek? Ten zawsze gdzieś się ulotni..",
                   20, 180, white)
        pisak.pisz("wers2", "Iwona poszła wziąć prysznic a Ty kładziesz się w ubraniu na łóżko - hmm jakie miękkie.",
                   20, 210, white)
        pisak.pisz("wers3", "Po 15 minutach wyszła Iwona ale zabrakło Ci sił by wstać.. albo to lenistwo.",
                   20, 240, white)
        pisak.pisz("wers4", "Przy świetle małej, 20 watowej lampki zaczynacie rozmawiać.", 20, 270, white)
        pisak.pisz("wers5", "Na początku obgadujecie wyjście do CELI, kto się napił, kto wygłupiał itd.",
                   20, 300, white)
        pisak.pisz("wers6", "Rozmowa schodzi na Wasze zainteresowania, troche Wam cięko, że w takich warunkach"
                            " trzeba było", 20, 330, white)
        pisak.pisz("wers7", "odstawić swoje pasje i hobby w domu. Jeszcze.. albo aż - 5 miesięcy i koniec"
                            " - pocieszacie się.", 20, 360, white)
        pisak.pisz("wers8", "Właściwie to koniec szkoły a początek prawdziwej służby - sam(-a) przecież o tym od"
                            " zawsze marzyłeś(-aś)", 20, 390, white)
        pisak.pisz("wers9", "Posiedziałeś(-aś) chwilę w milczeniu - Iwona zasnęła. Ty leżysz dalej w ubraniu przy"
                            " zapalonej lampce.", 20, 420, white)
        pisak.pisz("wers10", "Ehh dobra czas zamknąć okno i iść spać. Podchodzisz do okna, chwilę się zatrzymujesz"
                             " i spoglądasz w niebo..", 20, 450, white)
        pisak.pisz("wers11", "Gwiazdy delikatnie migoczą na niebie, na zewnątrz jest cicho a przez uchylone okno"
                             " wieje chłodem..", 20, 480, white)
        pisak.pisz("wers12", "- Pięknie.. - rozmyślasz - Dobra idę spać.. jutro kolejny dzień - zamykasz"
                             " okno..", 20, 510, white)

        pygame.display.update()
        mainClock.tick(60)


# Scena12


def scena12():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 3)
    siren.stop()
    barSound.stop()
    siren.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        wejsc_x = screen.blit(graph.wejsc[0], (1109, 212))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena13()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Mijają kolejne dni, a nauki jest coraz więcej. Codziennie uczysz się ciekawszych rzeczy.",
                   20, 150, white)
        pisak.pisz("wers1", "Pojutrze masz zajęcia z ruchu drogowego ale na dzisiejszą noc, masz służbę jako dyżurny"
                            " akademika.", 20, 180, white)
        pisak.pisz("wers2", "W sumie nic takiego - masz siedzieć w kanciapie przy wejściu do akademika i ogarniać jakąś"
                            " książkę wejść\\wyjść.", 20, 210, white)
        pisak.pisz("wers3", "Zresztą.. przed służbą masz odprawę, na której wszystko zostanie Ci wyjaśnione.",
                   20, 240, white)
        pisak.pisz("wers4", "Poprzednie osoby, które miały już taki dyżur mówiły, że służba zależy od dyżurnego"
                            " szkoły.", 20, 270, white)
        pisak.pisz("wers5", "Jak jest luzak, to i służba przebiega luźno. Jak upierdliwy, to przyczepi się nawet do"
                            " guzika.", 20, 300, white)
        pisak.pisz("wers6", "Oprócz służb dyżurnych są jeszcze służby obchodowe, gdzie patroluje się teren szkoły"
                            " i magazyny.", 20, 330, white)
        pisak.pisz("wers7", "Najgorsze, że taka służba może wypaść też w weekend i wtedy nici z wyjazdu do domu.",
                   20, 360, white)
        pisak.pisz("wers8", "** Reszta dnia minęła spokojnie - psychicznie przygotowujesz się do swojej pierwszej"
                            " odprawy.", 20, 390, white)
        if wejsc_x.collidepoint((mx, my)):
            screen.blit(graph.wejsc[1], (809, 238))
        pygame.display.update()
        mainClock.tick(60)


# Scena13


def scena13():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.odprawaBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena14()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "19:00 - ruszasz na odprawę do sali 212 w akademiku nr 3. Odczuwasz lekki stres choć masz"
                           " wszystko co trzeba.", 20, 150, white)
        pisak.pisz("wers1", "Oprócz Ciebie na odprawie czekają już 3 inne osoby, które będą pełnić służby.",
                   20, 180, white)
        pisak.pisz("wers2", "Na odprawę przyszedł  ponad 50 letni opasły policjant w stopniu nadkomisarza, siwe długie"
                            " wąsy całkowicie", 20, 210, white)
        pisak.pisz("wers3", "zakrywały mu usta. Nie spoglądając na Was przeczytał zadania z kartki. Nakazał je zapisać"
                            " w notatnikach.", 20, 240, white)
        pisak.pisz("wers4", "Po odprawie podbił notatniki swoją imienną pieczątką, podpisał się gryzmołkiem i"
                            " powiedział, że noc ma", 20, 270, white)
        pisak.pisz("wers5", "minąć spokojnie. Odprawa trwałą tak szybko, że tylko zapisywałeś(-aś) ale nawet nie wiesz"
                            " co.", 20, 300, white)
        pisak.pisz("wers6", "Otwierasz notatnik i czytasz co napisałeś(-aś): 1.Przejąś służbę. 2.Zrobić obchód"
                            " korytarzy w swoim akademiku.", 20, 330, white)
        pisak.pisz("wers7", "3.Meldować telefonicznie o problemach.", 20, 360, white)
        pisak.pisz("wers8", "'Kurde w sumie mało' - myślisz sobie. EEE będzie luzacka służba, jak będzie nudno to się"
                            " zdrzemnę.", 20, 390, white)
        pisak.pisz("wers9", "Wchodząc do akademika z kanciapy dyżurnego wychodzi chłopak, który daje Ci biało-czerwoną"
                            " opaskę z napisem 'DYŻURNY'", 20, 420, white)
        pisak.pisz("wers10", "Zamieniasz z nim 2 słowa i rozchodzicie się - on idzie do pokoju a Ty zasiadasz na starym"
                             " krześle w kanciape.", 20, 450, white)
        pisak.pisz("wers11", "Przed Tobą biurko, książka przebiegłu służby i telefon bez klawiatury do połączenia"
                             " z wąsatym dyżurnym szkoły.", 20, 480, white)
        pisak.pisz("wers12", "'No to czas odbębnić 12 godzin' - zsuwasz się z krzesła zajmując wygodniejszą pozycję..",
                   20, 510, white)

        pygame.display.update()
        mainClock.tick(60)


# Scena14


def scena14():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
    siren.stop()
    korytarzSound.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.korytarzBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena15()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Do północy w akademiku był jako taki ruch, dopiero o 1:00 nastał spokój. Postanawiasz"
                           " trochę przymknąć oko..", 20, 150, white)
        pisak.pisz("wers1", "Budzisz się w dość niewygodnej pozycji, jest zimno, spoglądasz na zegarek"
                            " - dochodzi 02:45.", 20, 180, white)
        pisak.pisz("wers2", "No dobra, czas na sprawdzenie korytarzy, zgodnie z poleceniem na odprawie. Nie chce się"
                            " wychodzić z kanciapy", 20, 210, white)
        pisak.pisz("wers3", "bo już trochę się w niej zadomowiłeś(-aś). Światła zapalone są tylko w centralnej części"
                            " budynku, przy klatkach", 20, 240, white)
        pisak.pisz("wers4", "schodowych. W innych częściach akademika - gdyby nie światła latarni z zewnątrz - nic"
                            " byś nie widział(-a)", 20, 270, white)
        pisak.pisz("wers5", "'Kto projektował te budynki, gdzie na każde piętro można wejść przez 1 klatkę? Gdzie"
                            " bezpieczeństwo na wypadek", 20, 300, white)
        pisak.pisz("wers6", "pożaru?' - zastanawiasz się wchodząc na kolejny schodek. Wchodzisz na I piętro - cisza,"
                            " na II też cisza.", 20, 330, white)
        pisak.pisz("wers7", "'No jeszcze ostatnie III i wracam do siebie' - myślisz o kanciapie jak o jakimś swoim"
                            " miłym lokum.", 20, 360, white)
        pisak.pisz("wers8", "Będąc na III piętrze dostrzegasz nieco inny układ korytarzy. Na parterze, I i II piętrze,"
                            " jest po jednym dużym", 20, 390, white)
        pisak.pisz("wers9", "korytarzu, który przecina wejście do klatki schodowej i kończy się dużym oknem. Na III "
                            "piętrze jest inaczej.", 20, 420, white)
        pisak.pisz("wers10", "Korytarz kończy się wiekszą przestrzenią - Coś jak miejsce na ulicy, dla zawracania "
                             "samochodów ze ślepej uliczki.", 20, 450, white)
        pisak.pisz("wers11", "Idziesz w kierunku tego miejsca, zobaczyć czy obok są pokoje kursantów, jakaś sala, "
                             "czy jakieś inne pomieszczenia.", 20, 480, white)

        plan_poj = screen.blit(graph.plan[0], (776, 236))

        if plan_poj.collidepoint((mx, my)):
            screen.blit(graph.plan[1], (600, 255))

        pygame.display.update()
        mainClock.tick(60)


# Scena15


def scena15():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.korytarzBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena_sciana()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers0", "Powoli zmierzasz w kierunku obranego miejsca oddalając się od źródła światła.",
                   20, 120, white)
        pisak.pisz("wers", "W ciemności widzisz jedynie lekki zarys okna, znajdującego się około 20 metrów przed Tobą.",
                   20, 150, white)
        pisak.pisz("wers1", "- 'K**** co tu tak zimno' - chowasz głowę w barkach czując na karku gęsią skórkę.",
                   20, 180, white)
        pisak.pisz("wers2", "Podchodzisz do okna i opierasz się rękoma o zimny parapet.", 20, 210, white)
        pisak.pisz("wers3", "Światła latarni z ulicy, pozwalają dostrzec znajdujący się przed Tobą parking.",
                   20, 240, white)
        pisak.pisz("wers4", "Po lewej stronie stoją drzewa - zasłaniają widok. Po prawej stronie widzisz szlaban i"
                            " biuro przepustek.", 20, 270, white)
        pisak.pisz("wers5", "W środku siedzi młody policjant a jego twarz rozświetla blask malutkiego przenośnego "
                            "telewizora.", 20, 300, white)
        pisak.pisz("wers6", "Z III piętra widać nieco więcej. Z tego miejsca daleko po prawej stronie, dostrzegasz "
                            "jakiś kompleks zabudowań.", 20, 330, white)
        pisak.pisz("wers7", "- Jakiś kilometr' - próbujesz obliczyć w myślach odległość. Budynek stoi na odludziu "
                            "przy lesie.", 20, 360, white)
        pisak.pisz("wers8", "Wpatrujesz się dłuższą chwilę w to miejsce, zastanawiając się co tam jest '- Hmm powojenny"
                            " bunkier? Magazyny?'", 20, 390, white)
        pisak.pisz("wers9", "Skupiasz wzrok i dostrzegasz dziwny mały błysk przy zabudowaniach, światełko porusza się"
                            " wokół budynku,", 20, 420, white)
        pisak.pisz("wers10", "co chwile się zatrzymując. - Aaa już wiem - odpowiadasz sobie '- To te słynne"
                             " Falklandy.'", 20, 450, white)
        pisak.pisz("wers11", "'Falklandy' to nazwa magazynów i miejsce pełnienia służb przez policjantów "
                             "będących na kursie.", 20, 480, white)
        pisak.pisz("wers12", "Magazyny są zamknięte, podobno nic tam nie ma, po co więc je ochraniać?", 20, 510, white)
        pisak.pisz("wers13", "Przyjrzysz się temu bliżej jak będziesz miał(-a) tam służbę.. ** Wracasz do "
                             "kanciapy dyżurnego.", 20, 540, white)

        falklandy_poj = screen.blit(graph.falklandy[0], (875, 446))
        if falklandy_poj.collidepoint((mx, my)):
            screen.blit(graph.falklandy[1], (500, 200))

        pygame.display.update()
        mainClock.tick()


# Scena15


def scena_sciana():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.korytarzNOC, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena_prog2()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        pisak.pisz("wers0", "Jeden z obrazów, przykuwa Twoją uwagę. (Najedź myszką)", 20, 120, white)
        pisak.pisz("wers", "Ta kobieta jest jakaś.. ", 20, 150, white)
        pisak.pisz("wers1", "Obserwujesz jeszcze chwilę i wracasz do siebie. ", 20, 210, white)

        obraz_stary = screen.blit(graph.staryObraz[0], (334, 273))
        if obraz_stary.collidepoint((mx, my)):
            screen.blit(graph.staryObraz[1], (450, 50))

        screen.blit(graph.oko, (mx, my))
        pygame.display.update()
        mainClock.tick()


# SCENA PROG2


def scena_prog2():
    pygame.mouse.set_visible(False)
    korytarzSound.stop()
    progOGG.play()
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.prog, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        napis_policja_x = screen.blit(graph.napisPolicja, (640, 190))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                pygame.mouse.set_visible(True)
                progOGG.stop()
                loadingSound.play()
                scena16()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if napis_policja_x.collidepoint((mx, my)):
            screen.blit(graph.napisPolicja1, (640, 250))

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Jeśli napotkasz scenę, w której przy kursorze wyświetla się lupa - tak jak teraz",
                   20, 490, dyellow)
        pisak.pisz("wers1", "Bacznie obserwuj i poszukuj ciekawych przedmiotów na ekranie.",
                   20, 520, dyellow)
        screen.blit(graph.oko, (mx, my))
        pygame.display.update()
        mainClock.tick()


# Scena16


def scena16():
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    siren.play(-1)
    db_save.add_1_value("dane_notatki", "ruchdrogowy")
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena17()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Służba jako dyżurny to już przeszłość, czas wrócić do nauki.", 20, 120, white)
        pisak.pisz("wers1", "Pierwsze zajęcia z ruchu drogowego były nawet ciekawe, gdyby nie kilka jedynek na"
                            " 'dzień dobry'.", 20, 150, white)
        pisak.pisz("wers2", "Wykładowca chyba oszalał.. Pierwszy raz mieliście z nim zajęcia a on odpytywał"
                            " z zasad ruchu.", 20, 180, white)
        pisak.pisz("wers3", "Na początku zapytał kto ma prawo jazdy a później zadawał po jednym pytaniu.",
                   20, 210, white)
        pisak.pisz("wers4", "Kto znał odpowiedź, to przechodził do kolejnej osoby. Kto nie znał - dostawał pałę.",
                   20, 240, white)
        pisak.pisz("wers5", "Stwierdził, że policjant takie rzeczy musi mieć w paluszku, skoro ma wyciągać "
                            "konsekwencje od innych.", 20, 270, white)
        pisak.pisz("wers6", "Później puścił kilkadziesiąt slajdów i zapisywałeś(-aś) wszystko jak leciało, nawet "
                            "numery slajdów.", 20, 300, white)
        pisak.pisz("wers7", "Lepiej być przygotowanym na każdą ewentualność, skoro to taki oszołom..  "
                            "(Sprawdź notatnik)", 20, 330, white)
        pisak.pisz("wers8", "Po zajęciach wszyscy zakuwacie, no prawie wszyscy.. Anka coraz częściej przebywa z "
                            "Jackiem.", 20, 360, white)
        pisak.pisz("wers9", "Ostatnio to zrzuca tylko mundur, przebiera się w cywilki i wychodzą gdzieś na "
                            "przepustki.", 20, 390, white)
        pisak.pisz("wers10", "Ktoś z plutonu widział ich razem w parku i restauracji.. Waszą naukę przerywa"
                             " Iwona:", 20, 420, white)
        pisak.pisz("wers11", "- No i jak było na służbie, opowiadaj? - zadaje Ci pytanie. - No też jestem ciekawy "
                             "- dołącza się Tomek.", 20, 450, white)
        pisak.pisz("wers12", "- Aaa spoko.. - odpowiadasz na odczepnego.", 20, 480, white)
        pisak.pisz("wers13", "- Nic ciekawego? Żadnych interwencji? - drąży temat Iwona odkłądając zeszyt i "
                             "siada na krawędzi łóżka.", 20, 510, white)
        pisak.pisz("wers14", "- No nic ciekawego, zrobiłem(-am) ten nocny obchód po akademiku i wróciłem(-am) "
                             "do kanciapy", 20, 540, white)

        cywilkix = screen.blit(graph.cywilki[0], (557, 388))
        if cywilkix.collidepoint((mx, my)):
            screen.blit(graph.cywilki[1], (557, 428))

        pygame.display.update()
        mainClock.tick()


# Scena17


def scena17():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena18()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "- A to faktycznie nudną miałeś(-aś) nockę - puentuje Tomek, poprawia poduszkę i"
                           " kładzie się na niej wygodnie.", 20, 120, white)
        pisak.pisz("wers1", "Przypomina Ci się jednak magazyn, na który spoglądałeś(-aś) z III piętra i "
                            "zadajesz pytanie:", 20, 150, white)
        pisak.pisz("wers2", "- Słuchajcie a te Falklandy to co tam jest? Jakiś magazyn czy co?", 20, 180, white)
        pisak.pisz("wers3", "- Tak, jakiś stary przedwojenny - mówi Tomek - kiedyś składowano tam broń,",
                   20, 210, white)
        pisak.pisz("wers4", "później materace i koce a teraz.. teraz nic tam nie ma, a że to teren szkoły ",
                   20, 240, white)
        pisak.pisz("wers5", "to aby doszczętnie nie niszczało, policjanci mają tam patrole i łażą w dzień i w nocy.",
                   20, 270, white)
        pisak.pisz("wers6", "- No nie wiem czy nic.. - odpowiada Iwona spoglądając z politowaniem na "
                            "Tomka i kontynuuje.", 20, 300, white)
        pisak.pisz("wers7", "- Coś jest ale nie wiedzą o tym ani wykładowcy ani dyżurni, napewno wie komendant "
                            "szkoły, no bo po co", 20, 330, white)
        pisak.pisz("wers8", "wypuszczać tam codziennie patrole, które co.. które mają pilnować pustego magazynu? "
                            "Przecież jest ogrodzenie.", 20, 360, white)
        pisak.pisz("wers9", "- A na przykład po to by jako element zajęć był m.in. patrol tej rudery - odpowiada "
                            "Tomek.", 20, 390, white)
        pisak.pisz("wers10", "- A ja myślę, że tam jest coś innego - Iwona stwierdza stanowczo - Na poprzednim "
                             "kursie jak byłam, był w plutonie", 20, 420, white)
        pisak.pisz("wers11", "były student historii, gość z pasją. W cywilu lubił robić sobie wycieczki w różne "
                             "miejsca i odnajdywać..", 20, 450, white)
        pisak.pisz("wers12", "- Skarby!? HAHA - wtrącił Tomek. - Skarby - Srarby - odpowiadziała spokojnie Iwona - "
                             "Odnajdywał bunkry..", 20, 480, white)
        pisak.pisz("wers13", "- Na temat naszego szkolnego magazynu opowiedział pewną ciekawostkę. Przysłuchujesz "
                             "się uważniej.", 20, 510, white)
        pisak.pisz("wers14", "- To nie był magazyn czy bunkier tylko.. - Tylko co? - dopytujesz - Nazistowski "
                             "szpital..", 20, 540, white)

        pygame.display.update()
        mainClock.tick()


# Scena18


def scena18():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena19()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "- No i co w tym takiego dziwnego? Szpital, bunkier, magazyn i tak puste stoi. Dobra idę"
                           " spać, nie chce mi", 20, 120, white)
        pisak.pisz("wers1", "się Was wyprowadzać z tych bajek, dobranoc - zakończył Tomek i przewrócił się na"
                            " drugi bok.", 20, 150, white)
        pisak.pisz("wers2", "Spoglądasz w milczeniu na Iwonę i pytasz cicho - Co z tym szpitalem?", 20, 180, white)
        pisak.pisz("wers3", "- Wiesz, aż tak dużo nie pamiętam co mi ten historyk opowiadał ale mówił, że",
                   20, 210, white)
        pisak.pisz("wers4", "nie leczono tam ludzi a zajmowano się jakimiś badaniami snów, marzeń sennych,"
                            " czy coś takiego.", 20, 240, white)
        pisak.pisz("wers5", "- Aha - wzdychasz, bo spodziewałeś(-aś) się odpowiedzi w stylu 'razili ludziom"
                            " mózgi prądem.", 20, 270, white)
        pisak.pisz("wers6", "Iwona to dostrzega, siada obok Ciebie, kładzie rękę na Twoim ramieniu i mówi:",
                   20, 300, white)
        pisak.pisz("wers7", "- Możesz wierzyć lub nie ale daj mi znać, jak przyśni Ci się tutaj coś dziwnego..",
                   20, 330, white)
        pisak.pisz("wers8", "- Ok, dzięki że opowiedziałaś, to co idziemy spać?  - Idziemy - odpowiada Iwona.",
                   20, 360, white)
        pisak.pisz("wers9", "***Rozmyślasz o tym czego się dzisiaj dowiedziałeś(-aś), o reszcie dnia.. Ehh jutro"
                            " znowu zaprawa..", 20, 390, white)

        pygame.display.update()
        mainClock.tick()


# Scena19


def scena19():
    db_save.update_exp_ang_dni("exp", "dane_konta", 2)
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 3)
    running = True
    quest_tomek = db_save.search_data("quest_tomek", "dane_quest_tomek")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.wspol2, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        wybor1 = screen.blit(graph.silownia_N[0], (470, 600))
        wybor2 = screen.blit(graph.spacer_N[0], (660, 600))

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

        if wybor1.collidepoint((mx, my)):
            screen.blit(graph.silownia_N[1], (470, 600))
            if click:
                loadingSound.play()
                silownia2()

        if wybor2.collidepoint((mx, my)):
            screen.blit(graph.spacer_N[1], (660, 600))
            if click:
                loadingSound.play()
                spacer()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Minęło kilka dni - kilka a każdy.. jak dzień świstaka.", 20, 120, white)
        pisak.pisz("wers1", "Zaprawa, nauka, spanie.. Zaprawa, nauka, spanie.. zajęcia to tu, to tam.. eh.. ",
                   20, 150, white)
        pisak.pisz("wers2", "W plutonie porobiły się podgrupy, które przesiadują razem po zajęciach i piją "
                            "podlaski bimber.", 20, 180, white)
        pisak.pisz("wers3", "Szkoda Ci czasu na alkohol a szukasz jakiegoś pożytecznego zajęcia.", 20, 210, white)
        pisak.pisz("wers4", "Zastanawiasz się co robić:", 20, 240, white)
        for q in quest_tomek:
            if q == "bar":
                pisak.pisz("wers5x", "1. Iść na siłownię? I może zobaczę Tomka i zagadam co robił w CELI", 20, 270,
                           green)
            else:
                pisak.pisz("wers5", "1. Iść na siłownię?", 20, 270, white)
        pisak.pisz("wers6", "2. Iść na spacer?", 20, 300, white)
        pisak.pisz("wers7", "Jakaś część Ciebie mówi 'Rusz dupę!'", 20, 330, white)
        pisak.pisz("wers8", "--> Gdzie idziesz?", 520, 530, dyellow)

        bimberx = screen.blit(graph.bimber[0], (878, 180))
        if bimberx.collidepoint((mx, my)):
            screen.blit(graph.bimber[1], (878, 208))

        pygame.display.update()
        mainClock.tick()


# Silownia2


def silownia2():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    siren.stop()
    silowniaOGG.play(-1)
    db_save.add_1_value("dane_quest_tomek", "silownia_3")
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.silka, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena20()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Siłownia to nie Twoje klimaty ale z nudów można poprzeciągać trochę złomu.", 20, 90, white)
        pisak.pisz("wers1", "Wchodzisz do budynku, w tle słychać dźwięki odkładanych hantli i drążków.", 20, 120, white)
        pisak.pisz("wers2", "Zaglądasz żeby rozejrzeć się czy ćwiczy ktoś znajomy. Tomka nie ma, sami obcy.",
                   20, 150, white)
        pisak.pisz("wers3", "- No jak już jestem to.. ehh.. dobra idę trochę poćwiczę, gdzie była ta szatnia",
                   20, 180, white)
        pisak.pisz("wers4", "Wchodzisz do szatni, siadasz na ławeczce, zmieniasz buty na wygodniejsze.", 20, 210, white)
        pisak.pisz("wers5", "Słyszysz z korytarza, rozmowę jakiegoś mężczyzny przez telefon, głos jakby Tomka:", 20,
                   240, white)
        pisak.pisz("wers6", "(Tomek) - Za krótko, mówiłem Ci.. To sam tu przyjedź i siedź.. Jeszcze nie wiem kto..",
                   20, 270, white)
        pisak.pisz("wers7", "**Słyszysz tylko rozmówcę z korytarza, głos w słuchawce jest niezrozumiały.",
                   20, 300, white)
        pisak.pisz("wers8", "(Tomek) - Nie wiem, dużo.. dobra muszę kończyć bo się zczają.. ", 20, 330, white)
        pisak.pisz("wers9", "Słysząc to wbijasz tępo wzrok w szafkę i nasłuchujesz dalej ale jest cicho.", 20, 360,
                   white)
        pisak.pisz("wers10", "*Hmm to była nieco dziwna rozmowa - zastanawiasz się i wychodzisz na korytarz", 20, 390,
                   white)
        pisak.pisz("wers11", "ale nikogo już tam nie ma.", 20, 420, white)
        pisak.pisz("wers12", "*Odechciało Ci się ćwiczeń i nie zmieniając butów i wracasz do akademika.", 20, 450,
                   white)

        pygame.display.update()
        mainClock.tick()


# Spacer


def spacer():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    siren.stop()
    spacerOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.szczytno_nocBG, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                spacer1()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "No pewnie! Lepiej trochę się przejść i zwiedzić trochę miasta. Jest 19:00 trochę późno..",
                   20, 900, white)
        pisak.pisz("wers1", "Wychodzisz główną bramą nr 1 na ulicę Piłsudskiego, po lewej stronie widzisz Pub 'CELA'",
                   20, 120, white)
        pisak.pisz("wers2", "Rozglądasz się i postanawiasz iść w lewo. Po przejściu kilkudziesięciu metrów zauważasz"
                            " komendę Policji.", 20, 150, white)
        pisak.pisz("wers3", "Po prawej jakiś dworzec PKS, widzisz kilka starych 'ogórków', jest też stacja CPN i"
                            " jakiś sklep.", 20, 180, white)
        pisak.pisz("wers4", "- Chyba trzeba było iść w prawo od bramy.. tu nic nie ma.. - zastanawiasz się.",
                   20, 210, white)
        pisak.pisz("wers5", "Dochodzisz do skrzyżowania przypominającego pętlę autobusową, spoglądasz na słupek",
                   20, 240, white)
        pisak.pisz("wers6", "z nazwą ulicy - [ ul.Działkowa ]. - Przed Tobą, za 200 metrów koniec miasta.. "
                            "No to niezły spacer.. ", 20, 270, white)
        pisak.pisz("wers7", "Skręcasz w lewo i drepczesz chodnikiem ale płyty są tak nierówne, że postanawiasz "
                            "iść ulicą.", 20, 300, white)
        pisak.pisz("wers8", "Okolica jest spokojna - niewielkie domki, w niektórych za szybą ktoś wstawił kartkę "
                            "'Pokoje do wynajęcia'", 20, 330, white)
        pisak.pisz("wers9", "Idziesz jakieś 300 metrów i dochodzisz do kolejnego skrzyżowania, patrzysz na słupek..",
                   20, 360, white)
        pisak.pisz("wers10", "[ ul.Solidarności ]. Przed Tobą łąka ale daleko po lewej stronie, dostrzegasz "
                             "duży parking..", 20, 390, white)
        pisak.pisz("wers11", "- To parking policji?! - myślisz. No tak! Widziałem go z okna na służbie!",
                   20, 420, white)
        pisak.pisz("wers12", "Okolica wydaje Ci się nawet urocza. Cisza, spokój.. ", 20, 450, white)

        ogorkowx = screen.blit(graph.ogorkow[0], (577, 177))
        if ogorkowx.collidepoint((mx, my)):
            screen.blit(graph.ogorkow[1], (577, 210))

        pygame.display.update()
        mainClock.tick()


# Spacer1


def spacer1():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.szczytno_nocBG, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena20()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Stoisz chwilę i przypomina Ci się noc jako dyżurny - No tak! Gdzieś po prawej są"
                           " magazyny!", 20, 90, white)
        pisak.pisz("wers1", "Skręcasz w prawo, wchodzisz na żwir bo asfalt skończył się na skrzyżowaniu."
                            " Tak - tu miasto się kończy.", 20, 120, white)
        pisak.pisz("wers2", "Po prawej stronie mijasz nieduże domki, po lewej łąka i widać już tylko krzaki"
                            " i małe drzewka", 20, 150, white)
        pisak.pisz("wers3", "Jest też jakaś wąziutka polna zabłocona droga - Iść czy nie iść? - znowu myślisz",
                   20, 180, white)
        pisak.pisz("wers4", "- No myśl, myśl - poganiasz się. Miał być spacer to może warto się przejść.",
                   20, 210, white)
        pisak.pisz("wers5", "Decydujesz się iść polną drogą ale po przejściu kilku kroków widzisz jak światła"
                            " nadjeżdżającego samochodu", 20, 240, white)
        pisak.pisz("wers6", "rozświetlają drogę przed Tobą, jednocześnie Cię oślepiając. - Boooże.. co za osioł"
                            " jezdzi tu na długich?", 20, 270, white)
        pisak.pisz("wers7", "Nic nie widzisz, dopiero gdy pojazd mija Cię odwracasz się by zobaczyć bagażnik",
                   20, 300, white)
        pisak.pisz("wers8", "Chcesz zobaczyć co to za marka, może jakiś nr rejestracyjny.. cokolwiek.",
                   20, 330, white)
        pisak.pisz("wers9", "Ale szybko zapominasz o tym, bo wracający wzrok ukazuje Ci srebrno-niebieskie"
                            " napisy 'POLICJA' - To radiowóz.. ", 20, 360, white)
        pisak.pisz("wers10", "Srebrna KIA Ceed, w środku 2 policjantów ale to nie kursanci. Pewnie miejscowi"
                             " z komendy, którą mijałeś(-aś)", 20, 390, white)
        pisak.pisz("wers11", "- No teraz to lipa ze zwiedzania, pewnie mnie zobaczyli - mówisz do siebie",
                   20, 420, white)
        pisak.pisz("wers12", "I co teraz pójdę tam bez celu ktoś zapyta, ktoś zobaczy i pójdzie fama po"
                             " szkole, że szwędam", 20, 450, white)
        pisak.pisz("wers13", "się zamiast zakuwać do egzaminów i się uczyć..", 20, 480, white)
        pisak.pisz("wers14", "**Wracasz do akademika. W sumie magazyny zwiedzisz jak będziesz mieć tam "
                             "służbę.. ", 20, 510, white)

        pygame.display.update()
        mainClock.tick(60)


# Scena20


def scena20():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    spacerOGG.stop()
    silowniaOGG.stop()
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokojnocBG, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena21()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Wchodzisz do pokoju. Iwona rozmawia z Anką o jutrzejszych zajęciach na strzelnicy.",
                   30, 120, white)
        pisak.pisz("wers1", "Tomek bierze prysznic.", 30, 150, white)
        pisak.pisz("wers2", "Kładziesz się i idziesz spać.", 30, 180, white)

        pygame.display.update()
        mainClock.tick()


def scena21():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
    strzelnicaOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.strzelnica1, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                strzelnica_scena_1()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Nowy dzionek zapowiada się całkiem przyzwoicie. Będziesz strzelać na strzelnicy.",
                   30, 150, white)
        pisak.pisz("wers1", "Z prawdziwych nabojów!", 30, 180, white)
        pisak.pisz("wers2", "Czujesz stresik.. ", 30, 210, white)
        pisak.pisz("wers3", "Prowadzący zajęcia policjant tłumaczy zasady strzelania:", 30, 240, white)
        pisak.pisz("wers4", "1.Macie 25 naboi!", 30, 270, white)
        pisak.pisz("wers5", "2.Celujecie w sam środek!", 30, 300, white)
        pisak.pisz("wers6", ".. i zaliczacie zajęcia", 30, 330, white)
        pisak.pisz("wers7", "Wchodzisz na pozycję do strzelania i ładujesz pełny magazynek", 30, 360, white)
        pisak.pisz("wers8", "Wkładasz okulary ochronne i słuchawki wygłuszające. Słyszysz stłumiony głos"
                            " prowadzącego:", 30, 390, white)
        pisak.pisz("wers9", "- Przygotować się do strzelania!", 30, 420, white)
        pisak.pisz("wers10", "* Za bardzo dobre wyniki, możesz zyskać cenne przedmioty", 30, 450, dyellow)

        pygame.display.update()
        mainClock.tick()


def strzelnica_scena_1():
    pygame.mouse.set_visible(False)
    ox = 600 - tarcza_rect.center[0]
    oy = 200 - tarcza_rect.center[1]
    ox_move = 1
    oy_move = 1
    punkty = 0
    naboje = 25
    startx = 500
    delta = 0.0
    dane_gracza = db_save.pobierz_dane("dane_gracza")
    global blob_color
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()

        losowa = random.randrange(-150, 150)
        punkty_str = str(punkty)
        naboje_str = str(naboje)

        screen.blit(graph.strzelnica1, (0, 0))
        if naboje <= 0:
            if punkty > 200:
                tk_box.informacja("+10 doświadczenia, +12 zaangażowania ", graph.zaang_up)
                db_save.add_1_value("dane_ekwipunek", "skrawek")
                db_save.update_exp_ang_dni("ang", "dane_konta", 12)
                db_save.update_exp_ang_dni("exp", "dane_konta", 10)
                db_save.add_1_value("dane_baretki", "p99")
            pygame.mouse.set_visible(True)
            db_save.add_1_value("dane_strzelnica", punkty)
            strzelnica1wyniki(punkty)

        screen.blit(graph.tabelaIMG, (5, 600))

        mx, my = pygame.mouse.get_pos()
        ox += ox_move * 1
        oy += oy_move * 2

        if ox <= startx:
            ox_move = random.randint(1, 2)
        elif ox >= 600:
            ox_move = random.randint(-2, -1)
            oy_move = 1
        elif oy >= 300:
            oy_move = -1

        offset = (mx - ox, my - oy)
        result = tarcza_mask.overlap(blob_mask, offset)
        result9 = tarcza9_mask.overlap(blob_mask, offset)
        result8 = tarcza8_mask.overlap(blob_mask, offset)
        result7 = tarcza7_mask.overlap(blob_mask, offset)
        result6 = tarcza6_mask.overlap(blob_mask, offset)
        result5 = tarcza5_mask.overlap(blob_mask, offset)
        result4 = tarcza4_mask.overlap(blob_mask, offset)
        result3 = tarcza3_mask.overlap(blob_mask, offset)
        result2 = tarcza2_mask.overlap(blob_mask, offset)
        result1 = tarcza1_mask.overlap(blob_mask, offset)

        delta += mainClock.tick(40) / 600.0
        while delta > 1 / 10.0:
            delta -= 1 / 10.0
            if result:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        if click:
                            punkty += 10
                            naboje -= 1
                            shot.play()
                            ox += losowa
            else:
                blob_color = green_blob

            if result9:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        if click:
                            punkty += 9
                            naboje -= 1
                            shot.play()
                            ox += losowa
            if result8:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        if click:
                            punkty += 8
                            naboje -= 1
                            shot.play()
                            ox += losowa
            if result7:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        if click:
                            punkty += 7
                            naboje -= 1
                            shot.play()
                            ox += losowa
            if result6:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        if click:
                            punkty += 6
                            naboje -= 1
                            shot.play()
                            ox += losowa
            if result5:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    click = True
                    if click:
                        punkty += 5
                        naboje -= 1
                        shot.play()
                        ox += losowa

            if result4:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    click = True
                    if click:
                        punkty += 4
                        naboje -= 1
                        shot.play()
                        ox += losowa
            if result3:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    click = True
                    if click:
                        punkty += 3
                        naboje -= 1
                        shot.play()
                        ox += losowa
            if result2:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    click = True
                    if click:
                        punkty += 2
                        naboje -= 1
                        shot.play()
                        ox += losowa
            if result1:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    click = True
                    if click:
                        punkty += 1
                        naboje -= 1
                        shot.play()
                        ox += losowa

        screen.blit(tarczaIMG, (ox, oy))
        screen.blit(tarcza1IMG, (ox, oy))
        screen.blit(tarcza2IMG, (ox, oy))
        screen.blit(tarcza3IMG, (ox, oy))
        screen.blit(tarcza4IMG, (ox, oy))
        screen.blit(tarcza5IMG, (ox, oy))
        screen.blit(tarcza6IMG, (ox, oy))
        screen.blit(tarcza7IMG, (ox, oy))
        screen.blit(tarcza8IMG, (ox, oy))
        screen.blit(tarcza9IMG, (ox, oy))
        screen.blit(tarcza0IMG, (ox, oy))
        screen.blit(blob_color, (mx, my))
        screen.blit(gun, (mx, my))

        pisak.pisz("imie", dane_gracza[0][0], 50, 650, black)
        pisak.pisz("naboje", naboje_str, 345, 650, black)
        pisak.pisz("wers2", punkty_str, 265, 650, black)

        pygame.display.update()


# Strzelnica1 Wyniki


def strzelnica1wyniki(punkty):
    running = True
    dane_gracza = db_save.pobierz_dane("dane_gracza")
    wynik = db_save.search_data("punkty", "dane_strzelnica")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.wynikiBG, (260, 10))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                if punkty > 200:
                    tk_box.informacja("Zwitek papieru", graph.skrawek_src)
                loadingSound.play()
                scena22()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers1", str(wynik[0]), 730, 238, black)
        pisak.pisz("wers2", dane_gracza[0][0], 460, 60, black)
        pygame.display.update()
        mainClock.tick()


# Scena22


def scena22():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
    strzelnicaOGG.stop()
    eq = db_save.search_data("ekwipunek", "dane_ekwipunek")
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                egzamin_ruch()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Pierwsze strzelanie za Tobą! Polubiłeś(-aś) to..  odgłosy strzałów, spadających łusek,"
                           " zapach prochu.", 20, 90, white)
        pisak.pisz("wers1", "Robi się fajniej, bo wykładowcy trochę odpuścili upierdliwość ale.. nie ma nic za darmo.",
                   20, 120, white)
        pisak.pisz("wers2", "Jutro masz sprawdzian z ruchu drogowego i wypadałoby coś się pouczyć.", 20, 150, white)
        for i in eq:
            if i == "skrawek":
                pisak.pisz("wers3", "*Miałeś(-aś) dobry wynik, ze strzelania. Powyżej 200 to już sokole oko!",
                           20, 180, green)
                pisak.pisz("wers4", "*Prowadzący powiedział, że szkoda zmarnować taki talent i przekazał Ci małą"
                                    " podpowiedź.", 20, 210, green)
                pisak.pisz("wers5", "*Podpowiedź znajdziesz w plecaku.", 20, 240, green)

        pygame.display.update()
        mainClock.tick()


# Egzamin z ruchu drogowego ---------------


def egzamin_ruch():
    szum.play(-1)
    running = True
    odp1_ruch = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        if active == "skrawek":
            pisak.pisz("wers5", "[Podpowiedź ze świstka papieru] - B lub C", 455, 550, brown)

        pisak.pisz("wers", "Podstawowa zasada ruchu to..?", 450, 100, red)
        pisak.pisz("wers1", "Ruch prawostronny", 450, 130, white)
        if odp1_ruch == "a":
            pisak.pisz("wers1", "Ruch prawostronny", 450, 130, dyellow)
        pisak.pisz("wers2", "Unikanie kolizji", 450, 190, white)
        if odp1_ruch == "b":
            pisak.pisz("wers2", "Unikanie kolizji", 450, 190, dyellow)
        pisak.pisz("wers3", "Jazda na podwójnym gazie", 450, 250, white)
        if odp1_ruch == "c":
            pisak.pisz("wers3", "Jazda na podwójnym gazie", 450, 250, dyellow)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp1_ruch:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp1_ruch = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp1_ruch = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp1_ruch = "c"

        if odp1_ruch:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_ruch2(odp1_ruch)

        pygame.display.update()
        mainClock.tick()


# Pytanie 2----------------------


def egzamin_ruch2(odp1_ruch):
    odp2_ruch = None
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        if active == "skrawek":
            pisak.pisz("wers5", "[Podpowiedź ze świstka papieru] - A", 455, 550, brown)

        pisak.pisz("wers", "W jakim dokumencie w Polsce, określono zasady ruchu drogowego?", 450, 100, red)
        pisak.pisz("wers1", "w Ustawie 'Prawo o ruchu drogowym'", 450, 130, white)
        if odp2_ruch == "a":
            pisak.pisz("wers1", "w Ustawie 'Prawo o ruchu drogowym'", 450, 130, dyellow)
        pisak.pisz("wers2", "w tygodniku 'AutoSzrot'", 450, 190, white)
        if odp2_ruch == "b":
            pisak.pisz("wers2", "w tygodniku 'AutoSzrot'", 450, 190, dyellow)
        pisak.pisz("wers3", "w Konstytucji RP", 450, 250, white)
        if odp2_ruch == "c":
            pisak.pisz("wers3", "w Konstytucji RP", 450, 250, dyellow)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp2_ruch:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp2_ruch = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp2_ruch = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp2_ruch = "c"

        if odp2_ruch:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_ruch3(odp1_ruch, odp2_ruch)
        pygame.display.update()
        mainClock.tick(60)


# Pytanie 3----------------------


def egzamin_ruch3(odp1_ruch, odp2_ruch):
    odp3_ruch = None
    running = True
    while running:
        click = False
        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        if active == "skrawek":
            pisak.pisz("wers5", "[Podpowiedź ze świstka papieru] - A", 455, 550, brown)

        pisak.pisz("wers", "Z jaką prędkością można jechać w strefie zamieszkania?", 450, 100, red)
        pisak.pisz("wers1", "20 km\\h", 450, 130, white)
        if odp3_ruch == "a":
            pisak.pisz("wers1", "20 km\\h", 450, 130, dyellow)
        pisak.pisz("wers2", "30 km\\h", 450, 190, white)
        if odp3_ruch == "b":
            pisak.pisz("wers2", "30 km\\h", 450, 190, dyellow)
        pisak.pisz("wers3", "8 km\\h", 450, 250, white)
        if odp3_ruch == "c":
            pisak.pisz("wers3", "8 km\\h", 450, 250, dyellow)
        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp3_ruch:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp3_ruch = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp3_ruch = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp3_ruch = "c"

        if odp3_ruch:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_ruch4(odp1_ruch, odp2_ruch, odp3_ruch)

        pygame.display.update()
        mainClock.tick(60)


# Pytanie 4----------------------


def egzamin_ruch4(odp1_ruch, odp2_ruch, odp3_ruch):
    odp4_ruch = None
    running = True
    while running:
        click = False
        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        if active == "skrawek":
            pisak.pisz("wers5", "[Podpowiedź ze świstka papieru] - A lub B", 455, 550, brown)

        pisak.pisz("wers", "Podstawowa klasyfikacja pojazdów to:", 450, 100, red)
        pisak.pisz("wers1", "Silnikowe i łańcuchowe", 450, 130, white)
        if odp4_ruch == "a":
            pisak.pisz("wers1", "Silnikowe i łańcuchowe", 450, 130, dyellow)
        pisak.pisz("wers2", "Mechaniczne i niemechaniczne", 450, 190, white)
        if odp4_ruch == "b":
            pisak.pisz("wers2", "Mechaniczne i niemechaniczne", 450, 190, dyellow)
        pisak.pisz("wers3", "Osobowe i dostawcze", 450, 250, white)
        if odp4_ruch == "c":
            pisak.pisz("wers3", "Osobowe i dostawcze", 450, 250, dyellow)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                delete_db.delete_db_0_save()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp4_ruch:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp4_ruch = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp4_ruch = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp4_ruch = "c"

        if odp4_ruch:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    wyniki_ruch(odp1_ruch, odp2_ruch, odp3_ruch, odp4_ruch)

        pygame.display.update()
        mainClock.tick(60)


# Wyniki z ruchu drogowego


def wyniki_ruch(odp1_ruch, odp2_ruch, odp3_ruch, odp4_ruch):
    dane_gracza = db_save.pobierz_dane("dane_gracza")
    jeden = 1
    if odp1_ruch == "b":
        odp1x = 1
    else:
        odp1x = 0

    if odp2_ruch == "a":
        odp2x = 1
    else:
        odp2x = 0

    if odp3_ruch == "a":
        odp3x = 1
    else:
        odp3x = 0

    if odp4_ruch == "b":
        odp4x = 1
    else:
        odp4x = 0

    ocena_ruch = jeden + odp1x + odp2x + odp3x + odp4x
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        tornister = screen.blit(graph.plecak, (200, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                if ocena_ruch == 5:
                    tk_box.informacja("+5 doświadczenia, +5 zaangażowania ", graph.zaang_up)
                    db_save.update_exp_ang_dni("exp", "dane_konta", 5)
                    db_save.update_exp_ang_dni("ang", "dane_konta", 5)
                    db_save.add_1_value("dane_indeks", 5)
                elif ocena_ruch == 4:
                    tk_box.informacja("+4 doświadczenia", graph.zaang_up)
                    db_save.update_exp_ang_dni("exp", "dane_konta", 4)
                    db_save.add_1_value("dane_indeks", 4)
                elif ocena_ruch == 3:
                    tk_box.informacja("+3 doświadczenia", graph.zaang_up)
                    db_save.update_exp_ang_dni("exp", "dane_konta", 3)
                    db_save.add_1_value("dane_indeks", 3)
                elif ocena_ruch == 2:
                    db_save.update_exp_ang_dni("exp", "dane_konta", 2)
                    db_save.add_1_value("dane_indeks", 2)
                else:
                    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                    db_save.add_1_value("dane_indeks", 1)
                siren.stop()
                loadingSound.play()
                scena23()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wersX", dane_gracza[0][0], 600, 220, white)
        pisak.pisz("wers", "Twoja ocena z testu RUCH DROGOWY!", 450, 250, white)

        try:
            if ocena_ruch == 5:
                pisak.pisz("wers1", "Gratulacje kujonie! Dostałeś 5!", 450, 510, dyellow)
                screen.blit(graph.cyfra5, (580, 300))
            if ocena_ruch == 4:
                pisak.pisz("wers2", "Całkiem, całkiem. Dostałeś 4!", 450, 510, dyellow)
                screen.blit(graph.cyfra4, (580, 300))
            if ocena_ruch == 3:
                pisak.pisz("wers3", "Mogło pójść lepiej.. Tylko 3?", 450, 510, dyellow)
                screen.blit(graph.cyfra3, (580, 300))
            if ocena_ruch == 2:
                pisak.pisz("wers4", "Jak chcesz skończyć kurs to weź się do nauki miernoto. Dostałeś(-aś) 2!",
                           250, 510, dyellow)
                screen.blit(graph.cyfra2, (580, 300))
            if ocena_ruch == 1:
                pisak.pisz("wers5", "Głowa pusta jak kapusta. Dostałeś pałę..", 400, 510, dyellow)
                screen.blit(graph.cyfra1, (580, 300))
        except ValueError:
            pisak.pisz("wersX", "Jeśli to widzisz - to jest to nieoczekiwany błąd gry (Zgłoś mi to)", 300, 510, red)

        pygame.display.update()
        mainClock.tick(60)


# Scena23


def scena23():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
    szum.stop()
    siren.play(-1)
    quest_tomek = db_save.search_data("quest_tomek", "dane_quest_tomek")
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokojnocBG, (0, 0))
        button_nie = screen.blit(graph.cela_nav[0], (470, 600))
        button_tak = screen.blit(graph.miasto[0], (660, 600))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if button_nie.collidepoint((mx, my)):
            screen.blit(graph.cela_nav[1], (470, 600))
            if click:
                loadingSound.play()
                scena_cela()

        if button_tak.collidepoint((mx, my)):
            screen.blit(graph.miasto[1], (660, 600))
            if click:
                loadingSound.play()
                scena_miasto()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Drugi sprawdzian za Tobą. Z tego co widać w indeksie, to pozostały jeszcze dwa do"
                           " egzaminu końcowego", 30, 120, white)
        pisak.pisz("wers1", "Na odstresowanie Tomek proponuje by wyjść na jakieś piwko. ", 30, 150, white)
        pisak.pisz("wers2", "Anka z Iwoną, chcą iść na miasto. Tomek naciska by wyjść do CELI.", 30, 180, white)
        for q in quest_tomek:
            if q == "silownia_3":
                pisak.pisz("wers3", "*Znowu CELA? No tak, wychodził kiedyś z drzwi dla personelu.", 30, 210, green)
                pisak.pisz("wers4", "*Może dowiem się czegoś więcej o tym miejscu.", 30, 240, green)
        pisak.pisz("wers6", "--> To gdzie idziemy?", 520, 530, dyellow)

        pygame.display.update()
        mainClock.tick()


# Scena_CELA


def scena_cela():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    siren.stop()
    barSound.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.barBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena_cela2()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "W CELI jak zwykle - głośna muzyka i tłum ludzi. Czy każdy 'opija' tutaj sprawdziany?",
                   20, 150, white)
        pisak.pisz("wers1", "Myślisz, że chyba lepiej było wybrać wyjście na miasto ale.. Tomek tak nalegał.",
                   20, 180, white)
        pisak.pisz("wers2", "- Szybciej! - krzyczy Anka pchając Cię do przodu - Przed nami wolny stolik.",
                   20, 210, white)
        pisak.pisz("wers3", "- Uff udało się, jeden wolny się uchował - Iwona wygodnie się rozsiada i poprawia włosy.",
                   20, 240, white)
        pisak.pisz("wers4", "Tomek stoi przed stolikiem, spogląda na Was, po czym proponuje klasyczne piwko"
                            " z nalewaka.", 20, 270, white)
        pisak.pisz("wers5", "- Ja z sokiem - rzuca Anka. - Dla mnie weź coś z ciemnych - odpowiada spokojnie Iwona.",
                   20, 300, white)
        pisak.pisz("wers6", "- A mi weź.. - zastanawiasz się.", 20, 330, white)
        pisak.pisz("wers7", "- Karmi? - dodaje Tomek - A w sumie to.. - nie możesz podjąć decyzji.", 20, 360, white)
        pisak.pisz("wers8", "- Dobra wezmę Ci coś specjalnego - uśmiecha się Tomek i znika w tłumie.", 20, 390, white)
        pisak.pisz("wers9", "Siedzicie i rozmawiacie, klimat w sam raz na odstresowanie, luźne głośne rozmowy, "
                            "znajome twarze, ahh.", 20, 420, white)
        pisak.pisz("wers10", "Po 20 minutach Tomka wciąż nie ma - Pić mi się chce, gdzie on jest - przerywa Anka.",
                   20, 450, white)
        pisak.pisz("wers11", "Postanawiasz iść pod bar i sprawdzić co z Tomkiem.", 20, 480, white)

        pygame.display.update()
        mainClock.tick()


# Scena_CELA2


def scena_cela2():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.barBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena24()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Pod barem tłoczą się ludzie ale Tomka nie widać.", 20, 150, white)
        pisak.pisz("wers1", "Na blacie, dostrzegasz samotnie stojące 4 kufle piwa, w tym jedno ciemne.."
                            " - To pewnie nasze - myślisz", 20, 180, white)
        pisak.pisz("wers2", "Za barem uwijają się barmani, zręcznie wymijają się w wąskim przejściu jak jaskółki"
                            " przed burzą.", 20, 210, white)
        pisak.pisz("wers3", "- Co podać? - wyrywa Cię pytaniem jeden z nich.", 20, 240, white)
        pisak.pisz("wers4", "- Ja po te 4 piwa - szybko odpowiadasz. - Te 4? - wskazuje stojące obok siebie kufle.",
                   20, 270, white)
        pisak.pisz("wers5", "- Tak.. Tomek.. mój kolega miał wziąć ale.. - Aaa Tomek - przerywa barman - dobra,"
                            " jasne bierz.", 20, 300, white)
        pisak.pisz("wers6", "Albo poczekaj - kontynuuje - pokaż mi gdzie siedzicie, a zaraz Wam przyniosę. ",
                   20, 330, white)
        pisak.pisz("wers7", "Wracasz do stolika a po chwili na plastikowej czerwonej tacy z napisem WARKA",
                   20, 360, white)
        pisak.pisz("wers8", "stoją wasze 4 piwka: ciemne - Iwony, ze słomką - Anki i 2 kufle z jasnym piwem z "
                            "dużą ilością piany.", 20, 390, white)
        pisak.pisz("wers9", "Siedzicie i rozmawiacie, po 15 minutach przychodzi Tomek i rzuca jakby nigdy nic -"
                            " O i tak beze mnie?", 20, 420, white)
        pisak.pisz("wers10", "- Gdzieś Ty był?! - pytasz wkurzony(-a). - Oj już nie denerwuj się, w kibelku, sprawy"
                             " służbowe - odpowiada", 20, 450, white)
        pisak.pisz("wers11", "- Taa w kibelku.. - dołącza się Anka - byłam w kolejce i jakoś Cię tam nie widziałam.",
                   20, 480, white)
        pisak.pisz("wers11", "- Oj już dobrze, dobrze - odpowiada Tomek wymijająco - Pijmy i wracamy bo już późno.. ",
                   20, 510, white)

        pygame.display.update()
        mainClock.tick()


# Spacer


def scena_miasto():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    siren.stop()
    spacerOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.szczytno_nocBG, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

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

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena24()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Tomek nalegał ale zdecydowliście sie pójść na miasto. Trzeba się ruszyć dalej a nie"
                           " kisić przy szkole.", 20, 90, white)
        pisak.pisz("wers1", "Przeszliście się główną ulicą Szczytna -ul.Polską i doszliście do ronda przy "
                            "pizzerii 'Toscana'.", 20, 120, white)
        pisak.pisz("wers2", "Skręciliście w prawo i doszliście do Jeziora Domowego Białego.", 20, 150, white)
        pisak.pisz("wers3", "- O fajnie tu - powiedziała Anka rozglądając się to w lewo to w prawo. ", 20, 180, white)
        pisak.pisz("wers4", "- To co po piwku? - proponuje Tomek. - Gdzie? Tutaj?! - Iwona dodaje z niedowierzaniem.",
                   20, 210, white)
        pisak.pisz("wers5", "- Chyba Cię pogrzało, jesteśmy policjantami - kontynuuje - Masz głupie pomysły.",
                   20, 240, white)
        pisak.pisz("wers6", "- Oj dobra, przecież żartowałem - Tomek jakby zmieszany, próbuje jakoś wybrnąć.",
                   20, 270, white)
        pisak.pisz("wers7", "Proponujesz przejść się do pizzerii, którą mijaliście na rondzie. Wszyscy się zgadzają.",
                   20, 300, white)
        pisak.pisz("wers8", "Po 10 minutach zajmujecie niewielki stolik w kameralnym pomieszczeniu, w środku "
                            "unosi się zapach pizzy.", 20, 330, white)
        pisak.pisz("wers9", "- Tu możemy wypić piwko - stwierdza Iwona - a nie w parku jak jakieś miejskie żule.",
                   20, 360, white)
        pisak.pisz("wers10", "*Zjedliście 1 dużą wiejską pizzę popijając chłodnym piwkiem i wróciliście do akademika.",
                   20, 390, white)

        pygame.display.update()
        mainClock.tick()


# Scena24


def scena24():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    siren.play(-1)
    spacerOGG.stop()
    barSound.stop()
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena_prog_3()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Wyjście za mury szkoły to jest coś co lubisz. Takie piwko po egzaminie chyba stanie"
                           " się Waszą tradycją.", 20, 120, white)
        pisak.pisz("wers1", "Można wypić i zjeść jak człowiek a nie tylko obżerać się stołówkowym jedzeniem.",
                   20, 150, white)
        pisak.pisz("wers2", "Wieczór minął miło i spokojnie na rozmowach. Doszliście do wniosku, że czas szybko leci",
                   20, 180, white)
        pisak.pisz("wers3", "a Wam została już połowa kursu. Można powiedzieć, że jest z górki.", 20, 210, white)
        pisak.pisz("wers4", "Przed Wami 2 sprawdziany; kiedy będą? Widzą to tylko wykładowcy. Czy będą trudne? Nikt"
                            " tego nie wie.", 20, 240, white)
        pisak.pisz("wers5", "Ogólnie zostały jeszcze 3 strzelania na strzelnicy, z 3 różnych jednostek broni.",
                   20, 270, white)
        pisak.pisz("wers6", "No i egzamin końcowy.. oby zdać. No nic.. zobaczymy co będzie. Ludzie przecież zdają..",
                   20, 300, white)
        pisak.pisz("wers7", "Jutro piątek, to wystarczy tylko się przespać, przebimbać wykłady i można jechać do domu.",
                   20, 330, white)
        pisak.pisz("wers8", "No tak.. jeszcze tylko ta poranna zaprawa..", 20, 360, white)

        pygame.display.update()
        mainClock.tick()


# SCENA PROG_SAVE_1


def scena_prog_3(co_dalej=0):
    siren.stop()
    saveOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.prog, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                saveOGG.stop()
                loadingSound.play()
                scena25()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if not co_dalej:
            zapisz_x = screen.blit(graph.zapisz[0], (570, 600))
            if zapisz_x.collidepoint((mx, my)):
                screen.blit(graph.zapisz[1], (570, 600))
                if click:
                    loadingSound.play()
                    co_dalej = save_1()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        if not co_dalej:
            pisak.pisz("wers", "Ten etap pozwala zapisać stan Gry.", 20, 460, dyellow)
            pisak.pisz("wers2", "Jest to również miejsce, z którego będziesz kontynuował(-a) dalszą grę.", 20, 490,
                       dyellow)
        else:
            pisak.pisz("wers", "Możesz kontynuować swoją służbę.", 460, 490, dyellow)
        pygame.display.update()
        mainClock.tick()


#  SAVE_1

def save_1():
    running = True
    control_pc = None
    co_dalej = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.bg_conn, (0, 0))
        zapisz_x = screen.blit(graph.button_pc[0], (570, 300))

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

        cofnij_x = screen.blit(graph.cofnij[0], (560, 600))
        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 600))
            if click:
                loadingSound.play()
                break

        if zapisz_x.collidepoint((mx, my)):
            screen.blit(graph.button_pc[1], (570, 300))
            if click:
                loadingSound.play()
                db_save.add_1_value("dane_save", "save_1")
                control_pc = 1
                co_dalej = 1

        if not control_pc:
            screen.blit(graph.status_pc[0], (1030, 20))
            pisak.pisz("wers", "Kliknij w przycisk by zapisać", 480, 440, white)
        else:
            screen.blit(graph.status_pc[1], (1030, 20))

        pygame.display.update()
        mainClock.tick()
    return co_dalej


# Scena15


def scena25():
    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
    pygame.mixer.music.stop()
    siren.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.korytarzDZIEN, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

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

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena26()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers0", "Piątek, piąteczek, piątunio! Nie dość, że za chwilę pojedziecie do domu to jeszcze"
                            " okazało się", 20, 120, white)
        pisak.pisz("wers", "że macie wszystkie zajęcia w akademiku nr 1 na III piętrze. Super! Nie będzie"
                           " tego łażenia z ", 20, 150, white)
        pisak.pisz("wers1", "budynku do budynku! Okazało się, że macie zajęcia w znajomym Ci miejscu"
                            " - pamiętasz służbę jako dyżurny?", 20, 180, white)
        pisak.pisz("wers2", "Podchodzisz do ściany by ponownie przyjrzeć się ciekawemu obrazkowi..", 20, 210, white)
        pisak.pisz("wers3", "Dziwne.. a czy nie było tutaj czegoś innego?", 20, 380, white)
        pisak.pisz("wers4", "No tak, może byłem(-am) zaspany(-a).. przecież była 3 w nocy..", 20, 410, white)

        obraz_nowy = screen.blit(graph.nowyObraz[0], (334, 273))
        if obraz_nowy.collidepoint((mx, my)):
            screen.blit(graph.nowyObraz[1], (450, 50))

        screen.blit(graph.oko, (mx, my))
        pygame.display.update()
        mainClock.tick()


# Scena26


def scena26():
    running = True
    quest_tomek = db_save.search_data("quest_tomek", "dane_quest_tomek")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.wspol, (0, 0))
        button_nie = screen.blit(graph.nie[0], (470, 600))
        button_tak = screen.blit(graph.tak[0], (660, 600))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_nie.collidepoint((mx, my)):
            screen.blit(graph.nie[1], (470, 600))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                loadingSound.play()
                scena27()

        if button_tak.collidepoint((mx, my)):
            screen.blit(graph.tak[1], (660, 600))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                loadingSound.play()
                scena_torba()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "I po zajęciach, weekend można uznać za rozpoczety, no.. prawie rozpoczety.", 20, 90, white)
        pisak.pisz("wers1", "Wszyscy się spieszą i nikt już nie czeka na obiad, każdy chce czym prędzej wsiąść"
                            " do samochodu", 20, 120, white)
        pisak.pisz("wers2", "pociągu, autobusu i wracać do domu, do rodziny, przyjaciół.", 20, 150, white)
        pisak.pisz("wers3", "Iwona z Anką były bardziej ogarnięte bo już wyszły z pokoju.", 20, 180, white)
        pisak.pisz("wers4", "Ty z Tomkiem jeszcze się guzdrzesz i pakujesz ostanie rzeczy do wyjazdu.", 20, 210, white)
        pisak.pisz("wers5", "- Lecę jeszcze pod prysznic - mówi Tomek i zamyka za sobą drzwi do łazienki.",
                   20, 240, white)
        pisak.pisz("wers6", "- Żeby nie przebieranie się z munduru, poszło by mi szybciej - odpowiadasz i po"
                            " chwili słyszysz odgłos", 20, 270, white)
        pisak.pisz("wers7", "cieknącej wody w kabinie prysznicowej.", 20, 300, white)
        pisak.pisz("wers8", "Tomek nie skończył się pakować a na łóżku leży jego torba podróżna.", 20, 330, white)
        pisak.pisz("wers9", "Wiesz, że za bardzo nie wypada ale zastanawiasz się czy przyjrzeć się jej bliżej.",
                   20, 360, white)
        for q in quest_tomek:
            if q == "silownia_3":
                pisak.pisz("wers10", "*Może znajdziesz coś.. cokolwiek.. może związanego z dziwną rozmową w korytarzu"
                                     " siłowni?", 20, 390, green)
        pisak.pisz("wers12", "--> Zaglądasz do torby?", 500, 530, dyellow)

        pygame.display.update()
        mainClock.tick()


# Scena Torba Tomka


def scena_torba():
    running = True
    db_save.add_1_value("dane_quest_tomek", "torba_tomka")
    while running:
        click = False

        screen.fill(black)
        inicjalyx = screen.blit(graph.inicjaly[0], (880, 33))
        naszywkax = screen.blit(graph.naszywka[0], (783, 415))
        ksiazkax = screen.blit(graph.ksiazka[0], (587, 264))
        knigax = screen.blit(graph.kniga[0], (264, 275))
        screen.blit(graph.torbaBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                loadingSound.play()
                scena27()

        if inicjalyx.collidepoint((mx, my)):
            screen.blit(graph.inicjaly[1], (880, 120))

        if naszywkax.collidepoint((mx, my)):
            screen.blit(graph.naszywka[1], (783, 510))

        if ksiazkax.collidepoint((mx, my)):
            screen.blit(graph.ksiazka[1], (587, 360))

        if knigax.collidepoint((mx, my)):
            screen.blit(graph.kniga[1], (264, 370))

        screen.blit(graph.oko, (mx, my))
        pygame.display.update()
        mainClock.tick()


# Scena27


def scena27():
    running = True
    quest_tomek = db_save.search_data("quest_tomek", "dane_quest_tomek")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.drogaBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 3)
                loadingSound.play()
                scena_prog_4()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Spakowałeś(-aś) się do końca, zamknąłeś(-aś) pokój i wypisałeś(-aś) się u dyżurnego"
                           " akademika na wyjazd.", 20, 90, white)
        pisak.pisz("wers1", "Już po 15 minutach siedzisz w swoim autku i obierasz kierunek DOM.", 20, 120, white)
        pisak.pisz("wers2", "Droga daleka.. odpalasz ulubioną stację radiową i suniesz przed siebie.", 20, 150, white)
        for q in quest_tomek:
            if q == "torba_tomka":
                pisak.pisz("wers3", "*Jednak to co zobaczyłeś(-aś) w torbie, trochę nie daje Ci spokoju.", 20, 180,
                           green)
                pisak.pisz("wers4", "*Te dziwne inicjały.. No gdyby były tylko na torbie to zrozumiałe - pożyczona ale"
                                    " takie same na butach?", 20, 210, green)
                pisak.pisz("wers5", "*No i te książki.. Od kiedy Tomek jest taki oczytany? Taktyka wojny? Testy"
                                    " oficerskie?", 20, 240, green)
                pisak.pisz("wers6", "*Prędzej mu do jakiegoś koksa, bo tak często przesiaduje w siłowni.. no właśnie.."
                                    " przesiaduje..", 20, 270, green)
                pisak.pisz("wers7", "*bo jak mnie wyciąga na siłownię to jakoś nigdy nie widziałem(-am) by ćwiczył.. ",
                           20, 300, green)

        pygame.display.update()
        mainClock.tick()


# SCENA PROG 4


def scena_prog_4():
    siren.stop()
    progOGG.play()
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.prog, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                progOGG.stop()
                loadingSound.play()
                scena28()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Może być tak, że część tekstu wypisywana jest w grze na zielono z gwiazdką '*'.",
                   20, 430, dyellow)
        pisak.pisz("wers1", "*Taki tekst pojawia się jedynie, gdy pokierowałeś(-aś) fabułą w interesującym kierunku,"
                            " wykonujesz zadanie lub", 20, 460, green)
        pisak.pisz("wers2", "*wykazałeś(-aś) się sprawnością w jakimś etapie gry.", 20, 490, green)
        pisak.pisz("wers3", "*Są to też dodatkowe dialogi, pomocnicze przemyślenia bohatera lub specjalne sceny.",
                   20, 520, green)

        pygame.display.update()
        mainClock.tick()


# Scena28


def scena28():
    siren.play(-1)
    running = True
    quest_tomek = db_save.search_data("quest_tomek", "dane_quest_tomek")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.wspol, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                loadingSound.play()
                scena29()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Weekend zleciał nim się obejrzałeś(-aś), szkoda że kurs nie leci tak szybko..",
                   20, 90, white)
        pisak.pisz("wers1", "Powrót do szkoły był męczący, na trasie miałeś(-aś) spore korki, przez padający deszcz.",
                   20, 120, white)
        pisak.pisz("wers2", "Jest 21:00 ale okazuje się, że jesteś jako pierwszy(-a) w pokoju. Kładziesz się na"
                            " chwilę.", 20, 150, white)
        for q in quest_tomek:
            if q == "torba_tomka":
                pisak.pisz("wers3", "*Zastanawiasz się czy zapytać Tomka o jego zainteresowania, no.. te książki",
                           20, 180, green)
                pisak.pisz("wers4", "*Tylko lipa o tym rozmawiać, bo wyjdzie na jaw, że grzebałem(-am) mu w torbie",
                           20, 210, green)
                pisak.pisz("wers5", "*Dobrym pomysłem na ten tydzień, będzie obserwacja Tomka. Może wtedy czegoś więcej"
                                    " się dowiesz.", 20, 240, green)

        pygame.display.update()
        mainClock.tick()


# Scena29


def scena29():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
                loadingSound.play()
                scena30()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Bach! - drzwi otwierają się z impetem aż wyrywa Cię na baczność z łóżka.", 20, 90, white)
        pisak.pisz("wers1", "- Czeeeeeeśc! O a myślałam, że będę pierwsza. A Ty co tak na baczność stoisz?"
                            " Meldujesz mi się?", 20, 120, white)
        pisak.pisz("wers2", "- Anka! Co to miało być?! - pytasz i czujesz jak ciśnienie pulsuje Ci w tyle głowy.",
                   20, 150, white)
        pisak.pisz("wers3", "- Co wystraszyłam? Haha. Pewnie znowu wsiąkłeś(-aś) w naukę i nie słyszysz co się"
                            " dzieje wokoło.", 20, 180, white)
        pisak.pisz("wers4", "- Nie.. to znaczy tak, to znaczy nie w książkach ale tak się nie wchodzi. ",
                   20, 210, white)
        pisak.pisz("wers5", "Anka patrzy na Ciebie z politowaniem - Oj juś dobzie, dobzie wyśtrasiłam biedulkę,"
                            " nie gniewaj.", 20, 240, white)
        pisak.pisz("wers6", "Powoli przysiadasz na łóżko. Anka zdejmuje plecak a z korytarza wciąga do pokoju wielką"
                            " podróżną torbę na kółkach", 20, 270, white)
        pisak.pisz("wers7", "i zaczyna ją rozpakowywać - Jak tam? Co jutro mamy za zajęcia? Patrzyłeś plan zajęć?",
                   20, 300, white)
        pisak.pisz("wers8", "Wzdychasz - Tak patrzyłem(-am), podobno mamy nowe zajęcia z kodeksu wykroczeń.",
                   20, 330, white)
        pisak.pisz("wers9", "- A to luzik, dobra idę się wypisać u dyżurnego z powrotu - Anka wychodzi z pokoju.",
                   20, 360, white)
        pisak.pisz("wers10", "Siedzisz spoglądając na wpół-rozpakowaną torbę - Jeeezu, jaka roztrzepana.. ",
                   20, 390, white)
        pisak.pisz("wers11", "*Po 10 minutach do pokoju weszła Anka a za nią Iwona z Tomkiem.", 20, 420, white)
        pisak.pisz("wers12", "*Porozmawialiście jeszcze z 30 minut i poszliście spać.", 20, 450, white)

        pygame.display.update()
        mainClock.tick()


# Scena30


def scena30():
    running = True
    db_save.add_1_value("dane_notatki", "wykroczenia")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.wspol2, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
                loadingSound.play()
                egzamin_wykr()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Dzisiaj był chyba jeden z cięższych dni na kursie. Zajęcia z wykroczeń, to dużo wiedzy"
                           " do przyswojenia.", 20, 90, white)
        pisak.pisz("wers1", "Zajęcia prowadziła chuda policjantka w stopniu aspiranta, w wieku ok 35 lat.",
                   20, 120, white)
        pisak.pisz("wers2", "Gadała, gadała i gadała, było tego tak dużo, że wszystko już Ci się myli.. czyn"
                            " zabroniony, ustawa, kodeks,", 20, 150, white)
        pisak.pisz("wers3", "umyślność, nieumyślność, usiłowanie, podżeganie, pomocnictwo, grzywna.. Nic z tego"
                            " nie rozumiesz..", 20, 180, white)
        pisak.pisz("wers4", "Zapisałeś(-aś) chyba pół zeszytu na zajęciach a najgorsze jest to, że jutro macie"
                            " mieć sprawdzian!", 20, 210, white)
        pisak.pisz("wers5", "Ktoś z plutonu powiedział, że prowadzącą nazywają w szkole 'żyletą', bo nie"
                            " odpuszcza nikomu.", 20, 240, white)
        pisak.pisz("wers6", "Uzgodniliście, że po kolacji zasiadacie wspólnie do nauki. (Sprawdź notatnik)",
                   20, 270, white)

        pygame.display.update()
        mainClock.tick()


# Egzamin z wykroczeń ---------------
# Pytanie 1


def egzamin_wykr():
    odp1_wykr = None
    siren.stop()
    szum.play(-1)
    running = True
    while running:
        click = False
        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        pisak.pisz("wers", "Kodeks wykroczeń to..?", 450, 100, red)
        pisak.pisz("wers1", "Rozporządzenie", 450, 130, white)
        if odp1_wykr == "a":
            pisak.pisz("wers1", "Rozporządzenie", 450, 130, dyellow)
        pisak.pisz("wers2", "Ustawa", 450, 190, white)
        if odp1_wykr == "b":
            pisak.pisz("wers2", "Ustawa", 450, 190, dyellow)
        pisak.pisz("wers3", "Tygodnik policyjny", 450, 250, white)
        if odp1_wykr == "c":
            pisak.pisz("wers3", "Tygodnik policyjny", 450, 250, dyellow)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp1_wykr:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp1_wykr = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp1_wykr = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp1_wykr = "c"

        if odp1_wykr:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_wykr2(odp1_wykr)

        pygame.display.update()
        mainClock.tick()


# Pytanie 2----------------------


def egzamin_wykr2(odp1_wykr):
    odp2_wykr = None
    running = True
    while running:
        click = False
        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        pisak.pisz("wers", "Wykroczenie można popełnić..", 450, 100, red)
        pisak.pisz("wers1", "Tylko umyślnie", 450, 130, white)
        if odp2_wykr == "a":
            pisak.pisz("wers1", "Tylko umyślnie", 450, 130, dyellow)
        pisak.pisz("wers2", "Tylko nieumyślnie", 450, 190, white)
        if odp2_wykr == "b":
            pisak.pisz("wers2", "Tylko nieumyślnie", 450, 190, dyellow)
        pisak.pisz("wers3", "Umyślnie i nieumyślnie", 450, 250, white)
        if odp2_wykr == "c":
            pisak.pisz("wers3", "Umyślnie i nieumyślnie", 450, 250, dyellow)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp2_wykr:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp2_wykr = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp2_wykr = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp2_wykr = "c"

        if odp2_wykr:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_wykr3(odp1_wykr, odp2_wykr)

        pygame.display.update()
        mainClock.tick()


# Pytanie 3----------------------


def egzamin_wykr3(odp1_wykr, odp2_wykr):
    odp3_wykr = None
    running = True
    while running:
        click = False
        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        pisak.pisz("wers", "Odpowiada za usiłowanie ten kto..", 450, 100, red)
        pisak.pisz("wers1", "Zmierza do popełniania czynu, który nie następuje", 450, 130, white)
        if odp3_wykr == "a":
            pisak.pisz("wers1", "Zmierza do popełniania czynu, który nie następuje", 450, 130, dyellow)
        pisak.pisz("wers2", "Myśli o popełnieniu czynu", 450, 190, white)
        if odp3_wykr == "b":
            pisak.pisz("wers2", "Myśli o popełnieniu czynu", 450, 190, dyellow)
        pisak.pisz("wers3", "Śni mu się jak popełnia przestępstwo", 450, 250, white)
        if odp3_wykr == "c":
            pisak.pisz("wers3", "Śni mu się jak popełnia przestępstwo", 450, 250, dyellow)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp3_wykr:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp3_wykr = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp3_wykr = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp3_wykr = "c"

        if odp3_wykr:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_wykr4(odp1_wykr, odp2_wykr, odp3_wykr)

        pygame.display.update()
        mainClock.tick()


# Pytanie 4----------------------


def egzamin_wykr4(odp1_wykr, odp2_wykr, odp3_wykr):
    odp4_wykr = None
    running = True
    while running:
        click = False
        screen.fill(black)
        screen.blit(graph.egzaminFoto, (200, 0))
        pisak.pisz("wers", "Nakłanianie innej osoby do popełniania czynu to..", 450, 100, red)
        pisak.pisz("wers1", "Pomocnictwo", 450, 130, white)
        if odp4_wykr == "a":
            pisak.pisz("wers1", "Pomocnictwo", 450, 130, dyellow)
        pisak.pisz("wers2", "Zachęcanie", 450, 190, white)
        if odp4_wykr == "b":
            pisak.pisz("wers2", "Zachęcanie", 450, 190, dyellow)
        pisak.pisz("wers3", "Podżeganie", 450, 250, white)
        if odp4_wykr == "c":
            pisak.pisz("wers3", "Podżeganie", 450, 250, dyellow)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp4_wykr:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(graph.key_a[0], (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_a[1], (338, 115))
            if click:
                pen.play()
                odp4_wykr = "a"

        b_nopress = screen.blit(graph.key_b[0], (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_b[1], (338, 175))
            if click:
                pen.play()
                odp4_wykr = "b"

        c_nopress = screen.blit(graph.key_c[0], (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(graph.key_c[1], (338, 235))
            if click:
                pen.play()
                odp4_wykr = "c"

        if odp4_wykr:
            dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    loadingSound.play()
                    wyniki_wykr(odp1_wykr, odp2_wykr, odp3_wykr, odp4_wykr)
        pygame.display.update()
        mainClock.tick()


# Wyniki z wykroczeń


def wyniki_wykr(odp1_wykr, odp2_wykr, odp3_wykr, odp4_wykr):
    running = True
    dane_gracza = db_save.pobierz_dane("dane_gracza")
    jeden = 1
    if odp1_wykr == "b":
        odp1x = 1
    else:
        odp1x = 0

    if odp2_wykr == "c":
        odp2x = 1
    else:
        odp2x = 0

    if odp3_wykr == "a":
        odp3x = 1
    else:
        odp3x = 0

    if odp4_wykr == "c":
        odp4x = 1
    else:
        odp4x = 0

    ocena_wykr = jeden + odp1x + odp2x + odp3x + odp4x
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        tornister = screen.blit(graph.plecak, (200, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                if ocena_wykr == 5:
                    tk_box.informacja("+5 doświadczenia, +5 zaangażowania ", graph.zaang_up)
                    db_save.update_exp_ang_dni("exp", "dane_konta", 5)
                    db_save.update_exp_ang_dni("ang", "dane_konta", 5)
                    db_save.add_1_value("dane_indeks", 5)
                elif ocena_wykr == 4:
                    tk_box.informacja("+4 doświadczenia", graph.zaang_up)
                    db_save.update_exp_ang_dni("exp", "dane_konta", 4)
                    db_save.add_1_value("dane_indeks", 4)
                elif ocena_wykr == 3:
                    tk_box.informacja("+3 doświadczenia", graph.zaang_up)
                    db_save.update_exp_ang_dni("exp", "dane_konta", 3)
                    db_save.add_1_value("dane_indeks", 3)
                elif ocena_wykr == 2:
                    db_save.update_exp_ang_dni("exp", "dane_konta", 2)
                    db_save.add_1_value("dane_indeks", 2)
                else:
                    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                    db_save.add_1_value("dane_indeks", 1)
                szum.stop()
                loadingSound.play()
                scena31()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()
        pisak.pisz("wersX", dane_gracza[0][0], 600, 220, white)
        pisak.pisz("wers", "Twoja ocena z testu KODEKS WYKROCZEN!", 450, 250, white)

        try:
            if ocena_wykr == 5:
                pisak.pisz("wers1", "Gratulacje kujonie! Dostałeś 5!", 450, 510, dyellow)
                screen.blit(graph.cyfra5, (580, 300))
            if ocena_wykr == 4:
                pisak.pisz("wers2", "Całkiem, całkiem. Dostałeś 4!", 450, 510, dyellow)
                screen.blit(graph.cyfra4, (580, 300))
            if ocena_wykr == 3:
                pisak.pisz("wers3", "Mogło pójść lepiej.. Tylko 3?", 450, 510, dyellow)
                screen.blit(graph.cyfra3, (580, 300))
            if ocena_wykr == 2:
                pisak.pisz("wers4", "Jak chcesz skończyć kurs to weź się do nauki miernoto. Dostałeś(-aś) 2!",
                           250, 510, dyellow)
                screen.blit(graph.cyfra2, (580, 300))
            if ocena_wykr == 1:
                pisak.pisz("wers5", "Głowa pusta jak kapusta. Dostałeś pałę..", 400, 510, dyellow)
                screen.blit(graph.cyfra1, (580, 300))
        except ValueError:
            pisak.pisz("wersX", "Jeśli to widzisz - to jest to nieoczekiwany błąd gry (Zgłoś mi to)", 300, 510, red)

        pygame.display.update()
        mainClock.tick()


# Scena31


def scena31():
    siren.play(-1)
    running = True
    quest_tomek = db_save.search_data("quest_tomek", "dane_quest_tomek")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        button_nie = screen.blit(graph.nie[0], (470, 600))
        button_tak = screen.blit(graph.tak[0], (660, 600))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_nie.collidepoint((mx, my)):
            screen.blit(graph.nie[1], (470, 600))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
                loadingSound.play()
                scena_cela3()

        if button_tak.collidepoint((mx, my)):
            screen.blit(graph.tak[1], (660, 600))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 1)
                loadingSound.play()
                scena_anka()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Jesteście już po zajęciach. Trzeci sprawdzian za Wami. Tomek z Iwoną dostali po 3,"
                           " Anka pójdzie na poprawkę.", 20, 90, white)
        pisak.pisz("wers1", "Wracaliście w milczeniu by jej nie drażnić.", 20, 120, white)
        pisak.pisz("wers2", "- Jak to się stało? - Tomek próbuje zagaić i przerwać tę grobową ciszę.", 20, 150, white)
        pisak.pisz("wers3", "- Stało - odpowiada poddenerwowana - Żeby tego było mało, to zgadnijcie kiedy"
                            " mam poprawkę? ", 20, 180, white)
        pisak.pisz("wers4", "- Nie, serio? - Iwona aż podnosi brwi ze zdziwienia.", 20, 210, white)
        pisak.pisz("wers5", "- Tak.. Dokładnie to jutro w porze obiadowej, bo szanowne żylecisko jest tak wychudzone,"
                            " że nie pozwoli nawet zjeść.", 20, 240, white)
        pisak.pisz("wers6", "- Słuchaj - wtrąca Tomek - To może my sobie pójdziemy i nie będziemy Ci przeszkadzać"
                            " w nauce.", 20, 270, white)
        pisak.pisz("wers7", "Anka nic nie odpowiada, widzisz na twarzy jej zrezygnowanie.", 20, 300, white)
        pisak.pisz("wers8", "*Sumienie podpowiada Ci zostać z Anką i pomóc jej w nauce.", 20, 330, white)
        pisak.pisz("wers9", "*Rozsądek każe Ci iść z Tomkiem i Iwoną.", 20, 360, white)
        for q in quest_tomek:
            if q == "torba_tomka":
                pisak.pisz("wers10", "*Zawsze to jakaś okazja do obserwacji Tomka.", 20, 390, green)
        pisak.pisz("wersX", "--> Zostajesz z Anką?", 520, 530, dyellow)

        pygame.display.update()
        mainClock.tick()


# Scena_anka


def scena_anka():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                loadingSound.play()
                scena32()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Postanowiłeś(-aś) wesprzeć koleżankę i pomóc jej w nauce. Tomek z Iwoną poszli do CELI"
                           " opić sprawdzian.", 20, 120, white)
        pisak.pisz("wers1", "Pouczyliście się prawie 2 godziny, wydaje się, że Anka coś tam zrozumiała. Może"
                            " nie na 5 ale 3 powinna być.", 20, 150, white)
        pisak.pisz("wers2", "- Dziękuję Ci - Anka wpatruje się w Ciebie z drugiego końca pokoju.", 20, 180, white)
        pisak.pisz("wers3", "- Nie ma sprawy, obyś to jutro zaliczyła - odpowiadasz.", 20, 210, white)
        pisak.pisz("wers4", "- To moja wina - Anka robi się wylewna - Nie wiem, co sie ze mną stało, nie byłam taka.",
                   20, 240, white)
        pisak.pisz("wers5", "- Nie panikuj, zdasz, tylko nastepnym razem trochę wiecej czasu poświęcaj nauce"
                            " - starasz się ją pouczyć.", 20, 270, white)
        pisak.pisz("wers6", "- To nie chodzi o sprawdzian, chodzi o mnie, o to jaka jestem, jak się zachowuje"
                            " - jej ton głosu", 20, 300, white)
        pisak.pisz("wers7", "robi się łagodniejszy - Gram tutaj słodką idiotkę, nawet nie wiem kiedy to się stało,"
                            " nigdy taka nie byłam.", 20, 330, white)
        pisak.pisz("wers8", "Anka kontynuuje - Chciałam chyba zaimponować Wam, Jackowi, nie wiem komu jeszcze..",
                   20, 360, white)
        pisak.pisz("wers9",
                   "Tak naprawdę byłam i jestem cichą osobą, z reguły unikam imprez, czytam książki, często myślę.."
                   " To co tu odwalam",
                   20, 390, white)
        pisak.pisz("wers10",
                   "w ogóle do mnie nie pasuje.. To miejsce trochę mnie zmieniło.. Przepraszam Was za to.. ",
                   20, 420, white)
        pisak.pisz("wers11",
                   "Porozmawialiście dobrą godzinę, dowiedziałeś(-aś) się, że Anka hobbystycznie tworzy grafiki do"
                   " bajek dla dzieci.",
                   20, 450, white)
        pisak.pisz("wers12",
                   "Ah ta Anka, całkiem sympatyczna z niej dziewczyna. Pozory czasem mylą.. ",
                   20, 480, white)
        pygame.display.update()
        mainClock.tick()


# Scena_CELA3


def scena_cela3():
    siren.stop()
    barSound.play(-1)
    running = True
    quest_tomek = db_save.search_data("quest_tomek", "dane_quest_tomek")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.barBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                loadingSound.play()
                scena_cela4()

        pisak.pisz("wers", "Wyszliście we 3 do CELI. Ance zostawiłeś do nauki swoje zapiski z notanika - powinny"
                           " jej wystarczyć.", 20, 150, white)
        pisak.pisz("wers1", "W barze czujesz się już pewniej, nawet barman Was poznał i na powitanie kiwnął głową.",
                   20, 180, white)
        pisak.pisz("wers2", "Klasycznie, zasiadacie w tym samym stoliku co zwykle, krótkie zastanowienie, co kto pije.",
                   20, 210, white)
        pisak.pisz("wers3", "Tomek wstaje od stolika, zbiera Wasze zamówienia i idzie w kierunku baru.", 20, 240, white)
        pisak.pisz("wers4", "- Tylko się streszczaj, bo jestem spragniona! - krzyczy za nim Iwona.", 20, 270, white)
        for q in quest_tomek:
            if q == "torba_tomka":
                pisak.pisz("wers5", "*Myślisz sobie, że znając Tomka, pewnie znowu gdzieś zniknie na 15 minut",
                           20, 300, green)
                pisak.pisz("wers6", "*Nie chcesz mówić o tym Iwonie ale jest okazja by wyrwać się pod pretekstem "
                                    "kibelka i pójść za nim.", 20, 330, green)
                pisak.pisz("wers7", "[ZADANIE] --> Możesz pójść za Tomkiem lub pozostać w tej scenie klikając 'dalej'",
                           20, 560, green)
                idex = screen.blit(graph.ide[0], (550, 620))
                if idex.collidepoint((mx, my)):
                    screen.blit(graph.ide[1], (550, 620))
                    if click:
                        db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                        loadingSound.play()
                        scena_cela_quest()

        pygame.display.update()
        mainClock.tick()


# Scena_CELA_quest


def scena_cela_quest():
    running = True
    db_save.add_1_value("dane_quest_tomek", "bar_2")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.barBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                loadingSound.play()
                scena_cela4()

        pisak.pisz("wers", "*Idziesz za Tomkiem, trzymasz się w odległości 4-5 metrów od niego. Tomek podchodzi"
                           " pod bar.", 20, 150, green)
        pisak.pisz("wers1", "*Ty przystajesz niedaleko toalet udając, że stoisz w kolejce. Wyciągasz telefon"
                            " ale dyskretnie spoglądasz na to", 20, 180, green)
        pisak.pisz("wers2", "*co dzieje się pod barem. Wydaje się, że barman zna Tomka, krótką chwilę rozmawiają "
                            "po czym barman kiwa głową", 20, 210, green)
        pisak.pisz("wers3", "*właściwie odchyla ją lekko w lewo pokazując mu gestem drzwi dla personelu. Tomek "
                            "ogląda się za siebie próbując", 20, 240, green)
        pisak.pisz("wers4", "*zobaczyć Wasz stolik ale tłum ludzi, skutecznie mu go zasłania. Chowasz się "
                            "powoli za ścianą cały czas obserwując.", 20, 270, green)
        pisak.pisz("wers5", "*Tomek idzie w kierunku drzwi dla personelu, szybko je otwiera na szerokość, "
                            "dla której może tylko się przecisnąć.", 20, 300, green)
        pisak.pisz("wers6", "*To jednak wystarcza, byś dostrzegł(-a), że w środku na krześle siedzi jedna osoba,"
                            " widzisz tylko nogawki ciemnych ", 20, 330, green)
        pisak.pisz("wers7", "*spodni i... buty! Te same pomarańczowe buty taktyczne, które widziałeś(-aś) u "
                            "Tomka w torbie.", 20, 360, green)
        pisak.pisz("wers8", "*Drzwi się zamykają a Ty postanawiasz wrócić do stolika.", 20, 390, green)

        pygame.display.update()
        mainClock.tick()


# Scena_cela4


def scena_cela4():
    running = True
    quest_tomek = db_save.search_data("quest_tomek", "dane_quest_tomek")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.barBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                barSound.stop()
                loadingSound.play()
                siren.play(-1)
                scena32()

        pisak.pisz("wers", "- No i się nie posłuchał - zaczyna zniecierpliwona Iwona.", 20, 150, white)
        pisak.pisz("wers1", "- Tak, można go wysyłać po... śmierć! - śmiejecie się razem.", 20, 180, white)
        pisak.pisz("wers2", "- Dokładnie, a tak w ogóle to szkoda mi Anki, dobrze, że dałeś(-aś) jej swoje notatki. "
                            "Fajnie by było, żeby ", 20, 210, white)
        pisak.pisz("wers3", "jutro zaliczyła te nieszczęsne wykroczenia.", 20, 240, white)
        pisak.pisz("wers4", "- Nom - przytakujesz - Szkoda, że Jacek jej nie pouczył.", 20, 270, white)
        pisak.pisz("wers5", "- Eeee.. no uczył, uczył - Iwona nachyla się i mówi nieco ciszej - Tylko nie tego "
                            "co trzeba.", 20, 300, white)
        pisak.pisz("wers6", "Zaczynacie się głośno śmiać a do stolika podchodzi Tomek, w dłoniach ściskając 3 "
                            "kufle piwa.", 20, 330, white)
        pisak.pisz("wers7", "- Ostatni raz poszedłeś mi po piwo - Iwona zwraca się do Tomka - Sprawdziany lubię "
                            "opijać szybko.", 20, 360, white)
        pisak.pisz("wers8", "Tomek siada przy stoliku, ignorując to co do niego powiedziała i mówi:", 20, 390, white)
        pisak.pisz("wers9", "- Zdrowie tej pani - zwraca kufel w jej kierunku. Iwona mierzy go wzrokiem i powtarza:",
                   20, 420, white)
        pisak.pisz("wers10", "- Ostatni raz poszedłeś mi po piwo, nalegasz na wyjście, idziesz po piwo a "
                             "później czekam bez sensu..", 20, 450, white)
        pisak.pisz("wers11", "- Soryy - Tomek wydaje się zmieszany - Musiałem jeszcze skorzystać z toalety.",
                   20, 480, white)
        for q in quest_tomek:
            if q == "bar_2":
                pisak.pisz("wers12", "*Skłamał! Teraz jestem pewny(-a)! On coś ukrywa! Tylko co?", 20, 520, green)
        pygame.display.update()
        mainClock.tick()


# Scena32


def scena32():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                loadingSound.play()
                scena33()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Minął kolejny dzień kursu. Trzymaliście kciuki za Ankę i opłaciło się - zaliczyła"
                           " sprawdzian poprawkowy.", 20, 120, white)
        pisak.pisz("wers1", "W pokoju panuje wesoła atmosfera, która wszystkim się udziela.", 20, 150, white)
        pisak.pisz("wers2", "Na dodatek jutro jest luźniejszy dzień, z ciekawszych zajęć macie aż 5 godzin"
                            " na strzelnicy.", 20, 180, white)
        pisak.pisz("wers3", "Jest tylko jedna zła wiadomość.. Zostałeś(-aś) wybrany(-a) na służbę w weekend.",
                   20, 210, white)
        pisak.pisz("wers4", "Także nici z powrotu do domu.. ", 20, 240, white)

        pygame.display.update()
        mainClock.tick()


# Scena 33


def scena33():
    siren.stop()
    strzelnicaOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.strzelnica2, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                loadingSound.play()
                strzelnica_mossberg()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Nowy dzionek zapowiada się całkiem przyzwoicie. Będziesz strzelać na strzelnicy.",
                   30, 150, white)
        pisak.pisz("wers1", "Znowu z prawdziwych nabojów!", 30, 180, white)
        pisak.pisz("wers2", "Czujesz lekki stresik.", 30, 210, white)
        pisak.pisz("wers3", "Prowadzący zajęcia policjant, tłumaczy zasady strzelania:", 30, 240, white)
        pisak.pisz("wers4", "1.Macie 25 naboi!", 30, 270, dyellow)
        pisak.pisz("wers5", "2.Celujecie w bandytów!", 30, 300, dyellow)
        pisak.pisz("wers6", ".. i zaliczacie zajęcia", 30, 330, dyellow)
        pisak.pisz("wers7", "Wchodzisz na pozycję do strzelania i ładujesz pełny magazynek", 30, 360, white)
        pisak.pisz("wers8", "Wkładasz okulary ochronne i słuchawki wygłuszające. Słyszysz stłumiony głos prowadzącego:",
                   30, 390, white)
        pisak.pisz("wers9", "- Przygotować się do strzelania!", 30, 420, white)
        pisak.pisz("wers10", "* Za bardzo dobre wyniki, możesz zyskać cenne przedmioty", 30, 450, dyellow)

        pygame.display.update()
        mainClock.tick()


# Strzelnica Mossberg


def strzelnica_mossberg():
    pygame.mouse.set_visible(False)
    postac = 1
    ox = 400
    oy = 200
    punkty = 0
    naboje = 25
    delta = 0.0
    dane_gracza = db_save.pobierz_dane("dane_gracza")
    global blob_color
    running = True
    while running:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.blit(graph.strzelnica2, (0, 0))
        if naboje <= 0:
            if punkty > 200:
                tk_box.informacja("+5 doświadczenia, +5 zaangażowania ", graph.zaang_up)
                db_save.update_exp_ang_dni("ang", "dane_konta", 5)
                db_save.update_exp_ang_dni("exp", "dane_konta", 5)
                db_save.add_1_value("dane_baretki", "mosberg")
            pygame.mouse.set_visible(True)
            db_save.add_1_value("dane_strzelnica", punkty)
            strzelnica2wyniki()

        screen.blit(graph.tabelaIMG, (5, 600))
        mx, my = pygame.mouse.get_pos()
        offset = (mx - ox, my - oy)
        result = francuz_mask.overlap(blob_mask, offset)
        result1 = tifa_mask.overlap(blob_mask, offset)

        losowa = random.randint(200, 500)
        if ox < 10 or ox > 1000:
            ox = 200
        if oy < 10 or oy > 500:
            oy = 300
        poswiata = 55
        poswiata_y = 150
        delta += mainClock.tick(26) / 1000.0
        if delta > 1.5 / 1.0:
            if postac == 1:
                screen.blit(francuzIMG, (ox, oy))
                if delta > 2.99 / 1.0:
                    shot.play()
                    punkty -= 5
                    naboje -= 1
                    screen.blit(blood_IMG, (ox - 400, oy - 200))
                if result:
                    blob_color = orange_blob
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True
                            if click:
                                if losowa > 440:
                                    ricochet.play()
                                delta = 0.0
                                punkty += 10
                                naboje -= 1
                                shotgun.play()
                                ox += losowa
                                oy += losowa - 100
                                postac = random.randint(1, 3)
                                for i in range(len(efe)):
                                    screen.blit(efe[i], (mx - poswiata, my - poswiata_y))
                else:
                    blob_color = green_blob
            elif postac == 2:
                screen.blit(francuz1IMG, (ox, oy))
                if delta > 2.99 / 1.0:
                    shot.play()
                    punkty -= 5
                    naboje -= 1
                    screen.blit(blood_IMG, (ox - 400, oy - 200))
                if result:
                    blob_color = orange_blob
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True
                            if click:
                                if losowa > 440:
                                    ricochet.play()
                                delta = 0.0
                                punkty += 10
                                naboje -= 1
                                shotgun.play()
                                ox += losowa
                                oy += losowa - 100
                                postac = random.randint(1, 3)
                                for i in range(len(efe)):
                                    screen.blit(efe[i], (mx - poswiata, my - poswiata_y))
                else:
                    blob_color = green_blob
            elif postac == 3:
                screen.blit(tifaIMG, (ox, oy))
                if delta > 2.99 / 1.0:
                    delta = 0.0
                    postac = random.randint(1, 3)
                if result1:
                    blob_color = orange_blob
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True
                            if click:
                                if losowa > 440:
                                    ricochet.play()
                                delta = 0.0
                                punkty -= 10
                                naboje -= 2
                                shotgun.play()
                                ox += losowa
                                oy += losowa - 100
                                postac = random.randint(1, 3)
                                scream_girl.play()
                                for i in range(len(efe)):
                                    screen.blit(efe[i], (mx - poswiata, my - poswiata_y))
                else:
                    blob_color = green_blob

        while delta > 3 / 1.0:
            delta -= 3 / 1.0

        screen.blit(blob_color, (mx, my))
        screen.blit(gun2, (mx, my))

        pisak.pisz("imie", dane_gracza[0][0], 50, 650, black)
        pisak.pisz("naboje", str(naboje), 345, 650, black)
        pisak.pisz("wers2", str(punkty), 265, 650, black)

        pygame.display.update()


# Strzelnica2 Wyniki


def strzelnica2wyniki():
    running = True
    dane_gracza = db_save.pobierz_dane("dane_gracza")
    wynik = db_save.search_data("punkty", "dane_strzelnica")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.wynikiBG, (260, 10))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                loadingSound.play()
                scena34()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers1", str(wynik[0]), 730, 238, black)
        pisak.pisz("wers2", str(wynik[1]), 730, 328, black)
        pisak.pisz("wers3", dane_gracza[0][0], 460, 60, black)
        pygame.display.update()
        mainClock.tick()


# Scena34


def scena34():
    strzelnicaOGG.stop()
    siren.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                loadingSound.play()
                scena35()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Po strzelnicy wszyscy pakują się do wyjazdu.. no prawie wszyscy bo Ty zostajesz"
                           " na weekend.", 20, 120, white)
        pisak.pisz("wers1", "Odprowadziłeś(-aś) Tomka, Iwonę i Ankę pod szlaban. Wracając spotkałeś(-aś) dowócę"
                            " kompanii i ", 20, 150, white)
        pisak.pisz("wers2", "ustaliłeś(-aś), że służbę masz dzisiaj w nocy, a dokładniej to 12 godzinną..", 20, 180,
                   white)
        pisak.pisz("wers3", "Służba ma polegać, na patrolu a właściwie to obchodzie całego kompleksu szkoły.",
                   20, 210, white)
        pisak.pisz("wers4", "Takie służby są w parach, ale dowódca nie wiedział z kim będziesz mieć służbę."
                            " Dowiesz się na odprawie.", 20, 240, white)
        pisak.pisz("wers5", "Nie wiesz co robić z czasem, a odprawa jest o 18:00, na dodatek zaczęło padać.", 20, 270,
                   white)
        pisak.pisz("wers6", "Postanawiasz zdrzemnąć się do 17:30..",
                   20, 300, white)

        kompleksx = screen.blit(graph.kompleks[0], (623, 212))
        if kompleksx.collidepoint((mx, my)):
            screen.blit(graph.kompleks[1], (623, 235))

        pygame.display.update()
        mainClock.tick()


# Scena35


def scena35():
    running = True
    item = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pokoj_noc_bg, (0, 0))

        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if item:
            dalej_x = screen.blit(graph.press_Dalej[0], (1100, 640))
            if dalej_x.collidepoint((mx, my)):
                screen.blit(graph.press_Dalej[1], (1100, 640))
                if click:
                    db_save.update_exp_ang_dni("dni_sluzby", "dane_konta", 2)
                    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                    db_save.add_1_value("dane_ekwipunek", item)
                    loadingSound.play()
                    scena36()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "17:50 - choć tak dobrze Ci się spało, dźwięk budzika skutecznie wybudza Cię ze snu.", 20,
                   120, white)
        pisak.pisz("wers1", "Trzeba się zbierać bo zaraz odprawa! Lepiej się nie spóźnić!", 20, 150, white)
        pisak.pisz("wers2", "Notatnik, długopis, kajdanki, kabura, kanapki.. Chyba wszystko ale masz jeszcze"
                            " wolną kieszeń..", 20, 180, white)
        pisak.pisz("wers3", "Co wziąć ze sobą na nocną służbę? (Wybierz 1 rzecz)",
                   20, 210, dyellow)

        latarka_x = screen.blit(graph.latarka[0], (330, 340))
        if latarka_x.collidepoint((mx, my)):
            screen.blit(graph.latarka[1], (330, 340))
            if click:
                loadingSound.play()
                item = "latarka"

        nozyk_x = screen.blit(graph.nozyk[0], (530, 340))
        if nozyk_x.collidepoint((mx, my)):
            screen.blit(graph.nozyk[1], (530, 340))
            if click:
                loadingSound.play()
                item = "nozyk"

        fajki_x = screen.blit(graph.fajki[0], (730, 340))
        if fajki_x.collidepoint((mx, my)):
            screen.blit(graph.fajki[1], (730, 340))
            if click:
                loadingSound.play()
                item = "fajki"

        if item == "latarka":
            screen.blit(graph.nozyk[2], (530, 340))
            screen.blit(graph.fajki[2], (730, 340))
            pisak.pisz("wers_x", "Dobrej jakości aluminowa latarka..", 450, 500, white)
        elif item == "nozyk":
            screen.blit(graph.latarka[2], (330, 340))
            screen.blit(graph.fajki[2], (730, 340))
            pisak.pisz("wers_x", "Bardzo ostry nóż kieszonkowy..", 470, 500, white)
        elif item == "fajki":
            screen.blit(graph.latarka[2], (330, 340))
            screen.blit(graph.nozyk[2], (530, 340))
            pisak.pisz("wers_x", "Paczka 'KLUBOWYCH' z zapalniczką..", 450, 500, white)

        pygame.display.update()
        mainClock.tick()


# Scena36 (odprawa przed nocą)


def scena36():
    running = True
    db_save.add_1_value("dane_ekwipunek", "kod_pin")
    db_save.add_1_value("dane_ekwipunek", "klucz_klodka")
    eq = db_save.search_data("ekwipunek", "dane_ekwipunek")
    global active
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.odprawaBG, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                if active == "klucz_klodka":
                    active = ""
                db_save.delete_1_value("dane_ekwipunek", "klucz_klodka")
                loadingSound.play()
                siren.stop()
                rain_wav.play(-1)
                scena_brama_magazyn()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()
        for i in eq:
            if i == "latarka":
                pisak.pisz("wers", "Jak służba w nocy, to padło na latarkę. Może do czegoś się przyda.", 20, 90, white)
            elif i == "nozyk":
                pisak.pisz("wers", "Nie masz ze sobą konserwy ale.. ostry nóż może do czegoś się przydać.", 20, 90,
                           white)
            elif i == "fajki":
                pisak.pisz("wers", "Służba w nocy może się dłużyć, paczka papierosów przyda się na nudę..", 20, 90,
                           white)

        pisak.pisz("wers1", "Na zewnątrz rozpadało się jeszcze bardziej ale służba nie drużba - służyć trzeba.",
                   20, 120, white)
        pisak.pisz("wers2", "Odprawa jest w Twoim akademiku - sala 101. Plus jest taki - nie zmokniesz. Minus - odprawa"
                            " właśnie się zaczyna!", 20, 150, white)
        pisak.pisz("wers3", "Wchodzisz do sali - w środku przy ławkach siedzi już 5 innych osób, które tak jak ty"
                            " przyszły na odprawę.", 20, 180, white)
        pisak.pisz("wers4", "Z ich mokrych od deszczu mundurów, woda skapuje na posadzkę, tworząc małe, płytkie kałuże",
                   20, 210, white)
        pisak.pisz("wers5", "- Witamy królewnę - słyszysz głos z sali - Witamy, królewnę! - po chwili orientujesz się,"
                            " że po lewej", 20, 240, white)
        pisak.pisz("wers6", "stronie przy tablicy, za biurkiem siedzi 40 letni policjant w stopniu podkomisarza - "
                            "prowadzący odprawę.", 20, 270, white)
        pisak.pisz("wers7", "- Dzień dobry - odpowiadasz, po czym lekko zmieszany(-a) siadasz przy pierwszej wolnej"
                            " ławce", 20, 300, white)
        pisak.pisz("wers8", "Twoją ławkę dzieli odległość 2 metrów od biurka policjanta, na dodatek siedzisz"
                            " naprzeciwko.. ", 20, 330, white)
        pisak.pisz("wers9", "- No i znaleźliśmy chętnego(-ą)! - zwraca się do Ciebie - Chętnego(-ą) na co? - "
                            "odpowiadasz.", 20, 360, white)
        pisak.pisz("wers10", "- Zaraz się dowiesz - 'Kur**, no to ładnie' - myślisz - 'uwziął się czy co, nie wiadomo"
                             " nawet za co'", 20, 390, white)
        pisak.pisz("wers11", "- Nasza królewna - już wiesz, że zwraca się do Ciebie - przyszła sucha na odprawę dlatego"
                             " teraz", 20, 420, white)
        pisak.pisz("wers12", "  będzie miała zaszczyt zwiedzić magazyny/Falklandy i trochę zmoknąć! - czyli się"
                             " uwziął..", 20, 450, white)
        pisak.pisz("wers13", "- Królewna zacznie od Falklandów a jak je sprawdzi to wróci tutaj i zamelduje się po"
                             " resztę zadań", 20, 480, white)
        pisak.pisz("wers14", "  prowadzący wręcza Ci mokry świstek papieru i klucz (sprawdź plecak)", 20, 510, dyellow)
        pisak.pisz("wers15",
                   "  - to jest 5 -cyfrowy KOD PIN do wejścia na teren magazynów i klucz do kłódki. Rozejść się!! ", 20,
                   540, white)
        pygame.display.update()
        mainClock.tick()


# Scena Brama Magazyn


def scena_brama_magazyn(door_pkt=0):
    pygame.mouse.set_visible(False)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.magazyn_brama_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        alarm_pin_x = screen.blit(graph.alarm_pin[0], (847, 358))

        screen.blit(graph.rain, (0, 0))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if alarm_pin_x.collidepoint((mx, my)):
            screen.blit(graph.alarm_pin[1], (847, 358))
            if click:
                loadingSound.play()
                door_pkt = scena_brama_kod_pin()

        if door_pkt == 1:
            pisak.pisz("wers3", "To nie było trudne. Można iść dalej..", 20, 90, dyellow)
            drzwi_brama_x = screen.blit(graph.drzwi_brama[0], (900, 310))
            if drzwi_brama_x.collidepoint((mx, my)):
                screen.blit(graph.drzwi_brama[1], (900, 310))
                if click:
                    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                    door_open.play()
                    falklandy_mapa()
        else:
            pisak.pisz("wers", "Wychodzisz za teren szkoły od strony parkingu.. Nie przestaje padać.. ", 20, 60, white)
            pisak.pisz("wers1", "Po 10 minutach stajesz przed bramą na teren magazynów.", 20, 90, white)
            pisak.pisz("wers2", "Wiesz, że aby wejść, trzeba gdzieś wpisać KOD PIN..", 20, 120, white)
            pisak.pisz("wers3",
                       "W plecaku masz świstek z kodem PIN i.. O nie! Po drodze zgubiłeś(-aś) klucz do głównego magazynu!",
                       20, 150, white)
            pisak.pisz("wers4", "No i jak teraz sprawdzić wszystkie miejsca?", 20, 180, white)
            pisak.pisz("wers5", "Dyżurny pewnie się wkur**.. ", 20, 210, white)

        screen.blit(graph.rain, (0, 0))
        screen.blit(graph.palec, (mx, my))
        pygame.display.update()
        mainClock.tick(60)


# Scena Brama Magazyn (Wpisanie kodu PIN)


def scena_brama_kod_pin():
    pygame.mouse.set_visible(False)
    running = True
    pin_list = []
    door = 0
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.brama_kod_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        pin_1_x = screen.blit(graph.pin_1[0], (504, 283))
        pin_2_x = screen.blit(graph.pin_2[0], (577, 283))
        pin_3_x = screen.blit(graph.pin_3[0], (649, 283))
        pin_cancel_x = screen.blit(graph.pin_cancel[0], (719, 283))
        pin_4_x = screen.blit(graph.pin_4[0], (504, 356))
        pin_5_x = screen.blit(graph.pin_5[0], (577, 356))
        pin_6_x = screen.blit(graph.pin_6[0], (649, 355))
        pin_clear_x = screen.blit(graph.pin_clear[0], (721, 354))
        pin_7_x = screen.blit(graph.pin_7[0], (505, 429))
        pin_8_x = screen.blit(graph.pin_8[0], (578, 428))
        pin_9_x = screen.blit(graph.pin_9[0], (650, 428))
        pin_help_x = screen.blit(graph.pin_help[0], (723, 425))
        pin_0_x = screen.blit(graph.pin_0[0], (579, 500))
        pin_enter_x = screen.blit(graph.pin_enter[0], (723, 497))
        screen.blit(graph.rain, (0, 0))

        mx, my = pygame.mouse.get_pos()

        for i, cyfra in enumerate(pin_list):
            pisak.pisz("wers2", cyfra, 590 + i * 24, 150, black, 32)

        random_beep = random.randint(0, 2)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if pin_1_x.collidepoint((mx, my)):
            screen.blit(graph.pin_1[1], (504, 283))
            if click:
                pin_list.append('1')
                beep[random_beep].play()
        elif pin_2_x.collidepoint((mx, my)):
            screen.blit(graph.pin_2[1], (577, 283))
            if click:
                pin_list.append('2')
                beep[random_beep].play()
        elif pin_3_x.collidepoint((mx, my)):
            screen.blit(graph.pin_3[1], (649, 283))
            if click:
                pin_list.append('3')
                beep[random_beep].play()
        elif pin_cancel_x.collidepoint((mx, my)):
            screen.blit(graph.pin_cancel[1], (719, 283))
            if click:
                pin_list.clear()
                beep[random_beep].play()
        elif pin_4_x.collidepoint((mx, my)):
            screen.blit(graph.pin_4[1], (504, 356))
            if click:
                pin_list.append('4')
                beep[random_beep].play()
        elif pin_5_x.collidepoint((mx, my)):
            screen.blit(graph.pin_5[1], (577, 356))
            if click:
                pin_list.append('5')
                beep[random_beep].play()
        elif pin_6_x.collidepoint((mx, my)):
            screen.blit(graph.pin_6[1], (649, 355))
            if click:
                pin_list.append('6')
                beep[random_beep].play()
        elif pin_clear_x.collidepoint((mx, my)):
            screen.blit(graph.pin_clear[1], (721, 354))
            if click:
                pin_list.clear()
                beep[random_beep].play()
        elif pin_7_x.collidepoint((mx, my)):
            screen.blit(graph.pin_7[1], (505, 429))
            if click:
                pin_list.append('7')
                beep[random_beep].play()
        elif pin_8_x.collidepoint((mx, my)):
            screen.blit(graph.pin_8[1], (578, 428))
            if click:
                pin_list.append('8')
                beep[random_beep].play()
        elif pin_9_x.collidepoint((mx, my)):
            screen.blit(graph.pin_9[1], (650, 428))
            if click:
                pin_list.append('9')
                beep[random_beep].play()
        elif pin_help_x.collidepoint((mx, my)):
            screen.blit(graph.pin_help[1], (723, 425))
            if click:
                pin_list.clear()
                pin_list.append("!ERROR!")
                beep[random_beep].play()
        elif pin_0_x.collidepoint((mx, my)):
            screen.blit(graph.pin_0[1], (579, 500))
            if click:
                pin_list.append('0')
                beep[random_beep].play()
        elif pin_enter_x.collidepoint((mx, my)):
            screen.blit(graph.pin_enter[1], (723, 497))
            if click:
                try:
                    if pin_list[0] == "7" and pin_list[1] == "2" and pin_list[2] == "3" and pin_list[3] == "9" and \
                            pin_list[4] == "6":
                        pin_open.play()
                        door = 1
                    else:
                        pin_closed.play()
                        door = 0
                except IndexError:
                    pin_closed.play()
                    door = 0

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                running = False

        screen.blit(graph.rain, (0, 0))
        screen.blit(graph.palec, (mx, my))
        pygame.display.update()
        mainClock.tick(60)
    return door


# Scena Falklandy Mapa


def falklandy_mapa(text_radio=None, sektor_a=0, sektor_b=0, sektor_c=0, sektor_d=0, sektor_h=0, sektor_e=0, sektor_f=0,
                   sektor_i=0, sektor_g=0):
    pygame.mouse.set_visible(False)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.falklandy_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        reca_x = screen.blit(graph.reca[0], (352, 318))
        recb_x = screen.blit(graph.recb[0], (400, 144))
        recc_x = screen.blit(graph.recc[0], (602, 59))
        recd_x = screen.blit(graph.recd[0], (717, 54))
        rece_x = screen.blit(graph.rece[0], (717, 214))
        recf_x = screen.blit(graph.recf[0], (717, 318))
        recg_x = screen.blit(graph.recg[0], (602, 214))
        rech_x = screen.blit(graph.rech[0], (524, 318))
        reci_x = screen.blit(graph.reci[0], (524, 418))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        odwiedzone = sektor_a + sektor_b + sektor_c + sektor_d + sektor_h + sektor_e + sektor_f + sektor_i + sektor_g

        odwiedzone_str = str(odwiedzone)
        if odwiedzone == 9:
            pisak.pisz("wers2", "Sprawdzone sektory", 50, 50, green)
        else:
            pisak.pisz("wers2", "Sprawdzone sektory", 50, 50, dyellow)
        pisak.pisz("wers3", "/9", 160, 70, dyellow)
        pisak.pisz("wers4", odwiedzone_str, 140, 70, dyellow)

        if odwiedzone < 9:
            screen.blit(graph.szkola[0], (1100, 630))
        elif odwiedzone == 9 and text_radio == 1:
            dalej = screen.blit(graph.szkola[1], (1100, 630))
            if dalej.collidepoint((mx, my)):
                screen.blit(graph.szkola[2], (1100, 630))
                if click:
                    db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                    pygame.mouse.set_visible(True)
                    loadingSound.play()
                    trasa_falklandy()

        if reca_x.collidepoint((mx, my)):
            screen.blit(graph.reca[1], (352, 318))
            if click:
                loadingSound.play()
                sektor_a = falklandy_sektor_a()

        if recb_x.collidepoint((mx, my)):
            screen.blit(graph.recb[1], (400, 144))
            if click:
                loadingSound.play()
                sektor_b = falklandy_sektor_b()

        if recc_x.collidepoint((mx, my)):
            screen.blit(graph.recc[1], (602, 59))
            if click:
                loadingSound.play()
                sektor_c = falklandy_sektor_c()

        if recd_x.collidepoint((mx, my)):
            screen.blit(graph.recd[1], (717, 54))
            if click:
                loadingSound.play()
                sektor_d = falklandy_sektor_d()

        if rece_x.collidepoint((mx, my)):
            screen.blit(graph.rece[1], (717, 214))
            if click:
                loadingSound.play()
                sektor_e = falklandy_sektor_e()

        if recf_x.collidepoint((mx, my)):
            screen.blit(graph.recf[1], (717, 318))
            if click:
                loadingSound.play()
                sektor_f = falklandy_sektor_f()

        if recg_x.collidepoint((mx, my)):
            screen.blit(graph.recg[1], (602, 214))
            if click:
                loadingSound.play()
                sektor_g = falklandy_sektor_g()

        if rech_x.collidepoint((mx, my)):
            screen.blit(graph.rech[1], (524, 318))
            if click:
                loadingSound.play()
                sektor_h, text_radio = falklandy_sektor_h(text_radio)

        if reci_x.collidepoint((mx, my)):
            screen.blit(graph.reci[1], (524, 418))
            if click:
                loadingSound.play()
                sektor_i = falklandy_sektor_i()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Kliknij w sektor, by zwiedzić wybrane miejsce!", 350, 650, dyellow)

        screen.blit(graph.but, (mx, my))
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()


# Falklandy Sektor A


def falklandy_sektor_a():
    pygame.mouse.set_visible(False)
    running = True
    sektor_a = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.sektor_falklandy_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                sektor_a = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Brama - zamknięta.", 20, 90, white)
        pisak.pisz("wers1", "Ogrodzenie - bez uszkodzeń.", 20, 120, white)
        pisak.pisz("wers2", "To miejsce zostało sprawdzone..", 20, 150, white)

        screen.blit(graph.but, (mx, my))
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return sektor_a


# Falklandy Sektor B


def falklandy_sektor_b():
    pygame.mouse.set_visible(False)
    running = True
    sektor_b = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.sektor_falklandy_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                sektor_b = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Ogrodzenie, jeśli zardzewiałą siatkę można nazwać ogrodzeniem - bez uszkodzeń.", 20, 90,
                   white)
        pisak.pisz("wers1", "Ogólnie to pusto tutaj, ciekawe czy cały plac wygląda tak samo..", 20, 120, white)
        pisak.pisz("wers2", "To miejsce zostało sprawdzone..", 20, 150, white)

        screen.blit(graph.but, (mx, my))
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return sektor_b


# Falklandy Sektor C


def falklandy_sektor_c():
    pygame.mouse.set_visible(False)
    running = True
    sektor_c = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.sektor_falklandy_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                sektor_c = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Ogrodzenie - bez uszkodzeń.", 20, 90, white)
        pisak.pisz("wers1",
                   "Na ziemi walają się odłamki skruszonego mokrego betonu - Ten plac musi być bardzo stary - myślisz.",
                   20, 120, white)
        pisak.pisz("wers2", "Jest ciemno i co chwilę potykasz się o drobne kawałki złomu i kamieni.", 20, 150, white)
        pisak.pisz("wers3", "Tu jest wporządku - sprawdzone.", 20, 180, white)

        screen.blit(graph.but, (mx, my))
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return sektor_c


# Falklandy Sektor D


def falklandy_sektor_d():
    pygame.mouse.set_visible(False)
    running = True
    sektor_d = None
    while running:
        eq = db_save.search_data("ekwipunek", "dane_ekwipunek")
        click = False

        screen.fill(black)
        if active == "latarka":
            screen.blit(graph.sektor_falklandy_X_bg_light, (0, 0))
            pisak.pisz("wers_x", "Światło latarki odbija się w kilku miejscach..", 20, 180, brown)
        else:
            screen.blit(graph.sektor_falklandy_X_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        for q in eq:
            if q != "kluczyk":
                klucz_x = screen.blit(graph.klucz, (421, 245))
                if klucz_x.collidepoint((mx, my)):
                    screen.blit(graph.stary_klucz[0], (221, 245))
                    if click:
                        move.play()
                        db_save.add_1_value("dane_ekwipunek", "kluczyk")

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                sektor_d = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        for x in eq:
            if x != "kluczyk":
                pisak.pisz("wers", "Jakieś dziwne miejsce, jakby coś miało być budowane lub.. niszczone.", 20, 30,
                           white)
                pisak.pisz("wers1",
                           "Pełno tu starych przedmiotów, jakieś łopaty, skórzane wytarte rękawice, no.. prawie śmietnik.",
                           20, 60, white)
                pisak.pisz("wers2", "Spoglądasz na ogrodzenie.. - jest nienaruszone.", 20, 90, white)
                pisak.pisz("wers3",
                           "W sumie masz sporo wolnego czasu, może wśród tych staroci znajdziesz coś ciekawego.", 20,
                           120, white)
                pisak.pisz("wers4", "Latarka w tym miejscu byłaby pomocna..",
                           20, 150, white)
            if x == "kluczyk":
                pisak.pisz("wers3", "To szukanie już Cię nudziło ale.. w końcu znalazłeś coś ciekawego. Ba! Klucz!", 20,
                           60, dyellow)
                pisak.pisz("wers4",
                           "Ciekawe czy będzie pasował do kłódki głównego magazynu. Bo stary się przecież.. zgubił.",
                           20, 90, dyellow)
                pisak.pisz("wers5", "Najwyżej zostanie jako pamiątka..", 20, 120, dyellow)

        screen.blit(graph.oko, (mx, my))
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return sektor_d


# Falklandy Sektor E


def falklandy_sektor_e():
    pygame.mouse.set_visible(False)
    running = True
    sektor_e = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.sektor_falklandy_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                sektor_e = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Ogrodzenie - bez uszkodzeń.", 20, 90, white)
        pisak.pisz("wers1", "Ponownie zastanawiasz się nad sensem sprawdzania tego miejsca.. pustki.. ciemno.. cicho..",
                   20, 120, white)
        pisak.pisz("wers2", "No.. prawie cicho. Słychać tylko padający deszcz, spływający po rynnie magazynu.", 20, 150,
                   white)
        pisak.pisz("wers3", "'Dyżury w tym miejscu są bez sensu' - powtarzasz sobie co kilka kroków.", 20, 180, white)
        pisak.pisz("wers4", "'Najgorsze, że mogłem(-am) być w domu a wypadła akurat na mnie ta cholerna służba!'", 20,
                   210, white)
        pisak.pisz("wers5", "'Gdyby chociaż nie padało..'", 20, 240, white)

        screen.blit(graph.but, (mx, my))
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return sektor_e


# Falklandy Sektor F


def falklandy_sektor_f():
    pygame.mouse.set_visible(False)
    running = True
    sektor_f = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.sektor_falklandy_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                sektor_f = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Nic tu nie ma.. Żywej duszy.. A ty chodzisz wzdłuż ogrodzenia jak pies.. Mokry pies..", 20,
                   90, white)
        pisak.pisz("wers1", "Nie lepiej zamontować tu kamery? - zastanawiasz się.", 20, 120, white)
        pisak.pisz("wers2", "Ogrodzenie całe, bez uszkodzeń - to miejsce zostało sprawdzone.", 20, 150, white)

        screen.blit(graph.but, (mx, my))
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return sektor_f


# Falklandy Sektor G


def falklandy_sektor_g():
    pygame.mouse.set_visible(False)
    running = True
    sektor_i_wav.play()
    sektor_g = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.sektor_falklandy_sektor_g_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                sektor_i_wav.stop()
                sektor_g = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers",
                   "Miejsce za magazynem, to pozostałości po starym chodniku, prowadzącym w kierunku zardzewiałych drzwi pod nasypem.",
                   20, 60, white)
        pisak.pisz("wers1", "To miejsce wydaje się tajemnicze.. Masywne drzwi bez klamki i zamka?", 20, 90, white)
        pisak.pisz("wers2",
                   "'Komuś chyba zależało żeby nikt tam nie mógł wejść' - przyglądasz się drzwiom, szukając mechanizmu otwarcia.",
                   20, 120, white)
        pisak.pisz("wers3",
                   "'A co jest pod nasypem?' - zadajesz sobie kolejne pytanie, wiedząc że nie znasz na nie odpowiedzi.",
                   20, 150, white)
        pisak.pisz("wers3",
                   "Postanawiasz zgłębić temat tego miejsca tylko.. nie wiesz za bardzo od czego zacząć.",
                   20, 180, white)
        pisak.pisz("wers3",
                   "Podchodzisz do drzwi, opuszczasz wzrok i spokojnie nasłuchujesz.. nic.. cisza..",
                   20, 210, white)
        pisak.pisz("wers3",
                   "W tym skupieniu, dostrzegasz leżący na ziemi niedopałek cienkiego papierosa marki 'Cristal'",
                   20, 240, white)
        pisak.pisz("wers1", "Eh, nic tu nie ma.. Ale gdyby dyżurny zapytał, to drzwi zamknięte a miejsce sprawdzone.",
                   20, 270, white)

        screen.blit(graph.but, (mx, my))
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return sektor_g


# Falklandy Sektor I


def falklandy_sektor_i():
    pygame.mouse.set_visible(False)
    running = True
    sektor_i = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.sektor_falklandy_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                sektor_i = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Zastanawiasz się, że oprócz magazynu, nic tutaj nie ma ciekawego do oglądania.", 20, 90,
                   white)
        pisak.pisz("wers1",
                   "'Iwona naopowiadała nam pewnie bajek na dobranoc' - przypominasz sobie historię ze szpitalem.", 20,
                   120, white)
        pisak.pisz("wers2",
                   "'Gdyby mieć więcej czasu tutaj, to można sprawdzić ten magazyn dokładniej' - kontynuujesz myśl.",
                   20, 150, white)
        pisak.pisz("wers2", " Ogrodzenie bez uszkodzeń - to miejsce zostało sprawdzone.", 20, 180, white)

        screen.blit(graph.but, (mx, my))
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return sektor_i


# Falklandy Sektor H (drzwi)


def falklandy_sektor_h(text_radio):
    pygame.mouse.set_visible(False)
    running = True
    sektor_h = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.sektor_falklandy_drzwi_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        drzwi_x = screen.blit(graph.falklandy_drzwi[0], (630, 160))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if drzwi_x.collidepoint((mx, my)):
            screen.blit(graph.falklandy_drzwi[1], (630, 160))
            if click:
                loadingSound.play()
                text_radio = falklandy_sektor_h_klodka(text_radio)

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                sektor_h = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Obchodzisz cały budynek dookoła ale nic nie znajdujesz..", 20, 60, white)
        pisak.pisz("wers1", "Podchodzisz od frontu do zardzewiałych drzwi - zamknięte.", 20, 90, white)
        pisak.pisz("wers3", "Przyglądasz się chwilę i widzisz na drzwiach zatrzaśniętą kłódkę.", 20, 120, white)
        pisak.pisz("wers4", "'- To pewnie ten budynek mam sprawdzić' - myślisz - 'A zgubiony klucz, otwierał kłódkę..'",
                   20, 150, white)

        screen.blit(graph.palec, (mx, my))
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return sektor_h, text_radio


# Falklandy Sektor H Kłódka


def falklandy_sektor_h_klodka(text_radio):
    pygame.mouse.set_visible(False)
    running = True
    delta = 0.0
    correct = 0
    eq = db_save.search_data("ekwipunek", "dane_ekwipunek")
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.sektor_falklandy_klodka_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        klodka_x = screen.blit(graph.falklandy_klodka[0], (480, 207))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if klodka_x.collidepoint((mx, my)):
            screen.blit(graph.falklandy_klodka[1], (480, 207))
            if click:
                for q in eq:
                    if q != "kluczyk":
                        door_close.play()
                    elif q == "kluczyk" and correct == 4:
                        door_open.play()
                    else:
                        door_close.play()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        if text_radio != 1:
            pisak.pisz("wers2", "Na drzwiach wisi kłódka.", 20, 30, white)
            pisak.pisz("wers1", "Musisz sprawdzić wnętrze tego budynku.", 20, 60, white)
        if text_radio != 1 and (y for y in eq if y != "kluczyk"):
            pisak.pisz("wers3", "Hmm.. Czym ją otworzyć jak zgubiłem(-am) klucz.. ", 20, 90, white)
        elif text_radio != 1 and (v for v in eq if v == "kluczyk"):
            pisak.pisz("wers3", "Hmm.. Czy mój znaleziony klucz ją otworzy? Jakby pasuje..", 20, 90, white)
            pisak.pisz("wers4", "Muszę być ostrożny(-a) i spróbować naruszyć jej mechanizm w odpowiednim momencie.", 20,
                       120, white)
            pisak.pisz("wers5", "Nożem mógłbym pewnie podważyć ten klucz..", 20,
                       150, white)
        if text_radio == 1:
            pisak.pisz("wers4x", "JEST! Otworzyła się ale.. ktoś wzywa Cię przez radiostację.", 20, 30, white)
            pisak.pisz("wers4", "To chyba dyżurny.. radiostacja ma jakieś zakłócenia - pewnie od pogody", 20, 60, white)
            pisak.pisz("wers6", "Nie słyszałeś(-aś) dokładnego komunikatu ale postanawiasz szybko wracać do szkoły.",
                       20, 90,
                       white)
            pisak.pisz("wers5", "Nie masz już czasu na sprawdzenie budynku! Nie masz oryginalnego klucza!",
                       20, 120, white)
            pisak.pisz("wers7", "Kurde.. jak oddać klucz, jak się zgubił..", 20, 150,
                       white)

        screen.blit(graph.sensivity_range, (440, 520))
        if active == "nozyk":
            delta += mainClock.tick(30) / 9.0
        else:
            delta += mainClock.tick(30) / 3.0
        for z in eq:
            if z == "kluczyk":
                if correct < 3:
                    if delta < 390:
                        screen.blit(graph.sensivity_point[0], (440 + int(delta), 505))
                        if 190 < delta < 210:
                            screen.blit(graph.sensivity_point[1], (440 + int(delta), 505))
                            if click:
                                correct += 1
                    elif delta >= 390:
                        delta = 0.0
                elif correct == 3:
                    door_open.play()
                    radios.play()
                    text_radio = 1
                    correct = 4

        if correct == 0:
            screen.blit(graph.zamek[0], (1020, 250))
        elif correct == 1:
            screen.blit(graph.zamek[1], (1020, 250))
        elif correct == 2:
            screen.blit(graph.zamek[2], (1020, 250))
        elif correct >= 3:
            screen.blit(graph.zamek[3], (1020, 250))

        screen.blit(graph.palec, (mx, my))
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
    return text_radio


# Trasa Falklandy


def trasa_falklandy():
    running = True
    db_save.add_1_value("dane_ekwipunek", "klucz_klodka")
    radios.play()
    while running:
        click = False
        screen.fill(black)
        screen.blit(graph.trasa_falklandy_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                rain_wav.stop()
                loadingSound.play()
                akademik_dyzurny()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Dyżurny ponownie wzywa przez radiostację ale nic z tego nie rozumiesz, przez zakłócenia.",
                   20, 60, white)
        pisak.pisz("wers1", "Idąc ulicą Solidarności i tak unikając co większych kałuż, Twoja twarz się rozpromienia.",
                   20, 90, white)
        pisak.pisz("wers2", "Na chodniku leży.. klucz! Klucz, który wcześniej zgubiłeś(-aś).", 20, 120, white)
        pisak.pisz("wers3",
                   "'Teraz spokojnie mogę iść do dyżurnego po resztę zadań, ciekawe co wymyśli' - jesteś pełen(-na) optymizmu.",
                   20, 150, white)
        pisak.pisz("wers4",
                   "Zastanawiasz się czy powiedzieć mu o znalezionym kluczu, czy taką informację pozostawić sobie..",
                   20, 180, white)

        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()


# Akademik I - powrót do dyżurnego


def akademik_dyzurny():
    siren.play()
    running = True
    global active
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.odprawaBG, (0, 0))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                db_save.update_exp_ang_dni("exp", "dane_konta", 1)
                if active == "klucz_klodka":
                    active = ""
                klucz_klodka = ""
                siren.stop()
                loadingSound.play()
                rain_wav.play(-1)
                plan_szkoly()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers",
                   "- Nooo nareszcie! - dyżurny ironicznie zwraca się do Ciebie - A radiostacji to nie nauczyli Cię obsługować?",
                   20, 30, white)
        pisak.pisz("wers1",
                   "- Rozumiem, że Falklandy zostały sprawdzone i wszystko jest wporządku, tak? - spogląda marszcząc brwi",
                   20, 60, white)
        pisak.pisz("wers2", "- Tak - odpowiedasz - Miałem zakłócenia to dlatego..", 20, 90, white)
        pisak.pisz("wers3",
                   "- Na pewno? - próbuje wymusić od Ciebie inną odpowiedź ale odpowiadasz stanowczo - Tak, bez uwag!",
                   20, 120, white)
        pisak.pisz("wers4", "- No dobrze, to czas na resztę zadań.. Słuchaj uważnie bo dwa razy powtarzać nie będę..",
                   20, 150,
                   white)
        pisak.pisz("wers5",
                   "- Polecam sprawdzić wszystkie obiekty w szkole. Wchodzisz, sprawdzasz zabezpieczenia i wychodzisz.",
                   20, 180, white)
        pisak.pisz("wers6", "- Do 6 rano masz niewiele czasu - dyżury kontynuuje - dlatego w tył zwrot i do roboty!",
                   20, 210, white)
        pisak.pisz("wers7",
                   "- I proszę mi tu oddać klucz od magazynu - wskazuje palcem na blat a Ty odkładasz felerny klucz",
                   20, 240, white)
        pygame.display.update()
        mainClock.tick()


# Sala Kinowa


def kinowa_budynek():
    running = True
    kinowa_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.wspol2, (0, 0))
        screen.blit(graph.rain, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                kinowa_budynek_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Budynek nr 7 - znajduje się w nim sala kinowa i centrum konferencyjne.", 20, 90, white)
        pisak.pisz("wers1", "Drzwi są otwarte, dlatego wchodzisz do środka, po lewej stronie schody do góry,"
                            " po prawej - na dół.", 20, 120, white)
        pisak.pisz("wers2", "Słyszysz głosy dobiegające z jakiegoś pomieszczenia, gdzie prowadzą schody po prawej"
                            " stronie.", 20, 150, white)
        pisak.pisz("wers3", "Schodzisz na dół i.. Wooo! Tu jest bar z niezdrowym jedzonkiem!", 20, 180, white)
        pisak.pisz("wers4", "Podchodzisz do baru i zamawiasz hamburgera ze wszystkimi dodatkami.", 20, 210, white)
        pisak.pisz("wers5", "Mniam! To miejsce warto zapamiętać!", 20, 240, white)

        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return kinowa_budynek_pkt


# Sala Dziekanat


def dziekanat_budynek():
    running = True
    dziekanat_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.wspol2, (0, 0))
        screen.blit(graph.rain, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                dziekanat_budynek_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Budynek nr 6 - dziekanaty, sale wykładowe.. nic ciekawego.. ",
                   20, 90, white)
        pisak.pisz("wers", "Tu wszsytko jest wporządku.",
                   20, 90, white)
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()

    return dziekanat_budynek_pkt


# Sala Tajwan


def tajwan_budynek():
    running = True
    tajwan_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.tajwan_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                tajwan_budynek_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Budynek nr 28 - stary budynek na uboczu, nazywany przez policjantów - TAJWAN.",
                   20, 90, white)
        pisak.pisz("wers1", "Na Tajwanie obdywają się różne ćwiczenia i wykłady z kursu podstawowego.", 20, 120, white)
        pisak.pisz("wers2", "Strasznie wkurzające jest to, że trzeba iść szmat drogi na zajęcia i jeszcze uważać,"
                            " żeby się nie spóźnić.",
                   20, 150, white)
        pisak.pisz("wers3", "Tajwan swoją nazwę zawdzięcza temu, że posiada dość nietypowy dach, przypominający "
                            "chińską budowlę.", 20, 180, white)
        pisak.pisz("wers4", "Ten budynek, dawno nie był remontowany i przez to można poczuć 'smak' starej szkoły.",
                   20, 210, white)
        pisak.pisz("wers5", "*Naciskasz na klamkę ale drzwi są zamknięte..", 20, 240, white)
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()

    return tajwan_budynek_pkt


# Sala Budowla


def budowla_budynek():
    running = True
    budowla_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.palarnia_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                budowla_budynek_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Budynek nr 27 - Dział zaopatrzenia i transportu.",
                   20, 90, white)
        pisak.pisz("wers1", "To budynek, w którym nigdy nie będziesz mieć zajęć.", 20, 120, white)
        pisak.pisz("wers2", "Jak sama nazwa wskazuje, załatwia się tam sprawy zaopatrzeniowe.",
                   20, 150, white)
        pisak.pisz("wers3", "Wpatrujesz się w duże metalowe drzwi, które nagle zaczynają się otwierać.", 20, 180, white)
        pisak.pisz("wers4", "Wychodzi z nich mężczyzna ubrany w czarny uniform - ale nie robotniczy, wygląda trochę jak"
                            " Twój mundur ćwiczebny ", 20, 210, white)
        pisak.pisz("wers5", "ale jest jednoczęściowy. Przez otwarte drzwi słyszysz głośne śmiechy i rozmowy.", 20, 240,
                   white)
        pisak.pisz("wers6", "Jeden ze śmiejących się głosów obniża nieco ton i mówi: - Jarek!", 20, 270, white)
        pisak.pisz("wers7", "- Czego!? - odpowiada mężczyzna w czarnym uniformie.", 20, 300, white)
        pisak.pisz("wers8", "- Tylko nie zapomnij zadzownić do Tomka!", 20, 330, white)
        pisak.pisz("wers9", "- Jakiego Tomka?", 20, 360, white)
        pisak.pisz("wers10", "- Znaczy się Marka - odpowiada głos z budynku.", 20, 390, white)
        pisak.pisz("wers11", "- No dobra, jasna sprawa - mężczyzna w uniformie zamyka za sobą drzwi i idzie w kierunku"
                             " siłowni.", 20, 420, white)
        pisak.pisz("wers12", "*Heh same Tomki w tym Szczytnie - myślisz sobie.", 20, 450, white)
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return budowla_budynek_pkt


# Sala Palarnia


def palarnia_budynek(drzwi_otwarte):
    pygame.mouse.set_visible(False)
    running = True
    palarnia_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.palarnia_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        drzwi_warsztat_x = screen.blit(graph.drzwi_warsztat[0], (786, 180))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                palarnia_budynek_pkt = 1
                loadingSound.play()
                running = False

        if drzwi_warsztat_x.collidepoint((mx, my)):
            screen.blit(graph.drzwi_warsztat[1], (786, 180))
            if click:
                if drzwi_otwarte is not False:
                    door_open.play()
                    drzwi_otwarte = warsztat(drzwi_otwarte)
                else:
                    door_close.play()

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Warsztat i zabudowania gospodarcze.",
                   20, 90, white)
        pisak.pisz("wers1", "Z budynku, dochodzi odgłos pracującej pompy wodnej.", 20, 120, white)

        if drzwi_otwarte is not False:
            pisak.pisz("wers2", "Sprawdź zamknięcie drzwi.",
                       20, 150, white)
        else:
            pisak.pisz("wers2", "Wychodząc zatrzasnąłeś(-aś) za sobą drzwi.",
                       20, 150, white)

        screen.blit(graph.rain, (0, 0))
        screen.blit(graph.palec, (mx, my))
        pygame.display.update()
        mainClock.tick()

    return palarnia_budynek_pkt, drzwi_otwarte


# Warsztat


def warsztat(drzwi_otwarte):
    pygame.mouse.set_visible(True)
    warsztat_wav.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.warsztat_bg, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                warsztat_wav.stop()
                door_open.play()
                drzwi_otwarte = False
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "- Oho.. drzwi są otwarte.",
                   20, 30, white)
        pisak.pisz("wers", "- Co do.. ?! - spoglądasz na obrysowaną kredą, sylwetkę człowieka.",
                   20, 60, white)
        pisak.pisz("wers1", "Zastanawiasz się dłuższą chwilę.. po co ktoś miałby narysować akurat tutaj, coś takiego..",
                   20, 90, white)
        pisak.pisz("wers2", "Wpatrujesz się w posadzkę a wzrok wędruje po białej linii.. centymetr po centymetrze.",
                   20, 120, white)
        pisak.pisz("wers3",
                   "Rozglądasz się po pomieszczeniu, wszędzie leżą jakieś narzędzia: - No warsztat - głośno myślisz.",
                   20, 150, white)
        pisak.pisz("wers4",
                   "- Warsztat i miejsce.. O kurwa! - przypominasz sobie pierwsze dni szkolenia i dziwnego kolesia",
                   20, 180, white)
        pisak.pisz("wers5",
                   "który jak nakręcony opowiadał jak wygląda kurs i mówił coś o.. samobóju.",
                   20, 210, white)
        pisak.pisz("wers6",
                   "- No tak.. czyli chodziło mu o samobójstwo!",
                   20, 240, white)
        pisak.pisz("wers8",
                   "- A więc to tak wygląda miejsce zbrodni.. ciekawe jak.. odebrał sobie życie..",
                   20, 270, white)
        pisak.pisz("wers7",
                   "- Czy którymś z narzędzi.. czy się powiesił.. czy się zastrzelił.. czy nałykał tabletek.. ",
                   20, 300, white)
        pisak.pisz("wers9",
                   "A w ogóle to.. dlaczego warsztat jest otwarty o tej porze.. - rozkminiasz dalej.",
                   20, 330, white)
        pisak.pisz("wers10",
                   "- No nic.. Trzeba będzie dowiedzieć się więcej o tej historii i tym miejscu.",
                   20, 360, white)
        pisak.pisz("wers9",
                   "Ok, ogólnie to nikogo tu nie ma i chyba jest wporządku, zatrzasnę drzwi i po sprawie.",
                   20, 390, white)

        pygame.display.update()
        mainClock.tick()
    return drzwi_otwarte


# Sala Biblioteka


def biblioteka_budynek():
    rain_wav.stop()
    stolowkaOGG.play(-1)
    running = True
    biblioteka_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.biblioteka_bg, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                biblioteka_budynek_pkt = 1
                stolowkaOGG.stop()
                rain_wav.play(-1)
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Biblioteka - tutejsza biblioteka posiada dużą bazę ciekawych książek i czasopism.",
                   20, 90, white)
        pisak.pisz("wers1", "Można by coś przeczytać skoro już zostałeś(-aś) na weekend.", 20, 120, white)
        pisak.pisz("wers2", "Na drzwiach wejściowych wisi kartka: 'Biblioteka nieczynna z powodu remontu'",
                   20, 150, white)
        pisak.pisz("wers3", "'Przepraszamy i zapraszamy za 2 tygodnie'", 20, 180, white)
        pisak.pisz("wers4", " Postanawiasz wrócić tu po remoncie, by dowiedzieć się czegoś więcej o Falklandach.", 20,
                   210, white)

        pygame.display.update()
        mainClock.tick()
    return biblioteka_budynek_pkt


# Sala Kantyna


def kantyna_budynek():
    running = True
    kantyna_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.kantyna_bg, (0, 0))
        screen.blit(graph.rain, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                kantyna_budynek_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Budynek nr 18 - siedziba Kanclerza i Prorektora WSPOL.", 20, 90, white)
        pisak.pisz("wers1", "Drzwi są zamknięte.. ", 20, 120, white)
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()
    return kantyna_budynek_pkt


# Sala Symulator


def symulator_budynek():
    running = True
    symulator_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pcab_bg, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                symulator_budynek_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Budunek nr 11 - znajdują się w nim: aula, sale wykładowe oraz symulator w sytuacjach"
                           " kryzysowych.", 20, 90, white)
        pisak.pisz("wers1", "Miałeś(-aś) tu już zajęcia, kilka razy zdarzyło Ci się przymknąć oko przy nudnych"
                            " wykładach..", 20, 120, white)
        pisak.pisz("wers2", "Symulator to miejsce imitujące pomieszczenie dyżurnego tzw. 'dyżurkę', w którym stwarza"
                            " się różne sytuacje", 20, 150, white)
        pisak.pisz("wers3", "które mogą wystąpić na prawdziwej służbie.", 20, 180, white)
        pisak.pisz("wers4", "Widziałeś(-aś) kiedyś dyżurkę? Na policjanta, który tam pełni służbę nazywa się dyżurnym.",
                   20, 210, white)
        pisak.pisz("wers5", "Na biurku przeważnie ma kilka telefonów, kilka monitorów, mapy czy ekrany "
                            "z monitoringiem.", 20, 240, white)
        pisak.pisz("wers6", "To właśnie on jako pierwszy odbiera telefon, gdy dzwonimy na komisariat.", 20, 270, white)
        pisak.pisz("wers7", "No właściwie to odbierał.. bo teraz dzowniąc na numer alarmowy 112, pierwszą osobą jest",
                   20, 300, white)
        pisak.pisz("wers8", "operator WCPR - Wojewódzkiego Centrum Powiadamiania Ratunkowego, który następnie "
                            "przełącza rozmowę do dyżurnego.", 20, 330, white)
        pisak.pisz("wers9", "Dyżurnym może zostać tylko doświadczony policjant, jest to bardzo odpowiedzialne "
                            "stanowisko.", 20, 360, white)
        pisak.pisz("wers10", "Ty jesteś na kursie podstawowym, dlatego bycie dyżurnym to narazie odległa przyszłość..",
                   20, 390, white)

        pygame.display.update()
        mainClock.tick()

    return symulator_budynek_pkt


# Sala siłownia


def silownia_budynek():
    rain_wav.stop()
    silowniaOGG.play(-1)
    running = True
    silownia_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.silka, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                silownia_budynek_pkt = 1
                silowniaOGG.stop()
                rain_wav.play(-1)
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Siłownia - ot taki niewielki budynek.", 20, 90, white)
        pisak.pisz("wers1", "Hantle, ławeczki, ciężarki i różnorakie machiny na rozrost mięśni.",
                   20, 120, white)
        pisak.pisz("wers2", "Mało kiedy wietrzona - wali potem na kilometr..", 20, 150, white)

        pygame.display.update()
        mainClock.tick()
    return silownia_budynek_pkt


# Sala karate


def karate_budynek():
    running = True
    karate_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.karate_bg, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                karate_budynek_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Hala sportów walki - tu również odbywają się zajęcia WF.", 20, 90, white)
        pisak.pisz("wers1", "Jest to trochę inna hala a to dlatego, że na podłodze rozłożone są materace.",
                   20, 120, white)
        pisak.pisz("wers2", "Sala służy m.in. do ćwiczeń samoobrony, chwytów obezwładniających i posługiwania się pałką"
                            " służbową.", 20, 150, white)
        pisak.pisz("wers3", "Na zajęcia przychodzi się w.. kimonie i na boso.. Jak prawdziwy karateka :) ",
                   20, 180, white)
        pisak.pisz("wers4", "Rozgrzewki są bardzo męczące: podskoki, turlania, fikołki, przysiady i pompki",
                   20, 210, white)
        pisak.pisz("wers5", "Z sali można korzystać po zajęciach i ćwiczyć np. boks jak masz ochotę.", 20, 240, white)
        pisak.pisz("wers6", "Teraz jest tutaj pusto.. ", 20, 270, white)

        pygame.display.update()
        mainClock.tick()

    return karate_budynek_pkt


# Hilton


def hilton_budynek():
    running = True
    hilton_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.hilton_bg, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                hilton_budynek_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Budynek nr 9 to akademik, nazywany przez kursantów - Hilton", 20, 90, white)
        pisak.pisz("wers1", "Nazwę zawdzięcza temu, że w pokojach panuje nieco wyższy standard wypoczynku.",
                   20, 120, white)
        pisak.pisz("wers2", "Pokoje są 1 lub 2 osobowe, nieco bardziej zadbane łazienki z kabinami prysznicowymi",
                   20, 150, white)
        pisak.pisz("wers3", "W każdej łazience można znaleźć takie gadżety jak 'resortowe' mydełka i szampony.",
                   20, 180, white)
        pisak.pisz("wers4", "W akademiku sypiają policjanci będący na kursach specjalistycznych, często "
                            "w stopniach oficerskich",
                   20, 210, white)
        pisak.pisz("wers5", "Można tam spotkać komendantów, naczelników i kierowników różnych jednostek policji"
                            " w kraju", 20, 240, white)
        pisak.pisz("wers6", "a także wykładowców, którzy dojeżdżają z odległych miast na prowadzenie zajęć.",
                   20, 270, white)
        pisak.pisz("wers7", "No taki 'niby hotel' policyjny.. ale żeby odrazu Hilton?", 20, 300, white)

        pygame.display.update()
        mainClock.tick()

    return hilton_budynek_pkt


# PCAB


def pcab_budynek():
    rain_wav.stop()
    stolowkaOGG.play(-1)
    running = True
    pcab_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pcab_bg, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                pcab_budynek_pkt = 1
                stolowkaOGG.stop()
                rain_wav.play(-1)
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Nowoczesny budynek PCAB - Policyjne Centrum Analityczno-Badawcze.", 20, 90, white)
        pisak.pisz("wers1", "Ciekawe miejsce, w którym jeszcze nie miałeś(-aś) zajęć i.. chyba mieć nie będziesz.",
                   20, 120, white)
        pisak.pisz("wers2", "Są tutaj nowoczesne sale dydaktyczne, w których szkolą się policjanci będący na kursach"
                            " specjalistycznych:", 20, 150, white)
        pisak.pisz("wers3", " - analitycznych, oficerskich, operacyjnych, technik kryminalistycznych i innych.",
                   20, 180, white)
        pisak.pisz("wers4", "Na kurs specjalistyczny, kierowani są policjanci będący już w służbie.", 20, 210, white)
        pisak.pisz("wers5", "Fajnie by było kiedyś, pojechać na taki kurs.. tylko narazie trzeba zdać kurs podstawowy",
                   20, 240, white)

        pygame.display.update()
        mainClock.tick()

    return pcab_budynek_pkt


# Strzelnica budynek


def strzelnica_budynek():
    rain_wav.stop()
    stolowkaOGG.play(-1)
    running = True
    strzelnica_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.strzelnica_bg, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                strzelnica_budynek_pkt = 1
                stolowkaOGG.stop()
                rain_wav.play(-1)
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Strzelnica - to niewielki budynek zaraz za salą gimnastyczną.", 20, 90, white)
        pisak.pisz("wers1", "W środku są 2 strzelnice, jedna wewnątrz, w której już strzelałeś(-aś) i druga na"
                            " zewnątrz", 20, 120, white)
        pisak.pisz("wers2", "Na drugiej już się nie prowadzi strzelań i służy częściej jako miejsce na wykłady lub"
                            " strzelanie 'na sucho'", 20, 150, white)
        pisak.pisz("wers3", "No cóż.. jest praktycznie weekend i strzelnica jest zamknięta do poniedziałku.",
                   20, 180, white)

        nasucho_x = screen.blit(graph.nasucho[0], (1090, 151))
        if nasucho_x.collidepoint((mx, my)):
            screen.blit(graph.nasucho[1], (850, 178))

        pygame.display.update()
        mainClock.tick()

    return strzelnica_budynek_pkt


# Sala WF


def salawf_budynek():
    rain_wav.stop()
    salawfOGG.play(-1)
    running = True
    quest_tomek = db_save.search_data("quest_tomek", "dane_quest_tomek")
    salawf_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.salawfBG, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                salawf_budynek_pkt = 1
                salawfOGG.stop()
                rain_wav.play(-1)
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Wchodzisz do sali gimnastycznej. Miało być pusto ale..  na boisku rozgrywa się mecz piłki"
                           " halowej.", 20, 120, white)
        pisak.pisz("wers1", "Masz trochę czasu więc postanawiasz chwilę posiedzieć.",
                   20, 150, white)
        pisak.pisz("wers2", "Zasiadasz w III rzędzie niewielkich trybun, znajdujących się po prawej stronie.",
                   20, 180, white)
        pisak.pisz("wers3", "Oprócz Ciebie, na trybunach siedzi kilka osób, które wpatrują się bezinteresowanie w"
                            " toczoną rozgrywkę.", 20, 210, white)
        pisak.pisz("wers4", "Mecz rozgrywa się pomiędzy 2 drużynami ale nie są to żadne zawody, każdy zawodnik gra "
                            "w innej koszulce.", 20, 240, white)
        pisak.pisz("wers5", "*Eee - zamyślasz się - to wykładowcy grają po zajęciach wraz z osobami, które pozostały "
                            "na weekend.", 20, 270, white)
        for q in quest_tomek:
            if q == "bar_2":
                pisak.pisz("wers6", "*Ale.. chwila.. Jeden z mężczyzn szczególnie przykuwa Twoją uwagę.. hmm..",
                           20, 300, green)
                pisak.pisz("wers7",
                           "*Twarz jakby znajoma.. wykładowca? - Nieee. - Kursant? - Nie.. ale coś powoli świta"
                           " w głowie", 20, 330, green)
                pisak.pisz("wers8", "*No jasne, poznajesz.. przecież to.. barman! Barman z CELI!", 20, 360, green)

        pygame.display.update()
        mainClock.tick()

    return salawf_budynek_pkt


# Akademik I


def akademik_budynek_1():
    running = True
    akademik_budynek_1_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.akademik_bg_noc, (0, 0))
        screen.blit(graph.rain, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                akademik_budynek_1_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Akademik nr 1 - to miejsce znasz już jak własną kieszeń. Logiczne - masz tu"
                           " przecież pokój!", 20, 60, white)
        pisak.pisz("wers7", "W sali 101 pusto - dyżurny poszedł już do sztabu.", 20, 90, white)
        pisak.pisz("wers8", "Sprawdzasz drzwi przeciwpożarowe - zamknięte. Na korytarzach pusto, cisza, spokój.", 20,
                   120, white)

        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()

    return akademik_budynek_1_pkt


# Akademik II


def akademik_budynek_2():
    running = True
    akademik_budynek_2_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.akademik_bg_noc, (0, 0))
        screen.blit(graph.rain, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                akademik_budynek_2_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Akademik nr 2 - Drugi z akademików na terenie szkoły.", 20, 60, white)
        pisak.pisz("wers1", "Szkoda, że nie macie tu pokoju - byłoby bliżej na stołówkę.", 20, 90, white)
        pisak.pisz("wers2", "Rozglądasz się ale.. nie ma tu nic ciekawego.", 20, 120, white)
        pisak.pisz("wers3", "Sprawdzasz drzwi przeciwpożarowe - zamknięte. Na korytarzach pusto, cisza, spokój.", 20,
                   150, white)
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()

    return akademik_budynek_2_pkt


# Akademik III


def akademik_budynek_3():
    running = True
    akademik_budynek_3_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.akademik_bg_noc, (0, 0))
        screen.blit(graph.rain, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                akademik_budynek_3_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Akademik nr 3 - Trzeci z akademików na terenie szkoły, pomiędzy stołówką a basenem.",
                   20, 60, white)
        pisak.pisz("wers1", "Charakteryzuje się tym, że na parterze jest 'podwyższony standard' warunków mieszkalnych.",
                   20, 90, white)
        pisak.pisz("wers2", "Pokoje są 3-osobowe, codziennie sprzątane, jest w nich nawet telewizor z kablówką.",
                   20, 120, white)
        pisak.pisz("wers3", "Na parterze znajduje się też niewielka przychodnia, czynna w godz.08:00-10:00.",
                   20, 150, white)
        pisak.pisz("wers4", "Zwykle w tym akademiku, mieszkają policjanci uczestniczący w kursach specjalistycznych.",
                   20, 180, white)
        pisak.pisz("wers5", "Teraz jest tu pusto, wszyscy wyjechali na weekend..", 20, 210, white)
        pisak.pisz("wers6", "Rozglądasz się jeszcze chwilkę i wychodzisz na zewnątrz. Tu wszystko jest ok.", 20, 240,
                   white)
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()

    return akademik_budynek_3_pkt


# Sztab


def sztab_budynek():
    running = True
    sztab_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.sztabBG, (0, 0))
        screen.blit(graph.rain, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                sztab_budynek_pkt = 1
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Budynek nr 1 - Najważniejszy budynek na kampusie Wyższej Szkoły Policji w Szczytnie.",
                   20, 60, white)
        pisak.pisz("wers1", "To tu znajduje się rektorat. Swoją siedzibę ma tu m.in. Komendant-Rektor WSPOL"
                            " oraz dyżurny.", 20, 90, white)
        pisak.pisz("wers2", "Na budynku od strony [al.Marszałka Józefa Piłsudskiego], znajduje się duży napis z"
                            " nazwą szkoły.", 20, 120, white)
        pisak.pisz("wers3", "Jeszcze nie byłeś(-aś) w tym budynku, dlatego postanawiasz go zwiedzić.", 20, 150, white)
        pisak.pisz("wers4", "Otwierasz drzwi i zaczynasz wchodzić po schodach, przed sobą, po prawej stronie"
                            " widzisz jakiś pokój za szybą.", 20, 180, white)
        pisak.pisz("wers5", "- Halo, a Ty dokąd? A Ty dokąd?! - słyszysz ponownie.", 20, 210, white)
        pisak.pisz("wers6", "Wchodzisz jeszcze kilka schodków, do wysokości szyby, za którą przy biurku"
                            " siedzi policjant.", 20, 240, white)
        pisak.pisz("wers7", "W jego pokoju jest z 6 monitorów, na których widać podgląd z monitoringu,"
                            " za nim na ścianie wisi mapa szkoły.", 20, 270, white)
        pisak.pisz("wers8", "Na biurku kilka telefonów, 2 małe przenośne radiostacje. Z jednej słyszysz"
                            " jak ktoś powtarza: 'Bez uwag'", 20, 300, white)
        pisak.pisz("wers9", "- Słucham? - odpowiadasz lekko zmieszany(-a), policjant za szybą podsuwa "
                            "się bliżej szyby i mówi.", 20, 330, white)
        pisak.pisz("wers10", "- To ja słucham, coś się stało? - spogląda na Ciebie i widzisz jak mierzy"
                             " Cię wzrokiem od stóp do głowy.", 20, 360, white)
        pisak.pisz("wers11", "- Chciałem(-am) tylko zobaczyć.. - próbujesz wytłumaczyć po co tu jesteś.",
                   20, 390, white)
        pisak.pisz("wers12", "- Tu nie ma czego oglądać - dyżurny przerywa Twoją wypowiedź - Wracaj do roboty!",
                   20, 420, white)
        pisak.pisz("wers13", "- Aha - Nie wiesz co odpowiedzieć i wychodzisz z budynku.", 20, 450, white)

        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()

    return sztab_budynek_pkt


# Stołówka


def stolowka_budynek():
    rain_wav.stop()
    stolowkaOGG.play(-1)
    running = True
    stolowka_budynek_pkt = None
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.stolowkaBG, (0, 0))
        screen.blit(graph.rain, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                stolowka_budynek_pkt = 1
                stolowkaOGG.stop()
                rain_wav.play(-1)
                loadingSound.play()
                running = False

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Wchodzisz po schodach na I piętro. Posiłów nie wydają już od kilku godzin.", 20, 120, white)
        pisak.pisz("wers1", "Na sali jest ze 100 stolików, przy każdym stoliku stoją po 4 krzesła.", 20, 150, white)
        pisak.pisz("wers2", "Panie barmanki, zsuwają krzesła i zabierają plastikowe koszyki z chlebem. ",
                   20, 180, white)
        pisak.pisz("wers3", "Na ogół to miejsce tętni życiem w porach obiadowych a teraz? Cisza, spokój.. ",
                   20, 210, white)
        pisak.pisz("wers4", "Podchodzisz do wielkiego filaru przy okienku do wydawania posiłków na którym "
                            "przyczepiona jest kartka z MENU.", 20, 240, white)
        pisak.pisz("wers5", "Sobota - Kolacja: Makaron z sosem grzybowym, chleb, serek, kompot. *Grubo.. - "
                            "myślisz sobie.", 20, 270, white)
        pisak.pisz("wers6", "Jedyny plus tej kolacji jest taki, że dużo osób pojechało do domu i jest szansa na "
                            "dostanie 2 porcji.", 20, 300, white)
        pisak.pisz("wers7", "Rozglądasz się.. chyba wszystko tu jest na swoim miejscu.", 20, 330, white)
        screen.blit(graph.rain, (0, 0))
        pygame.display.update()
        mainClock.tick()

    return stolowka_budynek_pkt


# Plan_szkoły


def plan_szkoly(stolowka_budynek_pkt=0, sztab_budynek_pkt=0, akademik_budynek_3_pkt=0, akademik_budynek_2_pkt=0,
                akademik_budynek_1_pkt=0, salawf_budynek_pkt=0, strzelnica_budynek_pkt=0, pcab_budynek_pkt=0,
                hilton_budynek_pkt=0, karate_budynek_pkt=0, silownia_budynek_pkt=0, symulator_budynek_pkt=0,
                kantyna_budynek_pkt=0, biblioteka_budynek_pkt=0, palarnia_budynek_pkt=0, budowla_budynek_pkt=0,
                tajwan_budynek_pkt=0, dziekanat_budynek_pkt=0, kinowa_budynek_pkt=0, drzwi_otwarte=True):
    running = True
    pygame.mouse.set_visible(False)
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.planBG, (0, 0))
        screen.blit(graph.rain, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        screen.blit(graph.rain, (0, 0))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                loadingSound.play()
                scena_prog_5()  # SAVE

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        odwiedzone = stolowka_budynek_pkt + sztab_budynek_pkt + akademik_budynek_3_pkt + akademik_budynek_2_pkt + \
                     akademik_budynek_1_pkt + salawf_budynek_pkt + strzelnica_budynek_pkt + pcab_budynek_pkt + \
                     hilton_budynek_pkt + karate_budynek_pkt + silownia_budynek_pkt + symulator_budynek_pkt + \
                     kantyna_budynek_pkt + biblioteka_budynek_pkt + palarnia_budynek_pkt + budowla_budynek_pkt + \
                     tajwan_budynek_pkt + dziekanat_budynek_pkt + kinowa_budynek_pkt

        pisak.pisz("wers", "Kliknij na budynek, by zwiedzić wybrane miejsce!", 350, 650, dyellow)

        if odwiedzone == 18:
            pisak.pisz("wers2", "Odwiedzone miejsca", 50, 50, green)
        else:
            pisak.pisz("wers2", "Odwiedzone miejsca", 50, 50, dyellow)

        pisak.pisz("wers3", "/18", 160, 70, dyellow)
        pisak.pisz("wers4", str(odwiedzone), 140, 70, dyellow)

        stolowkax = screen.blit(graph.stolowka[0], (468, 86))
        if stolowkax.collidepoint((mx, my)):
            screen.blit(graph.stolowka[1], (468, 86))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                stolowka_budynek_pkt = stolowka_budynek()

        bibliotekax = screen.blit(graph.biblioteka[0], (513, 254))
        if bibliotekax.collidepoint((mx, my)):
            screen.blit(graph.biblioteka[1], (513, 254))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                biblioteka_budynek_pkt = biblioteka_budynek()

        sala_rdx = screen.blit(graph.sala_rd[0], (458, 185))
        if sala_rdx.collidepoint((mx, my)):
            screen.blit(graph.sala_rd[1], (458, 185))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                symulator_budynek_pkt = symulator_budynek()

        hiltonx = screen.blit(graph.hilton[0], (457, 361))
        if hiltonx.collidepoint((mx, my)):
            screen.blit(graph.hilton[1], (457, 361))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                hilton_budynek_pkt = hilton_budynek()

        akademik_x = screen.blit(graph.akademik2[0], (379, 45))
        if akademik_x.collidepoint((mx, my)):
            screen.blit(graph.akademik2[1], (379, 45))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                akademik_budynek_2_pkt = akademik_budynek_2()

        akademik1x = screen.blit(graph.akademik_1[0], (313, 71))
        if akademik1x.collidepoint((mx, my)):
            screen.blit(graph.akademik_1[1], (313, 71))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                akademik_budynek_1_pkt = akademik_budynek_1()

        karatex = screen.blit(graph.karate[0], (318, 291))
        if karatex.collidepoint((mx, my)):
            screen.blit(graph.karate[1], (318, 291))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                karate_budynek_pkt = karate_budynek()

        akademik3x = screen.blit(graph.akademik3[0], (569, 83))
        if akademik3x.collidepoint((mx, my)):
            screen.blit(graph.akademik3[1], (569, 83))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                akademik_budynek_3_pkt = akademik_budynek_3()

        budynekx = screen.blit(graph.budynek[0], (324, 438))
        if budynekx.collidepoint((mx, my)):
            screen.blit(graph.budynek[1], (324, 438))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                dziekanat_budynek_pkt = dziekanat_budynek()

        odprawyx = screen.blit(graph.odprawy[0], (378, 447))
        if odprawyx.collidepoint((mx, my)):
            screen.blit(graph.odprawy[1], (378, 447))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                kinowa_budynek_pkt = kinowa_budynek()

        salawfx = screen.blit(graph.salawf[0], (608, 167))
        if salawfx.collidepoint((mx, my)):
            screen.blit(graph.salawf[1], (608, 167))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                salawf_budynek_pkt = salawf_budynek()

        cyberx = screen.blit(graph.cyber[0], (666, 311))
        if cyberx.collidepoint((mx, my)):
            screen.blit(graph.cyber[1], (666, 311))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                pcab_budynek_pkt = pcab_budynek()

        pifpaf_x = screen.blit(graph.pifpaf[0], (725, 161))
        if pifpaf_x.collidepoint((mx, my)):
            screen.blit(graph.pifpaf[1], (725, 161))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                strzelnica_budynek_pkt = strzelnica_budynek()

        palarniax = screen.blit(graph.palarnia[0], (735, 266))
        if palarniax.collidepoint((mx, my)):
            screen.blit(graph.palarnia[1], (735, 266))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                palarnia_budynek_pkt, drzwi_otwarte = palarnia_budynek(drzwi_otwarte)

        kantynax = screen.blit(graph.kantyna[0], (511, 383))
        if kantynax.collidepoint((mx, my)):
            screen.blit(graph.kantyna[1], (511, 383))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                kantyna_budynek_pkt = kantyna_budynek()

        silkasx = screen.blit(graph.silkas[0], (613, 405))
        if silkasx.collidepoint((mx, my)):
            screen.blit(graph.silkas[1], (613, 405))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                silownia_budynek_pkt = silownia_budynek()

        budowlax = screen.blit(graph.budowla[0], (753, 418))
        if budowlax.collidepoint((mx, my)):
            screen.blit(graph.budowla[1], (753, 418))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                budowla_budynek_pkt = budowla_budynek()

        tajwanx = screen.blit(graph.tajwan[0], (840, 442))
        if tajwanx.collidepoint((mx, my)):
            screen.blit(graph.tajwan[1], (840, 442))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                tajwan_budynek_pkt = tajwan_budynek()

        sztabx = screen.blit(graph.sztab[0], (367, 511))
        if sztabx.collidepoint((mx, my)):
            screen.blit(graph.sztab[1], (367, 511))
            if click:
                pygame.mouse.set_visible(True)
                loadingSound.play()
                sztab_budynek_pkt = sztab_budynek()

        screen.blit(graph.rain, (0, 0))
        screen.blit(graph.but, (mx, my))
        pygame.display.update()
        mainClock.tick()


# SCENA PROG 5 - SAVE 2


def scena_prog_5():
    siren.stop()
    saveOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.prog, (0, 0))
        dalej = screen.blit(graph.press_Dalej[0], (1100, 640))
        notka = screen.blit(graph.notatnikA, (20, 570))
        tornister = screen.blit(graph.plecak, (200, 570))
        indeks_ocen = screen.blit(graph.indeks, (900, 570))
        zapisz_x = screen.blit(graph.zapisz[0], (570, 600))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(graph.press_Dalej[1], (1100, 640))
            if click:
                saveOGG.stop()
                loadingSound.play()

        if notka.collidepoint((mx, my)):
            screen.blit(graph.notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(graph.plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(graph.indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykaz_ocen()

        if zapisz_x.collidepoint((mx, my)):
            screen.blit(graph.zapisz[1], (570, 600))
            if click:
                loadingSound.play()
                pass

        akta_x = screen.blit(graph.button_odznaka[0], (1150, 20))
        if akta_x.collidepoint((mx, my)):
            screen.blit(graph.button_odznaka[1], (1150, 20))
            if click:
                loadingSound.play()
                akta_osobowe()

        pisak.pisz("wers", "Ten etap pozwala zapisać stan Gry.", 20, 460, dyellow)
        pisak.pisz("wers1", "Przy kolejnym uruchomieniu gry, w MENU pojawi się ikona plusa '+' - oznaczająca"
                            " kontynuację", 20, 490, dyellow)
        pisak.pisz("wers2", "Jest to również miejsce, z którego będziesz kontynuował(-a) dalszą grę.", 20, 520, dyellow)
        pygame.display.update()
        mainClock.tick()


# INFO


def info():
    running = True
    while running:
        global screen, xw, xh
        rozm = pygame.display.get_window_size()
        click = False
        screen.fill(black)
        screen.blit(graph.bgopcje, (0, 0))
        screen.blit(graph.licencja, (20 * xw, 520 * xh))
        volume = pygame.mixer.music.get_volume()

        if 0.2 < volume < 0.7:
            screen.blit(graph.volPanel[1], (950 * xw, 300 * xh))
        elif volume > 0.7:
            screen.blit(graph.volPanel[2], (950 * xw, 300* xh))
        elif volume < 0.2:
            screen.blit(graph.volPanel[0], (950 * xw, 300 * xh))

        if rozm[0] == 1280:
            screen.blit(graph.rozdz[0], (440 * xw, 500 * xh))
        if rozm[0] == 1600:
            screen.blit(graph.rozdz[1], (440 * xw, 500 * xh))


        cicho = screen.blit(graph.volLow[0], (1000 * xw, 530 * xh))
        srednio = screen.blit(graph.volNormal[0], (960 * xw, 570* xh))
        glosno = screen.blit(graph.volHI[0], (982 * xw, 610 * xh))
        cofnij_x = screen.blit(graph.cofnij[0], (120 * xw, 450 * xh))
        rozm_1280 = screen.blit(graph.rozdz_box[0], (640 * xw, 530 * xh))
        rozm_1600 = screen.blit(graph.rozdz_box[2], (640 * xw, 580 * xh))

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if cicho.collidepoint((mx, my)):
            screen.blit(graph.volLow[1], (1000 * xw, 530 * xh))
            if click:
                pisak.volume_low()

        if srednio.collidepoint((mx, my)):
            screen.blit(graph.volNormal[1], (960 * xw, 570 * xh))
            if click:
                pisak.volume_normal()

        if glosno.collidepoint((mx, my)):
            screen.blit(graph.volHI[1], (982 * xw, 610 * xh))
            if click:
                pisak.volume_hi()

        if rozm_1280.collidepoint((mx, my)):
            screen.blit(graph.rozdz_box[1], (640 * xw, 530 * xh))
            if click:
                screen = pygame.display.set_mode((1280, 720))
                xw = 1
                xh = 1

        if rozm_1600.collidepoint((mx, my)):
            screen.blit(graph.rozdz_box[3], (640 * xw, 580 * xh))
            if click:
                screen = pygame.display.set_mode((1600, 900))
                xw = 1.25
                xh = 1.25

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (120 * xw, 450 * xh))
            if click:
                loadingSound.play()
                running = False

        pisak.pisz("wers2", "'Policmajster' to gra tekstowa z elementami grafiki, opowiadająca historię z"
                            " Tobą w roli głównej.", 20 * xw, 150 * xh, white)
        pisak.pisz("wers3", "Gra rozpoczyna się od momentu gdy decydujesz się wstąpić do Policji a po"
                            " pomyślnym przejściu procedury doboru", 20 * xw, 180 * xh, white)
        pisak.pisz("wers4", "zostajesz wysłany(-a) na kilkumiesięczne szkolenie do szkoły policyjnej.", 20 * xw, 210 * xh, white)
        pisak.pisz("wers5", "Możesz poprowadzić swoją karierę poprzez szkołę, egzaminy, następnie służbę jako "
                            "prawdziwy policjant", 20 * xw, 240 * xh, white)
        pisak.pisz("wers6", "i upragniony awans do Wydziału Dochodzeniowo-Śledczego, na jednym z miejscowych "
                            "komisariatów.", 20 * xw, 270 * xh, white)
        pisak.pisz("wers7", "Dochodzeniówka to 'sól' całej policji..", 20 * xw, 300 * xh, white)
        pisak.pisz("wers8", "Dostajesz wiele spraw, tony papierologii, kwitów do wypełnienia - dzień jak co dzień.",
                   20 * xw, 330 * xh, white)
        pisak.pisz("wers9", "Pewnego dnia może dostaniesz niepozorną sprawę..", 20 * xw, 360 * xh, white)
        pisak.pisz("wers11", "Zbieżność sytuacji - jeśli wystąpią - jest przypadkowa.", 20 * xw, 390 * xh, white)

        pygame.display.update()
        mainClock.tick(60)


# NOTATNIK


def notatnik():
    pygame.mouse.set_visible(True)
    notatki = db_save.search_data("notatki", "dane_notatki")
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.notatniczek, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        notatnik_x = screen.blit(graph.notatnikPistol, (20, 20))
        note_quest = screen.blit(graph.oststrona[0], (1150, 550))

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
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

        if notatnik_x.collidepoint((mx, my)):
            screen.blit(graph.zapiski, (20, 210))

        if note_quest.collidepoint((mx, my)):
            screen.blit(graph.oststrona[1], (1150, 550))
            if click:
                tx_notes.ostatnia_strona()

        for i in notatki:
            if i == "legitymowanie":
                zapislegitymowanie = screen.blit(graph.notatnikLegit, (200, 20))
                if zapislegitymowanie.collidepoint((mx, my)):
                    screen.blit(graph.zapiskiLegit, (70, 210))
            elif i == "ruchdrogowy":
                zapisruch = screen.blit(graph.notatnikRuch, (380, 20))
                if zapisruch.collidepoint((mx, my)):
                    screen.blit(graph.zapiskiRuch, (120, 210))
            elif i == "wykroczenia":
                zapiswykr = screen.blit(graph.notatnikWykr, (560, 20))
                if zapiswykr.collidepoint((mx, my)):
                    screen.blit(graph.zapiskiWykr, (170, 210))

        pisak.pisz("wers", "Najedź kursorem na notatki by przeczytać.", 20, 655, dyellow)
        pisak.pisz("wers", "Zapiski", 1160, 510, dyellow)

        pygame.display.update()
        mainClock.tick(60)


# PLECAK


def equip():
    pygame.mouse.set_visible(False)
    running = True
    eq = db_save.search_data("ekwipunek", "dane_ekwipunek")
    global active
    while running:
        poz_item = 0
        click = False
        screen.fill(black)
        screen.blit(graph.plecakIN, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        help_x = screen.blit(graph.help_banner[0], (1230, 10))
        if active == "usb":
            screen.blit(graph.pendrive[0], (1076, 520))
            screen.blit(graph.pendrive[1], (800, 580))
        elif active == "skrawek":
            screen.blit(graph.skrawek[0], (1076, 520))
            screen.blit(graph.skrawek[1], (800, 580))
        elif active == "latarka":
            screen.blit(graph.latarka[3], (1076, 520))
            screen.blit(graph.latarka[5], (800, 580))
        elif active == "nozyk":
            screen.blit(graph.nozyk[0], (1076, 520))
            screen.blit(graph.nozyk[4], (800, 580))
        elif active == "fajki":
            screen.blit(graph.fajki[0], (1076, 520))
            screen.blit(graph.fajki[4], (800, 580))
        elif active == "kod_pin":
            screen.blit(graph.kod_pin_img[2], (1096, 515))
            screen.blit(graph.kod_pin_img[1], (800, 580))
        elif active == "kluczyk":
            screen.blit(graph.stary_klucz[0], (1106, 520))
            screen.blit(graph.stary_klucz[2], (800, 580))
        elif active == "klucz_klodka":
            screen.blit(graph.nowy_klucz[0], (1106, 520))
            screen.blit(graph.nowy_klucz[2], (800, 580))

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
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
                pygame.mouse.set_visible(True)
                loadingSound.play()
                break

        if help_x.collidepoint((mx, my)):
            screen.blit(graph.help_banner[1], (660, 20))

        for i in eq:
            if i == "usb":
                ere = screen.blit(graph.pendrive[0], (20 + poz_item, 40))
                if ere.collidepoint((mx, my)):
                    screen.blit(graph.pendrive[2], (20 + poz_item, 40))
                    if click:
                        move.play()
                        active = "usb"
                poz_item += 170
            elif i == "skrawek":
                ere = screen.blit(graph.skrawek[0], (20 + poz_item, 40))
                if ere.collidepoint((mx, my)):
                    screen.blit(graph.skrawek[2], (20 + poz_item, 40))
                    if click:
                        move.play()
                        active = "skrawek"
                poz_item += 170
            elif i == "latarka":
                ere = screen.blit(graph.latarka[0], (20 + poz_item, 40))
                if ere.collidepoint((mx, my)):
                    screen.blit(graph.latarka[4], (20 + poz_item, 40))
                    if click:
                        move.play()
                        active = "latarka"
                poz_item += 170
            elif i == "nozyk":
                ere = screen.blit(graph.nozyk[0], (20 + poz_item, 40))
                if ere.collidepoint((mx, my)):
                    screen.blit(graph.nozyk[3], (20 + poz_item, 40))
                    if click:
                        move.play()
                        active = "nozyk"
                poz_item += 170
            elif i == "fajki":
                ere = screen.blit(graph.fajki[0], (20 + poz_item, 40))
                if ere.collidepoint((mx, my)):
                    screen.blit(graph.fajki[3], (20 + poz_item, 40))
                    if click:
                        move.play()
                        active = "fajki"
                poz_item += 170
            elif i == "kod_pin":
                ere = screen.blit(graph.kod_pin_img[0], (20 + poz_item, 40))
                if ere.collidepoint((mx, my)):
                    screen.blit(graph.kod_pin_img[3], (20 + poz_item, 40))
                    if click:
                        move.play()
                        active = "kod_pin"
                poz_item += 170
            elif i == "kluczyk":
                ere = screen.blit(graph.stary_klucz[0], (20 + poz_item, 40))
                if ere.collidepoint((mx, my)):
                    screen.blit(graph.stary_klucz[1], (20 + poz_item, 40))
                    if click:
                        move.play()
                        active = "kluczyk"
                poz_item += 170
            elif i == "klucz_klodka":
                ere = screen.blit(graph.nowy_klucz[0], (20 + poz_item, 40))
                if ere.collidepoint((mx, my)):
                    screen.blit(graph.nowy_klucz[1], (20 + poz_item, 40))
                    if click:
                        move.play()
                        active = "klucz_klodka"
                poz_item += 170

        pisak.pisz("wers", "Kliknij na przedmiot by go użyć.", 40, 655, dyellow)
        screen.blit(graph.glass_banner, (1050, 490))
        screen.blit(graph.palec, (mx, my))
        pygame.display.update()
        mainClock.tick(60)


# WYKAZ OCEN


def wykaz_ocen():
    pygame.mouse.set_visible(True)
    oceny = db_save.search_data("ocena", "dane_indeks")
    running = True
    while running:
        click = False
        screen.fill(black)
        screen.blit(graph.indeksBG, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
        try:
            if oceny[0] == 5:
                screen.blit(graph.podpis1, (710, 267))
                screen.blit(graph.cyfraIndex5, (910, 267))
            elif oceny[0] == 4:
                screen.blit(graph.podpis1, (710, 267))
                screen.blit(graph.cyfraIndex4, (910, 267))
            elif oceny[0] == 3:
                screen.blit(graph.podpis1, (710, 267))
                screen.blit(graph.cyfraIndex3, (910, 267))
            elif oceny[0] == 2:
                screen.blit(graph.podpis1, (710, 267))
                screen.blit(graph.cyfraIndex2, (910, 267))
            elif oceny[0] == 1:
                screen.blit(graph.podpis1, (710, 267))
                screen.blit(graph.cyfraIndex1, (910, 267))
        except IndexError:
            pass

        try:
            if oceny[1] == 5:
                screen.blit(graph.podpis2, (705, 400))
                screen.blit(graph.cyfraIndex5, (910, 400))
            elif oceny[1] == 4:
                screen.blit(graph.podpis2, (705, 400))
                screen.blit(graph.cyfraIndex4, (910, 400))
            elif oceny[1] == 3:
                screen.blit(graph.podpis2, (705, 400))
                screen.blit(graph.cyfraIndex3, (910, 400))
            elif oceny[1] == 2:
                screen.blit(graph.podpis2, (705, 400))
                screen.blit(graph.cyfraIndex2, (910, 400))
            elif oceny[1] == 1:
                screen.blit(graph.podpis2, (705, 400))
                screen.blit(graph.cyfraIndex1, (910, 400))
        except IndexError:
            pass

        try:
            if oceny[2] == 5:
                screen.blit(graph.podpis3, (705, 335))
                screen.blit(graph.cyfraIndex5, (910, 332))
            elif oceny[2] == 4:
                screen.blit(graph.podpis3, (705, 335))
                screen.blit(graph.cyfraIndex4, (910, 332))
            elif oceny[2] == 3:
                screen.blit(graph.podpis3, (705, 335))
                screen.blit(graph.cyfraIndex3, (910, 332))
            elif oceny[2] == 2:
                screen.blit(graph.podpis3, (705, 335))
                screen.blit(graph.cyfraIndex2, (910, 332))
            elif oceny[2] == 1:
                screen.blit(graph.podpis3, (705, 335))
                screen.blit(graph.cyfraIndex1, (910, 332))
        except IndexError:
            pass

        pygame.display.update()
        mainClock.tick()


# Sklep


def sklep():
    rain_wav.stop()
    running = True
    pamietnik_sklep = 1  # zrobić jako zmienną globalną bo zawsze będzie książka
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.sklep_bg, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                loadingSound.play()
                progOGG.stop()
                rain_wav.play(-1)
                running = False

        if pamietnik_sklep == 1:
            ksiazka_x = screen.blit(graph.stara_ksiazka[0], (50, 50))
            if ksiazka_x.collidepoint((mx, my)) and stan_konta > 500:
                screen.blit(graph.stara_ksiazka[1], (50, 50))
                pisak.pisz("wersa", "'Pamiętnik, 1952r. - autor nieznany", 35, 35, dyellow)
                if click:
                    stan_konta = stan_konta - 500
                    stan_konta = round(stan_konta, 2)
                    pamietnik_sklep = 0
        else:
            screen.blit(graph.stara_ksiazka[2], (50, 50))

        pisak.pisz("wersb", "Stan konta", 190, 600, white)
        pisak.pisz("wersa", str(stan_konta), 205, 632, black)

        pygame.display.update()
        mainClock.tick()


# Sklep


def stary_pamietnik():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(graph.pamietnik_bg, (0, 0))
        cofnij_x = screen.blit(graph.cofnij[0], (560, 640))
        kartka_1_x = screen.blit(graph.kartka[0], (150, 50))
        kartka_2_x = screen.blit(graph.kartka[1], (300, 50))
        kartka_3_x = screen.blit(graph.kartka[2], (450, 50))
        kartka_4_x = screen.blit(graph.kartka[3], (600, 50))
        kartka_5_x = screen.blit(graph.kartka[4], (750, 50))
        kartka_6_x = screen.blit(graph.kartka[5], (900, 50))
        kartka_7_x = screen.blit(graph.kartka[6], (1050, 50))
        kartka_8_x = screen.blit(graph.kartka[7], (150, 250))
        kartka_9_x = screen.blit(graph.kartka[8], (300, 250))
        kartka_10_x = screen.blit(graph.kartka[9], (450, 250))
        kartka_11_x = screen.blit(graph.kartka[10], (600, 250))
        kartka_12_x = screen.blit(graph.kartka[11], (750, 250))
        kartka_13_x = screen.blit(graph.kartka[12], (900, 250))
        kartka_14_x = screen.blit(graph.kartka[13], (1050, 250))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if cofnij_x.collidepoint((mx, my)):
            screen.blit(graph.cofnij[1], (560, 640))
            if click:
                loadingSound.play()
                progOGG.stop()
                rain_wav.play(-1)
                running = False

        if kartka_1_x.collidepoint((mx, my)):
            screen.blit(graph.strona[0], (450, 100))
        if kartka_2_x.collidepoint((mx, my)):
            screen.blit(graph.strona[1], (450, 100))
        if kartka_3_x.collidepoint((mx, my)):
            screen.blit(graph.strona[2], (450, 100))
        if kartka_4_x.collidepoint((mx, my)):
            screen.blit(graph.strona[3], (450, 100))
        if kartka_5_x.collidepoint((mx, my)):
            screen.blit(graph.strona[4], (450, 100))
        if kartka_6_x.collidepoint((mx, my)):
            screen.blit(graph.strona[5], (450, 100))
        if kartka_7_x.collidepoint((mx, my)):
            screen.blit(graph.strona[6], (450, 100))
        if kartka_8_x.collidepoint((mx, my)):
            screen.blit(graph.strona[7], (450, 100))
        if kartka_9_x.collidepoint((mx, my)):
            screen.blit(graph.strona[8], (450, 100))
        if kartka_10_x.collidepoint((mx, my)):
            screen.blit(graph.strona[9], (450, 100))
        if kartka_11_x.collidepoint((mx, my)):
            screen.blit(graph.strona[10], (450, 100))
        if kartka_12_x.collidepoint((mx, my)):
            screen.blit(graph.strona[11], (450, 100))
        if kartka_13_x.collidepoint((mx, my)):
            screen.blit(graph.strona[12], (450, 100))
        if kartka_14_x.collidepoint((mx, my)):
            screen.blit(graph.strona[13], (450, 100))

        pygame.display.update()
        mainClock.tick()


intro_dev()

