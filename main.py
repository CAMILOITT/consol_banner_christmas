import os
import random
import threading
from time import sleep

from src.ascii.banner import list_banner_print
from src.utils.music.get_all_music import get_music
from src.utils.music.play_music import play_music

list_music = get_music()
music: str = list_music[random.randrange(1, len(list_music) - 1)]
thread = threading.Thread(target=play_music, args=(music, 10))

os.system("clear")
name = input("Ingresa tu nombre: ")
custom_message = input("Ingresa un mensaje personalizado: ")
os.system("clear")

thread.start()

list_banner_print[random.randrange(1, len(list_banner_print)) - 1](name, custom_message)
print(f"""¡ Hola {name} !
{custom_message}""")

sleep(5)
thread.join()
