'''

Importation des fonctions necesssaire

'''

from tkinter import *
from random import *
from tkinter.font import Font
import time
import tkinter as tk
from PIL import Image, ImageTk

###############################################################################
## Deplacements
###############################################################################

# Fonction pour deplacer vers la droite

def fctdroite(ev=None):
    [a,b] = Canevas.coords(rex_img)
    j=int((a)/Larg)
    i=int((b)/Haut)
    #print("Avant mvt droite",i,j)
    #print(a,b)
     
    if Level1[i][j+1]==0:
        Canevas.coords(rex_img,a+Larg,b)
        if Level1[i+1][j+1]==0:
            Canevas.coords(rex_img,a+Larg,b+Haut)
        saut_en_cour=False
    elif Level1[i][j+1]==2:
        Canevas.coords(rex_img,a-Larg*34,b+Haut*6)
    elif Level1[i][j+1]==4:
        Canevas.coords(rex_img,a-Larg*34,b+Haut*7)
    elif Level1[i][j+1]==6:
        messagebox.showwarning("Gagner", "Bravo niveau suivant")
        niveau_suivant()
        Canevas.coords(rex_img,Larg*1.5,Haut*5.3 )
    elif Level1[i][j+1]==9:
        messagebox.showwarning("Perdu", "Quitter")
        Mafenetre.destroy() 
    elif Level1[i][j+1]==5:
        messagebox.showwarning("Vous avez gagné le jeu bravo", "Quitter")
        Mafenetre.destroy()
    appariton_luke()
    déplacement_luke()
    touche_luke()
    
# Fonction pour deplacer vers la gauche

def fctgauche(ev=None):
    [a,b] = Canevas.coords(rex_img)
    j=int((a)/Larg)
    i=int((b)/Haut)
    #print(i,j)
    if Level1[i][j-1]==0:
        Canevas.coords(rex_img,a-Larg,b)
        if Level1[i+1][j-1]==0:
            Canevas.coords(rex_img,a-Larg,b+Haut)
    elif Level1[i][j-1]==9:
        messagebox.showwarning("Perdu", "Quitter")      
        Mafenetre.destroy()    
    déplacement_luke()
    touche_luke()
    
#Fonction saut et descente Rex

def collision_detection(x, y):
    # Fonction de détection de collisiondzqd  
    i = int(y/Larg)
    j = int(x/Haut+1)
    return Level1[i][j]!=0  # Collision si le personnage atteint un 1
    


saut_en_cour=False
def Saut(ev=None):
    global saut_en_cour
    global rex_img
    [a,b] = Canevas.coords(rex_img)
    j=int((a)/Larg)
    i=int((b)/Haut)
    #print("Avant saut",i,j)
    #print(a,b)
    if saut_en_cour==False and j<34 and i!=8: #bloqué dans certaines coordonées pour eviter que le personnage passe a travers le plafond.
        saut_en_cour=True
        [a, b] = Canevas.coords(rex_img)
        [c, d] = Canevas.coords(rex_img)
        
        x = 0
        #print(a, b, x)
        #print(saut_en_cour)
        # Montée de rex dans le saut
        for k in range(4):
            x +=Larg/(Larg*2)
            y = (-1) * x**2 + 4 * x
            a2 = a + int(x *Larg/2)
            b2 = b - int(y *Larg/2)
            # Vérification des collisions après chaque déplacement
            Canevas.coords(rex_img, a2, b2)
            time.sleep(0.1)
            Canevas.update()
        # Descente de rex dans le saut
        for k in range(4):
            x +=Larg/(Larg*2)
            y = (-1) * x**2 + 4 * x
            a2 = a + int(x *Larg/2)
            b2 = b - int(y *Larg/2)    
            #print('avantcollision' ,a2,b2)
            #print(a2/Larg, b2/Haut)
            # Vérification des collisions après chaque déplacement
            if collision_detection(a2, b2):
                #print('debutcollision' ,a2,b2)
                break
            else:
                Canevas.coords(rex_img, a2, b2)
                time.sleep(0.1)
                Canevas.update() 
        

        [a,b] = Canevas.coords(rex_img)
        j=int((a)/Larg)
        i=int((b)/Haut)
        #print(i,j)

        #descente apres le saut si besoin    
        if b<d:
            #print('collision detectée decalage',b,d,Haut)
            b = d-Haut
            a = c+Larg*2
            Canevas.coords(rex_img, a, b)
            #print('aprescollision decallage',b,a)
   
        [a,b] = Canevas.coords(rex_img)
        j=int((a)/Larg)
        i=int((b)/Haut)
        
        
        if Level1[i+1][j]==0 and Level1[i+2][j]==0:
            #print(i,j)
            Canevas.coords(rex_img,a,b+Haut*2)
            #print('tombe double car vide')
        elif Level1[i+1][j]==0 and Level1[i+2][j]!=0:
            #print(i,j)
            Canevas.coords(rex_img,a,b+Haut)
            #print('tombe car vide')
        elif Level1[i+1][j]==9:
            messagebox.showwarning("Perdu", "Quitter")
            Mafenetre.destroy()   
        else:
            Canevas.coords(rex_img,a,b)

        saut_en_cour=False



###############################################################################
## changer tableau
###############################################################################     
        if Level1[i][j]==2:
            Canevas.coords(rex_img,a-Larg*34,b+Haut*6)
        elif Level1[i][j]==4:
            Canevas.coords(rex_img,a-Larg*34,b+Haut*7)
        elif  Level1[i][j]==6:
            messagebox.showwarning("Gagner", "Bravo niveau suivant")
            niveau_suivant()
            Canevas.coords(rex_img,Larg*1.5,Haut*5.3 )
        appariton_luke()
        déplacement_luke()
        touche_luke()    
             #changer tableau
             
             
###############################################################################
## Le jedi.....
###############################################################################             
#ce qui conserne le  jedi


def déplacement_luke(ev=None):
    [a,b] = Canevas.coords(luke_img)
    j=int((a)/Larg)
    i=int((b)/Haut)
    s=1
    if j==30:
        s=-1
    if j==25:
        s=1
    Canevas.coords(luke_img, a+s*Larg, b)
    #touche_luke()
        
def touche_luke(ev=None):
    global rex_img
    [a,b] = Canevas.coords(rex_img)  
    j=int((a)/Larg)
    i=int((b)/Haut)
    [a2,b2] = Canevas.coords(luke_img)
    k=int((a2)/Larg)
    l=int((b2)/Haut)
    if j==k and i==l or j==k-1 and i==l:
        messagebox.showwarning("Perdu", "Quitter")
        Mafenetre.destroy()
        
def appariton_luke():
    [a,b] = Canevas.coords(rex_img)
    j=int((a)/Larg)
    i=int((b)/Haut)
    if i==18 and j==2:
        Canevas.coords(luke_img,Larg*27,Haut*18.4)
             
###############################################################################
## Fonction Tir
###############################################################################
 
# Fonction pour deplacer le tir 

tire=False
def tirerRex(ev=None):
    global tire
    global tir
    [a, b] = Canevas.coords(rex_img)
    tir=Canevas.create_image(a-Larg , b-Haut, image=tire_image)
    [a2,b2]=Canevas.coords(tir)
    deplacement_tir()
    
 

# Fonction pour déplacer le tir 

def deplacement_tir():
    [a,b]=Canevas.coords(tir)
    luke_coords = Canevas.coords(luke_img)
    '''
    print("_____________________________________________________________________")
    print("coords luke",luke_coords)
    print("A+Larg", a+Larg)
    print("luke_coords[0]+Larg",luke_coords[0]+Larg)
    print('b+Haut',b+Haut)
    print('luke_coords[1]+Haut',luke_coords[1]+Haut)
    print('a',a)
    print("b",b)
    '''
    #if  luke_coords[0]<a+Larg and luke_coords[0]+Larg>a and luke_coords[1]<b+Haut and luke_coords[1]+Haut>b:
    if  luke_coords[0]<a+Larg and luke_coords[1]<b+2*Haut and luke_coords[1]>b-Haut:   
        Canevas.coords(luke_img,-Larg*17, -Haut*5.4)
        Canevas.delete(tir)
    
    elif a<screen_width:
        Canevas.coords(tir,a + Larg,b)
        Mafenetre.after(30, deplacement_tir)   
    else:
        Canevas.delete(tir)
    collision_tir()
def collision_tir():
    global tir
    [a,b]=Canevas.coords(tir)
    j=int((a)/Larg)
    i=int((b)/Haut)
    print('collision_tir()',i,j)
    if Level1[i+1][j]!=0:
        Canevas.delete(tir)

 

 
###############################################################################
## Affichage Niveau
###############################################################################
#niveau

   

#affichage des niveaux
def affichage(Level1):
    #affichage du veritable  niveau

    i=0
    while i<len(Level1[0]):
        j=0
        while j<len(Level1):
            if Level1[j][i]==1:
                couleur='grey'
                Canevas.create_rectangle(1+Larg*i,1+Haut*j,Larg+Larg*i,Haut+Haut*j,fill=couleur)
            elif Level1[j][i]>=2 and Level1[j][i]<=6:
                couleur='green'
                Canevas.create_rectangle(1+Larg*i,1+Haut*j,Larg+Larg*i,Haut+Haut*j,fill=couleur)
            elif Level1[j][i]>=7:
                couleur='grey'
                Canevas.create_polygon(1 + Larg * i, Haut + Haut * j, Larg + Larg * i, Haut + Haut * j, (1 + Larg * i + Larg + Larg * i) / 2, 1 + Haut * j, fill=couleur)
            else:
                couleur='white'
                #Canevas.create_rectangle(1+Larg*i,1+Haut*j,Larg+Larg*i,Haut+Haut*j,fill=couleur) #Pour tester et se repererdd
            j=j+1
        i=i+1




        
#niveau suivant
def niveau_suivant(ev=None):
    global Level1
    Level1 = Level2
    affichage(Level1)


###############################################################################
## Creation des obstacles
###############################################################################



Level1=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,9,0,9,0,0,0,0,0,0,0,0,0,0,9,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,9,0,9,0,0,9,0,0,0,0,0,9,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,4,1],
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,9,0,0,0,0,9,0,0,0,0,9,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,6,1],
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ]]


Level2=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,9,0,1,1,1,1,1,1,1,1,1,0,0,9,0,9,0,9,0,9,0,9,0,9,0,9,0,9,0,9,0,1,0,0,2,1],
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,9,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,9,0,0,0,0,0,0,4,1],
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,9,0,9,0,9,1,9,0,0,0,9,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,5,1],
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
# Interface graphique



Mafenetre = tk.Tk()
Mafenetre.attributes('-fullscreen', True)  
Mafenetre.bind('<Escape>',lambda e: Mafenetre.destroy())  #si echap est touché on ferme la fenetre
Mafenetre.title("Titre")
Canevas = Canvas(Mafenetre, bg='white', highlightthickness=0)
Canevas.pack(fill=tk.BOTH, expand=True) # configurer le canevas pour qu'il occupe toute la fenêtre principale
font = Font(family='Liberation Serif', size=10)  # creation d'une police pour l'affichage du texte
screen_width = Mafenetre.winfo_screenwidth() #recuperation de la largueur de la fentre
screen_height = Mafenetre.winfo_screenheight()#recuperation de la largueur de la hauteur
#print (screen_width)  #38
#print (screen_height) #20
Larg = screen_width/38 #largeur
Haut = screen_height/20  #hauteur
#print(Larg)
#print(Haut)


fichier=PhotoImage(file='fond.gif')
img=Canevas.create_image(950,500,image=fichier)

affichage(Level1)

Large_Rex=int(Larg*1.5)
Haut_Rex=int(Haut*1.5) 
img=(Image.open("rex.gif"))
resized_image=img.resize((Large_Rex,Haut_Rex),Image.BILINEAR)
rex_image=ImageTk.PhotoImage(resized_image)

rex_image = PhotoImage(file='rex.gif')
rex_img = Canevas.create_image(Larg*1.5,Haut*5.3 , image=rex_image)

tire_image= PhotoImage(file='tire clone.gif')

luke_image = PhotoImage(file='luke_reverse.gif')
luke_img = Canevas.create_image(-Larg*27, -Haut*18.4, image=luke_image)


# Receptionnaire d'evenements

Canevas.bind_all('<d>', fctdroite)
Canevas.bind_all('<q>', fctgauche)
Canevas.bind_all('<Button-1>', tirerRex)
Canevas.bind_all('<space>', Saut)

# Programme principal

#fin

Mafenetre.mainloop()