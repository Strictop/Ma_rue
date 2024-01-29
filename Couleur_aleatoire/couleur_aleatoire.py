#Dependance
from ma_rue import rue, affiche
from random import randint


def couleur_aleatoire():
    '''
    Renvoie une couleur HTML valide
    au format 'rgb(rouge, vert, bleu)'
    où rouge, vert et bleu sont des entiers
    compris entre 0 et 255 choisis aléatoirement.
    
    '''
    
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return f"rgb({r}, {g}, {b})"

# Tests
affiche(rue)
couleur = couleur_aleatoire()
rue.fill_style = couleur
rue.fill_rect(0, 0, rue.width, rue.height)
rue.font = '48px Lucida Console'
rue.text_align = 'center'
rue.stroke_text(couleur, rue.width/2, rue.height/2)

# Autres tests
from time import sleep
affiche(rue)
for i in range(30) :
    couleur = couleur_aleatoire()
    rue.fill_style = couleur
    rue.fill_rect(0, 0, rue.width, rue.height)
    rue.font = '48px Lucida Console'
    rue.text_align = 'center'
    rue.stroke_text(couleur, rue.width/2, rue.height/2)
    sleep(1)
