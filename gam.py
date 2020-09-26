import pygame
import sys
import random
import time
import os
import os.path
from pygame import mixer
#import pkg_resources.py2_warn
from pygame.locals import *
import pisak

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

mainClock = pygame.time.Clock()
filepath = os.path.dirname(__file__)

# Rozmiar_okna
screen = pygame.display.set_mode((1280, 720))

# Nazwa_okna_gry
pygame.display.set_caption("Policmajster: Początek")

# Panel głośności
volPanel = pygame.image.load(os.path.join(filepath, "data\\pics\\volPanel.png"))
volPanel0 = pygame.image.load(os.path.join(filepath, "data\\pics\\volPanel0.png"))
volPanel2 = pygame.image.load(os.path.join(filepath, "data\\pics\\volPanel2.png"))
volLow = pygame.image.load(os.path.join(filepath, "data\\pics\\cicho.png"))
volLow1 = pygame.image.load(os.path.join(filepath, "data\\pics\\cicho1.png"))
volNormal = pygame.image.load(os.path.join(filepath, "data\\pics\\srednio.png"))
volNormal1 = pygame.image.load(os.path.join(filepath, "data\\pics\\srednio1.png"))
volHI = pygame.image.load(os.path.join(filepath, "data\\pics\\glosno.png"))
volHI1 = pygame.image.load(os.path.join(filepath, "data\\pics\\glosno1.png"))

# Muzyka w tle \\ reszta w module
controlVol = 0.2
music = pygame.mixer.music.load(os.path.join(filepath, "data\\sound\\horror1.wav"))
pygame.mixer.music.set_volume(controlVol)

# Dźwięki
loadingSound = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\load.wav"))
loadingSoundDEV = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\loading1.wav"))
siren = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\norma.wav"))
szum = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\szumszkolny.wav"))
silowniaOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\silownia.wav"))
progOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\prog.wav"))
barSound = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\barSound.wav"))
korytarzSound = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\korytarz.wav"))
spacerOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\spacer.wav"))
strzelnicaOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\srzelnicaglucha.wav"))
shot = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\shot.wav"))
shotgun = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\shotgun.wav"))
saveOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\save.wav"))
stolowkaOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\stolowka.wav"))
salawfOGG = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\salawf.wav"))
klik = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\klik.wav"))
pen = pygame.mixer.Sound(os.path.join(filepath, "data\\sound\\pen.wav"))

# Tekst
myFont = pygame.font.SysFont("monospace", 18)

# Grafiki okna tytułowego
bg = pygame.image.load(os.path.join(filepath, "data\\pics\\intro.png"))
kajdanki = pygame.image.load(os.path.join(filepath, "data\\pics\\kajdanki.png"))
kajdanki1 = pygame.image.load(os.path.join(filepath, "data\\pics\\kajdanki1.png"))
pistol = pygame.image.load(os.path.join(filepath, "data\\pics\\bron.png"))
pistol1 = pygame.image.load(os.path.join(filepath, "data\\pics\\bron1.png"))

# Nawigacja
pressKariera = pygame.image.load(os.path.join(filepath, "data\\navi\\kariera.png"))
pressKariera1 = pygame.image.load(os.path.join(filepath, "data\\navi\\kariera1.png"))
pressEnter = pygame.image.load(os.path.join(filepath, "data\\navi\\enter.png"))
pressEnter1 = pygame.image.load(os.path.join(filepath, "data\\navi\\enter1.png"))
pressOption = pygame.image.load(os.path.join(filepath, "data\\navi\\info.png"))
pressOption1 = pygame.image.load(os.path.join(filepath, "data\\navi\\info1x.png"))
cofnij = pygame.image.load(os.path.join(filepath, "data\\navi\\cofnij.png"))
cofnij1 = pygame.image.load(os.path.join(filepath, "data\\navi\\cofnij1.png"))
pressDalej = pygame.image.load(os.path.join(filepath, "data\\navi\\dalej.png"))
pressDalej1 = pygame.image.load(os.path.join(filepath, "data\\navi\\dalej1.png"))
silowniaN = pygame.image.load(os.path.join(filepath, "data\\navi\\silownia.png"))
silowniaN1 = pygame.image.load(os.path.join(filepath, "data\\navi\\silownia1.png"))
spacerNAV = pygame.image.load(os.path.join(filepath, "data\\navi\\spacer.png"))
spacerNAV1 = pygame.image.load(os.path.join(filepath, "data\\navi\\spacer1.png"))
tak = pygame.image.load(os.path.join(filepath, "data\\navi\\tak.png"))
tak1 = pygame.image.load(os.path.join(filepath, "data\\navi\\tak1.png"))
nie = pygame.image.load(os.path.join(filepath, "data\\navi\\nie.png"))
nie1 = pygame.image.load(os.path.join(filepath, "data\\navi\\nie1.png"))
cela_nav = pygame.image.load(os.path.join(filepath, "data\\navi\\cela.png"))
cela1_nav = pygame.image.load(os.path.join(filepath, "data\\navi\\cela1.png"))
miasto = pygame.image.load(os.path.join(filepath, "data\\navi\\miasto.png"))
miasto1 = pygame.image.load(os.path.join(filepath, "data\\navi\\miasto1.png"))
zapisz = pygame.image.load(os.path.join(filepath, "data\\navi\\zapisz.png"))
zapisz1 = pygame.image.load(os.path.join(filepath, "data\\navi\\zapisz1.png"))
zapisano = pygame.image.load(os.path.join(filepath, "data\\navi\\zapisano.png"))
zapis = ""
kontynuacja = pygame.image.load(os.path.join(filepath, "data\\navi\\plusz.png"))
kontynuacja1 = pygame.image.load(os.path.join(filepath, "data\\navi\\plusz1.png"))
save_start = pygame.image.load(os.path.join(filepath, "data\\navi\\continue.png"))
save_start1 = pygame.image.load(os.path.join(filepath, "data\\navi\\continue1.png"))
ide = pygame.image.load(os.path.join(filepath, "data\\navi\\ide.png"))
ide1 = pygame.image.load(os.path.join(filepath, "data\\navi\\ide1.png"))
stolowka = pygame.image.load(os.path.join(filepath, "data\\navi\\stolowka.png"))
stolowka1 = pygame.image.load(os.path.join(filepath, "data\\navi\\stolowka1.png"))
biblioteka = pygame.image.load(os.path.join(filepath, "data\\navi\\biblioteka.png"))
biblioteka1 = pygame.image.load(os.path.join(filepath, "data\\navi\\biblioteka1.png"))
sala_rd = pygame.image.load(os.path.join(filepath, "data\\navi\\sala_rd.png"))
sala_rd1 = pygame.image.load(os.path.join(filepath, "data\\navi\\sala_rd1.png"))
hilton = pygame.image.load(os.path.join(filepath, "data\\navi\\hilton.png"))
hilton1 = pygame.image.load(os.path.join(filepath, "data\\navi\\hilton1.png"))
akademik2 = pygame.image.load(os.path.join(filepath, "data\\navi\\akademik2.png"))
akademik21 = pygame.image.load(os.path.join(filepath, "data\\navi\\akademik21.png"))
akademik_1 = pygame.image.load(os.path.join(filepath, "data\\navi\\akademik1.png"))
akademik_11 = pygame.image.load(os.path.join(filepath, "data\\navi\\akademik11.png"))
karate = pygame.image.load(os.path.join(filepath, "data\\navi\\karate.png"))
karate1 = pygame.image.load(os.path.join(filepath, "data\\navi\\karate1.png"))
akademik3 = pygame.image.load(os.path.join(filepath, "data\\navi\\akademik3.png"))
akademik31 = pygame.image.load(os.path.join(filepath, "data\\navi\\akademik31.png"))
budynek = pygame.image.load(os.path.join(filepath, "data\\navi\\budynek.png"))
budynek1 = pygame.image.load(os.path.join(filepath, "data\\navi\\budynek1.png"))
odprawy = pygame.image.load(os.path.join(filepath, "data\\navi\\odprawy.png"))
odprawy1 = pygame.image.load(os.path.join(filepath, "data\\navi\\odprawy1.png"))
salawf = pygame.image.load(os.path.join(filepath, "data\\navi\\salawf.png"))
salawf1 = pygame.image.load(os.path.join(filepath, "data\\navi\\salawf1.png"))
cyber = pygame.image.load(os.path.join(filepath, "data\\navi\\cyber.png"))
cyber1 = pygame.image.load(os.path.join(filepath, "data\\navi\\cyber1.png"))
pifpaf = pygame.image.load(os.path.join(filepath, "data\\navi\\pifpaf.png"))
pifpaf1 = pygame.image.load(os.path.join(filepath, "data\\navi\\pifpaf1.png"))
palarnia = pygame.image.load(os.path.join(filepath, "data\\navi\\palarnia.png"))
palarnia1 = pygame.image.load(os.path.join(filepath, "data\\navi\\palarnia1.png"))
kantyna = pygame.image.load(os.path.join(filepath, "data\\navi\\kantyna.png"))
kantyna1 = pygame.image.load(os.path.join(filepath, "data\\navi\\kantyna1.png"))
silkas = pygame.image.load(os.path.join(filepath, "data\\navi\\silka.png"))
silkas_1 = pygame.image.load(os.path.join(filepath, "data\\navi\\silka1.png"))
budowla = pygame.image.load(os.path.join(filepath, "data\\navi\\budowla.png"))
budowla1 = pygame.image.load(os.path.join(filepath, "data\\navi\\budowla1.png"))
tajwan = pygame.image.load(os.path.join(filepath, "data\\navi\\tajwan.png"))
tajwan1 = pygame.image.load(os.path.join(filepath, "data\\navi\\tajwan1.png"))
sztab = pygame.image.load(os.path.join(filepath, "data\\navi\\sztab.png"))
sztab1 = pygame.image.load(os.path.join(filepath, "data\\navi\\sztab1.png"))
rozp = pygame.image.load(os.path.join(filepath, "data\\navi\\rozp.png"))
rozp1 = pygame.image.load(os.path.join(filepath, "data\\navi\\rozp1.png"))

# Dodatkowe grafiki
odznaka = pygame.image.load(os.path.join(filepath, "data\\pics\\odznaka.png"))
bgopcje = pygame.image.load(os.path.join(filepath, "data\\sceny\\bgopcje.png"))
bgankieta = pygame.image.load(os.path.join(filepath, "data\\sceny\\ankieta.png"))
mundur = pygame.image.load(os.path.join(filepath, "data\\pics\\czarnuch.png"))
licencja = pygame.image.load(os.path.join(filepath, "data\\pics\\licencjaGimp.png"))
oko = pygame.image.load(os.path.join(filepath, "data\\pics\\oko.png")).convert_alpha()

# Grafiki scen
wspol = pygame.image.load(os.path.join(filepath, "data\\sceny\\wspol.png"))
wspol2 = pygame.image.load(os.path.join(filepath, "data\\sceny\\wspol2.png"))
pokoj = pygame.image.load(os.path.join(filepath, "data\\sceny\\pokoj.png"))
strzelnica = pygame.image.load(os.path.join(filepath, "data\\sceny\\strzelnica.png"))
silka = pygame.image.load(os.path.join(filepath, "data\\sceny\\silownia.png"))
prog = pygame.image.load(os.path.join(filepath, "data\\sceny\\prog.png"))
plecakIN = pygame.image.load(os.path.join(filepath, "data\\sceny\\plecak.png"))
egzaminFoto = pygame.image.load(os.path.join(filepath, "data\\sceny\\egzamin.png"))
indeksBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\indeksWykaz.png"))
barBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\bar.png"))
pokojnocBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\pokojnoc.png"))
odprawaBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\odprawa.png"))
korytarzBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\korytarz.png"))
korytarzNOC = pygame.image.load(os.path.join(filepath, "data\\sceny\\korytarzSciana.png"))
korytarzDZIEN = pygame.image.load(os.path.join(filepath, "data\\sceny\\korytarzSciana2.png"))
napisPolicja = pygame.image.load(os.path.join(filepath, "data\\pics\\napisPolicja.png"))
napisPolicja1 = pygame.image.load(os.path.join(filepath, "data\\pics\\napisPolicja1.png"))
szczytno_nocBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\szczytnonoc.png"))
strzelnica_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\strzelnica1.png"))
strzelnica1 = pygame.image.load(os.path.join(filepath, "data\\sceny\\strzelnica2.png"))
strzelnica2 = pygame.image.load(os.path.join(filepath, "data\\sceny\\strzelnica3.png"))
tabelaIMG = pygame.image.load(os.path.join(filepath, "data\\pics\\tabelawynikow.png"))
wynikiBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\wykazstrzelan.jpg"))
torbaBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\torba_Tomka.png"))
drogaBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\droga.png"))
planBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\planszkoly.png"))
stolowkaBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\stolowka.png"))
akademikBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\akademik.png"))
sztabBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\sztabBG.png"))
salawfBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\salawf.png"))
pcab_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\pcab.png"))
hilton_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\hilton.png"))
karate_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\salakarate.png"))
kantyna_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\kantyna.png"))
biblioteka_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\biblioteka.png"))
palarnia_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\palarnia.png"))
tajwan_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\tajwan.png"))
maszyna_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\maszyna.png"))

# Pojęcia + zdjęcia
czarnuch = pygame.image.load(os.path.join(filepath, "data\\pojecia\\czarnuch.png"))
czarnuch1 = pygame.image.load(os.path.join(filepath, "data\\pics\\czarnuch.png"))
p99 = pygame.image.load(os.path.join(filepath, "data\\pojecia\\p99.png"))
p991 = pygame.image.load(os.path.join(filepath, "data\\pics\\p99.png"))
kulkamocy = pygame.image.load(os.path.join(filepath, "data\\pojecia\\kulkamocy.png"))
kulkamocy1 = pygame.image.load(os.path.join(filepath, "data\\pics\\kulkamocy.png"))
cela = pygame.image.load(os.path.join(filepath, "data\\pojecia\\cela.png"))
cela1 = pygame.image.load(os.path.join(filepath, "data\\pics\\cela1.png"))
akademik = pygame.image.load(os.path.join(filepath, "data\\pojecia\\akademik.png"))
akademik1 = pygame.image.load(os.path.join(filepath, "data\\pics\\akademik.png"))
wodka = pygame.image.load(os.path.join(filepath, "data\\pojecia\\wodka.png"))
wodka1 = pygame.image.load(os.path.join(filepath, "data\\pics\\wodka.png"))
plan = pygame.image.load(os.path.join(filepath, "data\\pojecia\\korytarz.png"))
plan1 = pygame.image.load(os.path.join(filepath, "data\\pics\\korytarz.png"))
falklandy = pygame.image.load(os.path.join(filepath, "data\\pojecia\\falklandy.png"))
falklandy1 = pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy.png"))
staryObraz = pygame.image.load(os.path.join(filepath, "data\\pojecia\\staryObraz.png"))
staryObraz1 = pygame.image.load(os.path.join(filepath, "data\\pics\\obrazKobieta.png"))
nowyObraz = pygame.image.load(os.path.join(filepath, "data\\pojecia\\nowyObraz.png"))
nowyObraz1 = pygame.image.load(os.path.join(filepath, "data\\pics\\obrazAuto.png"))
bimber = pygame.image.load(os.path.join(filepath, "data\\pojecia\\bimber.png"))
bimber1 = pygame.image.load(os.path.join(filepath, "data\\pics\\bimber.png"))
cywilki = pygame.image.load(os.path.join(filepath, "data\\pojecia\\cywilki.png"))
cywilki1 = pygame.image.load(os.path.join(filepath, "data\\pics\\cywilki.png"))
ogorkow = pygame.image.load(os.path.join(filepath, "data\\pojecia\\ogorkow.png"))
ogorkow1 = pygame.image.load(os.path.join(filepath, "data\\pics\\ogorek.png"))
inicjaly = pygame.image.load(os.path.join(filepath, "data\\pojecia\\inicjaly.png"))
inicjaly1 = pygame.image.load(os.path.join(filepath, "data\\pojecia\\inicjaly1.png"))
naszywka = pygame.image.load(os.path.join(filepath, "data\\pojecia\\naszywkabut.png"))
naszywka1 = pygame.image.load(os.path.join(filepath, "data\\pojecia\\naszywkabut1.png"))
ksiazka = pygame.image.load(os.path.join(filepath, "data\\pojecia\\ksiazka.png"))
ksiazka1 = pygame.image.load(os.path.join(filepath, "data\\pojecia\\ksiazka1.png"))
kniga = pygame.image.load(os.path.join(filepath, "data\\pojecia\\kniga.png"))
kniga1 = pygame.image.load(os.path.join(filepath, "data\\pojecia\\kniga1.png"))
kompleks = pygame.image.load(os.path.join(filepath, "data\\pojecia\\kompleks.png"))
kompleks1 = pygame.image.load(os.path.join(filepath, "data\\pojecia\\kompleks1.png"))
nasucho = pygame.image.load(os.path.join(filepath, "data\\pojecia\\nasucho.png"))
nasucho1 = pygame.image.load(os.path.join(filepath, "data\\pojecia\\nasucho1.png"))

# Grafiki notatnika
notatnikA = pygame.image.load(os.path.join(filepath, "data\\navi\\notatnik.png"))
notatnikB = pygame.image.load(os.path.join(filepath, "data\\navi\\notatnik1.png"))
notatniczek = pygame.image.load(os.path.join(filepath, "data\\sceny\\notatniczek.png"))
notatnikPistol = pygame.image.load(os.path.join(filepath, "data\\note\\notatkiPistol.png"))
zapiski = pygame.image.load(os.path.join(filepath, "data\\note\\note1.png"))
notatnikLegit = pygame.image.load(os.path.join(filepath, "data\\note\\notatkiLegit.png"))
zapiskiLegit = pygame.image.load(os.path.join(filepath, "data\\note\\noteLegit.png"))
notatnikRuch = pygame.image.load(os.path.join(filepath, "data\\note\\notatkiRuch.png"))
zapiskiRuch = pygame.image.load(os.path.join(filepath, "data\\note\\noteRuch.png"))
notatnikWykr = pygame.image.load(os.path.join(filepath, "data\\note\\notatkiWykroczenia.png"))
zapiskiWykr = pygame.image.load(os.path.join(filepath, "data\\note\\noteWykr.png"))

# Zawartość notatnika
legitymowanie = ""
ruchdrogowy = ""
wykroczenia = ""

# Zawartość plecaka
pendrive1 = ""
skrawek1 = ""

# Quest TOMEK
quest_tomek_1 = ""  # personel #rozmowa
quest_tomek_torba = ""  # torebunia
quest_tomek_cela = ""  # cela

# Grafiki plecaka
plecak = pygame.image.load(os.path.join(filepath, "data\\navi\\plecak.png"))
plecak1 = pygame.image.load(os.path.join(filepath, "data\\navi\\plecak1.png"))
pendrive = pygame.image.load(os.path.join(filepath, "data\\plecak\\usb.png"))
pendriveOpis = pygame.image.load(os.path.join(filepath, "data\\pics\\usbTomka.png"))
skrawek = pygame.image.load(os.path.join(filepath, "data\\plecak\\skrawek.png"))
skrawekOpis = pygame.image.load(os.path.join(filepath, "data\\plecak\\skrawekOpis.png"))

# Grafiki indeksu
indeks = pygame.image.load(os.path.join(filepath, "data\\navi\\indeks.png"))
indeks1 = pygame.image.load(os.path.join(filepath, "data\\navi\\indeks1.png"))

# Ikona gry
icon = pygame.image.load(os.path.join(filepath, "data\\pics\\icon.png"))
pygame.display.set_icon(icon)

# Animacja logo
animatedLogo = [pygame.image.load(os.path.join(filepath, "data\\logo\\logo.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo1.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo2.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo3.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo4.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo5.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo6.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo7.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo8.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo9.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo10.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo11.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo12.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo13.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo14.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo15.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo16.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo17.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo18.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo19.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo20.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo21.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo22.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo23.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo24.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo25.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo26.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo27.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo28.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo29.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo30.png"))]

# Intro
intro = pygame.image.load(os.path.join(filepath, "data\\introDev\\1x.png"))
# Intro kafle
kafel = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel.png")).convert_alpha()
kafel1 = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel1.png")).convert_alpha()
kafel2 = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel2.png")).convert_alpha()
kafel2x = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel2x.png")).convert_alpha()
kafel3 = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel3.png")).convert_alpha()
kafel3x = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel3x.png")).convert_alpha()
kafel4 = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel4.png")).convert_alpha()
kafel4x = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel4x.png")).convert_alpha()
kafel5 = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel5.png")).convert_alpha()
kafel5x = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel5x.png")).convert_alpha()
kafel6 = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel6.png")).convert_alpha()
kafel6x = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel6x.png")).convert_alpha()
kafel7 = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel7.png")).convert_alpha()
kafel7x = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel7x.png")).convert_alpha()
kafel8 = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel8.png")).convert_alpha()
kafel8x = pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel8x.png")).convert_alpha()

# Stopnie służbowe
post = pygame.image.load(os.path.join(filepath, "data\\stopnie\\post.png"))

# Kolory
blue = (0, 0, 255)
black = (0, 0, 0)
white = (170, 170, 170)
red = (220, 0, 0)
green = (0, 140, 0)
dyellow = (115, 115, 0)

# Imię gracza
imieGracza = ""

# Egzaminy  [ ODPOWIEDZI ]
odp1 = ""
odp2 = ""
odp3 = ""
odp4 = ""
ocena = ""
ocenaSTR = ""

odp1_ruch = ""
odp2_ruch = ""
odp3_ruch = ""
odp4_ruch = ""
ocena_ruch = ""
ocena_ruchSTR = ""

odp1_wykr = ""
odp2_wykr = ""
odp3_wykr = ""
odp4_wykr = ""
ocena_wykr = ""
ocena_wykrSTR = ""

# Wyniki ze strzelania [0 = P99, 1 = pompka...]
tablica_wynikow = []
tablica_wynikow_mb = []
wynikp99 = ""
wynikmb = ""

# CYFRY do egzaminów------------------------------------------------------
cyfra5 = pygame.image.load(os.path.join(filepath, "data\\pics\\cyfra5.png"))
cyfra4 = pygame.image.load(os.path.join(filepath, "data\\pics\\cyfra4.png"))
cyfra3 = pygame.image.load(os.path.join(filepath, "data\\pics\\cyfra3.png"))
cyfra2 = pygame.image.load(os.path.join(filepath, "data\\pics\\cyfra2.png"))
cyfra1 = pygame.image.load(os.path.join(filepath, "data\\pics\\cyfra1.png"))

# CYFRY do indeksu---------------------------------------------------------
cyfraIndex1 = pygame.image.load(os.path.join(filepath, "data\\indeks\\1.png"))
cyfraIndex2 = pygame.image.load(os.path.join(filepath, "data\\indeks\\2.png"))
cyfraIndex3 = pygame.image.load(os.path.join(filepath, "data\\indeks\\3.png"))
cyfraIndex4 = pygame.image.load(os.path.join(filepath, "data\\indeks\\4.png"))
cyfraIndex5 = pygame.image.load(os.path.join(filepath, "data\\indeks\\5.png"))

# Podpisy w indeksie-----------------
podpis1 = pygame.image.load(os.path.join(filepath, "data\\indeks\\podpis1.png"))
podpis2 = pygame.image.load(os.path.join(filepath, "data\\indeks\\podpis2.png"))
podpis3 = pygame.image.load(os.path.join(filepath, "data\\indeks\\podpis3.png"))
podpis4 = pygame.image.load(os.path.join(filepath, "data\\indeks\\podpis4.png"))

# Strzelnica
gun = pygame.image.load(os.path.join(filepath, "data\\tarcze\\gun.png")).convert_alpha()
gun2 = pygame.image.load(os.path.join(filepath, "data\\tarcze\\gun1.png")).convert_alpha()
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

# Keyboard
key_enter = pygame.image.load(os.path.join(filepath, "data\\keyboard\\zatwierdz.png")).convert_alpha()
key_enter1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\zatwierdz1.png")).convert_alpha()
key_kasuj = pygame.image.load(os.path.join(filepath, "data\\keyboard\\kasuj.png")).convert_alpha()
key_kasuj1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\kasuj1.png")).convert_alpha()
key_q = pygame.image.load(os.path.join(filepath, "data\\keyboard\\q.png")).convert_alpha()
key_q1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\q1.png")).convert_alpha()
key_w = pygame.image.load(os.path.join(filepath, "data\\keyboard\\w.png")).convert_alpha()
key_w1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\w1.png")).convert_alpha()
key_e = pygame.image.load(os.path.join(filepath, "data\\keyboard\\e.png")).convert_alpha()
key_e1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\e1.png")).convert_alpha()
key_r = pygame.image.load(os.path.join(filepath, "data\\keyboard\\r.png")).convert_alpha()
key_r1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\r1.png")).convert_alpha()
key_t = pygame.image.load(os.path.join(filepath, "data\\keyboard\\t.png")).convert_alpha()
key_t1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\t1.png")).convert_alpha()
key_z = pygame.image.load(os.path.join(filepath, "data\\keyboard\\z.png")).convert_alpha()
key_z1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\z1.png")).convert_alpha()
key_u = pygame.image.load(os.path.join(filepath, "data\\keyboard\\u.png")).convert_alpha()
key_u1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\u1.png")).convert_alpha()
key_i = pygame.image.load(os.path.join(filepath, "data\\keyboard\\i.png")).convert_alpha()
key_i1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\i1.png")).convert_alpha()
key_o = pygame.image.load(os.path.join(filepath, "data\\keyboard\\o.png")).convert_alpha()
key_o1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\o1.png")).convert_alpha()
key_p = pygame.image.load(os.path.join(filepath, "data\\keyboard\\p.png")).convert_alpha()
key_p1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\p1.png")).convert_alpha()
key_os = pygame.image.load(os.path.join(filepath, "data\\keyboard\\os.png")).convert_alpha()
key_os1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\os1.png")).convert_alpha()
key_a = pygame.image.load(os.path.join(filepath, "data\\keyboard\\a.png")).convert_alpha()
key_a1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\a1.png")).convert_alpha()
key_s = pygame.image.load(os.path.join(filepath, "data\\keyboard\\s.png")).convert_alpha()
key_s1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\s1.png")).convert_alpha()
key_d = pygame.image.load(os.path.join(filepath, "data\\keyboard\\d.png")).convert_alpha()
key_d1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\d1.png")).convert_alpha()
key_f = pygame.image.load(os.path.join(filepath, "data\\keyboard\\f.png")).convert_alpha()
key_f1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\f1.png")).convert_alpha()
key_g = pygame.image.load(os.path.join(filepath, "data\\keyboard\\g.png")).convert_alpha()
key_g1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\g1.png")).convert_alpha()
key_h = pygame.image.load(os.path.join(filepath, "data\\keyboard\\h.png")).convert_alpha()
key_h1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\h1.png")).convert_alpha()
key_j = pygame.image.load(os.path.join(filepath, "data\\keyboard\\j.png")).convert_alpha()
key_j1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\j1.png")).convert_alpha()
key_k = pygame.image.load(os.path.join(filepath, "data\\keyboard\\k.png")).convert_alpha()
key_k1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\k1.png")).convert_alpha()
key_l = pygame.image.load(os.path.join(filepath, "data\\keyboard\\l.png")).convert_alpha()
key_l1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\l1.png")).convert_alpha()
key_es = pygame.image.load(os.path.join(filepath, "data\\keyboard\\es.png")).convert_alpha()
key_es1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\es1.png")).convert_alpha()
key_as = pygame.image.load(os.path.join(filepath, "data\\keyboard\\as.png")).convert_alpha()
key_as1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\as1.png")).convert_alpha()
key_y = pygame.image.load(os.path.join(filepath, "data\\keyboard\\y.png")).convert_alpha()
key_y1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\y1.png")).convert_alpha()
key_x = pygame.image.load(os.path.join(filepath, "data\\keyboard\\x.png")).convert_alpha()
key_x1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\x1.png")).convert_alpha()
key_c = pygame.image.load(os.path.join(filepath, "data\\keyboard\\c.png")).convert_alpha()
key_c1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\c1.png")).convert_alpha()
key_v = pygame.image.load(os.path.join(filepath, "data\\keyboard\\v.png")).convert_alpha()
key_v1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\v1.png")).convert_alpha()
key_b = pygame.image.load(os.path.join(filepath, "data\\keyboard\\b.png")).convert_alpha()
key_b1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\b1.png")).convert_alpha()
key_n = pygame.image.load(os.path.join(filepath, "data\\keyboard\\n.png")).convert_alpha()
key_n1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\n1.png")).convert_alpha()
key_m = pygame.image.load(os.path.join(filepath, "data\\keyboard\\m.png")).convert_alpha()
key_m1 = pygame.image.load(os.path.join(filepath, "data\\keyboard\\m1.png")).convert_alpha()




def intro_dev():
    while True:
        click = False
        mx, my = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        screen.blit(intro, (0, 0))
        pisak.pisz("wers1", "Kliknij by kontynuować..", 1000, 650, white)
        kaf1 = screen.blit(kafel, (507, 453))
        kaf2 = screen.blit(kafel2, (630, 382))
        kaf3 = screen.blit(kafel3, (644, 124))
        kaf4 = screen.blit(kafel4, (440, 218))
        kaf5 = screen.blit(kafel5, (762, 265))
        kaf6 = screen.blit(kafel6, (479, 116))
        kaf7 = screen.blit(kafel7, (868, 391))
        kaf8 = screen.blit(kafel8, (640, 44))
        if kaf1.collidepoint((mx, my)):
            screen.blit(kafel1, (507, 453))
        if kaf2.collidepoint((mx, my)):
            screen.blit(kafel2x, (630, 382))
        if kaf3.collidepoint((mx, my)):
            screen.blit(kafel3x, (644, 124))
        if kaf4.collidepoint((mx, my)):
            screen.blit(kafel4x, (440, 218))
        if kaf5.collidepoint((mx, my)):
            screen.blit(kafel5x, (762, 265))
        if kaf6.collidepoint((mx, my)):
            screen.blit(kafel6x, (479, 116))
        if kaf7.collidepoint((mx, my)):
            screen.blit(kafel7x, (868, 391))
            if mouse[0] == 1:
                click = True
                if click:
                    wejsciedogry()
        if kaf8.collidepoint((mx, my)):
            screen.blit(kafel8x, (640, 44))
        pygame.display.update()
        mainClock.tick()

# Wejście do gry


def wejsciedogry():
    pygame.mixer.music.play(-1)
    bg_x = 0
    bg_x2 = bg.get_width()
    starter = 0
    while True:
        click = False
        mouse = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        bg_x -= 1
        bg_x2 -= 1
        if bg_x < bg.get_width() * -1:
            bg_x = bg.get_width()
        if bg_x2 < bg.get_width() * -1:
            bg_x = bg.get_width()
                
        screen.fill(black)
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x2, 0))
        if starter != 29:
            screen.blit(animatedLogo[starter], (490, 430))
            starter += 1
            if starter == 29:
                starter = 0
                
        button = screen.blit(pressEnter, (450, 570))
        button1 = screen.blit(pressOption, (680, 570))
        screen.blit(kajdanki, (900, 500))
        screen.blit(pistol, (0, 500))

        mx, my = pygame.mouse.get_pos()

        if button1.collidepoint((mx, my)):
            screen.blit(pressOption1, (680, 570))
            screen.blit(kajdanki1, (900, 500))
            if mouse[0] == 1:
                click = True
                if click:
                    loadingSound.play()
                    info()

        if button.collidepoint((mx, my)):
            screen.blit(pressEnter1, (450, 570))
            screen.blit(pistol1, (0, 500))
            if mouse[0] == 1:
                click = True
                if click:
                    loadingSound.play()
                    start()

        try:
            save_file = open("data\\save\\save.txt", "r")
            if save_file:
                kontynuacja_x = screen.blit(kontynuacja, (618, 580))
                if kontynuacja_x.collidepoint((mx, my)):
                    screen.blit(kontynuacja1, (618, 580))
                    if mouse[0] == 1:
                        click = True
                        if click:
                            loadingSound.play()
                            save_file.close()
                            kontynuacja_gry()
        except (UnboundLocalError, FileNotFoundError):
            pass

        pygame.display.update()
        mainClock.tick(30)

# Kontynuacja gry


def kontynuacja_gry():
    running = True
    global imieGracza, legitymowanie, ruchdrogowy, pendrive1, skrawek1, ocenaSTR, ocena_ruchSTR
    global quest_tomek_1, wynikp99
    while running:
        click = False

        screen.fill(black)
        screen.blit(bgankieta, (200, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        dalejx = screen.blit(save_start, (1100, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                break

        if dalejx.collidepoint((mx, my)):
            screen.blit(save_start1, (1100, 570))
            if click:
                pygame.mixer.music.stop()
                loadingSoundDEV.play()
                scenaProg3()

        save_file = open("data\\save\\save.txt", "r")
        imie_save = save_file.readline()
        imieGracza = imie_save.replace("\n", "")
        legitymowanie_save = save_file.readline()
        legitymowanie = legitymowanie_save.replace("\n", "")
        ruchdrogowy_save = save_file.readline()
        ruchdrogowy = ruchdrogowy_save.replace("\n", "")
        pendrive1_save = save_file.readline()
        pendrive1 = pendrive1_save.replace("\n", "")
        skrawek1_save = save_file.readline()
        skrawek1 = skrawek1_save.replace("\n", "")
        quest_tomek_1_save = save_file.readline()
        quest_tomek_1 = quest_tomek_1_save.replace("\n", "")
        ocenaSTR_save = save_file.readline()
        ocenaSTR = ocenaSTR_save.replace("\n", "")
        ocena_ruchSTR_save = save_file.readline()
        ocena_ruchSTR = ocena_ruchSTR_save.replace("\n", "")
        wynikp99_save = save_file.readline()
        wynikp99 = wynikp99_save.replace("\n", "")
        save_file.close()
        czas_pliku = time.ctime(os.path.getctime("data\\save\\save.txt"))

        pisak.pisz("wers1", "Witaj!", 30, 90, dyellow)
        pisak.pisz("wers2", "Twój zapis gry posiada funkcjonariusza o imieniu: ", 30, 120, dyellow)
        pisak.pisz("wers3", imieGracza, 580, 120, white)
        pisak.pisz("wers4", "Data utworzenia: ", 30, 150, dyellow)
        pisak.pisz("wers3", czas_pliku, 230, 150, white)
        screen.blit(odznaka, (40, 490))

        pygame.display.update()
        mainClock.tick()

# Start


def start():
    nazwa_gracza = []
    running = True
    while running:
        global imieGracza
        click = False
        
        screen.fill(black)
        screen.blit(maszyna_bg, (0, 0))
        screen.blit(key_enter1, (565, 570))
        

        pisak.pisz("wers1", "Podaj imię. Zatwierdź        a następnie naciśnij 'Dalej'", 330, 600, white)
        pisak.pisz("wers2", imieGracza, 620, 150, white)
        
        for i, litera in enumerate(nazwa_gracza):
          pisak.pisz("wers2", litera, 620 + i * 12, 150, white)
        
        cofnijx = screen.blit(cofnij, (560, 640))

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
              
        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                break

        q_nopress = screen.blit(key_q, (315, 400))
        if q_nopress.collidepoint((mx, my)):
            screen.blit(key_q1, (315, 400))
            if click:
                klik.play()
                nazwa_gracza.append("Q")

        w_nopress = screen.blit(key_w, (365, 390))
        if w_nopress.collidepoint((mx, my)):
            screen.blit(key_w1, (365, 390))
            if click:
                klik.play()
                nazwa_gracza.append("W")

        e_nopress = screen.blit(key_e, (427, 388))
        if e_nopress.collidepoint((mx, my)):
            screen.blit(key_e1, (427, 388))
            if click:
                klik.play()
                nazwa_gracza.append("E")

        r_nopress = screen.blit(key_r, (487, 388))
        if r_nopress.collidepoint((mx, my)):
            screen.blit(key_r1, (487, 388))
            if click:
                klik.play()
                nazwa_gracza.append("R")

        t_nopress = screen.blit(key_t, (547, 388))
        if t_nopress.collidepoint((mx, my)):
            screen.blit(key_t1, (547, 388))
            if click:
                klik.play()
                nazwa_gracza.append("T")

        z_nopress = screen.blit(key_z, (610, 388))
        if z_nopress.collidepoint((mx, my)):
            screen.blit(key_z1, (610, 388))
            if click:
                klik.play()
                nazwa_gracza.append("Z")

        u_nopress = screen.blit(key_u, (670, 390))
        if u_nopress.collidepoint((mx, my)):
            screen.blit(key_u1, (670, 390))
            if click:
                klik.play()
                nazwa_gracza.append("U")

        i_nopress = screen.blit(key_i, (730, 390))
        if i_nopress.collidepoint((mx, my)):
            screen.blit(key_i1, (730, 390))
            if click:
                klik.play()
                nazwa_gracza.append("I")

        o_nopress = screen.blit(key_o, (790, 390))
        if o_nopress.collidepoint((mx, my)):
            screen.blit(key_o1, (790, 390))
            if click:
                klik.play()
                nazwa_gracza.append("O")

        p_nopress = screen.blit(key_p, (862, 399))
        if p_nopress.collidepoint((mx, my)):
            screen.blit(key_p1, (862, 399))
            if click:
                klik.play()
                nazwa_gracza.append("P")

        os_nopress = screen.blit(key_os, (922, 402))
        if os_nopress.collidepoint((mx, my)):
            screen.blit(key_os1, (922, 402))
            if click:
                klik.play()
                nazwa_gracza.append("Ó")

        a_nopress = screen.blit(key_a, (328, 459))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (328, 459))
            if click:
                klik.play()
                nazwa_gracza.append("A")

        s_nopress = screen.blit(key_s, (393, 460))
        if s_nopress.collidepoint((mx, my)):
            screen.blit(key_s1, (393, 460))
            if click:
                klik.play()
                nazwa_gracza.append("S")

        d_nopress = screen.blit(key_d, (455, 459))
        if d_nopress.collidepoint((mx, my)):
            screen.blit(key_d1, (455, 459))
            if click:
                klik.play()
                nazwa_gracza.append("D")

        f_nopress = screen.blit(key_f, (510, 460))
        if f_nopress.collidepoint((mx, my)):
            screen.blit(key_f1, (510, 460))
            if click:
                klik.play()
                nazwa_gracza.append("F")

        g_nopress = screen.blit(key_g, (575, 460))
        if g_nopress.collidepoint((mx, my)):
            screen.blit(key_g1, (575, 460))
            if click:
                klik.play()
                nazwa_gracza.append("G")

        h_nopress = screen.blit(key_h, (635, 460))
        if h_nopress.collidepoint((mx, my)):
            screen.blit(key_h1, (635, 460))
            if click:
                klik.play()
                nazwa_gracza.append("H")

        j_nopress = screen.blit(key_j, (695, 460))
        if j_nopress.collidepoint((mx, my)):
            screen.blit(key_j1, (695, 460))
            if click:
                klik.play()
                nazwa_gracza.append("J")

        k_nopress = screen.blit(key_k, (755, 460))
        if k_nopress.collidepoint((mx, my)):
            screen.blit(key_k1, (755, 460))
            if click:
                klik.play()
                nazwa_gracza.append("K")

        l_nopress = screen.blit(key_l, (815, 460))
        if l_nopress.collidepoint((mx, my)):
            screen.blit(key_l1, (815, 460))
            if click:
                klik.play()
                nazwa_gracza.append("L")

        es_nopress = screen.blit(key_es, (875, 460))
        if es_nopress.collidepoint((mx, my)):
            screen.blit(key_es1, (875, 460))
            if click:
                klik.play()
                nazwa_gracza.append("Ę")

        as_nopress = screen.blit(key_as, (932, 460))
        if as_nopress.collidepoint((mx, my)):
            screen.blit(key_as1, (932, 460))
            if click:
                klik.play()
                nazwa_gracza.append("Ą")

        y_nopress = screen.blit(key_y, (357, 516))
        if y_nopress.collidepoint((mx, my)):
            screen.blit(key_y1, (357, 516))
            if click:
                klik.play()
                nazwa_gracza.append("Y")

        x_nopress = screen.blit(key_x, (421, 516))
        if x_nopress.collidepoint((mx, my)):
            screen.blit(key_x1, (421, 516))
            if click:
                klik.play()
                nazwa_gracza.append("X")

        c_nopress = screen.blit(key_c, (481, 516))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (481, 516))
            if click:
                klik.play()
                nazwa_gracza.append("C")

        v_nopress = screen.blit(key_v, (542, 516))
        if v_nopress.collidepoint((mx, my)):
            screen.blit(key_v1, (542, 516))
            if click:
                klik.play()
                nazwa_gracza.append("V")

        b_nopress = screen.blit(key_b, (600, 516))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (600, 516))
            if click:
                klik.play()
                nazwa_gracza.append("B")

        n_nopress = screen.blit(key_n, (660, 516))
        if n_nopress.collidepoint((mx, my)):
            screen.blit(key_n1, (660, 516))
            if click:
                klik.play()
                nazwa_gracza.append("N")

        m_nopress = screen.blit(key_m, (720, 516))
        if m_nopress.collidepoint((mx, my)):
            screen.blit(key_m1, (720, 516))
            if click:
                klik.play()
                nazwa_gracza.append("M")

        del_nopress = screen.blit(key_kasuj, (275, 510))
        if del_nopress.collidepoint((mx, my)):
            screen.blit(key_kasuj1, (275, 510))
            if click:
                klik.play()
                nazwa_gracza.clear()
                imieGracza = "".join(str(x) for x in nazwa_gracza)

        if not nazwa_gracza:
            potwierdzenieNIE = myFont.render("Wpisz imię!", 1, red)
            screen.blit(potwierdzenieNIE, (600, 150))

        if nazwa_gracza:
            enter_nopress = screen.blit(key_enter, (965, 503))
            if enter_nopress.collidepoint((mx, my)):
                screen.blit(key_enter1, (965, 503))
                if click:
                    klik.play()
                    imieGracza = "".join(str(x) for x in nazwa_gracza)
        if imieGracza:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    objasnienie()
            
        pygame.display.update()
        mainClock.tick()

# Objaśnienie


def objasnienie():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(bgankieta, (200, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        dalej = screen.blit(pressKariera, (1100, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                break

        if dalej.collidepoint((mx, my)):
            screen.blit(pressKariera1, (1100, 570))
            if click:
                pygame.mixer.music.stop()
                scena1()

        pisak.pisz("wers", "[ AKTA OSOBOWE ]", 30, 120, white)
        pisak.pisz("wers1", "Dane funkcjonariusza :", 30, 150, white)
        text2 = myFont.render(imieGracza, 1, white)
        screen.blit(text2, (280, 150))
        pisak.pisz("wers3", "Stopień : Posterunkowy", 30, 180, white)
        screen.blit(post, (30, 210))
        pisak.pisz("wers4", "Data i miejsce urodzenia : 26.05.1988r Warszawa", 30, 340, white)
        pisak.pisz("wers5", "Postępowanie kwalifikacyjne : POZYTYWNIE", 30, 370, white)
        pisak.pisz("wers6", "Ankieta bezpieczeństwa : POZYTYWNIE", 30, 400, white)
        pisak.pisz("wers7", "Przydział : (brak) *kurs podstawowy od 06 października 2008r.", 30, 430, white)
        pisak.pisz("wers8", "NUMER ODZNAKI : 997187", 30, 460, white)
        pisak.pisz("wers9", "**Posterunkowy(-a)! Jeśli jesteś gotowy(-a) na szkolenie, naciśnij 'Kariera'**",
                   260, 500, dyellow)
        screen.blit(odznaka, (40, 490))
        
        pygame.display.update()
        mainClock.tick()

# Scena 1


def scena1():
    siren.play(-1)
    running = True
    while running:
        click = False
        
        screen.fill(black)
        screen.blit(wspol, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena2()

        pisak.pisz("wers", "Pierwszy dzień w nowym środowisku - czujesz ekscytację! Jest trochę dziwnie ale wkońcu"
                           " nałożyłeś(-aś) mundur.", 30, 150, white)
        pisak.pisz("wers1", "Wychodzisz na pierwszy apel przed budynkiem akademika nr 1. Kręcisz się a z Tobą pozostałe"
                            " 100 osób..", 30, 180, white)
        pisak.pisz("wers2", "Obok usłyszałeś(-aś), że na mundur który obecnie nosisz, mówi się potocznie..",
                   30, 210, white)
        pisak.pisz("wers3", "Narazie nie wiesz czy będziesz w klasie czy w grupie.. Właściwie to nic nie wiesz..",
                   30, 240, white)
        pisak.pisz("wers4", "K**** - myślisz sobie. - Co ja tu będę robić 6 miesięcy. Stoisz w 3 osobowej"
                            " 'niby grupie'", 30, 270, white)
        pisak.pisz("wers5", "z osobami z Twojego pokoju. Robi się jakieś zamieszanie, ktoś zaczyna krzyczeć z tłumu"
                            " - ktoś mówi, że to dowódca.", 30, 300, white)
        pisak.pisz("wers6", "Jeszcze go nie widzisz ale wyraźniej słyszysz jak krzyczy - Zbiórka! W dwuszeregu"
                            " zbiórka!", 30, 330, white)
        pisak.pisz("wers7", "Stajesz w drugim rzędzie za wielkim, rosłym mężczyzną. W sumie jest dobrze, jesteś"
                            " mniej widoczny(-a).", 30, 360, white)
        pisak.pisz("wers8", "- Kolejno odlicz! - krzyknął dowódca", 30, 390, white)
        pisak.pisz("wers9", "- 1, 2, 3, 4, 5 ,6 - i tak 10 razy bo ktoś się pomylił, ktoś spóźnił. Gdzie ja jestem?!"
                            " - myślisz.", 30, 420, white)
        pisak.pisz("wers10", "Po 15 minutach wkońcu idziecie na stołówkę - Nareszcie! Bo od wczorajszego obiadu nic"
                             " nie jadłeś(-aś)", 30, 450, white)
        pisak.pisz("wers11", "Uśmiech jednak szybko znika Ci z Twarzy.. bo kolejka ma chyba ze 100 metrów"
                             " - wzdychasz głęboko.", 30, 480, white)
        pisak.pisz("wers12", "**Możesz najechać myszką na słowa na niebieskim tle i podejrzeć co się tam"
                             " kryje.", 30, 580, dyellow)

        akademikPoj = screen.blit(akademik, (510, 177))
        mundurx = screen.blit(czarnuch, (885, 212))

        if mundurx.collidepoint((mx, my)):
            screen.blit(czarnuch1, (895, 230))

        if akademikPoj.collidepoint((mx, my)):
            screen.blit(akademik1, (500, 195))

        pygame.display.update()
        mainClock.tick()

# Scena 2


def scena2():
    running = True
    while running:
        click = False
        
        screen.fill(black)
        screen.blit(wspol, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena3()

        pisak.pisz("wers", "Po śniadaniu był dzień zapoznawczy - zapoznajesz się właściwie z nowym miejscem, "
                           "sytuacją i ludźmi.", 30, 150, white)
        pisak.pisz("wers1", "Nie będziesz w żadnej klasie czy grupie - Twoja grupa ma ok 20 osób i nazywa się"
                            " 'plutonem'.", 30, 180, white)
        pisak.pisz("wers2", "W ciągu dnia dowiedziałeś(-aś) się, że codziennie o 6 rano jest pobudka a po niej"
                            " około 30 minut biegania,", 30, 210, white)
        pisak.pisz("wers3", "skakania, pompek, rozciągania.. Dowódca kilkakrotnie zaznaczył, że taka pobudka"
                            " nazywa się - 'zaprawą'.", 30, 240, white)
        pisak.pisz("wers4", "Wyznaczyliście dowódce plutonu - szczupły, wysoki chłopak o sylwetce zgarbionego"
                            " koszykarza - Jacka Wilczka.", 30, 270, white)
        pisak.pisz("wers5", "Zapisałeś(-aś) sobie numer komórki Jacka w swoim telefonie, bo myślisz, że może"
                            " Ci się kiedyś przyda.", 30, 300, white)
        pisak.pisz("wers6", "Zresztą.. wszyscy zapisywali to i Ty - A jak jednak będzie do czegoś potrzebny?"
                            " - zastanawiasz się.", 30, 330, white)
        pisak.pisz("wers7", "Warunki jednak trochę Cię zaskakują: pokoje 4 osobowe, 1 ubikacja, brak telewizora,"
                            " jedna mała szafeczka przy", 30, 360, white)
        pisak.pisz("wers8", "małowygodnym łóżku z lekko dźwięcznymi sprężynami przy siadaniu, 1 szafa.. Gdzie"
                            " pomieścić ubrania?", 30, 390, white)
        pisak.pisz("wers9", "Masz ochotę na coś słodkiego ale nie można wyjść do sklepu, bo potrzebujesz przepustki"
                            " - bez tego nie", 30, 420, white)
        pisak.pisz("wers10", "możesz wyjść za teren szkoły. - Boże co tu robić?! - Nawet spacerować od tak sobie"
                             " nie można, trzeba iść", 30, 450, white)
        pisak.pisz("wers11", "w szeregu, maszerować jak w wojsku.. W myślach zaczynasz nudną rozkminę ale nagle"
                             " ktoś wchodzi do pokoju.", 30, 480, white)

        pygame.display.update()
        mainClock.tick()

# Scena 3


def scena3():
    running = True
    while running:
        click = False
        
        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena4()

        pisak.pisz("wers", "Do Twojego pokoju wchodzi pewny siebie gość, który dziarsko się wita i zaczyna"
                           " rozmowę.", 30, 150, white)
        pisak.pisz("wers1", "- No co tam? Jesteście nową kompanią z wczoraj? - nikt z was nie odpowiada a on"
                            " kontynuuje.", 30, 180, white)
        pisak.pisz("wers2", "- Korzystajcie z wolnego bo w następnym tygodniu zaczną się zaliczenia a za 2 tyg."
                            " egzaminy.", 30, 210, white)
        pisak.pisz("wers3", "Masz wrażenie, że gość wydaje się nadpobudliwy ale jego gadaniem zaczynasz lekko"
                            " się stresować,", 30, 240, white)
        pisak.pisz("wers4", "może nie tym, jak mówi ale co mówi.. - Egzaminy? - myślisz i po chwili zadajesz to"
                            " samo pytanie głośno.", 30, 270, white)
        pisak.pisz("wers5", "- No tak egzaminy zaliczeniowe przedmiotów, a co myśleliście, że egzaminy są dopiero"
                            " po 6 miesiącach?", 30, 300, white)
        pisak.pisz("wers6", "- No nie wiem - odpowiadasz, a chłopak kontynuuje - Tu takich egzaminów jest tyle,"
                            " że będziecie mieli", 30, 330, white)
        pisak.pisz("wers7", "po 3-4 w tygodniu, czasem 2-3 dziennie a jak nie zaliczysz to masz jeszcze egzaminy"
                            " poprawkowe.", 30, 360, white)
        pisak.pisz("wers8", "a jak tego poprawkowego nie zdasz to masz komisję, a u nas w tamtym tygodniu 2 osoby"
                            " nie zaliczyły..", 30, 390, white)
        pisak.pisz("wers9", "- Nie zaliczyły? - pytasz trochę bardziej przejęty(-a) - No tak i wyleciały z całego"
                            " kursu.", 30, 420, white)
        pisak.pisz("wers10", "- No dobra to trzymajcie się i korzystajcie z wolnego bo niebawem się zacznie -"
                             " pokiwał głową i wyszedł.", 30, 450, white)
        pisak.pisz("wers11", "- Co to był za koleś? - powiedział Tomek, który wstał z łóżka obok. - Nie wiem -"
                             " odpowiedziała Anka,", 30, 480, white)
        pisak.pisz("wers12", "odkładając swój telefon na łóżko. - A właśnie, skąd jesteście? - zapytała Iwona,"
                             " 3 kompan pokoju.", 30, 510, white)
        pisak.pisz("wers13", "** Wieczór minął miło, rozmawialiście do późna, pomyślałeś(-aś), że masz całkiem"
                             " fajne osoby w pokoju.", 30, 540, white)

        pygame.display.update()
        mainClock.tick()

# Scena 4


def scena4():
    running = True
    while running:
        click = False
        
        screen.fill(black)
        screen.blit(strzelnica, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena5()
        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        pisak.pisz("wers", "No w końcu! Dziś miałeś(-aś) bardzo ciekawe zajęcia na strzelnicy! Nie było jeszcze"
                           " strzelania ale..", 30, 150, white)
        pisak.pisz("wers1", "widziałeś(-aś) i trzymałeś(-aś) prawdziwą broń! Było dużo na temat zachowania się"
                            " na strzelnicy", 30, 180, white)
        pisak.pisz("wers2", "zasad i budowy broni. Często rozkładałeś(-aś) i składałeś(-aś) pistolet P99"
                            " 'Walther'.", 30, 210, white)
        pisak.pisz("wers3", "Na kolejnych zajęciach masz mieć sprawdzian, dlatego zrobiłeś(-aś) notatki."
                            " (Sprawdź notatnik)", 30, 240, white)
        pisak.pisz("wers4", "Po strzelnicy, było kilka godzin chodzenia po placu, chodziliście, maszerowaliście"
                            " - nogi włażą w dupę.", 30, 270, white)
        pisak.pisz("wers5", "Narazie jest spokojnie. I gdzie te egzaminy o których wspominał chłopak, który"
                            " nawiedził Twój pokój?", 30, 300, white)
        pisak.pisz("wers6", "- Oby tak dalej i do przodu - myślisz sobie - Z egzaminami jak będą, też sobie"
                            " poradzę!.", 30, 330, white)
        pisak.pisz("wers7", "Dzień - oprócz ciekawej strzelnicy - minał na zajęciach z musztry i oddawania"
                            " honorów.", 30, 360, white)
        pisak.pisz("wers8", "W rozpisce zajęć zobaczyłeś(-aś), że jeszcze przez 2 tygodnie będzie sporo"
                            " maszerowania ale..", 30, 390, white)
        pisak.pisz("wers9", "w następnym tygodniu są jakieś zajęcia z prawa karnego i wykroczeń - Hmm, zobaczymy"
                            " o czym będą.", 30, 420, white)
        pisak.pisz("wers10", "Od Tomka dowiadujesz się, że w weekend wszyscy mogą jechać do domu.",
                   30, 450, white)
        pisak.pisz("wers11", "- Spoko! W końcu mogę spotkać się ze znajomymi i poopowiadać jak to jest w"
                             " szkole policyjnej.", 30, 480, white)
        pisak.pisz("wers12", "Narazie jest fajnie, wkurzają tylko te poranne zaprawy, wczoraj rano było tylko"
                             " 2'C a musieliście ", 30, 510, white)
        pisak.pisz("wers13", "biegać po podwórku kilka okrążeń.. Ale to nic, może ciut schudnę? :)", 30, 540, white)

        spluwa = screen.blit(p99, (819, 211))

        if spluwa.collidepoint((mx, my)):
            screen.blit(p991, (820, 238))

        pygame.display.update()
        mainClock.tick(60)

# Scena 5


def scena5():
    running = True
    while running:
        click = False
        
        screen.fill(black)
        screen.blit(wspol, (0, 0))
        buttonNie = screen.blit(nie, (470, 600))
        buttonTak = screen.blit(tak, (660, 600))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if buttonNie.collidepoint((mx, my)):
            screen.blit(nie1, (470, 600))
            if click:
                loadingSound.play()
                scena_prog()
                
        if buttonTak.collidepoint((mx, my)):
            screen.blit(tak1, (660, 600))
            if click:
                loadingSound.play()
                silownia()

        pisak.pisz("wers", "No i po weekendzie. Najfajniejsze z weekendu to.. wyjazd na weekend, bo wolny czas"
                           " tak szybko minął. ", 20, 150, white)
        pisak.pisz("wers1", "Znowu poniedziałek, 5 dni maszerowania, zapraw i chodzenia wszędzie w 2-szeregu.. ",
                   20, 180, white)
        pisak.pisz("wers2", "Z zapowiedzianego sprawdzianu z zasad na strzelnicy - nic nie było. ", 20, 210, white)
        pisak.pisz("wers3", "Prowadzący powiedział, że i tak nie ma gdzie przeprowadzić testu i zaufał nam,"
                            " że umiemy.", 20, 240, white)
        pisak.pisz("wers4", "Później były 2 godziny strzelania 'na sucho' - tj. bez pocisków. Obiad był słaby,"
                            " jakieś dziwne mięso", 20, 270, white)
        pisak.pisz("wers5", "Usłyszałeś(-aś) jak ktoś w kolejce powiedział, że dziś podają", 20, 300, white)
        pisak.pisz("wers6", "Z ciekawszych rzeczy to fajne były zajęcia poznawcze - poznawaliśmy się nawzajem.",
                   20, 330, white)
        pisak.pisz("wers7", "Nie wiem kto to prowadził, czy to jakiś policjant czy psycholog, czy może jedno i"
                            " drugie.", 20, 360, white)
        pisak.pisz("wers8", "Poprostu każdy opowiadał o sobie, mogliśmy się przez to poznać, bo jeszcze wszyscy"
                            " się nie znają.", 20, 390, white)
        pisak.pisz("wers9", "Teraz tylko przebrać się z czarnucha w swoje ubranie - swoje tzw. 'cywilki' i można"
                            " sobie odpocząć.", 20, 420, white)
        pisak.pisz("wers10", "Tomek proponuje Ci żeby iść poćwiczyć, bo na terenie szkoły jest gdzieś siłownia.",
                   20, 450, white)
        pisak.pisz("wers11", "Swoją drogą to Tomek nie próżnuje jak Ty, tylko szuka ciekawszego zajęcia jak leżenie"
                             " odłogiem w pokoju.", 20, 480, white)
        pisak.pisz("wers12", "--> Idziesz z Tomkiem na siłownię ?", 20, 530, dyellow)

        kulka = screen.blit(kulkamocy, (700, 298))

        if kulka.collidepoint((mx, my)):
            screen.blit(kulkamocy1, (800, 320))

        pygame.display.update()
        mainClock.tick(60)

# Siłownia


def silownia():
    siren.stop()
    silowniaOGG.play(-1)
    running = True
    while running:
        click = False

        global pendrive1
        pendrive1 = "testyTomka"

        screen.fill(black)
        screen.blit(silka, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena_prog()

        pisak.pisz("wers", "Ruszyłeś(-aś) dupę, choć można było spędzić czas w pokoju.", 30, 150, white)
        pisak.pisz("wers1", "Siłownia to niewielki budynek, gdzieś na terenie szkoły, było ciemno i nie"
                            " widziałeś(-aś) jaką", 30, 180, white)
        pisak.pisz("wers2", "drogą prowadził Cię Tomek. W środku dziwny zapach, hmm wilgoć i coś jeszcze -"
                            " ćwiczy kilkanaście osób.", 30, 210, white)
        pisak.pisz("wers3", "Tomek na chwilę gdzieś wyszedł a Ty obierasz na cel jakąś wielofunkcyjną ławeczkę.",
                   30, 240, white)
        pisak.pisz("wers4", "Słyszysz jak, ktoś zwraca się do Ciebie po imieniu. Odwracasz się a na twarzy powoli"
                            " maluje Ci się uśmiech.", 30, 270, white)
        pisak.pisz("wers5", "- No co tam, i Ty tutaj? - No a jak!? - odpowiadasz zadowolony(-a). Nareszcie jakaś"
                            " znajoma morda - myślisz.", 30, 300, white)
        pisak.pisz("wers6", "Okazuje się, że spotykasz kolegę ze szkoły średniej, nie pamiętasz.. no właściwie"
                            " nie znasz jego imienia", 30, 330, white)
        pisak.pisz("wers7", "bo był w innej klasie ale kojarzysz go z widzenia bo często mieliście łączone zajęcia"
                            " WF-u.", 30, 360, white)
        pisak.pisz("wers8", "- Kurczę nie widziałem Cię wcześniej, ile czasu tutaj jesteś? - kontynuuje. -"
                            " Od 2 tygodni - odpowiadasz.", 30, 390, white)
        pisak.pisz("wers9", "- E to fajnie! Szkoda, że nie wcześniej bo mogliśmy razem dojeżdżać do szkoły."
                            " Ja za 3 tygodnie", 30, 420, white)
        pisak.pisz("wers10", "kończę już kurs. Odezwij się do mnie jutro dam Ci materiały do nauki, chyba"
                             " mam też jakieś testy..", 30, 450, white)
        pisak.pisz("wers11", "Zaje..fajnie! - myślisz sobie - Warto było iść na siłownię!. W międzyczasie"
                             " przyszedł Tomek.", 30, 480, white)
        pisak.pisz("wers12", "Twój kolega odchodząc puścił Ci oko i bezdźwięcznie powtórzył 'Odezwij się jutro'",
                   30, 510, white)
        pisak.pisz("wers13", "- To co wracamy? - zapytał Tomek. - No możemy wracać - odpowiadasz", 30, 540, white)
        pisak.pisz("wers14", "Swoją drogą, to gdzie był Tomek? Przyszedł z Tobą a nie było go na siłowni.",
                   30, 570, white)

        pygame.display.update()
        mainClock.tick(60)

# ScenaProg


def scena_prog():
    siren.stop()
    silowniaOGG.stop()
    progOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(prog, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena6()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        pisak.pisz("wers", "** Pamiętaj, że w tej grze, każda Twoja decyzja ma wpływ na dalszą fabułę.", 20, 330, white)
        pisak.pisz("wers1", "Nie oznacza to, że zawsze musisz się zgadzać na to co Cię spotyka.", 20, 360, white)
        pisak.pisz("wers2", "Jak w życiu - co byś nie zrobił i tak będzie dobrze.", 20, 390, white)
        pisak.pisz("wers3", "Poboczne wątki wzbogacają fabułę o dodatkowe historie, które mogą być pomocne w"
                            " późniejszym etapie gry.", 20, 420, white)
        pisak.pisz("wers4", "Jako młody adept otrzymujesz od szefa kompanii plecak podoficerski tzw. elewkę.",
                   20, 490, dyellow)
        pisak.pisz("wers5", "W elewce będziesz posiadać ciekawe przedmioty, które mogą Ci się do czegoś przydać.",
                   20, 520, dyellow)

        pygame.display.update()
        mainClock.tick()

# Scena 6


def scena6():
    progOGG.stop()
    siren.play(-1)
    running = True
    while running:
        click = False

        global legitymowanie
        legitymowanie = "legitymowanie"

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        buttonNie = screen.blit(nie, (470, 600))
        buttonTak = screen.blit(tak, (660, 600))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if buttonNie.collidepoint((mx, my)):
            screen.blit(nie1, (470, 600))
            if click:
                loadingSound.play()
                scena7()

        if buttonTak.collidepoint((mx, my)):
            screen.blit(tak1, (660, 600))
            if click:
                loadingSound.play()
                silownia1()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        pisak.pisz("wers", "Mijają kolejne dni, sporo zajęć, poranne zaprawy. Masz już dość kulek mocy.",
                   20, 150, white)
        pisak.pisz("wers1", "Dzisiaj były nowe zajęcia z legitymowania - czacha dymi ale zrobiłeś(-aś) notatki.",
                   20, 180, white)
        pisak.pisz("wers2", "Powoli ogarniasz osoby z Twojego plutonu - różni ludzie, w różnym wieku od 23 do 35 lat.",
                   20, 210, white)
        pisak.pisz("wers3", "Jest były piekarz, kierowca tira i nauczyciel. Jest też kilka młodych osób świeżo po"
                            " studiach.", 20, 240, white)
        pisak.pisz("wers4", "Ogólnie to nikt wcześniej się nie znał, bo każdy pochodzi z innego rejonu kraju ale..",
                   20, 270, white)
        pisak.pisz("wers5", "powoli dociera do Ciebie, że chyba jesteście podobni - to chyba ten sam cel - Policja.",
                   20, 300, white)
        pisak.pisz("wers6", "Po zajęciach Tomek znowu proponuje Ci siłownię.", 20, 330, white)
        pisak.pisz("wers7", "--> Idziesz z Tomkiem na siłownię ?", 20, 530, dyellow)

        pygame.display.update()
        mainClock.tick(60)

# Siłownia 1


def silownia1():
    siren.stop()
    silowniaOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(silka, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                silowniaOGG.stop()
                siren.play()
                loadingSound.play()
                scena7()

        pisak.pisz("wers", "Na siłowni ćwiczy kilkanaście osób.", 20, 150, white)
        pisak.pisz("wers1", "Nie widzisz nikogo znajomego.", 20, 180, white)
        pisak.pisz("wers2", "Tomek pobył z Tobą kilka minut i gdzieś się ulotnił.", 20, 210, white)
        pisak.pisz("wers3", "Wrócił po 20 minutach.", 20, 240, white)
        pisak.pisz("wers4", "Poćwiczyliście jeszcze 10 minut i wracacie razem do pokoju.", 20, 270, white)

        pygame.display.update()
        mainClock.tick(60)

# Scena 7


def scena7():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(wspol, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        # pozycja myszy-------
        mx, my = pygame.mouse.get_pos()
        # --------------------
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena8()
        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        pisak.pisz("wers", "Mijają kolejne dni.. Zajęcia trwają od 8 do 18 a po obiedzie i tak nic nie wchodzi"
                           " do głowy.", 20, 150, white)
        pisak.pisz("wers1", "Na obiad? Jak nie 'kulki mocy' to makaron z jakimś melepetum. Zamiast schudnąć przybywa"
                            " Ci 5 kg.", 20, 180, white)
        pisak.pisz("wers2", "Zaczynasz doceniać każą chwilę wolnego, którą wykorzystujesz na leżenie w łóżku.",
                   20, 210, white)
        pisak.pisz("wers3", "Po zajęciach próbujecie się uczyć w pokoju ale i tak kończy się na tym samym - na"
                            " plotkowaniu.", 20, 240, white)
        pisak.pisz("wers4", "Zaczynasz bardziej kumplować się z Anką, która pewnego dnia zadaje Ci nietypowe pytanie:",
                   20, 270, white)
        pisak.pisz("wers5", "- Słuchaj.. Ta Iwona z naszego pokoju nie wydaje Ci się dziwna? - Nie rozumiem?!"
                            " - odpowiadasz.", 20, 300, white)
        pisak.pisz("wers6", "- Wczoraj jak paliłam sobie na palarni po 20:00, to widziałam ją jak rozmawiała z"
                            " jednym wykładowcą.", 20, 330, white)
        pisak.pisz("wers7", "- No i co w tym dziwnego? - kontynuujesz - Przecież na palarniach nie obowiazują te"
                            " meldowania itd.", 20, 360, white)
        pisak.pisz("wers8", "- No tak - Anka scisza głos - ale rozmawiała z nim po imieniu, zna go, jestem na 100%"
                            " pewna", 20, 390, white)
        pisak.pisz("wers9", "Ty jednak nie wierzysz do końca w to co słyszysz, 'eee pewnie jest zazdrosna' ale po"
                            " chwili odpowiadasz.", 20, 420, white)
        pisak.pisz("wers10", "- No dobra, to jak przyjdziemy do pokoju to ją zapytamy wprost.", 20, 450, white)
        pisak.pisz("wers11", "Wracacie razem do pokoju.", 20, 480, white)

        pygame.display.update()
        mainClock.tick(60)

# Scena 8


def scena8():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena9()
        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        pisak.pisz("wers", "W pokoju zastajecie Iwonę, lekko zmieszana stoi przy szafie, po czym siada na łóżku"
                           " z telefonem.", 20, 150, white)
        pisak.pisz("wers1", "- Iwona.. - zaczyna Anka - Słuchaj możemy Cię o coś zapytać?", 20, 180, white)
        pisak.pisz("wers2", "- O co zapytać? - odpowiedziała zmęczonym głosem Iwona podnosząc delikatnie brwi.",
                   20, 210, white)
        pisak.pisz("wers3", "Nie chcesz stać jak kołek, dlatego walisz prosto z mostu.", 20, 240, white)
        pisak.pisz("wers4", "- Wczoraj widziałem(-am) Cię na palarni z.. - Z Adamem? - dodała Iwona.", 20, 270, white)
        pisak.pisz("wers5", "- Z wykładowcą - dokończyłeś(-aś). - No tak z Adamem, znam go. Znajomość to może nie"
                            " jest ale poznałam go", 20, 300, white)
        pisak.pisz("wers6", "w tamtym roku na kursie. - Na kursie?! - odpowiadasz razem z Anką. - No tak na kursie"
                            " podstawowym.", 20, 330, white)
        pisak.pisz("wers7", "- No dobrze, chyba muszę Wam coś wyjaśnić.. W międzyczasie przyszedł Tomek.",
                   20, 360, white)
        pisak.pisz("wers8", "Okazało się, że Iwona 1,5 roku temu musiała zakończyć kurs z powodów rodzinnych.",
                   20, 390, white)
        pisak.pisz("wers9", "Jej były, chorobliwie zazdrosny facet, nie mógł znieść, że jego kobieta może być"
                            " policjantem.", 20, 420, white)
        pisak.pisz("wers10", "Tak jej wjeżdżał na psychę podczas powrotów do domu, że zbierała się do kupy przez"
                             " kolejne dni szkoły.", 20, 450, white)
        pisak.pisz("wers11", "W końcu zrezygnowała i wróciła do matki. Teraz jest przekonana, że już się pozbierała,"
                             " dlatego spróbowała ponownie.", 20, 480, white)
        pisak.pisz("wers12", "Zrobiło Wam się żal koleżanki i trochę głupio. Masz wrażenie, że zmusiłes(-aś) ją"
                             " do bolesnego wyznania.", 20, 510, white)

        pygame.display.update()
        mainClock.tick(60)

# Scena 9


def scena9():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena10()
        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        pisak.pisz("wers", "Kolejnego dnia Wasz pokój ma 'rejony' to tzw. sprzątanie wyznaczonego miejsca.",
                   20, 150, white)
        pisak.pisz("wers1", "Ogarniacie cały korytarz na I piętrze swojego akademika. Wiadra, szmaty, ścierki"
                            " i do roboty!", 20, 180, white)
        pisak.pisz("wers2", "Sprzątacie i narzekacie: po co, komu, a co tu nie ma sprzątaczek, itd.",
                   20, 210, white)
        pisak.pisz("wers3", "Jednak dociera do Was, że przecież jesteście skoszarowaną formacją mundurową.",
                   20, 240, white)
        pisak.pisz("wers4", "Iwona zasuwa i nie narzeka, Anka uwija się jak mucha w smole i przewodzi w"
                            " narzekaniu.", 20, 270, white)
        pisak.pisz("wers5", "Ty jedziesz na mopie a Tomek? Tomek-śmieszek podjudza Ankę, która jeszcze"
                            " bardziej się nakręca", 20, 300, white)
        pisak.pisz("wers6", "i co chwilę wymyśla powody dla których Wasza praca nie ma sensu.", 20, 330, white)
        pisak.pisz("wers7", "Po skończonych rejonach korytarz lśni aż miło. Jesteście dumni z pracy którą"
                            " wykonaliście ale..", 20, 360, white)
        pisak.pisz("wers8", "to, że Wam się podoba to nic. Waszą robotę ma ocenić szef kompanii..", 20, 390, white)
        pisak.pisz("wers9", "Po kilku minutach przyszedł szef. Szefem jest 32 letni, niewielki grubcio w stopniu"
                            " sierżanta sztabowego.", 20, 420, white)
        pisak.pisz("wers10", "Od 7 lat szefuje to na jednym to na drugim akademiku. Przeszedł się po całym korytarzu,"
                             " kręcił nosem,", 20, 450, white)
        pisak.pisz("wers11", "widać było, że średnio mu się podoba Wasza praca i już miał coś powiedzieć ale spojrzał"
                             " na Iwonę, uśmiechnął się", 20, 480, white)
        pisak.pisz("wers12", "i stwierdził, że w sumie to może być. - Uff pewnie poznał ją z poprzedniego kursu"
                             " - pomyślałeś(-aś).", 20, 510, white)

        pygame.display.update()
        mainClock.tick(60)

# Scena 10


def scena10():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                egzamin_leg()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        pisak.pisz("wers", "Minął weekend.. Kurde.. powroty są fajne.. ale najfajniejsze są - wyjazdy na powroty"
                           " do domu..", 20, 150, white)
        pisak.pisz("wers1", "Po kompanii chodzi plotka, że jutro wszystkie plutony mają 'niezapowiedzianą' wejściówkę"
                            " z legitymowania.", 20, 180, white)
        pisak.pisz("wers2", "Wejściówka czyli kartkówka. O kurdę nic się nie uczyłeś(-aś) w weekend!", 20, 210, white)
        pisak.pisz("wers3", "Chyba warto sobie przypomnieć co ostatnio było na zajęciach..", 20, 240, white)

        pygame.display.update()
        mainClock.tick(60)

# Egzamin z legitymowania ---------------
# Pytanie 1


def egzamin_leg():
    siren.stop()
    szum.play(-1)
    running = True
    while running:
        global odp1
        click = False

        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))

        pisak.pisz("wers", "Czemu służy legitymowanie?", 450, 100, red)
        pisak.pisz("wers1", "Żeby potwierdzić tożsamość osoby", 450, 130, white)
        pisak.pisz("wers2", "Żeby wykazać, że coś robię na służbie", 450, 190, white)
        pisak.pisz("wers3", "Legitymowanie jest zbędne, służy statystyce", 450, 250, white)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp1:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp1 = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp1 = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp1 = "c"

        if odp1:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_leg2()
        pygame.display.update()
        mainClock.tick(60)

# Pytanie 2----------------------


def egzamin_leg2():
    running = True
    while running:
        global odp2
        click = False

        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))

        pisak.pisz("wers", "Przy legitymowaniu warto zachować..", 450, 100, red)
        pisak.pisz("wers1", "Kółko bezpieczeństwa", 450, 130, white)
        pisak.pisz("wers2", "Trójkąt bezpieczeństwa", 450, 190, white)
        pisak.pisz("wers3", "pół litra na czarną godzinę", 450, 250, white)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        if not odp2:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp2 = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp2 = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp2 = "c"

        if odp2:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_leg3()
        pygame.display.update()
        mainClock.tick(60)

# Pytanie 3----------------------


def egzamin_leg3():
    running = True
    while running:
        global odp3
        click = False

        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))

        pisak.pisz("wers", "Podstawą prawną legitymowania jest:", 450, 100, red)
        pisak.pisz("wers1", "Moje widzi mi się", 450, 130, white)
        pisak.pisz("wers2", "art. 515 Ustawy o broni i amunicji", 450, 190, white)
        pisak.pisz("wers3", "art. 15 Ustawy o Policji", 450, 250, white)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp3:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp3 = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp3 = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp3 = "c"

        if odp3:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_leg4()

        pygame.display.update()
        mainClock.tick(60)

# Pytanie 4----------------------


def egzamin_leg4():
    running = True
    while running:
        global odp4
        click = False

        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))
        pisak.pisz("wers", "W przypadku odmowy okazania dokumentu tożsamości, ma zastasowanie:", 450, 100, red)
        pisak.pisz("wers1", "art.65 par. 2 Kodeksu Wykroczeń", 450, 130, white)
        pisak.pisz("wers2", "Pałka służbowa", 450, 190, white)
        pisak.pisz("wers3", "art. 15 Ustawy o Policji", 450, 250, white)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp4:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp4 = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp4 = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp4 = "c"

        if odp4:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    wyniki_leg()
        pygame.display.update()
        mainClock.tick(60)

# Wyniki z legitymowania


def wyniki_leg():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                siren.stop()
                loadingSound.play()
                scena_prog1()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()
        pisak.pisz("wersX", imieGracza, 600, 220, white)
        pisak.pisz("wers", "Twoja ocena z testu LEGITYMOWANIA!", 450, 250, white)

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

        global ocena, ocenaSTR
        ocena = jeden + odp1x + odp2x + odp3x + odp4x
        ocenaSTR = str(ocena)

        try:
            if ocena == 5:
                pisak.pisz("wers1", "Gratulacje kujonie! Dostałeś 5!", 450, 510, dyellow)
                screen.blit(cyfra5, (580, 300))
            if ocena == 4:
                pisak.pisz("wers2", "Całkiem, całkiem. Dostałeś 4!", 450, 510, dyellow)
                screen.blit(cyfra4, (580, 300))
            if ocena == 3:
                pisak.pisz("wers3", "Mogło pójść lepiej.. Tylko 3?", 450, 510, dyellow)
                screen.blit(cyfra3, (580, 300))
            if ocena == 2:
                pisak.pisz("wers4", "Jak chcesz skończyć kurs to weź się do nauki miernoto. Dostałeś(-aś) 2!",
                           250, 510, dyellow)
                screen.blit(cyfra2, (580, 300))
            if ocena == 1:
                pisak.pisz("wers5", "Głowa pusta jak kapusta. Dostałeś pałę..", 400, 510, dyellow)
                screen.blit(cyfra1, (580, 300))
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
        screen.blit(prog, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                progOGG.stop()
                loadingSound.play()
                scena11()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        pisak.pisz("wers", "Jako młody adept otrzymujesz od szefa kompanii indeks!", 20, 490, dyellow)
        pisak.pisz("wers1", "W indeksie znajduje się spis przedmiotów do zaliczenia i Twoje dotychczasowe oceny.",
                   20, 520, dyellow)

        pygame.display.update()
        mainClock.tick(60)

# Scena 11


def scena11():
    siren.play()
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        buttonNie = screen.blit(nie, (470, 600))
        buttonTak = screen.blit(tak, (660, 600))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if buttonNie.collidepoint((mx, my)):
            screen.blit(nie1, (470, 600))
            if click:
                loadingSound.play()
                scena12()

        if buttonTak.collidepoint((mx, my)):
            screen.blit(tak1, (660, 600))
            if click:
                siren.stop()
                loadingSound.play()
                bar()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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
        pisak.pisz("wers6", "--> Idziesz na piwo?", 520, 530, dyellow)

        celaBar = screen.blit(cela, (627, 302))

        if celaBar.collidepoint((mx, my)):
            screen.blit(cela1, (630, 320))

        pygame.display.update()
        mainClock.tick()

# Bar


def bar():
    barSound.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(barBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
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

        pygame.display.update()
        mainClock.tick()

# Bar1


def bar1():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(barBG, (0, 0))
        buttonNie = screen.blit(nie, (470, 600))
        buttonTak = screen.blit(tak, (660, 600))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if buttonNie.collidepoint((mx, my)):
            screen.blit(nie1, (470, 600))
            if click:
                loadingSound.play()
                scena_bar_iwona()

        if buttonTak.collidepoint((mx, my)):
            screen.blit(tak1, (660, 600))
            if click:
                loadingSound.play()
                bar2()

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
        pisak.pisz("wers10", "--> Zostajesz jeszcze chwilę?", 20, 550, dyellow)

        wodkaPoj = screen.blit(wodka, (880, 210))
        if wodkaPoj.collidepoint((mx, my)):
            screen.blit(wodka1, (1000, 210))

        pygame.display.update()
        mainClock.tick(60)

# Bar2 + info do questu Tomka


def bar2():
    running = True
    global quest_tomek_1
    while running:
        click = False

        quest_tomek_1 = "personel"

        screen.fill(black)
        screen.blit(barBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
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

        pygame.display.update()
        mainClock.tick(60)

# ScenaBarIwona


def scena_bar_iwona():
    siren.stop()
    barSound.stop()
    siren.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokojnocBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
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
    siren.stop()
    barSound.stop()
    siren.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena13()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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

        pygame.display.update()
        mainClock.tick(60)

# Scena13


def scena13():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(odprawaBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena14()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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
    siren.stop()
    korytarzSound.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(korytarzBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena15()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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

        planPoj = screen.blit(plan, (776, 236))

        if planPoj.collidepoint((mx, my)):
            screen.blit(plan1, (600, 255))

        pygame.display.update()
        mainClock.tick(60)

# Scena15


def scena15():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(korytarzBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scenaSciana()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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

        falklandyPoj = screen.blit(falklandy, (875, 446))
        if falklandyPoj.collidepoint((mx, my)):
            screen.blit(falklandy1, (500, 200))

        pygame.display.update()
        mainClock.tick()

# Scena15


def scenaSciana():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(korytarzNOC, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scenaProg2()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        pisak.pisz("wers0", "Jeden z obrazów, przykuwa Twoją uwagę. (Najedź myszką)", 20, 120, white)
        pisak.pisz("wers", "Ta kobieta jest jakaś.. ", 20, 150, white)
        pisak.pisz("wers1", "Obserwujesz jeszcze chwilę i wracasz do siebie. ", 20, 210, white)

        obrazStary = screen.blit(staryObraz, (334, 273))
        if obrazStary.collidepoint((mx, my)):
            screen.blit(staryObraz1, (450, 50))

        screen.blit(oko, (mx, my))
        pygame.display.update()
        mainClock.tick()

# SCENA PROG1


def scenaProg2():
    korytarzSound.stop()
    progOGG.play()
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(prog, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        napisPolicjaX = screen.blit(napisPolicja, (640, 190))

        # pozycja myszy-------
        mx, my = pygame.mouse.get_pos()
        # --------------------

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                progOGG.stop()
                loadingSound.play()
                scena16()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if napisPolicjaX.collidepoint((mx, my)):
            screen.blit(napisPolicja1, (640, 250))

        pisak.pisz("wers", "Jeśli napotkasz scenę, w której przy kursorze wyświetla się oko - taki jak teraz",
                   20, 490, dyellow)
        pisak.pisz("wers1", "Bacznie obserwuj i poszukuj ciekawych przedmiotów, najeżdżając kursorem.",
                   20, 520, dyellow)
        screen.blit(oko, (mx, my))
        pygame.display.update()
        mainClock.tick()

# Scena16


def scena16():
    siren.play(-1)
    running = True
    while running:
        click = False

        global ruchdrogowy
        ruchdrogowy = "ruchdrogowy"

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

        # pozycja myszy-------
        mx, my = pygame.mouse.get_pos()
        # --------------------

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena17()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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

        cywilkiX = screen.blit(cywilki, (557, 388))
        if cywilkiX.collidepoint((mx, my)):
            screen.blit(cywilki1, (557, 428))

        pygame.display.update()
        mainClock.tick()

# Scena17


def scena17():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

        # pozycja myszy-------
        mx, my = pygame.mouse.get_pos()
        # --------------------

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena18()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

        # pozycja myszy-------
        mx, my = pygame.mouse.get_pos()
        # --------------------

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena19()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(wspol2, (0, 0))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

        wybor1 = screen.blit(silowniaN, (470, 600))
        wybor2 = screen.blit(spacerNAV, (660, 600))

        # pozycja myszy-------
        mx, my = pygame.mouse.get_pos()
        # --------------------

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if wybor1.collidepoint((mx, my)):
            screen.blit(silowniaN1, (470, 600))
            if click:
                loadingSound.play()
                silownia2()

        if wybor2.collidepoint((mx, my)):
            screen.blit(spacerNAV1, (660, 600))
            if click:
                loadingSound.play()
                spacer()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        pisak.pisz("wers", "Minęło kilka dni - kilka a każdy.. jak dzień świstaka.", 20, 120, white)
        pisak.pisz("wers1", "Zaprawa, nauka, spanie.. Zaprawa, nauka, spanie.. zajęcia to tu, to tam.. eh.. ",
                   20, 150, white)
        pisak.pisz("wers2", "W plutonie porobiły się podgrupy, które przesiadują razem po zajęciach i piją "
                            "podlaski bimber.", 20, 180, white)
        pisak.pisz("wers3", "Szkoda Ci czasu na alkohol a szukasz jakiegoś pożytecznego zajęcia.", 20, 210, white)
        pisak.pisz("wers4", "Zastanawiasz się co robić:", 20, 240, white)
        if quest_tomek_1 == "personel":
            pisak.pisz("wers5x", "1. Iść na siłownię? I może zobaczę Tomka i zagadam co robił w CELI", 20, 270, white)
        else:
            pisak.pisz("wers5", "1. Iść na siłownię?", 20, 270, white)
        pisak.pisz("wers6", "2. Iść na spacer?", 20, 300, white)
        pisak.pisz("wers7", "Jakaś część Ciebie mówi 'Rusz dupę!'", 20, 330, white)
        pisak.pisz("wers8", "--> Gdzie idziesz?", 520, 530, dyellow)

        bimberX = screen.blit(bimber, (878, 180))
        if bimberX.collidepoint((mx, my)):
            screen.blit(bimber1, (878, 208))

        pygame.display.update()
        mainClock.tick()

# Silownia2


def silownia2():
    siren.stop()
    silowniaOGG.play(-1)
    running = True
    global quest_tomek_1
    while running:
        click = False

        quest_tomek_1 = "rozmowa"

        screen.fill(black)
        screen.blit(silka, (0, 0))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena20()

        pisak.pisz("wers", "Siłownia to nie Twoje klimaty ale z nudów można poprzeciągać trochę złomu.", 20, 90, white)
        pisak.pisz("wers1", "Wchodzisz do budynku, w tle słychać dźwięki odkładanych hantli i drążków.", 20, 120, white)
        pisak.pisz("wers2", "Zaglądasz żeby rozejrzeć się czy ćwiczy ktoś znajomy. Tomka nie ma, sami obcy.",
                   20, 150, white)
        pisak.pisz("wers3", "- No jak już jestem to.. ehh.. dobra idę trochę poćwiczę, gdzie była ta szatnia",
                   20, 180, white)
        pisak.pisz("wers4", "Wchodzisz do szatni, siadasz na ławeczce, zmieniasz buty na wygodniejsze.", 20, 210, white)
        pisak.pisz("wers5", "Słyszysz z korytarza, rozmowę jakiegoś mężczyzny przez telefon:", 20, 240, white)
        pisak.pisz("wers6", "(ktoś) - Za krótko, mówiłem Ci.. To sam tu przyjedź i siedź.. Tak, jest może kilogram",
                   20, 270, white)
        pisak.pisz("wers7", "**Słyszysz tylko rozmówcę z korytarza, głos w słuchawce jest niezrozumiały.",
                   20, 300, white)
        pisak.pisz("wers8", "(ktoś) - Nie wiem, dużo.. dobra muszę kończyć bo się zczają.. ", 20, 330, white)
        pisak.pisz("wers9", "Słysząc to wbijasz tępo wzrok w szafkę - O k**** jak w filmie! - myślisz", 20, 360, white)
        pisak.pisz("wers10", "Co robić? Podpierdolić dla dowódcy czy robić własne przeszpiegi?", 20, 390, white)
        pisak.pisz("wers11", "Kilogram? Pewnie chodzi o narkotyki albo koks, napewno nie kartofle.", 20, 420, white)
        pisak.pisz("wers12", "Słyszysz jak ktoś chodzi po korytarzu - O fak! Teraz nie wychodzę.. - siedzisz cicho.",
                   20, 450, white)
        pisak.pisz("wers13", "Zobaczy mnie i.. no i nie wiem co.. lipa będzie no.. jak nie dostanę po gębie..",
                   20, 480, white)
        pisak.pisz("wers14", "To mnie zastraszą.. Albo.. k****.. a może wyjść jakby nigdy nic? Powiem cześć. "
                             "Chwila.. o cicho jest", 20, 510, white)
        pisak.pisz("wers15", " *Zbierasz się nie zmieniając butów i wracasz prędko do akademika.", 20, 540, white)

        pygame.display.update()
        mainClock.tick()

# Spacer


def spacer():
    siren.stop()
    spacerOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(szczytno_nocBG, (0, 0))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                spacer1()

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

        ogorkowX = screen.blit(ogorkow, (577, 177))
        if ogorkowX.collidepoint((mx, my)):
            screen.blit(ogorkow1, (577, 210))

        pygame.display.update()
        mainClock.tick()

# Spacer1


def spacer1():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(szczytno_nocBG, (0, 0))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena20()

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
    spacerOGG.stop()
    silowniaOGG.stop()
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokojnocBG, (0, 0))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena21()

        pisak.pisz("wers", "Wchodzisz do pokoju. Iwona rozmawia z Anką o jutrzejszych zajęciach na strzelnicy.",
                   30, 120, white)
        pisak.pisz("wers1", "Tomek bierze prysznic. Nie chwalisz się nikomu o tym co Cię spotkało.", 30, 150, white)
        pisak.pisz("wers2", "Kładziesz się i idziesz spać.", 30, 180, white)

        pygame.display.update()
        mainClock.tick()


def scena21():
    strzelnicaOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(strzelnica1, (0, 0))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                strzelnicaScena1()

        pisak.pisz("wers", "Nowy dzionek zapowiada się całkiem przyzwoicie. Będziesz strzelać na strzelnicy.",
                   30, 150, white)
        pisak.pisz("wers1", "Z prawdziwych nabojów!", 30, 180, white)
        pisak.pisz("wers2", "Czujesz stresik.. ", 30, 210, white)
        pisak.pisz("wers3", "Prowadzący zajęcia policjant tłumaczy zasady strzelania:", 30, 240, white)
        pisak.pisz("wers4", "1.Macie 50 naboi!", 30, 270, dyellow)
        pisak.pisz("wers5", "2.Celujecie w sam środek!", 30, 300, dyellow)
        pisak.pisz("wers6", ".. i zaliczacie zajęcia", 30, 330, dyellow)
        pisak.pisz("wers7", "Wchodzisz na pozycję do strzelania i ładujesz pełny magazynek", 30, 360, white)
        pisak.pisz("wers7", "Wkładasz okulary ochronne i słuchawki wygłuszające. Słyszysz stłumiony głos"
                            " prowadzącego:", 30, 390, white)
        pisak.pisz("wers7", "- Przygotować się do strzelania!", 30, 420, white)

        pygame.display.update()
        mainClock.tick()


def strzelnicaScena1():
    ox = 600 - tarcza_rect.center[0]
    oy = 200 - tarcza_rect.center[1]
    ox_move = 1
    oy_move = 1
    punkty = 0
    naboje = 50
    startx = 500
    delta = 0.0
    global blob_color, skrawek1, wynikp99
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        losowa = random.randrange(-150, 150)
        punktyStr = str(punkty)
        nabojeStr = str(naboje)
        wynikp99 = punktyStr

        screen.blit(strzelnica1, (0, 0))
        if naboje <= 0:
            tablica_wynikow.append(wynikp99)
            strzelnica1wyniki()

        if punkty > 400:
            skrawek1 = "skrawek"

        screen.blit(tabelaIMG, (5, 600))

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

        delta += mainClock.tick() / 1000.0
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

        pisak.pisz("imie", imieGracza, 50, 650, black)
        pisak.pisz("naboje", nabojeStr, 345, 650, black)
        pisak.pisz("wers2", punktyStr, 265, 650, black)

        pygame.display.update()

# Strzelnica1 Wyniki


def strzelnica1wyniki():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(wynikiBG, (260, 10))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena22()

        pisak.pisz("wers1", tablica_wynikow[0], 730, 238, black)
        pisak.pisz("wers2", imieGracza, 460, 60, black)
        pygame.display.update()
        mainClock.tick()

# Scena22


def scena22():
    strzelnicaOGG.stop()
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                egzamin_ruch()

        pisak.pisz("wers", "Pierwsze strzelanie za Tobą! Polubiłeś(-aś) to..  odgłosy strzałów, spadających łusek,"
                           " zapach prochu.", 20, 90, white)
        pisak.pisz("wers1", "Robi się fajniej, bo wykładowcy trochę odpuścili upierdliwość ale.. nie ma nic za darmo.",
                   20, 120, white)
        pisak.pisz("wers2", "Jutro masz sprawdzian z ruchu drogowego i wypadałoby coś się pouczyć.", 20, 150, white)
        if skrawek1 == "skrawek":
            pisak.pisz("wers3", "*Miałeś(-aś) dobry wynik, ze strzelania. Powyżej 400 to już sokole oko!",
                       20, 180, green)
            pisak.pisz("wers4", "*Prowadzący powiedział, że szkoda zmarnować taki talent i przekazał Ci małą"
                                " podpowiedź.", 20, 210, green)
            pisak.pisz("wers5", "*Podpowiedź znajdziesz w plecaku.", 20, 240, green)

        pygame.display.update()
        mainClock.tick()

# Egzamin z ruchu drogowego ---------------
# Pytanie 1


def egzamin_ruch():
    szum.play(-1)
    running = True
    while running:
        global odp1_ruch
        click = False

        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))

        pisak.pisz("wers", "Podstawowa zasada ruchu to..?", 450, 100, red)
        pisak.pisz("wers1", "Ruch prawostronny", 450, 130, white)
        pisak.pisz("wers2", "Unikanie kolizji", 450, 190, white)
        pisak.pisz("wers3", "Jazda na podwójnym gazie", 450, 250, white)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        if not odp1_ruch:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp1_ruch = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp1_ruch = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp1_ruch = "c"

        if odp1_ruch:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_ruch2()

        pygame.display.update()
        mainClock.tick()

# Pytanie 2----------------------


def egzamin_ruch2():
    running = True
    while running:
        global odp2_ruch
        click = False

        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))

        pisak.pisz("wers", "W jakim dokumencie w Polsce, określono zasady ruchu drogowego?", 450, 100, red)
        pisak.pisz("wers1", "w Ustawie 'Prawo o ruchu drogowym'", 450, 130, white)
        pisak.pisz("wers2", "w tygodniku 'AutoSzrot'", 450, 190, white)
        pisak.pisz("wers3", "w Konstytucji RP", 450, 250, white)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if not odp2_ruch:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp2_ruch = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp2_ruch = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp2_ruch = "c"

        if odp2_ruch:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_ruch3()
        pygame.display.update()
        mainClock.tick(60)

# Pytanie 3----------------------


def egzamin_ruch3():
    running = True
    while running:
        global odp3_ruch
        click = False
        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))
        pisak.pisz("wers", "Z jaką prędkością można jechać w strefie zamieszkania?", 450, 100, red)
        pisak.pisz("wers1", "20 km\\h", 450, 130, white)
        pisak.pisz("wers2", "30 km\\h", 450, 190, white)
        pisak.pisz("wers3", "8 km\\h", 450, 250, white)
        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
   
        if not odp3_ruch:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp3_ruch = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp3_ruch = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp3_ruch = "c"

        if odp3_ruch:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_ruch4()

        pygame.display.update()
        mainClock.tick(60)

# Pytanie 4----------------------


def egzamin_ruch4():
    running = True
    while running:
        global odp4_ruch
        click = False
        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))
        pisak.pisz("wers", "Podstawowa klasyfikacja pojazdów to:", 450, 100, red)
        pisak.pisz("wers1", "Silnikowe i łańcuchowe", 450, 130, white)
        pisak.pisz("wers2", "Mechaniczne i niemechaniczne", 450, 190, white)
        pisak.pisz("wers3", "Osobowe i dostawcze", 450, 250, white)

        events = pygame.event.get()
        mx, my = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        if not odp4_ruch:
            pisak.pisz("wers4", "Wybierz 'a' , 'b' lub 'c'", 455, 520, red)

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp4_ruch = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp4_ruch = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp4_ruch = "c"

        if odp4_ruch:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    wyniki_ruch()

        pygame.display.update()
        mainClock.tick(60)

# Wyniki z legitymowania


def wyniki_ruch():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        tornister = screen.blit(plecak, (200, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                siren.stop()
                loadingSound.play()
                scena23()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()
        pisak.pisz("wersX", imieGracza, 600, 220, white)
        pisak.pisz("wers", "Twoja ocena z testu RUCH DROGOWY!", 450, 250, white)

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

        global ocena_ruch, ocena_ruchSTR
        ocena_ruch = jeden + odp1x + odp2x + odp3x + odp4x
        ocena_ruchSTR = str(ocena_ruch)

        try:
            if ocena_ruch == 5:
                pisak.pisz("wers1", "Gratulacje kujonie! Dostałeś 5!", 450, 510, dyellow)
                screen.blit(cyfra5, (580, 300))
            if ocena_ruch == 4:
                pisak.pisz("wers2", "Całkiem, całkiem. Dostałeś 4!", 450, 510, dyellow)
                screen.blit(cyfra4, (580, 300))
            if ocena_ruch == 3:
                pisak.pisz("wers3", "Mogło pójść lepiej.. Tylko 3?", 450, 510, dyellow)
                screen.blit(cyfra3, (580, 300))
            if ocena_ruch == 2:
                pisak.pisz("wers4", "Jak chcesz skończyć kurs to weź się do nauki miernoto. Dostałeś(-aś) 2!",
                           250, 510, dyellow)
                screen.blit(cyfra2, (580, 300))
            if ocena_ruch == 1:
                pisak.pisz("wers5", "Głowa pusta jak kapusta. Dostałeś pałę..", 400, 510, dyellow)
                screen.blit(cyfra1, (580, 300))
        except ValueError:
            pisak.pisz("wersX", "Jeśli to widzisz - to jest to nieoczekiwany błąd gry (Zgłoś mi to)", 300, 510, red)

        pygame.display.update()
        mainClock.tick(60)


# Scena23


def scena23():
    szum.stop()
    siren.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokojnocBG, (0, 0))
        buttonNie = screen.blit(cela_nav, (470, 600))
        buttonTak = screen.blit(miasto, (660, 600))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if buttonNie.collidepoint((mx, my)):
            screen.blit(cela1_nav, (470, 600))
            if click:
                scena_cela()

        if buttonTak.collidepoint((mx, my)):
            screen.blit(miasto1, (660, 600))
            if click:
                scena_miasto()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        pisak.pisz("wers", "Drugi sprawdzian za Tobą. Z tego co widać w indeksie, to pozostały jeszcze dwa do"
                           " egzaminu końcowego", 30, 120, white)
        pisak.pisz("wers1", "Na odstresowanie Tomek proponuje by wyjść na jakieś piwko. ", 30, 150, white)
        pisak.pisz("wers2", "Anka z Iwoną, chcą iść na miasto. Tomek naciska by wyjść do CELI.", 30, 180, white)
        if quest_tomek_1 == "rozmowa":
            pisak.pisz("wers3", "*Znowu CELA? No tak, wychodził kiedyś z drzwi dla personelu.", 30, 210, green)
            pisak.pisz("wers4", "*Może dowiem się czegoś więcej o tym miejscu.", 30, 240, green)
        pisak.pisz("wers6", "--> To gdzie idziemy?", 520, 530, dyellow)

        pygame.display.update()
        mainClock.tick()

# Scena_CELA


def scena_cela():
    siren.stop()
    barSound.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(barBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena_cela2()

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
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(barBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena24()

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
    siren.stop()
    spacerOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(szczytno_nocBG, (0, 0))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena24()

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
    siren.play(-1)
    spacerOGG.stop()
    barSound.stop()
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scenaProg3()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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

# SCENA PROG3 - SAVE


def scenaProg3():
    siren.stop()
    saveOGG.play(-1)
    running = True
    global zapis
    while running:
        click = False

        screen.fill(black)
        screen.blit(prog, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        zapiszX = screen.blit(zapisz, (570, 600))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                saveOGG.stop()
                loadingSound.play()
                scena25()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if zapiszX.collidepoint((mx, my)):
            screen.blit(zapisz1, (570, 600))
            if click:
                loadingSound.play()
                save_file = open("data\\save\\save.txt", "w+")
                save_file.write(imieGracza)
                save_file.write("\n")
                save_file.write(legitymowanie)
                save_file.write("\n")
                save_file.write(ruchdrogowy)
                save_file.write("\n")
                save_file.write(pendrive1)
                save_file.write("\n")
                save_file.write(skrawek1)
                save_file.write("\n")
                save_file.write(quest_tomek_1)
                save_file.write("\n")
                save_file.write(ocenaSTR)
                save_file.write("\n")
                save_file.write(ocena_ruchSTR)
                save_file.write("\n")
                save_file.write(wynikp99)
                save_file.write("\n")
                save_file.close()
                zapis = "OK"

        if zapis == "OK":
            screen.blit(zapisano, (570, 675))
        pisak.pisz("wers", "Ten etap pozwala zapisać stan Gry. Wystarczy kliknąć 'ZAPISZ'", 20, 460, dyellow)
        pisak.pisz("wers1", "Przy kolejnym uruchomieniu gry, w MENU pojawi się ikona plusa '+' - oznaczająca"
                            " kontynuację", 20, 490, dyellow)
        pisak.pisz("wers2", "Jest to również miejsce, z którego będziesz kontynuował(-a) dalszą grę.", 20, 520, dyellow)
        pygame.display.update()
        mainClock.tick()

# Scena15


def scena25():
    pygame.mixer.music.stop()
    siren.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(korytarzDZIEN, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena26()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        pisak.pisz("wers0", "Piątek, piąteczek, piątunio! Nie dość, że za chwilę pojedziecie do domu to jeszcze"
                            " okazało się", 20, 120, white)
        pisak.pisz("wers", "że macie wszystkie zajęcia w akademiku nr 1 na III piętrze. Super! Nie będzie"
                           " tego łażenia z ", 20, 150, white)
        pisak.pisz("wers1", "budynku do budynku! Okazało się, że macie zajęcia w znajomym Ci miejscu"
                            " - pamiętasz służbę jako dyżurny?", 20, 180, white)
        pisak.pisz("wers2", "Podchodzisz do ściany by ponownie przyjrzeć się ciekawemu obrazkowi..", 20, 210, white)
        pisak.pisz("wers3", "Dziwne.. a czy nie było tutaj czegoś innego?", 20, 380, white)
        pisak.pisz("wers4", "No tak, może byłem(-am) zaspany(-a).. przecież była 3 w nocy..", 20, 410, white)

        obrazNowy = screen.blit(nowyObraz, (334, 273))
        if obrazNowy.collidepoint((mx, my)):
            screen.blit(nowyObraz1, (450, 50))

        screen.blit(oko, (mx, my))
        pygame.display.update()
        mainClock.tick()

# Scena26


def scena26():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(wspol, (0, 0))
        buttonNie = screen.blit(nie, (470, 600))
        buttonTak = screen.blit(tak, (660, 600))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if buttonNie.collidepoint((mx, my)):
            screen.blit(nie1, (470, 600))
            if click:
                loadingSound.play()
                scena27()

        if buttonTak.collidepoint((mx, my)):
            screen.blit(tak1, (660, 600))
            if click:
                loadingSound.play()
                scena_torba()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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
        if quest_tomek_1 == "rozmowa":
            pisak.pisz("wers10", "*Może znajdziesz coś.. cokolwiek.. może związanego z dziwną rozmową w korytarzu"
                                 " siłowni?", 20, 390, green)
        pisak.pisz("wers12", "--> Zaglądasz do torby?", 500, 530, dyellow)

        pygame.display.update()
        mainClock.tick()

# Scena Torba Tomka


def scena_torba():
    running = True
    global quest_tomek_torba
    while running:
        click = False
        quest_tomek_torba = "torebunia"

        screen.fill(black)
        inicjalyX = screen.blit(inicjaly, (880, 33))
        naszywkaX = screen.blit(naszywka, (783, 415))
        ksiazkaX = screen.blit(ksiazka, (587, 264))
        knigaX = screen.blit(kniga, (264, 275))
        screen.blit(torbaBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena27()
        pisak.pisz("wers1", "*4 przedmioty*", 20, 20, dyellow)

        if inicjalyX.collidepoint((mx, my)):
            screen.blit(inicjaly1, (880, 120))

        if naszywkaX.collidepoint((mx, my)):
            screen.blit(naszywka1, (783, 510))

        if ksiazkaX.collidepoint((mx, my)):
            screen.blit(ksiazka1, (587, 360))

        if knigaX.collidepoint((mx, my)):
            screen.blit(kniga1, (264, 370))

        screen.blit(oko, (mx, my))

        pygame.display.update()
        mainClock.tick()

# Scena27


def scena27():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(drogaBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scenaProg4()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        pisak.pisz("wers", "Spakowałeś(-aś) się do końca, zamknąłeś(-aś) pokój i wypisałeś(-aś) się u dyżurnego"
                           " akademika na wyjazd.", 20, 90, white)
        pisak.pisz("wers1", "Już po 15 minutach siedzisz w swoim autku i obierasz kierunek DOM.", 20, 120, white)
        pisak.pisz("wers2", "Droga daleka.. odpalasz ulubioną stację radiową i suniesz przed siebie.", 20, 150, white)
        if quest_tomek_torba == "torebunia":
            pisak.pisz("wers3", "*Jednak to co zobaczyłeś(-aś) w torbie, trochę nie daje Ci spokoju.", 20, 180, green)
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


def scenaProg4():
    siren.stop()
    progOGG.play()
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(prog, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                progOGG.stop()
                loadingSound.play()
                scena28()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        pisak.pisz("wers", "Może być tak, że część tekstu wypisywana jest w grze na zielono z gwiazdką '*'.",
                   20, 430, dyellow)
        pisak.pisz("wers1", "*Taki tekst pojawia się jedynie, gdy pokierowałeś fabułą w interesującym kierunku,"
                            " wykonujesz zadanie lub", 20, 460, green)
        pisak.pisz("wers2", "*wykazałeś się sprawnością w jakimś etapie gry.", 20, 490, green)
        pisak.pisz("wers3", "*Są to też dodatkowe dialogi, pomocnicze przemyślenia bohatera lub specjalne sceny.",
                   20, 520, green)

        pygame.display.update()
        mainClock.tick()

# Scena28


def scena28():
    siren.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(wspol, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena29()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        pisak.pisz("wers", "Weekend zleciał nim się obejrzałeś(-aś), szkoda że kurs nie leci tak szybko..",
                   20, 90, white)
        pisak.pisz("wers1", "Powrót do szkoły był męczący, na trasie miałeś(-aś) spore korki, przez padający deszcz.",
                   20, 120, white)
        pisak.pisz("wers2", "Jest 21:00 ale okazuje się, że jesteś jako pierwszy(-a) w pokoju. Kładziesz się na"
                            " chwilę.", 20, 150, white)
        if quest_tomek_torba == "torebunia":
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
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena30()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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
    while running:
        click = False
        global wykroczenia
        wykroczenia = "wykroczenia"

        screen.fill(black)
        screen.blit(wspol2, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                egzamin_wykr()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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
    siren.stop()
    szum.play(-1)
    running = True
    while running:
        global odp1_wykr
        click = False
        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))
        pisak.pisz("wers", "Kodeks wykroczeń to..?", 450, 100, red)
        pisak.pisz("wers1", "Rozporządzenie", 450, 130, white)
        pisak.pisz("wers2", "Ustawa", 450, 190, white)
        pisak.pisz("wers3", "Tygodnik policyjny", 450, 250, white)

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

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp1_wykr = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp1_wykr = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp1_wykr = "c"

        if odp1_wykr:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_wykr2()

        pygame.display.update()
        mainClock.tick()

# Pytanie 2----------------------


def egzamin_wykr2():
    running = True
    while running:
        global odp2_wykr
        click = False
        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))
        pisak.pisz("wers", "Wykroczenie można popełnić..", 450, 100, red)
        pisak.pisz("wers1", "Tylko umyślnie", 450, 130, white)
        pisak.pisz("wers2", "Tylko nieumyślnie", 450, 190, white)
        pisak.pisz("wers3", "Umyślnie i nieumyślnie", 450, 250, white)

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

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp2_wykr = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp2_wykr = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp2_wykr = "c"

        if odp2_wykr:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_wykr3()

        pygame.display.update()
        mainClock.tick()

# Pytanie 3----------------------


def egzamin_wykr3():
    running = True
    while running:
        global odp3_wykr
        click = False
        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))
        pisak.pisz("wers", "Odpowiada za usiłowanie ten kto..", 450, 100, red)
        pisak.pisz("wers1", "Zmierza do popełniania czynu, który nie następuje", 450, 130, white)
        pisak.pisz("wers2", "Myśli o popełnieniu czynu", 450, 190, white)
        pisak.pisz("wers3", "Śni mu się jak popełnia przestępstwo", 450, 250, white)

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

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp3_wykr = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp3_wykr = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp3_wykr = "c"

        if odp3_wykr:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    egzamin_wykr4()

        pygame.display.update()
        mainClock.tick()

# Pytanie 4----------------------


def egzamin_wykr4():
    running = True
    while running:
        global odp4_wykr
        click = False
        screen.fill(black)
        screen.blit(egzaminFoto, (200, 0))
        pisak.pisz("wers", "Nakłanianie innej osoby do popełniania czynu to..", 450, 100, red)
        pisak.pisz("wers1", "Pomocnictwo", 450, 130, white)
        pisak.pisz("wers2", "Zachęcanie", 450, 190, white)
        pisak.pisz("wers3", "Podżeganie", 450, 250, white)

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

        a_nopress = screen.blit(key_a, (338, 115))
        if a_nopress.collidepoint((mx, my)):
            screen.blit(key_a1, (338, 115))
            if click:
                pen.play()          
                odp4_wykr = "a"

        b_nopress = screen.blit(key_b, (338, 175))
        if b_nopress.collidepoint((mx, my)):
            screen.blit(key_b1, (338, 175))
            if click:
                pen.play()          
                odp4_wykr = "b"

        c_nopress = screen.blit(key_c, (338, 235))
        if c_nopress.collidepoint((mx, my)):
            screen.blit(key_c1, (338, 235))
            if click:
                pen.play()          
                odp4_wykr = "c"

        if odp4_wykr:
            dalej = screen.blit(pressDalej, (1100, 640))
            if dalej.collidepoint((mx, my)):
                screen.blit(pressDalej1, (1100, 640))
                if click:
                    loadingSound.play()
                    wyniki_wykr()
        pygame.display.update()
        mainClock.tick()

# Wyniki z wykroczeń


def wyniki_wykr():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        tornister = screen.blit(plecak, (200, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                szum.stop()
                loadingSound.play()
                scena31()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()
        pisak.pisz("wersX", imieGracza, 600, 220, white)
        pisak.pisz("wers", "Twoja ocena z testu KODEKS WYKROCZEN!", 450, 250, white)

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

        global ocena_wykr, ocena_wykrSTR
        ocena_wykr = jeden + odp1x + odp2x + odp3x + odp4x
        ocena_wykrSTR = str(ocena_wykr)

        try:
            if ocena_wykr == 5:
                pisak.pisz("wers1", "Gratulacje kujonie! Dostałeś 5!", 450, 510, dyellow)
                screen.blit(cyfra5, (580, 300))
            if ocena_wykr == 4:
                pisak.pisz("wers2", "Całkiem, całkiem. Dostałeś 4!", 450, 510, dyellow)
                screen.blit(cyfra4, (580, 300))
            if ocena_wykr == 3:
                pisak.pisz("wers3", "Mogło pójść lepiej.. Tylko 3?", 450, 510, dyellow)
                screen.blit(cyfra3, (580, 300))
            if ocena_wykr == 2:
                pisak.pisz("wers4", "Jak chcesz skończyć kurs to weź się do nauki miernoto. Dostałeś(-aś) 2!",
                           250, 510, dyellow)
                screen.blit(cyfra2, (580, 300))
            if ocena_wykr == 1:
                pisak.pisz("wers5", "Głowa pusta jak kapusta. Dostałeś pałę..", 400, 510, dyellow)
                screen.blit(cyfra1, (580, 300))
        except ValueError:
            pisak.pisz("wersX", "Jeśli to widzisz - to jest to nieoczekiwany błąd gry (Zgłoś mi to)", 300, 510, red)

        pygame.display.update()
        mainClock.tick()

# Scena31


def scena31():
    siren.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        buttonNie = screen.blit(nie, (470, 600))
        buttonTak = screen.blit(tak, (660, 600))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

        mx, my = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if buttonNie.collidepoint((mx, my)):
            screen.blit(nie1, (470, 600))
            if click:
                loadingSound.play()
                scena_cela3()

        if buttonTak.collidepoint((mx, my)):
            screen.blit(tak1, (660, 600))
            if click:
                loadingSound.play()
                scena_anka()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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
        if quest_tomek_torba == "torebunia":
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
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena32()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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
    while running:
        click = False

        screen.fill(black)
        screen.blit(barBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena_cela4()

        pisak.pisz("wers", "Wyszliście we 3 do CELI. Ance zostawiłeś do nauki swoje zapiski z notanika - powinny"
                           " jej wystarczyć.", 20, 150, white)
        pisak.pisz("wers1", "W barze czujesz się już pewniej, nawet barman Was poznał i na powitanie kiwnął głową.",
                   20, 180, white)
        pisak.pisz("wers2", "Klasycznie, zasiadacie w tym samym stoliku co zwykle, krótkie zastanowienie, co kto pije.",
                   20, 210, white)
        pisak.pisz("wers3", "Tomek wstaje od stolika, zbiera Wasze zamówienia i idzie w kierunku baru.", 20, 240, white)
        pisak.pisz("wers4", "- Tylko się straszczaj, bo jestem spragniona! - krzyczy za nim Iwona.", 20, 270, white)
        if quest_tomek_torba == "torebunia":
            pisak.pisz("wers5", "*Myślisz sobie, że znając Tomka, pewnie znowu gdzieś zniknie na 15 minut",
                       20, 300, green)
            pisak.pisz("wers6", "*Nie chcesz mówić o tym Iwonie ale jest okazja by wyrwać się pod pretekstem "
                                "kibelka i pójść za nim.", 20, 330, green)
            pisak.pisz("wers7", "[ZADANIE] --> Możesz pójść za Tomkiem lub pozostać w tej scenie klikając 'dalej'",
                       20, 560, green)
            ideX = screen.blit(ide, (550, 620))
            if ideX.collidepoint((mx, my)):
                screen.blit(ide1, (550, 620))
                if click:
                    loadingSound.play()
                    scena_cela_quest()

        pygame.display.update()
        mainClock.tick()

# Scena_CELA_quest


def scena_cela_quest():
    running = True
    global quest_tomek_cela
    while running:
        click = False
        quest_tomek_cela = "cela"

        screen.fill(black)
        screen.blit(barBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
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
    while running:
        click = False

        screen.fill(black)
        screen.blit(barBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
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
        if quest_tomek_cela == "cela":
            pisak.pisz("wers12", "*Skłamał! Teraz jestem pewny(-a)! On coś ukrywa! Tylko co?", 20, 520, green)
        pygame.display.update()
        mainClock.tick()

# Scena32


def scena32():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena33()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

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
        screen.blit(strzelnica2, (0, 0))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                strzelnica_mossberg()

        pisak.pisz("wers", "Nowy dzionek zapowiada się całkiem przyzwoicie. Będziesz strzelać na strzelnicy.",
                   30, 150, white)
        pisak.pisz("wers1", "Znowu z prawdziwych nabojów!", 30, 180, white)
        pisak.pisz("wers2", "Czujesz lekki stresik.", 30, 210, white)
        pisak.pisz("wers3", "Prowadzący zajęcia policjant, tłumaczy zasady strzelania:", 30, 240, white)
        pisak.pisz("wers4", "1.Macie 50 naboi!", 30, 270, dyellow)
        pisak.pisz("wers5", "2.Celujecie w sam środek!", 30, 300, dyellow)
        pisak.pisz("wers6", ".. i zaliczacie zajęcia", 30, 330, dyellow)
        pisak.pisz("wers7", "Wchodzisz na pozycję do strzelania i ładujesz pełny magazynek", 30, 360, white)
        pisak.pisz("wers7", "Wkładasz okulary ochronne i słuchawki wygłuszające. Słyszysz stłumiony głos prowadzącego:",
                   30, 390, white)
        pisak.pisz("wers7", "- Przygotować się do strzelania!", 30, 420, white)

        pygame.display.update()
        mainClock.tick()

# Strzelnica Mossberg


def strzelnica_mossberg():
    ox = 600 - tarcza_rect.center[0]
    oy = 200 - tarcza_rect.center[1]
    ox_move = 1
    oy_move = 1
    punkty = 0
    naboje = 50
    startx = 500
    delta = 0.0
    global blob_color, wynikmb
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        losowa = random.randrange(-150, 150)
        punktyStr = str(punkty)
        nabojeStr = str(naboje)
        wynikmb = punktyStr

        screen.blit(strzelnica2, (0, 0))
        if naboje <= 0:
            tablica_wynikow_mb.append(wynikmb)
            strzelnica2wyniki()

        screen.blit(tabelaIMG, (5, 600))

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

        delta += mainClock.tick() / 1000.0
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
                            shotgun.play()
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
                            shotgun.play()
                            ox += losowa
            if result8:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        if click:
                            punkty += 8
                            naboje -= 1
                            shotgun.play()
                            ox += losowa
            if result7:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        if click:
                            punkty += 7
                            naboje -= 1
                            shotgun.play()
                            ox += losowa
            if result6:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        if click:
                            punkty += 6
                            naboje -= 1
                            shotgun.play()
                            ox += losowa
            if result5:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    click = True
                    if click:
                        punkty += 5
                        naboje -= 1
                        shotgun.play()
                        ox += losowa

            if result4:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    click = True
                    if click:
                        punkty += 4
                        naboje -= 1
                        shotgun.play()
                        ox += losowa
            if result3:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    click = True
                    if click:
                        punkty += 3
                        naboje -= 1
                        shotgun.play()
                        ox += losowa
            if result2:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    click = True
                    if click:
                        punkty += 2
                        naboje -= 1
                        shotgun.play()
                        ox += losowa
            if result1:
                blob_color = orange_blob
                if event.type == MOUSEBUTTONDOWN:
                    click = True
                    if click:
                        punkty += 1
                        naboje -= 1
                        shotgun.play()
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
        screen.blit(gun2, (mx, my))

        pisak.pisz("imie", imieGracza, 50, 650, black)
        pisak.pisz("naboje", nabojeStr, 345, 650, black)
        pisak.pisz("wers2", punktyStr, 265, 650, black)

        pygame.display.update()

# Strzelnica2 Wyniki


def strzelnica2wyniki():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(wynikiBG, (260, 10))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))
        dalej = screen.blit(pressDalej, (1100, 640))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if dalej.collidepoint((mx, my)):
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena34()
                
        pisak.pisz("wers1", wynikp99, 730, 238, black)
        pisak.pisz("wers2", wynikmb, 730, 328, black)
        pisak.pisz("wers3", imieGracza, 460, 60, black)
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
        screen.blit(pokoj, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                plan_szkoly()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        pisak.pisz("wers", "Po strzelnicy wszyscy pakują się do wyjazdu.. no prawie wszyscy bo Ty zostajesz"
                           " na weekend.", 20, 120, white)
        pisak.pisz("wers1", "Odprowadziłeś(-aś) Tomka, Iwonę i Ankę pod szlaban. Wracając spotkałeś(-aś) dowócę"
                            " kompanii i ", 20, 150, white)
        pisak.pisz("wers2", "ustaliłeś(-aś), że służbę masz jutro, a dokładniej to 12 godzinną służbę z soboty"
                            " na niedzielę.", 20, 180, white)
        pisak.pisz("wers3", "Służba ma polegać, na patrolu a właściwie to obchodzie całego kompleksu szkoły.",
                   20, 210, white)
        pisak.pisz("wers4", "Takie służby są w parach, ale dowódca nie wiedział z kim będziesz mieć służbę."
                            " Dowiesz się jutro.", 20, 240, white)
        pisak.pisz("wers5", "W sumie to masz bardzo dużo czasu do jutrzejszej służby tylko, że nie wiesz co "
                            "z tym czasem robić.", 20, 270, white)
        pisak.pisz("wers6", "Z racji tego, że nie wracasz dziś do domu, postanawiasz iść na stołówkę i zjeść obiad.",
                   20, 300, white)
        pisak.pisz("wers7", "Na stołówce było kilkanaście osób. Jedząc sobie spokojnie usłyszałeś(-aś), że w weekendy ",
                   20, 330, white)
        pisak.pisz("wers8", "w całej szkole panuje luz - można przemieszczać się samemu(-ej) i korzystać z"
                            " jej dobrodziejstw.", 20, 360, white)
        pisak.pisz("wers9", "Jest basen, biblioteka, kantyna, sala do ćwiczeń. Warto to zwiedzić!",
                   20, 390, white)

        kompleksX = screen.blit(kompleks, (623, 212))
        if kompleksX.collidepoint((mx, my)):
            screen.blit(kompleks1, (623, 235))

        pygame.display.update()
        mainClock.tick()

# Plan_szkoły


def plan_szkoly():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(planBG, (0, 0))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                scena35()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        pisak.pisz("wers", "Kliknij na budynek, by zwiedzić wybrane miejsce!", 350, 650, dyellow)

        stolowkax = screen.blit(stolowka, (468, 86))
        if stolowkax.collidepoint((mx, my)):
            screen.blit(stolowka1, (468, 86))
            if click:
                loadingSound.play()
                stolowka_budynek()

        bibliotekax = screen.blit(biblioteka, (513, 254))
        if bibliotekax.collidepoint((mx, my)):
            screen.blit(biblioteka1, (513, 254))
            if click:
                loadingSound.play()
                biblioteka_budynek()

        sala_rdx = screen.blit(sala_rd, (458, 185))
        if sala_rdx.collidepoint((mx, my)):
            screen.blit(sala_rd1, (458, 185))
            if click:
                loadingSound.play()
                symulator_budynek()

        hiltonx = screen.blit(hilton, (457, 361))
        if hiltonx.collidepoint((mx, my)):
            screen.blit(hilton1, (457, 361))
            if click:
                loadingSound.play()
                hilton_budynek()

        akademik_x = screen.blit(akademik2, (379, 45))
        if akademik_x.collidepoint((mx, my)):
            screen.blit(akademik21, (379, 45))
            if click:
                loadingSound.play()
                akademik_budynek_2()

        akademik1X = screen.blit(akademik_1, (313, 71))
        if akademik1X.collidepoint((mx, my)):
            screen.blit(akademik_11, (313, 71))
            if click:
                loadingSound.play()
                akademik_budynek_1()

        karatex = screen.blit(karate, (318, 291))
        if karatex.collidepoint((mx, my)):
            screen.blit(karate1, (318, 291))
            if click:
                loadingSound.play()
                karate_budynek()

        akademik3X = screen.blit(akademik3, (569, 83))
        if akademik3X.collidepoint((mx, my)):
            screen.blit(akademik31, (569, 83))
            if click:
                loadingSound.play()
                akademik_budynek_3()

        budynekx = screen.blit(budynek, (324, 438))
        if budynekx.collidepoint((mx, my)):
            screen.blit(budynek1, (324, 438))
            if click:
                loadingSound.play()
                dziekanat_budynek()

        odprawyx = screen.blit(odprawy, (378, 447))
        if odprawyx.collidepoint((mx, my)):
            screen.blit(odprawy1, (378, 447))
            if click:
                loadingSound.play()
                kinowa_budynek()

        salawfx = screen.blit(salawf, (607, 171))
        if salawfx.collidepoint((mx, my)):
            screen.blit(salawf1, (607, 171))
            if click:
                loadingSound.play()
                salawf_budynek()

        cyberx = screen.blit(cyber, (666, 311))
        if cyberx.collidepoint((mx, my)):
            screen.blit(cyber1, (666, 311))
            if click:
                loadingSound.play()
                pcab_budynek()

        pifpaf_x = screen.blit(pifpaf, (725, 163))
        if pifpaf_x.collidepoint((mx, my)):
            screen.blit(pifpaf1, (725, 163))
            if click:
                loadingSound.play()
                strzelnica_budynek()

        palarniax = screen.blit(palarnia, (735, 269))
        if palarniax.collidepoint((mx, my)):
            screen.blit(palarnia1, (735, 269))
            if click:
                loadingSound.play()
                palarnia_budynek()

        kantynax = screen.blit(kantyna, (511, 383))
        if kantynax.collidepoint((mx, my)):
            screen.blit(kantyna1, (511, 383))
            if click:
                loadingSound.play()
                kantyna_budynek()

        silkasx = screen.blit(silkas, (613, 405))
        if silkasx.collidepoint((mx, my)):
            screen.blit(silkas_1, (613, 405))
            if click:
                loadingSound.play()
                silownia_budynek()

        budowlax = screen.blit(budowla, (753, 418))
        if budowlax.collidepoint((mx, my)):
            screen.blit(budowla1, (753, 418))
            if click:
                loadingSound.play()
                budowla_budynek()

        tajwanx = screen.blit(tajwan, (840, 442))
        if tajwanx.collidepoint((mx, my)):
            screen.blit(tajwan1, (840, 442))
            if click:
                loadingSound.play()
                tajwan_budynek()

        sztabx = screen.blit(sztab, (367, 511))
        if sztabx.collidepoint((mx, my)):
            screen.blit(sztab1, (367, 511))
            if click:
                loadingSound.play()
                sztab_budynek()

        pygame.display.update()
        mainClock.tick()


# Sala Kinowa


def kinowa_budynek():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(wspol2, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeks_ocen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Budynek nr 7 - znajduje się w nim sala kinowa i centrum konferencyjne.", 20, 90, white)
        pisak.pisz("wers1", "Drzwi są otwarte, dlatego wchodzisz do środka, po lewej stronie schody do góry,"
                           " po prawej - na dół.", 20, 120, white)
        pisak.pisz("wers2", "Słyszysz głosy dobiegające z jakiegoś pomieszczenia, gdzie prowadzą schody po prawej"
                           " stronie.", 20, 150, white)
        pisak.pisz("wers3", "Schodzisz na dół i.. Wooo! Tu jest bar z niezdrowym jedzonkiem!", 20, 180, white)
        pisak.pisz("wers4", "Podchodzisz do baru i zamawiasz hamburgera ze wszystkimi dodatkami.", 20, 210, white)
        pisak.pisz("wers5", "Mniam! To miejsce warto zapamiętać!", 20, 240, white)

        pygame.display.update()
        mainClock.tick()


# Sala Dziekanat


def dziekanat_budynek():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(wspol2, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeks_ocen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Budynek nr 6 - dziekanaty, sale wykładowe.. nic ciekawego.. ",
                   20, 90, white)

        pygame.display.update()
        mainClock.tick()


# Sala Tajwan


def tajwan_budynek():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(tajwan_bg, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeks_ocen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

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

        pygame.display.update()
        mainClock.tick()


# Sala Budowla


def budowla_budynek():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(palarnia_bg, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeks_ocen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Budynek nr 27 - Dział zaopatrzenia i transportu.",
                   20, 90, white)
        pisak.pisz("wers1", "To budynek, w którym nigdy nie będziesz mieć zajęć.", 20, 120, white)
        pisak.pisz("wers2", "Jak sama nazwa wskazuje, załatwia się tam sprawy zaopatrzeniowe.",
                   20, 150, white)
        pisak.pisz("wers3", "Wpatrujesz się w duże metalowe drzwi, które nagle zaczynają się otwierać.", 20, 180, white)
        pisak.pisz("wers4", "Wychodzi z nich mężczyzna ubrany w czarny uniform - ale nie robotniczy, wygląda trochę jak"
                            " Twój mundur ćwiczebny ", 20, 210, white)
        pisak.pisz("wers5", "ale jest jednoczęściowy. Przez otwarte drzwi słyszysz głośne śmiechy i rozmowy.", 20, 240, white)
        pisak.pisz("wers6", "Jeden ze śmiejących się głosów obniża nieco ton i mówi: - Jarek!", 20, 270, white)
        pisak.pisz("wers7", "- Czego!? - odpowiada mężczyzna w czarnym uniformie.", 20, 300, white)
        pisak.pisz("wers8", "- Tylko nie zapomnij zadzownić do Tomka!", 20, 330, white)
        pisak.pisz("wers9", "- Jakiego Tomka?", 20, 360, white)
        pisak.pisz("wers10", "- Znaczy się Marka - odpowiada głos z budynku.", 20, 390, white)
        pisak.pisz("wers11", "- No dobra, jasna sprawa - mężczyzna w uniformie zamyka za sobą drzwi i idzie w kierunku"
                            " siłowni.", 20, 420, white)
        pisak.pisz("wers12", "*Heh same Tomki w tym Szczytnie - myślisz sobie.", 20, 450, white)

        pygame.display.update()
        mainClock.tick()


# Sala Palarnia


def palarnia_budynek():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(palarnia_bg, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeks_ocen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Magazyny i budynki gospodarcze.",
                   20, 90, white)
        pisak.pisz("wers1", "Z budynku, dochodzi odgłos pracującej pompy wodnej.", 20, 120, white)
        pisak.pisz("wers2", "Eh nic tu nie ma ciekawego..",
                   20, 150, white)

        pygame.display.update()
        mainClock.tick()


# Sala Biblioteka


def biblioteka_budynek():
    siren.stop()
    stolowkaOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(biblioteka_bg, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeks_ocen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                stolowkaOGG.stop()
                siren.play(-1)
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Biblioteka - tutejsza biblioteka posiada dużą bazę ciekawych książek i czasopism.",
                   20, 90, white)
        pisak.pisz("wers1", "Można by coś przeczytać skoro zostajesz na weekend.", 20, 120, white)
        pisak.pisz("wers2", "Na drzwiach wejściowych wisi kartka: 'Biblioteka nieczynna z powodu remontu'",
                   20, 150, white)
        pisak.pisz("wers3", "'Przepraszamy i zapraszamy za 2 tygodnie'", 20, 180, white)
        pisak.pisz("wers4", "No nic.. najwyżej wrócisz tu  za 2 tygodnie..", 20, 210, white)

        pygame.display.update()
        mainClock.tick()


# Sala Kantyna


def kantyna_budynek():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(kantyna_bg, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeks_ocen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Budunek nr 18 - siedziba Kanclerza i Prorektora WSPOL.", 20, 90, white)
        pisak.pisz("wers1", "Drzwi są zamknięte.. ", 20, 120, white)

        pygame.display.update()
        mainClock.tick()


# Sala Symulator


def symulator_budynek():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pcab_bg, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeks_ocen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

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


# Sala siłownia


def silownia_budynek():
    siren.stop()
    silowniaOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(silka, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeks_ocen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                silowniaOGG.stop()
                siren.play(-1)
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Siłownia - ot taki niewielki budynek.", 20, 90, white)
        pisak.pisz("wers1", "Hantle, ławeczki, ciężarki i różnorakie machiny na rozrost mięśni.",
                   20, 120, white)
        pisak.pisz("wers2", "Mało kiedy wietrzona - wali potem na kilometr..", 20, 150, white)

        pygame.display.update()
        mainClock.tick()


# Sala karate


def karate_budynek():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(karate_bg, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeks_ocen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

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


# Hilton


def hilton_budynek():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(hilton_bg, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeks_ocen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeks_ocen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

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


# PCAB


def pcab_budynek():
    siren.stop()
    stolowkaOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(pcab_bg, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                stolowkaOGG.stop()
                siren.play(-1)
                loadingSound.play()
                running = False

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


# Strzelnica budynek


def strzelnica_budynek():
    siren.stop()
    stolowkaOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(strzelnica_bg, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                stolowkaOGG.stop()
                siren.play(-1)
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Strzelnica - to niewielki budynek zaraz za salą gimnastyczną.", 20, 90, white)
        pisak.pisz("wers1", "W środku są 2 strzelnice, jedna wewnątrz, w której już strzelałeś(-aś) i druga na"
                            " zewnątrz", 20, 120, white)
        pisak.pisz("wers2", "Na drugiej już się nie prowadzi strzelań i służy częściej jako miejsce na wykłady lub"
                            " strzelanie 'na sucho'", 20, 150, white)
        pisak.pisz("wers3", "No cóż.. jest praktycznie weekend i strzelnica jest zamknięta do poniedziałku.",
                   20, 180, white)

        nasucho_x = screen.blit(nasucho, (1090, 151))
        if nasucho_x.collidepoint((mx, my)):
            screen.blit(nasucho1, (850, 178))

        pygame.display.update()
        mainClock.tick()


# Sala WF


def salawf_budynek():
    siren.stop()
    salawfOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(salawfBG, (0, 0))
        cofnijX = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijX.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                salawfOGG.stop()
                siren.play(-1)
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Wchodzisz do sali gimnastycznej. Miało być pusto ale..  na boisku rozgrywa się mecz piłki"
                           " halowej.", 20, 120, white)
        pisak.pisz("wers1", "Z racji wolnego czasu z którym nie wiesz co robić, postanawiasz chwilę posiedzieć.",
                   20, 150, white)
        pisak.pisz("wers2", "Zasiadasz w III rzędzie niewielkich trybun, znajdujących się po prawej stronie.",
                   20, 180, white)
        pisak.pisz("wers3", "Oprócz Ciebie, na trybunach siedzi kilka osób, które wpatrują się bezinteresowanie w"
                            " toczoną rozgrywkę.", 20, 210, white)
        pisak.pisz("wers4", "Mecz rozgrywa się pomiędzy 2 drużynami ale nie są to żadne zawody, każdy zawodnik gra "
                            "w innej koszulce.", 20, 240, white)
        pisak.pisz("wers5", "*Eee - zamyślasz się - to wykładowcy grają po zajęciach wraz z osobami, które pozostały "
                            "na weekend.", 20, 270, white)
        if quest_tomek_cela == "cela":
            pisak.pisz("wers6", "*Ale.. chwila.. Jeden z mężczyzn szczególnie przykuwa Twoją uwagę.. hmm..",
                       20, 300, green)
            pisak.pisz("wers7", "*Twarz jakby znajoma.. wykładowca? - Nieee. - Kursant? - Nie.. ale coś powoli świta"
                                " w głowie", 20, 330, green)
            pisak.pisz("wers8", "*No jasne, poznajesz.. przecież to.. barman! Barman z CELI!", 20, 360, green)

        pygame.display.update()
        mainClock.tick()


# Akademik I


def akademik_budynek_1():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(akademikBG, (0, 0))
        cofnijX = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijX.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Akademik nr 1 - to miejsce znasz już jak własną kieszeń. Logiczne - masz tu"
                           " przecież pokój!", 20, 120, white)
        pisak.pisz("wers7", "Eee nudno.. tu nie ma co robić.. ", 20, 150, white)

        pygame.display.update()
        mainClock.tick()

# Akademik II


def akademik_budynek_2():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(akademikBG, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Akademik nr 2 - Drugi z akademików na terenie szkoły.", 20, 120, white)
        pisak.pisz("wers1", "Szkoda, że nie macie tu pokoju - byłoby bliżej na stołówkę.", 20, 150, white)
        pisak.pisz("wers2", "Rozglądasz się ale.. nie ma tu nic ciekawego.", 20, 180, white)

        pygame.display.update()
        mainClock.tick()

# Akademik III


def akademik_budynek_3():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(akademikBG, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Akademik nr 3 - Trzeci z akademików na terenie szkoły, pomiędzy stołówką a basenem.",
                   20, 120, white)
        pisak.pisz("wers1", "Charakteryzuje się tym, że na parterze jest 'podwyższony standard' warunków mieszkalnych.",
                   20, 150, white)
        pisak.pisz("wers2", "Pokoje są 3-osobowe, codziennie sprzątane, jest w nich nawet telewizor z kablówką.",
                   20, 180, white)
        pisak.pisz("wers3", "Na parterze znajduje się też niewielka przychodnia, czynna w godz.08:00-10:00.",
                   20, 210, white)
        pisak.pisz("wers4", "Zwykle w tym akademiku, mieszkają policjanci uczestniczący w kursach specjalistycznych.",
                   20, 240, white)
        pisak.pisz("wers5", "Teraz jest tu pusto, wszyscy wyjechali na weekend..", 20, 270, white)
        pisak.pisz("wers6", "Rozglądasz się jeszcze chwilkę i wychodzisz na zewnątrz.", 20, 300, white)

        pygame.display.update()
        mainClock.tick()

# Sztab


def sztab_budynek():
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(sztabBG, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Budynek nr 1 - Najważniejszy budynek na kampusie Wyższej Szkoły Policji w Szczytnie.",
                   20, 120, white)
        pisak.pisz("wers1", "To tu znajduje się rektorat. Swoją siedzibę ma tu m.in. Komendant-Rektor WSPOL"
                            " oraz dyżurny.", 20, 150, white)
        pisak.pisz("wers2", "Na budynku od strony [al.Marszałka Józefa Piłsudskiego], znajduje się duży napis z"
                            " nazwą szkoły.", 20, 180, white)
        pisak.pisz("wers3", "Jeszcze nie byłeś(-aś) w tym budynku, dlatego postanawiasz go zwiedzić.", 20, 210, white)
        pisak.pisz("wers4", "Otwierasz drzwi i zaczynasz wchodzić po schodach, przed sobą, po prawej stronie"
                            " widzisz jakiś pokój za szybą.", 20, 240, white)
        pisak.pisz("wers5", "- Halo, a Ty dokąd? A Ty dokąd?! - słyszysz ponownie.", 20, 270, white)
        pisak.pisz("wers6", "Wchodzisz jeszcze kilka schodków, do wysokości szyby, za którą przy biurku"
                            " siedzi policjant.", 20, 300, white)
        pisak.pisz("wers7", "W jego pokoju jest z 6 monitorów, na których widać podgląd z monitoringu,"
                            " za nim na ścianie wisi mapa szkoły.", 20, 330, white)
        pisak.pisz("wers8", "Na biurku kilka telefonów, 2 małe przenośne radiostacje. Z jednej słyszysz"
                            " jak ktoś powtarza: 'Bez uwag'", 20, 360, white)
        pisak.pisz("wers9", "- Słucham? - odpowiadasz lekko zmieszany(-a), policjant za szybą podsuwa "
                            "się bliżej szyby i mówi.", 20, 390, white)
        pisak.pisz("wers10", "- To ja słucham, coś się stało? - spogląda na Ciebie i widzisz jak mierzy"
                             " Cię wzrokiem od stóp do głowy.", 20, 420, white)
        pisak.pisz("wers11", "- Chciałem(-am) tylko zobaczyć.. - próbujesz wytłumaczyć po co tu jesteś.",
                   20, 450, white)
        pisak.pisz("wers12", "- Tu nie ma czego oglądać - policjant przerywa Twoją wypowiedź - Jest weekend.",
                   20, 480, white)
        pisak.pisz("wers13", "- Aha - Nie wiesz co odpowiedzieć i wychodzisz z budynku.", 20, 510, white)

        pygame.display.update()
        mainClock.tick()

# Stołówka


def stolowka_budynek():
    siren.stop()
    stolowkaOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(stolowkaBG, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                stolowkaOGG.stop()
                siren.play(-1)
                loadingSound.play()
                running = False

        pisak.pisz("wers", "Wchodzisz po schodach na I piętro. Widzisz, że na sali posila się jeszcze kilka osób."
                           " Obiadów już nie wydają.", 20, 120, white)
        pisak.pisz("wers1", "Na sali jest ze 100 stolików, przy każdym stoliku stoją po 4 krzesła.", 20, 150, white)
        pisak.pisz("wers2", "Panie barmanki, zsuwają krzesła i zabierają plastikowe koszyki z chlebem. ",
                   20, 180, white)
        pisak.pisz("wers3", "Na ogół to miejsce tętni życiem w porach obiadowych a teraz? Cisza, spokój.. ",
                   20, 210, white)
        pisak.pisz("wers4", "Podchodzisz do wielkiego filaru przy okienku do wydawania posiłków na którym "
                            "przyczepiona jest kartka z MENU.", 20, 240, white)
        pisak.pisz("wers5", "Piątek - Kolacja: Makaron z sosem grzybowym, chleb, serek, kompot. *Grubo.. - "
                            "myślisz sobie.", 20, 270, white)
        pisak.pisz("wers6", "Jedyny plus tej kolacji jest taki, że dużo osób pojechało do domu i jest szansa na "
                            "dostanie 2 porcji.", 20, 300, white)
        pisak.pisz("wers7", "Eee nudno.. tu nie ma co robić.. ", 20, 330, white)

        pygame.display.update()
        mainClock.tick()


# Scena35


def scena35():
    siren.stop()
    progOGG.play(-1)
    running = True
    while running:
        click = False

        screen.fill(black)
        screen.blit(prog, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        dalej = screen.blit(pressDalej, (1100, 640))
        notka = screen.blit(notatnikA, (20, 570))
        tornister = screen.blit(plecak, (200, 570))
        indeksOcen = screen.blit(indeks, (900, 570))

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
            screen.blit(pressDalej1, (1100, 640))
            if click:
                loadingSound.play()
                progOGG.stop()
                plan_szkoly()

        if notka.collidepoint((mx, my)):
            screen.blit(notatnikB, (20, 570))
            if click:
                loadingSound.play()
                notatnik()

        if tornister.collidepoint((mx, my)):
            screen.blit(plecak1, (200, 570))
            if click:
                loadingSound.play()
                equip()

        if indeksOcen.collidepoint((mx, my)):
            screen.blit(indeks1, (900, 570))
            if click:
                loadingSound.play()
                wykazOcen()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                progOGG.stop()
                siren.play(-1)
                running = False


        pisak.pisz("wers3", "Za chwilę opuścisz plan szkoły.",
                   20, 400, dyellow)
        pisak.pisz("wers4", "Jeśli nie chcesz już zwiedzać - naciśnij 'Dalej'", 20, 430, dyellow)
        pisak.pisz("wers5", "Jeśli chcesz kontynuować zwiedzanie - naciśnij 'Cofnij'", 20, 460, dyellow)

        pygame.display.update()
        mainClock.tick()


# INFO


def info():
    running = True
    while running:
        click = False
        screen.fill(black)
        screen.blit(bgopcje, (0, 0))
        screen.blit(licencja, (20, 520))

        volume = pygame.mixer.music.get_volume()
        if 0.2 < volume < 0.7:
            screen.blit(volPanel0, (950, 300))
        elif volume > 0.7:
            screen.blit(volPanel2, (950, 300))
        elif volume < 0.2:
            screen.blit(volPanel, (950, 300))

        cicho = screen.blit(volLow, (1000, 530))
        srednio = screen.blit(volNormal, (960, 570))
        glosno = screen.blit(volHI, (982, 610))
        cofnijx = screen.blit(cofnij, (560, 640))
        
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if cicho.collidepoint((mx, my)):
            screen.blit(volLow1, (1000, 530))
            if click:
                pisak.volume_low()

        if srednio.collidepoint((mx, my)):
            screen.blit(volNormal1, (960, 570))
            if click:
                pisak.volume_normal()

        if glosno.collidepoint((mx, my)):
            screen.blit(volHI1, (982, 610))
            if click:
                pisak.volume_hi()

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                running = False

        pisak.pisz("wers2", "'Policmajster' to gra tekstowa z elementami grafiki, opowiadająca historię z"
                            " Tobą w roli głównej.", 20, 150, white)
        pisak.pisz("wers3", "Gra rozpoczyna się od momentu gdy decydujesz się wstąpić do Policji a po"
                            " pomyślnym przejściu procedury doboru", 20, 180, white)
        pisak.pisz("wers4", "zostajesz wysłany(-a) na kilkumiesięczne szkolenie do szkoły policyjnej.", 20, 210, white)
        pisak.pisz("wers5", "Możesz poprowadzić swoją karierę poprzez szkołę, egzaminy, następnie służbę jako "
                            "prawdziwy policjant", 20, 240, white)
        pisak.pisz("wers6", "i upragniony awans do Wydziału Dochodzeniowo-Śledczego, na jednym z miejscowych "
                            "komisariatów.", 20, 270, white)
        pisak.pisz("wers7", "Dochodzeniówka to 'sól' całej policji..", 20, 300, white)
        pisak.pisz("wers8", "Dostajesz wiele spraw, tony papierologii, kwitów do wypełnienia - dzień jak co dzień.",
                   20, 330, white)
        pisak.pisz("wers9", "Pewnego dnia może dostaniesz niepozorną sprawę..", 20, 360, white)
        pisak.pisz("wers11", "Zbieżność sytuacji - jeśli wystąpią - jest przypadkowa.", 20, 460, white)
        pisak.pisz("wers12", "Gra wyświetla się domyślnie (poprawnie) w rozdzieczości 1280x720.", 20, 500, dyellow)

        pygame.display.update()
        mainClock.tick(60)

# NOTATNIK


def notatnik():
    running = True
    while running:
        click = False
        
        screen.fill(black)
        screen.blit(notatniczek, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))
        notatnikP = screen.blit(notatnikPistol, (20, 20))
        
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                break
        if notatnikP.collidepoint((mx, my)):
            screen.blit(zapiski, (20, 210))

        try:
            if legitymowanie == "legitymowanie":
                zapisLegitymowanie = screen.blit(notatnikLegit, (200, 20))
                if zapisLegitymowanie.collidepoint((mx, my)):
                    screen.blit(zapiskiLegit, (70, 210))
        except ValueError:
            pass

        try:
            if ruchdrogowy == "ruchdrogowy":
                zapisRuch = screen.blit(notatnikRuch, (380, 20))
                if zapisRuch.collidepoint((mx, my)):
                    screen.blit(zapiskiRuch, (120, 210))
        except ValueError:
            pass

        try:
            if wykroczenia == "wykroczenia":
                zapisWykr = screen.blit(notatnikWykr, (560, 20))
                if zapisWykr.collidepoint((mx, my)):
                    screen.blit(zapiskiWykr, (170, 210))
        except ValueError:
            pass

        pisak.pisz("wers", "Najedź kursorem na notatki by przeczytać.", 20, 655, dyellow)
                                   
        pygame.display.update()
        mainClock.tick(60)

# PLECAK


def equip():
    running = True
    while running:
        click = False
        screen.fill(black)
        screen.blit(plecakIN, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                break
        try:
            if pendrive1 == "testyTomka":
                usbTomka = screen.blit(pendrive, (20, 40))
                if usbTomka.collidepoint((mx, my)):
                    screen.blit(pendriveOpis, (70, 130))
        except ValueError:
            pass

        try:
            if skrawek1 == "skrawek":
                skrawek_PNG = screen.blit(skrawek, (130, 40))
                if skrawek_PNG.collidepoint((mx, my)):
                    screen.blit(skrawekOpis, (160, 130))
        except ValueError:
            pass

        pisak.pisz("wers", "Najedź myszką na przedmiot by podejrzeć.", 455, 550, dyellow)

        pygame.display.update()
        mainClock.tick(60)

# WYKAZ OCEN


def wykazOcen():
    running = True
    while running:
        click = False
        screen.fill(black)
        screen.blit(indeksBG, (0, 0))
        cofnijx = screen.blit(cofnij, (560, 640))

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if cofnijx.collidepoint((mx, my)):
            screen.blit(cofnij1, (560, 640))
            if click:
                loadingSound.play()
                break

        if ocenaSTR == "5":
            screen.blit(podpis1, (710, 267))
            screen.blit(cyfraIndex5, (910, 267))
        elif ocenaSTR == "4":
            screen.blit(podpis1, (710, 267))
            screen.blit(cyfraIndex4, (910, 267))
        elif ocenaSTR == "3":
            screen.blit(podpis1, (710, 267))
            screen.blit(cyfraIndex3, (910, 267))
        elif ocenaSTR == "2":
            screen.blit(podpis1, (710, 267))
            screen.blit(cyfraIndex2, (910, 267))
        elif ocenaSTR == "1":
            screen.blit(podpis1, (710, 267))
            screen.blit(cyfraIndex1, (910, 267))

        if ocena_ruchSTR == "5":
            screen.blit(podpis2, (705, 400))
            screen.blit(cyfraIndex5, (910, 400))
        elif ocena_ruchSTR == "4":
            screen.blit(podpis2, (705, 400))
            screen.blit(cyfraIndex4, (910, 400))
        elif ocena_ruchSTR == "3":
            screen.blit(podpis2, (705, 400))
            screen.blit(cyfraIndex3, (910, 400))
        elif ocena_ruchSTR == "2":
            screen.blit(podpis2, (705, 400))
            screen.blit(cyfraIndex2, (910, 400))
        elif ocena_ruchSTR == "1":
            screen.blit(podpis2, (705, 400))
            screen.blit(cyfraIndex1, (910, 400))

        if ocena_wykrSTR == "5":
            screen.blit(podpis3, (705, 335))
            screen.blit(cyfraIndex5, (910, 332))
        elif ocena_wykrSTR == "4":
            screen.blit(podpis3, (705, 335))
            screen.blit(cyfraIndex4, (910, 332))
        elif ocena_wykrSTR == "3":
            screen.blit(podpis3, (705, 335))
            screen.blit(cyfraIndex3, (910, 332))
        elif ocena_wykrSTR == "2":
            screen.blit(podpis3, (705, 335))
            screen.blit(cyfraIndex2, (910, 332))
        elif ocena_wykrSTR == "1":
            screen.blit(podpis3, (705, 335))
            screen.blit(cyfraIndex1, (910, 332))

        pygame.display.update()
        mainClock.tick()

intro_dev()



