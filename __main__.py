import customtkinter
from  PIL import Image

from interfaces.creation_compte import afficherPageCompte

if __name__ == '__main__':
    customtkinter.set_default_color_theme("theme/theme.json")
    logo = customtkinter.CTkImage(light_image=Image.open("icons/logo.png"), size=(150, 150))
    root = customtkinter.CTk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.title('KeepControl')
    im = customtkinter.CTkLabel(root, text="", image=logo)
    im.place(x=0, y=0)
    afficherPageCompte(root)
    root.mainloop()