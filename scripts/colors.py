from pystyle import Colorate, Colors
              
def purple(text):
    t = Colorate.Horizontal(Colors.purple_to_blue, f"{text}")
    return t

def blue(text):
    t = Colorate.Horizontal(Colors.blue_to_cyan, f"{text}")
    return t

def cyan(text):
    t = Colorate.Horizontal(Colors.cyan_to_green, f"{text}")
    return t

