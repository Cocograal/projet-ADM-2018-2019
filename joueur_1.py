# -*- coding: utf-8 -*-
"""
création de la balle, des mouvements et des
options que le joueur 1 peut faire
"""
import munition as m
import canon_pour_direction as c

class Player_1():
    def __init__(self, window, canvas):
        # Pour savoir la position que doit avoir le canon
        self.index = 1
        # faire un dictionnaire vide pour pouvoir cliquer sur plusieurs
        # touches en même temps après
        self.continue_movement = {}
        # Créer le plateau où il y aura les objets dessus
        self.canvas = canvas
        # La balle qui bougera
        self.ball1 = self.canvas.create_rectangle(9, 9, 27, 27, fill="light green", outline = "light green")
        self.ball1_coords = self.canvas.coords(self.ball1)

        # Le canon
        self.cannon = c.gun(self.canvas, self.ball1)
        # On connecte les touches (keyboard, function)
        self.canvas.bind_all("<KeyPress>", lambda event: self.key_press(window, event))
        self.canvas.bind_all("<KeyRelease>", lambda event: self.key_release(window, event))
        self.canvas.pack()


    
    def move(self, window, event):
        """
        Fonction qui fais les mouvements
        """
        if event.keysym == "a":
            if self.ball1_coords[0] > 5:
                self.canvas.move(self.ball1, -5, 0)
                self.canvas.move(self.cannon, -5, 0)
                self.ball_coords()

        elif event.keysym == "w":
            if self.ball1_coords[1] > 5:
                self.canvas.move(self.ball1, 0, -5)
                self.canvas.move(self.cannon, 0, -5)
                self.ball_coords()

        elif event.keysym == "d":
            if self.ball1_coords[2] < 597:
                self.canvas.move(self.ball1, 5, 0)
                self.canvas.move(self.cannon, 5, 0)
                self.ball_coords()

        elif event.keysym == "s":
            if self.ball1_coords[3] < 597:
                self.canvas.move(self.ball1, 0, 5)
                self.canvas.move(self.cannon, 0, 5)
                self.ball_coords()

        self.canvas.update()
        # Le mouvement continu tant que key_release() ne l'arrête pas
        self.continue_movement[event.keysym] = window.after(100, lambda: 
                                                              self.move(window, event))

    def key_press(self, window, event):
        """
        Savoir si une touche a été appuyée
        """
        if (event.keysym in ("a", "w", "d", "s") and
            self.continue_movement.get(event.keysym) is None):
            self.move(window, event)
        elif (event.keysym == "space" and
            self.continue_movement.get(event.keysym) is None):
            self.shoot(window, event)
        elif event.keysym == "q":
            self.cannon = c.rotation(self.canvas, self.ball1, self.cannon, self.index)
            self.index += 1

    def key_release(self, window, event):
        """
        Pour savoir si une touche appuyée a été relachée
        """
        # Si une touche a été relachée on annule ce qu'elle faisait,
        # donc on annule la direction vers laquelle elle allait
        if (event.keysym in ("a", "w", "d", "s") and
            self.continue_movement.get(event.keysym) is not None):
            window.after_cancel(self.continue_movement[event.keysym])
            self.continue_movement[event.keysym] = None
        elif (event.keysym in ("<space>") and
              self.continue_movement.get(event.keysym) is not None):
            window.after_cancel(self.continue_movement[event.keysym])
            self.continue_movement[event.keysym] = None

    def shoot(self, window, event):
        """
        Quand on tire un missile
        """
        self.projectile = m.Missile(self.canvas, self.ball1, window, self.cannon)
        # Si le joueur maintient la touche pour tirer, il y a un temps
        # entre les deux tires
        self.continue_movement[event.keysym] = window.after(1000, lambda:
                                                            self.shoot(window, event))
    def ball_coords(self):
        self.ball1_coords = self.canvas.coords(self.ball1)