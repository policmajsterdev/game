import os.path
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
filepath = os.path.dirname(__file__)

# Grafiki okna tytułowego

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
