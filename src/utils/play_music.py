import time

import pygame


def play_music(path, duration):
  pygame.mixer.init()
  pygame.mixer.music.load(path)
  pygame.mixer.music.play()
  time.sleep(duration)
  pygame.mixer.music.stop()
