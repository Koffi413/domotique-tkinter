import __main__

etape=0
def suivant(root,suiv,frameForm,barreCompte,etapeCompte):
    global etape
    if etape == 0:
        suiv.place_forget()
        frameForm.pack_forget()
        barreCompte.configure(fg_color="#198754")
        etapeCompte.configure(text_color="#198754")
        __main__.afficherPageConfig(root)
        etape+=1
        return
    elif etape == 1:
        frameForm.pack_forget()



