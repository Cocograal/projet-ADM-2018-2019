
"""
Dossier qui contient les collisions
pour le jeu
"""
import tkinter as tk
import tkinter.messagebox as tkm
import joueur_1 as j1
import joueur_2 as j2
import Map_1 as map
import menu_jeu as mj


class SameCanvas():
    def __init__(self, window):
        self.canvas = tk.Canvas(window, height=600, width=600,
                                background="DeepSkyBlue2")
        self.player1 = j1.Player_1(window, self.canvas)
        self.player2 = j2.Player_2(window, self.canvas)
        obstacles = map.chart(self.canvas)
        for obstacle in obstacles:
            obstacle
        self.canvas.pack()
        # Un bouton pour quitter l'interface
        self.button = tk.Button(window, text="Quitter", command=window.destroy)
        self.button.pack()
        self.impact(window)

    def impact(self, window):
        """
        Voir s'il y a un impacte entre les objets
        """
        self.len_overlap1 = len(self.canvas.
                               find_overlapping(self.player1.ball1_coords[0] - 5,
                                                self.player1.ball1_coords[1] - 5,
                                                self.player1.ball1_coords[2] + 5,
                                                self.player1.ball1_coords[3] + 5))
        self.len_overlap2 = len(self.canvas.
                               find_overlapping(self.player2.ball2_coords[0] - 5,
                                                self.player2.ball2_coords[1] - 5,
                                                self.player2.ball2_coords[2] + 5,
                                                self.player2.ball2_coords[3] + 5))

        if self.len_overlap1 > 2 and self.len_overlap2 > 2:
            self.choice = tkm.askretrycancel("Collision",
                                        """Les deux joueurs sont entrés en
                                        \rcollision, Voulez vous refaire
                                        \rune partie?""")
            self.restart_or_stop = self.restart_or_stop(self.choice, window)

        elif self.len_overlap1 > 2:
            #self.canvas.destroy()
            self.canvas.create_rectangle(self.player1.ball1_coords[0]-30,
                                       self.player1.ball1_coords[1],
                                       self.player1.ball1_coords[0]-27,
                                       self.player1.ball1_coords[3],
                                       fill='red') #D
            
            self.choice = tkm.askretrycancel("Collision", """Le joueur 1 a perdu,
                               \rVoulez vous refaire une partie?""")
            self.restart_or_stop = self.restart_or_stop(self.choice, window)
            
        elif self.len_overlap2 > 2:
            self.canvas.create_rectangle(self.player2.ball2_coords[0]-30,
                                       self.player2.ball2_coords[1],
                                       self.player2.ball2_coords[0]-27,
                                       self.player2.ball2_coords[3],
                                       fill='red')
            self.choice = tkm.askretrycancel("Collision", """Le joueur 2 a perdu,
                               \rVoulez vous refaire une partie?""")
            self.restart_or_stop = self.restart_or_stop(self.choice, window)

        self.try_impact = window.after(1, lambda: self.impact(window))

    def restart_or_stop(self, answer, window):
        """
        Savoir si recommencer ou rejouer
        """
        if answer == True:
            return self.restartGame(window)
        elif answer == False:
            return self.stop(window)

    def stop(self, window):
        """
        Fonction qui ramene au menu principal
        """
        window.destroy()
        mj.startMenu()

    def restartGame(self, window):
        """
        Fonction qui recommence une partie
        """
        window.destroy()
        launchGame()

def launchGame():
    window = tk.Tk()
    SameCanvas(window)
    window.mainloop()


if __name__ == "__main__":
    launchGame()