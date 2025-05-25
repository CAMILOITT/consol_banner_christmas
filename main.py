import os
import random
import threading
from time import sleep

from src.ascii.banner import list_banner_print
from src.utils.play_music import play_music

thread = threading.Thread(target=play_music, args=("./src/music/navidad_light.mp3", 10))


name = input("Ingresa tu nombre: ")
custom_message = input("Ingresa un mensaje personalizado: ")
os.system("clear")

thread.start()

list_banner_print[random.randrange(1, len(list_banner_print)) - 1](name, custom_message)
print(f"""¡ Hola {name} !
{custom_message}""")

sleep(5)
thread.join()
print("La música se detuvo.")
