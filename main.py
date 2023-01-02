import tkinter as tk


def start_game():
    window.destroy()

    exec(open('game.py').read())


def quit_game():
    window.destroy()


# Création de la fenêtre principale
window = tk.Tk()
window.title("Appel du Devoir")

# Création du canvas
canvas = tk.Canvas(window, bg='#3498db', height=600, width=800)
canvas.pack()
# Titre du menu
title = tk.Label(canvas, text='Appel du Devoir', font=(
    'Verdana', 24), bg='#3498db', fg='#ecf0f1')
title.place(relx=0.5, rely=0.1, anchor='n')
# Bouton pour lancer la partie
play_button = tk.Button(canvas, text='Jouer', font=('Verdana', 16), bg='#2ecc71', fg='#ecf0f1',
                        activebackground='#27ae60', activeforeground='#ecf0f1', width=10, command=start_game)
play_button.place(relx=0.5, rely=0.3, anchor='n')


# Bouton pour quitter le jeu
quit_button = tk.Button(canvas, text='Quitter', font=('Verdana', 16), bg='#e74c3c', fg='#ecf0f1',
                        activebackground='#c0392b', activeforeground='#ecf0f1', width=10, command=quit_game)
quit_button.place(relx=0.5, rely=0.5, anchor='n')

window.mainloop()
