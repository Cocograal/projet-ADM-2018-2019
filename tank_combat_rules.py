"""

I GOT NEW RULEZ I COUNT 'EM

"""
import tkinter as tk
import menu_jeu as mj

COMMAND1 = """W pour aller en haut
              \rA pour aller a gauche
              \rS pour aller en bas
              \rD pour aller à droite
              \rQ pour tourner le canon
              \respace pour tirer le missile"""
COMMAND2 = """
              \rflèche haut pour aller en haut
              \rflèche gauche pour aller a gauche
              \rflèche bas pour aller en bas
              \rflèche droite pour aller à droite
              \rL pour tourner le canon
              \rP pour tirer le missile
              """
RULES = """Ne pas toucher les obstacles et le lac
           \rLes missiles traversent le lac mais pas les obstacles"""
GOAL = "Toucher votre adversaire avec un missile"


def open_rules():
    root = tk.Tk()
    root.title("Tank Combat")
    Rules(root)
    root.mainloop()

class Rules():
    def __init__(self, root):
        self.rules_canvas = tk.Canvas(root, height=600, width=600, background="SkyBlue")
        self.rules_canvas.create_text(300, 50, text="COMMANDE")
        self.rules_canvas.create_text(60, 100, text="joueur 1:")
        self.rules_canvas.create_text(170, 200, text=COMMAND1)
        self.rules_canvas.create_text(340, 100, text="joueur 2:")
        self.rules_canvas.create_text(470, 200, text=COMMAND2)
        self.rules_canvas.create_text(300, 350, text="REGLES")
        self.rules_canvas.create_text(300, 400, text=RULES)
        self.rules_canvas.create_text(300, 450, text="BUT")
        self.rules_canvas.create_text(300, 500, text=GOAL)
        
        self.go_back = tk.Button(root, text="Retour au menu", command=lambda: self.back(root))
        self.backWindow = self.rules_canvas.create_window(300, 550, window=self.go_back)
        self.rules_canvas.pack()

    def back(self, root):
        root.destroy()
        mj.startMenu()
    
if __name__ == "__main__":
    open_rules()
