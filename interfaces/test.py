import sys
import os
import tkinter as tk

def redemarrer():
    """Redémarre l'application Tkinter."""
    python = sys.executable
    os.execl(python, python, *sys.argv)  # Relance le script actuel

# Exemple d'interface Tkinter
root = tk.Tk()
root.title("Exemple Tkinter")

label = tk.Label(root, text="Cliquez sur le bouton pour redémarrer l'application")
label.pack(pady=10)

bouton = tk.Button(root, text="Redémarrer", command=redemarrer)
bouton.pack(pady=10)

root.mainloop()
