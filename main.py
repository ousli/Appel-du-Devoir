import tkinter as tk
import subprocess


class Menu(tk.Tk):
    def __init__(self):
        """
        Il crée un menu pour le jeu.
        """

        super().__init__()

        self.title("L'Appel du Devoir")

        # Création du canvas
        self.canvas = tk.Canvas(self, bg='#3498db', height=600, width=800)
        self.canvas.pack()

        # Titre du menu
        self.title = tk.Label(self.canvas, text='L\'Appel du Devoir', font=(
            'Verdana', 24), bg='#3498db', fg='#ecf0f1')
        self.title.place(relx=0.5, rely=0.1, anchor='n')

        # Bouton pour lancer la partie
        self.play_button = tk.Button(self.canvas, text='Jouer', font=('Verdana', 16), bg='#2ecc71', fg='#ecf0f1',
                                     activebackground='#27ae60', activeforeground='#ecf0f1', width=10, command=self.start_game)
        self.play_button.place(relx=0.5, rely=0.3, anchor='n')

        # Bouton pour quitter le jeu
        self.quit_button = tk.Button(self.canvas, text='Quitter', font=('Verdana', 16), bg='#e74c3c', fg='#ecf0f1',
                                     activebackground='#c0392b', activeforeground='#ecf0f1', width=10, command=self.quit_game)
        self.quit_button.place(relx=0.5, rely=0.5, anchor='n')

    def start_game(self):
        """
        Il détruit la fenêtre actuelle et ouvre une nouvelle fenêtre appelée game.py.
        """
        self.destroy()
        subprocess.call(['python', 'game.py'])

    def quit_game(self):
        """
        Il détruit la fenêtre
        """
        self.destroy()


# Créer une nouvelle instance de la classe Menu, puis appeler la méthode mainloop dessus.
menu = Menu()
menu.mainloop()
