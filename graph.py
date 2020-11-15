import os.path
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
filepath = os.path.dirname(__file__)

# Grafiki okna tytułowego
icon = pygame.image.load(os.path.join(filepath, "data\\pics\\icon.png"))
intro = pygame.image.load(os.path.join(filepath, "data\\introDev\\1x.png")).convert()
bg = pygame.image.load(os.path.join(filepath, "data\\pics\\intro.png")).convert()
kajdanki = [pygame.image.load(os.path.join(filepath, "data\\pics\\kajdanki.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\pics\\kajdanki1.png")).convert()]
pistol = [pygame.image.load(os.path.join(filepath, "data\\pics\\bron.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\pics\\bron1.png")).convert()]
nakladka_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\nakladka.png")).convert_alpha()

# Intro kafle

kafel = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel1.png")).convert_alpha()]
kafel_2 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel2.png")).convert_alpha(),
           pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel2x.png")).convert_alpha()]
kafel_3 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel3.png")).convert_alpha(),
           pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel3x.png")).convert_alpha()]
kafel_4 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel4.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel4x.png")).convert_alpha()]
kafel_5 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel5.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel5x.png")).convert_alpha()]
kafel_6 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel6.png")).convert_alpha(),
           pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel6x.png")).convert_alpha()]
kafel_7 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel7.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel7x.png")).convert_alpha()]
kafel_8 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel8.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel8x.png")).convert_alpha()]

# Animacja logo

animated_Logo = [pygame.image.load(os.path.join(filepath, "data\\logo\\logo.png")),
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

# Nawigacja

press_Kariera = [pygame.image.load(os.path.join(filepath, "data\\navi\\kariera.png")).convert(),
                 pygame.image.load(os.path.join(filepath, "data\\navi\\kariera1.png")).convert()]
press_Enter = [pygame.image.load(os.path.join(filepath, "data\\navi\\enter.png")).convert(),
               pygame.image.load(os.path.join(filepath, "data\\navi\\enter1.png")).convert()]
press_Option = [pygame.image.load(os.path.join(filepath, "data\\navi\\info.png")).convert(),
                pygame.image.load(os.path.join(filepath, "data\\navi\\info1x.png")).convert()]
cofnij = [pygame.image.load(os.path.join(filepath, "data\\navi\\cofnij.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\cofnij1.png")).convert()]
press_Dalej = [pygame.image.load(os.path.join(filepath, "data\\navi\\dalej.png")).convert(),
               pygame.image.load(os.path.join(filepath, "data\\navi\\dalej1.png")).convert()]
silownia_N = [pygame.image.load(os.path.join(filepath, "data\\navi\\silownia.png")).convert(),
              pygame.image.load(os.path.join(filepath, "data\\navi\\silownia1.png")).convert()]
spacer_N = [pygame.image.load(os.path.join(filepath, "data\\navi\\spacer.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\navi\\spacer1.png")).convert()]
tak = [pygame.image.load(os.path.join(filepath, "data\\navi\\tak.png")).convert(),
       pygame.image.load(os.path.join(filepath, "data\\navi\\tak1.png")).convert()]
nie = [pygame.image.load(os.path.join(filepath, "data\\navi\\nie.png")).convert(),
       pygame.image.load(os.path.join(filepath, "data\\navi\\nie1.png")).convert()]
cela_nav = [pygame.image.load(os.path.join(filepath, "data\\navi\\cela.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\navi\\cela1.png")).convert()]
miasto = [pygame.image.load(os.path.join(filepath, "data\\navi\\miasto.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\miasto1.png")).convert()]
zapisz = [pygame.image.load(os.path.join(filepath, "data\\navi\\zapisz.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\zapisz1.png")).convert()]
zapisano = pygame.image.load(os.path.join(filepath, "data\\navi\\zapisano.png")).convert()
kontynuacja = [pygame.image.load(os.path.join(filepath, "data\\navi\\plusz.png")).convert(),
               pygame.image.load(os.path.join(filepath, "data\\navi\\plusz1.png")).convert()]
save_start = [pygame.image.load(os.path.join(filepath, "data\\navi\\continue.png")).convert(),
              pygame.image.load(os.path.join(filepath, "data\\navi\\continue1.png")).convert()]
ide = [pygame.image.load(os.path.join(filepath, "data\\navi\\ide.png")).convert(),
       pygame.image.load(os.path.join(filepath, "data\\navi\\ide1.png")).convert()]
stolowka = [pygame.image.load(os.path.join(filepath, "data\\navi\\stolowka.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\navi\\stolowka1.png")).convert()]
biblioteka = [pygame.image.load(os.path.join(filepath, "data\\navi\\biblioteka.png")).convert(),
              pygame.image.load(os.path.join(filepath, "data\\navi\\biblioteka1.png")).convert()]
sala_rd = [pygame.image.load(os.path.join(filepath, "data\\navi\\sala_rd.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\navi\\sala_rd1.png")).convert()]
hilton = [pygame.image.load(os.path.join(filepath, "data\\navi\\hilton.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\hilton1.png")).convert()]
akademik2 = [pygame.image.load(os.path.join(filepath, "data\\navi\\akademik2.png")).convert(),
             pygame.image.load(os.path.join(filepath, "data\\navi\\akademik21.png")).convert()]
akademik_1 = [pygame.image.load(os.path.join(filepath, "data\\navi\\akademik1.png")).convert(),
              pygame.image.load(os.path.join(filepath, "data\\navi\\akademik11.png")).convert()]
karate = [pygame.image.load(os.path.join(filepath, "data\\navi\\karate.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\karate1.png")).convert()]
akademik3 = [pygame.image.load(os.path.join(filepath, "data\\navi\\akademik3.png")).convert(),
             pygame.image.load(os.path.join(filepath, "data\\navi\\akademik31.png")).convert()]
budynek = [pygame.image.load(os.path.join(filepath, "data\\navi\\budynek.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\navi\\budynek1.png")).convert()]
odprawy = [pygame.image.load(os.path.join(filepath, "data\\navi\\odprawy.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\navi\\odprawy1.png")).convert()]
salawf = [pygame.image.load(os.path.join(filepath, "data\\navi\\salawf.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\salawf1.png")).convert()]
cyber = [pygame.image.load(os.path.join(filepath, "data\\navi\\cyber.png")).convert(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\cyber1.png")).convert()]
pifpaf = [pygame.image.load(os.path.join(filepath, "data\\navi\\pifpaf.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\pifpaf1.png")).convert()]
palarnia = [pygame.image.load(os.path.join(filepath, "data\\navi\\palarnia.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\navi\\palarnia1.png")).convert()]
kantyna = [pygame.image.load(os.path.join(filepath, "data\\navi\\kantyna.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\navi\\kantyna1.png")).convert()]
silkas = [pygame.image.load(os.path.join(filepath, "data\\navi\\silka.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\silka1.png")).convert()]
budowla = [pygame.image.load(os.path.join(filepath, "data\\navi\\budowla.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\navi\\budowla1.png")).convert()]
tajwan = [pygame.image.load(os.path.join(filepath, "data\\navi\\tajwan.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\tajwan1.png")).convert()]
sztab = [pygame.image.load(os.path.join(filepath, "data\\navi\\sztab.png")).convert(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\sztab1.png")).convert()]
alarm_pin = [pygame.image.load(os.path.join(filepath, "data\\navi\\alarm_pin1.png")).convert(),
             pygame.image.load(os.path.join(filepath, "data\\navi\\alarm_pin.png")).convert()]

# Dodatkowe grafiki
odznaka = pygame.image.load(os.path.join(filepath, "data\\pics\\odznaka.png")).convert()
bgopcje = pygame.image.load(os.path.join(filepath, "data\\sceny\\bgopcje.png")).convert()
bgankieta = pygame.image.load(os.path.join(filepath, "data\\sceny\\ankieta.png")).convert()
licencja = pygame.image.load(os.path.join(filepath, "data\\pics\\licencjaGimp.png"))
oko = pygame.image.load(os.path.join(filepath, "data\\pics\\oko.png")).convert_alpha()
palec = pygame.image.load(os.path.join(filepath, "data\\pics\\palec.png")).convert_alpha()
but = pygame.image.load(os.path.join(filepath, "data\\pics\\podeszwa.png")).convert_alpha()
rain = pygame.image.load(os.path.join(filepath, "data\\pics\\rain.png")).convert_alpha()
latarka = [pygame.image.load(os.path.join(filepath, "data\\pics\\latarka.png")).convert_alpha(),
           pygame.image.load(os.path.join(filepath, "data\\pics\\latarka1.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\pics\\latarka2.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\pics\\latarkaON.png")).convert_alpha(),
           pygame.image.load(os.path.join(filepath, "data\\pics\\latarka3.png")).convert_alpha(),
           pygame.image.load(os.path.join(filepath, "data\\pics\\latarka4.png")).convert_alpha()]
nozyk = [pygame.image.load(os.path.join(filepath, "data\\pics\\nozyk.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\nozyk1.png")).convert(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\nozyk2.png")).convert(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\nozyk3.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\nozyk4.png")).convert_alpha()]
fajki = [pygame.image.load(os.path.join(filepath, "data\\pics\\fajki.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\fajki1.png")).convert(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\fajki2.png")).convert(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\fajki3.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\fajki4.png")).convert_alpha()]
latarka_ON = pygame.image.load(os.path.join(filepath, "data\\pics\\latarkaON.png")).convert()

# Grafiki scen
wspol = pygame.image.load(os.path.join(filepath, "data\\sceny\\wspol.png")).convert()
wspol2 = pygame.image.load(os.path.join(filepath, "data\\sceny\\wspol2.png")).convert()
pokoj = pygame.image.load(os.path.join(filepath, "data\\sceny\\pokoj.png")).convert()
strzelnica = pygame.image.load(os.path.join(filepath, "data\\sceny\\strzelnica.png")).convert()
silka = pygame.image.load(os.path.join(filepath, "data\\sceny\\silownia.png")).convert()
prog = pygame.image.load(os.path.join(filepath, "data\\sceny\\prog.png")).convert()
plecakIN = pygame.image.load(os.path.join(filepath, "data\\sceny\\plecak.png")).convert()
egzaminFoto = pygame.image.load(os.path.join(filepath, "data\\sceny\\egzamin.png")).convert()
indeksBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\indeksWykaz.png")).convert()
barBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\bar.png")).convert()
pokojnocBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\pokojnoc.png")).convert()
odprawaBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\odprawa.png")).convert()
korytarzBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\korytarz.png")).convert()
korytarzNOC = pygame.image.load(os.path.join(filepath, "data\\sceny\\korytarzSciana.png")).convert()
korytarzDZIEN = pygame.image.load(os.path.join(filepath, "data\\sceny\\korytarzSciana2.png")).convert()
napisPolicja = pygame.image.load(os.path.join(filepath, "data\\pics\\napisPolicja.png")).convert()
napisPolicja1 = pygame.image.load(os.path.join(filepath, "data\\pics\\napisPolicja1.png")).convert()
szczytno_nocBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\szczytnonoc.png")).convert()
strzelnica_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\strzelnica1.png")).convert()
strzelnica1 = pygame.image.load(os.path.join(filepath, "data\\sceny\\strzelnica2.png")).convert()
strzelnica2 = pygame.image.load(os.path.join(filepath, "data\\sceny\\strzelnica3.png")).convert()
tabelaIMG = pygame.image.load(os.path.join(filepath, "data\\pics\\tabelawynikow.png")).convert()
wynikiBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\wykazstrzelan.jpg")).convert()
torbaBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\torba_Tomka.png")).convert()
drogaBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\droga.png")).convert()
planBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\planszkoly.png")).convert()
stolowkaBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\stolowka.png")).convert()
akademikBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\akademik.png")).convert()
akademik_bg_noc = pygame.image.load(os.path.join(filepath, "data\\sceny\\akademik_noc.png")).convert()
sztabBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\sztabBG.png")).convert()
salawfBG = pygame.image.load(os.path.join(filepath, "data\\sceny\\salawf.png")).convert()
pcab_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\pcab.png")).convert()
hilton_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\hilton.png")).convert()
karate_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\salakarate.png")).convert()
kantyna_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\kantyna.png")).convert()
biblioteka_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\biblioteka.png")).convert()
palarnia_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\palarnia.png")).convert()
tajwan_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\tajwan.png")).convert()
maszyna_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\maszyna.png")).convert()
pokoj_noc_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\pokoj_noc.png")).convert()
magazyn_brama_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\magazyn_brama.png")).convert()
brama_kod_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\brama_kod_bg.png")).convert()
falklandy_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\falklandy_bg.png")).convert()
sektor_falklandy_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\falklandy_sektor_bg.png")).convert()
sektor_falklandy_X_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\falklandy_sektor_X_bg.png")).convert()
sektor_falklandy_X_bg_light = pygame.image.load(os.path.join(filepath, "data\\sceny\\falklandy_sektor_X_bg_light.png")).convert()
sektor_falklandy_drzwi_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\falklandy_drzwi_bg.png")).convert()
sektor_falklandy_klodka_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\falklandy_klodka_bg.png")).convert()
sektor_falklandy_sektor_g_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\falklandy_sektor_g.png")).convert()
trasa_falklandy_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\trasa_falklandy.png")).convert()

# Pojęcia + zdjęcia
czarnuch = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\czarnuch.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\pics\\czarnuch.png")).convert()]
p99 = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\p99.png")).convert(),
       pygame.image.load(os.path.join(filepath, "data\\pics\\p99.png")).convert()]
kulkamocy = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\kulkamocy.png")).convert(),
             pygame.image.load(os.path.join(filepath, "data\\pics\\kulkamocy.png")).convert()]
cela = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\cela.png")).convert(),
        pygame.image.load(os.path.join(filepath, "data\\pics\\cela1.png")).convert()]
akademik = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\akademik.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\pics\\akademik.png")).convert()]
wodka = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\wodka.png")).convert(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\wodka.png")).convert()]
plan = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\korytarz.png")).convert(),
        pygame.image.load(os.path.join(filepath, "data\\pics\\korytarz.png")).convert()]
falklandy = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\falklandy.png")).convert(),
             pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy.png")).convert()]
staryObraz = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\staryObraz.png")).convert(),
              pygame.image.load(os.path.join(filepath, "data\\pics\\obrazKobieta.png")).convert()]
nowyObraz = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\nowyObraz.png")).convert(),
             pygame.image.load(os.path.join(filepath, "data\\pics\\obrazAuto.png")).convert()]
bimber = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\bimber.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\pics\\bimber.png")).convert()]
cywilki = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\cywilki.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\pics\\cywilki.png")).convert()]
ogorkow = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\ogorkow.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\pics\\ogorek.png")).convert()]
inicjaly = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\inicjaly.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\pojecia\\inicjaly1.png")).convert()]
naszywka = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\naszywkabut.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\pojecia\\naszywkabut1.png")).convert()]
ksiazka = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\ksiazka.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\pojecia\\ksiazka1.png")).convert()]
kniga = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\kniga.png")).convert(),
         pygame.image.load(os.path.join(filepath, "data\\pojecia\\kniga1.png")).convert()]
kompleks = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\kompleks.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\pojecia\\kompleks1.png")).convert()]
nasucho = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\nasucho.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\pojecia\\nasucho1.png")).convert()]
wejsc = [pygame.image.load(os.path.join(filepath, "data\\pojecia\\wejsc.png")).convert(),
         pygame.image.load(os.path.join(filepath, "data\\pojecia\\wejsc1.png")).convert_alpha()]

# Grafiki notatnika
notatnikA = pygame.image.load(os.path.join(filepath, "data\\navi\\notatnik.png")).convert()
notatnikB = pygame.image.load(os.path.join(filepath, "data\\navi\\notatnik1.png")).convert()
notatniczek = pygame.image.load(os.path.join(filepath, "data\\sceny\\notatniczek.png")).convert()
notatnikPistol = pygame.image.load(os.path.join(filepath, "data\\note\\notatkiPistol.png")).convert()
zapiski = pygame.image.load(os.path.join(filepath, "data\\note\\note1.png")).convert()
notatnikLegit = pygame.image.load(os.path.join(filepath, "data\\note\\notatkiLegit.png")).convert()
zapiskiLegit = pygame.image.load(os.path.join(filepath, "data\\note\\noteLegit.png")).convert()
notatnikRuch = pygame.image.load(os.path.join(filepath, "data\\note\\notatkiRuch.png")).convert()
zapiskiRuch = pygame.image.load(os.path.join(filepath, "data\\note\\noteRuch.png")).convert()
notatnikWykr = pygame.image.load(os.path.join(filepath, "data\\note\\notatkiWykroczenia.png")).convert()
zapiskiWykr = pygame.image.load(os.path.join(filepath, "data\\note\\noteWykr.png")).convert()

# Grafiki plecaka
plecak = pygame.image.load(os.path.join(filepath, "data\\navi\\plecak.png")).convert()
plecak1 = pygame.image.load(os.path.join(filepath, "data\\navi\\plecak1.png")).convert()
pendrive = [pygame.image.load(os.path.join(filepath, "data\\plecak\\usb.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\pics\\usbTomka.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\plecak\\usb1.png")).convert()]
skrawek = [pygame.image.load(os.path.join(filepath, "data\\plecak\\skrawek.png")),
           pygame.image.load(os.path.join(filepath, "data\\plecak\\skrawekOpis.png")).convert(),
           pygame.image.load(os.path.join(filepath, "data\\plecak\\skrawek1.png"))]
kod_pin_img = [pygame.image.load(os.path.join(filepath, "data\\pics\\kod_pin_blank.png")).convert_alpha(),
               pygame.image.load(os.path.join(filepath, "data\\plecak\\kod_pin_opis.png")).convert_alpha(),
               pygame.image.load(os.path.join(filepath, "data\\pics\\kod_pin.png")).convert_alpha(),
               pygame.image.load(os.path.join(filepath, "data\\pics\\kod_pin_blank1.png")).convert_alpha()]

# Grafiki alarmu
pin_1 = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin1.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\pin1_press.png")).convert_alpha()]
pin_2 = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin2.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\pin2_press.png")).convert_alpha()]
pin_3 = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin3.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\pin3_press.png")).convert_alpha()]
pin_cancel = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin_cancel.png")).convert_alpha(),
              pygame.image.load(os.path.join(filepath, "data\\navi\\pin_cancel_press.png")).convert_alpha()]
pin_4 = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin4.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\pin4_press.png")).convert_alpha()]
pin_5 = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin5.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\pin5_press.png")).convert_alpha()]
pin_6 = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin6.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\pin6_press.png")).convert_alpha()]
pin_clear = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin_clear.png")).convert_alpha(),
             pygame.image.load(os.path.join(filepath, "data\\navi\\pin_clear_press.png")).convert_alpha()]
pin_7 = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin7.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\pin7_press.png")).convert_alpha()]
pin_8 = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin8.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\pin8_press.png")).convert_alpha()]
pin_9 = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin9.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\pin9_press.png")).convert_alpha()]
pin_help = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin_help.png")).convert_alpha(),
            pygame.image.load(os.path.join(filepath, "data\\navi\\pin_help_press.png")).convert_alpha()]
pin_0 = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin0.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\navi\\pin0_press.png")).convert_alpha()]
pin_enter = [pygame.image.load(os.path.join(filepath, "data\\navi\\pin_enter.png")).convert_alpha(),
             pygame.image.load(os.path.join(filepath, "data\\navi\\pin_enter_press.png")).convert_alpha()]

# Grafiki indeksu
indeks = pygame.image.load(os.path.join(filepath, "data\\navi\\indeks.png")).convert()
indeks1 = pygame.image.load(os.path.join(filepath, "data\\navi\\indeks1.png")).convert()

# CYFRY do egzaminów
cyfra5 = pygame.image.load(os.path.join(filepath, "data\\pics\\cyfra5.png")).convert()
cyfra4 = pygame.image.load(os.path.join(filepath, "data\\pics\\cyfra4.png")).convert()
cyfra3 = pygame.image.load(os.path.join(filepath, "data\\pics\\cyfra3.png")).convert()
cyfra2 = pygame.image.load(os.path.join(filepath, "data\\pics\\cyfra2.png")).convert()
cyfra1 = pygame.image.load(os.path.join(filepath, "data\\pics\\cyfra1.png")).convert()

# CYFRY do indeksu
cyfraIndex1 = pygame.image.load(os.path.join(filepath, "data\\indeks\\1.png")).convert()
cyfraIndex2 = pygame.image.load(os.path.join(filepath, "data\\indeks\\2.png")).convert()
cyfraIndex3 = pygame.image.load(os.path.join(filepath, "data\\indeks\\3.png")).convert()
cyfraIndex4 = pygame.image.load(os.path.join(filepath, "data\\indeks\\4.png")).convert()
cyfraIndex5 = pygame.image.load(os.path.join(filepath, "data\\indeks\\5.png")).convert()

# Podpisy w indeksie
podpis1 = pygame.image.load(os.path.join(filepath, "data\\indeks\\podpis1.png")).convert()
podpis2 = pygame.image.load(os.path.join(filepath, "data\\indeks\\podpis2.png")).convert()
podpis3 = pygame.image.load(os.path.join(filepath, "data\\indeks\\podpis3.png")).convert()
podpis4 = pygame.image.load(os.path.join(filepath, "data\\indeks\\podpis4.png")).convert()

# Keyboard
key_enter = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\zatwierdz.png")).convert_alpha(),
             pygame.image.load(os.path.join(filepath, "data\\keyboard\\zatwierdz1.png")).convert_alpha()]
key_kasuj = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\kasuj.png")).convert_alpha(),
             pygame.image.load(os.path.join(filepath, "data\\keyboard\\kasuj1.png")).convert_alpha()]
key_q = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\q.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\q1.png")).convert_alpha()]
key_w = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\w.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\w1.png")).convert_alpha()]
key_e = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\e.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\e1.png")).convert_alpha()]
key_r = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\r.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\r1.png")).convert_alpha()]
key_t = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\t.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\t1.png")).convert_alpha()]
key_z = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\z.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\z1.png")).convert_alpha()]
key_u = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\u.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\u1.png")).convert_alpha()]
key_i = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\i.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\i1.png")).convert_alpha()]
key_o = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\o.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\o1.png")).convert_alpha()]
key_p = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\p.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\p1.png")).convert_alpha()]
key_os = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\os.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\keyboard\\os1.png")).convert_alpha()]
key_a = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\a.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\a1.png")).convert_alpha()]
key_s = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\s.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\s1.png")).convert_alpha()]
key_d = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\d.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\d1.png")).convert_alpha()]
key_f = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\f.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\f1.png")).convert_alpha()]
key_g = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\g.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\g1.png")).convert_alpha()]
key_h = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\h.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\h1.png")).convert_alpha()]
key_j = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\j.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\j1.png")).convert_alpha()]
key_k = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\k.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\k1.png")).convert_alpha()]
key_l = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\l.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\l1.png")).convert_alpha()]
key_es = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\es.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\keyboard\\es1.png")).convert_alpha()]
key_as = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\as.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\keyboard\\as1.png")).convert_alpha()]
key_y = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\y.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\y1.png")).convert_alpha()]
key_x = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\x.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\x1.png")).convert_alpha()]
key_c = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\c.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\c1.png")).convert_alpha()]
key_v = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\v.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\v1.png")).convert_alpha()]
key_b = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\b.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\b1.png")).convert_alpha()]
key_n = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\n.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\n1.png")).convert_alpha()]
key_m = [pygame.image.load(os.path.join(filepath, "data\\keyboard\\m.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\keyboard\\m1.png")).convert_alpha()]

# Panel_głośności
volPanel = [pygame.image.load(os.path.join(filepath, "data\\pics\\volPanel.png")),
            pygame.image.load(os.path.join(filepath, "data\\pics\\volPanel0.png")),
            pygame.image.load(os.path.join(filepath, "data\\pics\\volPanel2.png"))]
volLow = [pygame.image.load(os.path.join(filepath, "data\\pics\\cicho.png")),
          pygame.image.load(os.path.join(filepath, "data\\pics\\cicho1.png"))]
volNormal = [pygame.image.load(os.path.join(filepath, "data\\pics\\srednio.png")),
             pygame.image.load(os.path.join(filepath, "data\\pics\\srednio1.png"))]
volHI = [pygame.image.load(os.path.join(filepath, "data\\pics\\glosno.png")),
        pygame.image.load(os.path.join(filepath, "data\\pics\\glosno1.png"))]

# Stopnie służbowe
post = pygame.image.load(os.path.join(filepath, "data\\stopnie\\post.png")).convert()

# Lokacje i grafiki Falklandów
reca = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\reca.png")).convert_alpha(),
        pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\reca1.png")).convert_alpha()]
recb = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\recb.png")).convert_alpha(),
        pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\recb1.png")).convert_alpha()]
recc = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\recc.png")).convert_alpha(),
        pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\recc1.png")).convert_alpha()]
recd = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\recd.png")).convert_alpha(),
        pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\recd1.png")).convert_alpha()]
rece = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\rece.png")).convert_alpha(),
        pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\rece1.png")).convert_alpha()]
recf = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\recf.png")).convert_alpha(),
        pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\recf1.png")).convert_alpha()]
recg = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\recg.png")).convert_alpha(),
        pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\recg1.png")).convert_alpha()]
rech = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\rech.png")).convert_alpha(),
        pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\rech1.png")).convert_alpha()]
reci = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\reci.png")).convert_alpha(),
        pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\reci1.png")).convert_alpha()]
klucz = pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\klucz.png")).convert_alpha()
stary_klucz = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\stary_klucz.png")).convert_alpha(),
               pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\stary_klucz1.png")).convert_alpha(),
               pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\stary_klucz2.png")).convert_alpha()]
nowy_klucz = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\klucz_klodka.png")).convert_alpha(),
              pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\klucz_klodka1.png")).convert_alpha(),
              pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\klucz_klodka2.png")).convert_alpha()]
falklandy_drzwi = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\drzwi.png")).convert_alpha(),
                   pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\drzwi1.png")).convert_alpha()]
falklandy_klodka = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\klodka.png")).convert_alpha(),
                    pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\klodka1.png")).convert_alpha()]

szkola = [pygame.image.load(os.path.join(filepath, "data\\navi\\szkola0.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\szkola.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\szkola1.png")).convert_alpha()]

sensivity_range = pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\sensivity_range.png")).convert_alpha()
sensivity_point = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\sensivity_point.png")).convert_alpha(),
                   pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\sensivity_point1.png")).convert_alpha()]

zamek = [pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\zamek0.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\zamek1.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\zamek2.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\pics\\falklandy_map\\zamek3.png")).convert_alpha()]
# Banery plecaka
glass_banner = pygame.image.load(os.path.join(filepath, "data\\pics\\glass_banner.png")).convert_alpha()
help_banner = [pygame.image.load(os.path.join(filepath, "data\\pics\\pomoc.png")),
               pygame.image.load(os.path.join(filepath, "data\\pics\\pomoc1.png")).convert()]
