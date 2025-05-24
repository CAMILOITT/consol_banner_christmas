import os
from time import sleep

from colorama import Fore, init

import src.ascii.banner as banner

init(autoreset=True)

name = input("Ingresa tu nombre: ")
custom_message = input("Ingresa un mensaje personalizado: ")
os.system("clear")


banner.print_banner()


head = f"{Fore.LIGHTMAGENTA_EX} ¡Hola, {name}!"

print(Fore.LIGHTMAGENTA_EX + "¡Hola, {}! {}".format(name, custom_message))


sleep(1)
print(os.name)
