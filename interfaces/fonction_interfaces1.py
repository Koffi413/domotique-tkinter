def etats(barreCompte,etapeCompte, barreConf, etapeConf, barreFin,etapeFin):
    etape = 0
    if etape == 0:
        barreCompte.configure(fg_color="#212529")
        etapeCompte.configure(text_color="#212529")
        barreConf.configure(fg_color= "#D9D9D9")
        etapeConf.configure(text_color= "#D9D9D9")
        barreConf.configure(fg_color= "#D9D9D9")
        barreFin.configure(fg_color= "#D9D9D9")
        etapeFin.configure(text_color= "#D9D9D9")