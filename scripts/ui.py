import os

from .colors import *
          
def clear():
    os.system('cls')

def reset():
    clear(); banner()

def banner():
    banner = f"""

               ______      _ __    __         __   ______         
              / ____/_  __(_) /___/ /__  ____/ /  / ____/__  ____ 
             / / __/ / / / / / __  / _ \/ __  /  / / __/ _ \/ __ /
            / /_/ / /_/ / / / /_/ /  __/ /_/ /  / /_/ /  __/ / / /
            \____/\__,_/_/_/\__,_/\___/\__,_/   \____/\___/_/ /_/ 
            
    """

    print(f"{purple(banner)}")

def menu():
    print(f"""
                            {purple('01')} Generate Accounts        
                            {purple('02')} Join Our Discord        
                            {purple('03')} Exit
    """)

def ui():
    clear(); banner(); menu()
