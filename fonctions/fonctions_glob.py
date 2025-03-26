etape=0
def suivant(page1,page2):
    global etape
    if etape == 0:
       page1.suiv.place_forget()
       page1.frameForm.pack_forget()
       page1.barreCompte.configure(fg_color="#198754")
       page1.etapeCompte.configure(text_color="#198754")
       page2.frameConfig.place(x=200, y=20)
       etape += 1
       return
    elif etape == 1:
       page1.frameForm.pack_forget()
