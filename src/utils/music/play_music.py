import time

import pygame


def play_music(path, duration):
  pygame.mixer.init()
  pygame.mixer.music.load(f"src/music/{path}")
  pygame.mixer.music.play()
  time.sleep(duration)
  pygame.mixer.music.fadeout(duration - 1)
  pygame.mixer.music.stop()
