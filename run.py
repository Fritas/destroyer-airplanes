from model.menu import Menu
from tkinter import Tk
#import sys
#sys.path.append("..")
#from menu import *

if __name__ == '__main__':
    root = Tk()
    root.wm_attributes("-topmost", False) # mantem a tela sempre em cima
    root.wm_attributes("-alpha", 1) # ('-alpha', 0) - Linux // ('-transparentcolor', 'white') - Windows
    Menu(root, 'Destroyer Airplanes', '#eeefff') # parametros --> Menu(root, titulo do formulario, cor do plano de fundo)
    root.mainloop()