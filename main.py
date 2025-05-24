import os
import random
from time import sleep

from src.ascii.banner import list_banner_print

# import pygame
# import time

# pygame.mixer.init()
# pygame.mixer.music.load("ruta/al/archivo.mp3")  # acepta .mp3 y .wav
# pygame.mixer.music.play()

# time.sleep(10)
# pygame.mixer.music.stop()


# from colorama import Fore, init

# init(autoreset=True)
# name = "Camilo Torres"
# custom_message = "¡Feliz Navidad!"
name = input("Ingresa tu nombre: ")
custom_message = input("Ingresa un mensaje personalizado: ")
os.system("clear")

list_banner_print[random.randrange(1, len(list_banner_print)) - 1](name, custom_message)
print(f"""¡ Hola {name} !
{custom_message}""")

sleep(1)
