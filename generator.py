import time
import threading

from scripts.functions import *
from scripts.colors import *
from scripts.ui import *

os.system(f'title Guilded Account Generator   I   Made by nrxlvyy   I   Join discord.gg/aquaticraider')
def main():
    ui()
    choice = input(f"{purple('Your Choice')} -> ")
    match choice:
        case "1":
            reset()
            count = int(input(f"{purple('Accounts Count')} -> "))
            if count > 0:
                reset()
                for _ in range(count):
                    threading.Thread(target=generate, args=()).start()
            main()

        case "2":
            reset()
            print(f"--> {purple('discord.gg/aquaticraider')} <--")
            time.sleep(3)
            main()

        case "3":
            exit()

        case _:
            main()

main()





