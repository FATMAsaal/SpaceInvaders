
'''
o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
Space Invaders
Auteur: SAAL FATMA
Date : 20/11/2018
o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
'''


import time
from tkinter import *

class Jeu:
    def __init__(self,fenlargeur,fenhauteur):
        self.__fenlargeur=fenlargeur
        self.__fenhauteur=fenhauteur

        

   
        self.__Fen= Tk()
        #creation de la fenetre
        self.__Fenetre=Canvas(self.__Fen, height = self.__fenhauteur, width =self.__fenlargeur)
        #creation des rectangles
        self.EcranDePresentation()
        

        self.__Fen.title("space Invaders")
        self.debut=0

        self.__Fen.bind("<Up>", self.deplacement_canon_haut)
        self.__Fen.bind("<Down>", self.deplacement_canon_bas)
        self.__Fen.bind("<Left>", self.deplacement_canon_gauche)
        self.__Fen.bind("<Right>", self.deplacement_canon_droite)
        self.score=0
        self.vie=3
        self.Txt_score=self.__Fenetre.create_text(50,20,text="SCORE : 0")
        self.Txt_vie=self.__Fenetre.create_text(200,20,text="nombre de vies : 3")
        self.deplacement_rect()
        self.tuer_une_case()
        self.monBouton = Button(self.__Fen, text="nouvelle partie",command=self.nouvelle_partie).place(x=60, y=500, width=100, height=30)
        self.monBouton2 = Button(self.__Fen, text="Quitter",command=self.__Fen.destroy).place(x=200, y=500, width=100, height=30)

        self.__Fenetre.pack()
        self.__Fen.mainloop()



    def EcranDePresentation(self):
        self.Titre()


    def Titre(self):
        self.__Fenetre.create_text(220,150,font=('Fixedsys',24),text="SPACE INVADERS",fill='blue')


    def deplacement_canon_gauche(self,event):
        """
        cette methode gére le  déplacement a gauche du canon en cas
        de clique sur la fleche gauche du clavier
        """
        self.__Fenetre.move(self.__canon,-5,0)
    def deplacement_canon_droite(self,event):
        """
        cette methode gére le  déplacement a droite du canon en cas
        de clique sur la fleche droitedu clavier
        """
        self.__Fenetre.move(self.__canon,5,0)

    
    def deplacement_canon_bas(self,event):
        """
        cette methode gére le  déplacement a droite du canon en cas
        de clique sur la fleche droitedu clavier
        """
        self.__Fenetre.move(self.__canon,0,5)
    def deplacement_canon_haut(self,event):
        """
        cette methode gére le  déplacement a droite du canon en cas
        de clique sur la fleche droitedu clavier
        """
        self.__Fenetre.move(self.__canon,0,-5)
    

    def deplacement_rect(self):
        if self.debut==1:
            for i in self.__vivant:
                self.__Fenetre.move(i,0,+4)
        self.__Fenetre.after(500,self.deplacement_rect)

    def tuer_une_case(self):
        """
        le principe de cette fonction c'est de retirer une case de la liste vivant
        et l'ajouter dans la liste des cases mortes

        """
        if self.debut==1:
            for i in self.__vivant:

                if (self.__Fenetre.coords(i)[3]>=self.__Fenetre.coords(self.__ligne)[3]):
                    self.game_over()

                if self.__Fenetre.coords(i)[0]<=self.__Fenetre.coords(self.__canon)[0] and self.__Fenetre.coords(i)[1]<=self.__Fenetre.coords(self.__canon)[1] and self.__Fenetre.coords(i)[2]>=self.__Fenetre.coords(self.__canon)[2] and self.__Fenetre.coords(i)[3]>=self.__Fenetre.coords(self.__canon)[3]:


                    self.__vivant.remove(i)
                    self.__Fenetre.itemconfig(i,fill="red")
                    self.__mort.append(i)

                    self.score+=50
                    self.__Fenetre.itemconfig(self.Txt_score, text="SCORE : "+str(self.score))
                    #si une des cases atteint la ligne de limite se sera la fin de la parie (game over)
                    if len(self.__vivant)==0:
                        self.succes()

        self.__Fenetre.after(1,self.tuer_une_case)


    def game_over(self):
        """
        cette methode permet d'arreter le jeu quand le joueur a perdu
        """
        self.__Fenetre.create_text(250,250,text="GAME OVER !",fill="white")
        for i in self.__vivant:
            self.__Fenetre.itemconfig(i,fill="black")
            self.__vivant.remove(i)
        for i in self.__mort:
            self.__Fenetre.itemconfig(i,fill="black")
        self.__Fenetre.itemconfig(self.__canon,fill="black")

    def succes(self):
        """
        une methode qui permet d'afficher un message une fois c'est reussi
        """
        self.__Fenetre.create_text(250,250,text="Bravooooooooooooo vous avez reussi :) :) :) !",fill="red")
        for i in self.__vivant:
            self.__Fenetre.itemconfig(i,fill="black")
        for i in self.__mort:
            self.__Fenetre.itemconfig(i,fill="black")
        self.__Fenetre.itemconfig(self.__canon,fill="black")
        self.__Fenetre.itemconfig(self.Txt_score, text="SCORE : "+str(self.score),fill="white")

    def nouvelle_partie(self):
        """
        cette methode permet de quitter la partie d jeu courante et recommencer une nouvelle
        """

        self.__Fenetre.delete(ALL)
        self.debut=1
        c1 = self.__Fenetre.create_rectangle(10, 50, 50, 80, fill = "gray")
        c2 = self.__Fenetre.create_rectangle(60, 50, 100, 80, fill = "gray")
        c3 = self.__Fenetre.create_rectangle(110, 50, 150, 80, fill = "gray")
        c4 = self.__Fenetre.create_rectangle(160, 50, 200, 80, fill = "gray")
        c5 = self.__Fenetre.create_rectangle(210, 50, 250, 80, fill = "gray")
        c6 = self.__Fenetre.create_rectangle(260, 50, 300, 80, fill = "gray")
        c7 = self.__Fenetre.create_rectangle(310, 50, 350, 80, fill = "gray")
        c8 = self.__Fenetre.create_rectangle(360, 50, 400, 80, fill = "gray")

        c9 =  self.__Fenetre.create_rectangle(10, 120,50, 90, fill = "gray")
        c10 = self.__Fenetre.create_rectangle(60, 120,100, 90, fill = "gray")
        c11 = self.__Fenetre.create_rectangle(110, 120,150, 90, fill = "gray")
        c12 = self.__Fenetre.create_rectangle(160, 120,200, 90, fill = "gray")
        c13 = self.__Fenetre.create_rectangle(210, 120,250, 90, fill = "gray")
        c14 = self.__Fenetre.create_rectangle(260, 120,300, 90, fill = "gray")
        c15 = self.__Fenetre.create_rectangle(310, 120,350, 90, fill = "gray")
        c16 = self.__Fenetre.create_rectangle(360, 120,400, 90, fill = "gray")

        c17 = self.__Fenetre.create_rectangle(10, 160,50, 130, fill = "gray")
        c18 = self.__Fenetre.create_rectangle(60, 160,100, 130, fill = "gray")
        c19 = self.__Fenetre.create_rectangle(110, 160,150, 130, fill = "gray")
        c20 = self.__Fenetre.create_rectangle(160, 160,200, 130, fill = "gray")
        c21 = self.__Fenetre.create_rectangle(210, 160,250, 130, fill = "gray")
        c22 = self.__Fenetre.create_rectangle(260, 160,300, 130, fill = "gray")
        c23 = self.__Fenetre.create_rectangle(310, 160,350, 130, fill = "gray")
        c24 = self.__Fenetre.create_rectangle(360, 160,400, 130, fill = "gray")

        self.__canon=self.__Fenetre.create_oval(30,400,15,410,fill='green')
        self.__ligne = self.__Fenetre.create_rectangle(400,415,10,415, fill = "black")
        self.__vivant = [c1, c2, c3, c4, c5, c6, c7, c8,
                  c9,c10,c11,c12,c13,c14,c15,c16,
                  c17,c18,c19,c20,c21,c22,c23,c24]
        self.__mort = []
        self.score=0
        self.Txt_score=self.__Fenetre.create_text(50,20,text="SCORE : 0")



class Test:
    g=Jeu(410,600)
