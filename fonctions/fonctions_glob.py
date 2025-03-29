import os
import sys

import __main__
etape=0
def suivant(root,suiv,frameForm,crea,nomMaison):
    global etape
    if etape == 0:
        suiv.place_forget()
        if crea != None:
            crea.place_forget()
        frameForm.pack_forget()
        __main__.barreCompte.configure(fg_color="#198754")
        __main__.etapeCompte.configure(text_color="#198754")
        __main__.barreConf.configure(fg_color="#212529")
        __main__.etapeConf.configure(text_color="#212529")
        __main__.barreFin.configure(fg_color="#D9D9D9")
        __main__.etapeFin.configure(text_color="#D9D9D9")
        __main__.afficherPageConfig(root)
        etape+=1
        return
    elif etape == 1:
        suiv.place_forget()
        frameForm.place_forget()
        __main__.barreCompte.configure(fg_color="#198754")
        __main__.etapeCompte.configure(text_color="#198754")
        __main__.barreConf.configure(fg_color="#198754")
        __main__.etapeConf.configure(text_color="#198754")
        __main__.barreFin.configure(fg_color="#198754")
        __main__.etapeFin.configure(text_color="#198754")
        __main__.afficherPageRecap(root,suiv,nomMaison)
        etape+=1
    else:
        return
def redemarrer():
    """Redémarre l'application Tkinter."""
    python = sys.executable
    os.execl(python, python, *sys.argv)