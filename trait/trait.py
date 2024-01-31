# Dépendances
from Ma_rue import rue, affiche

# Définitions

# Fonction trait()
def trait(x1,y1,x2,y2):
    '''
    dessine un trait entre les 2 points transmis en paramètres
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    
    '''
    rue.stroke_style = 'black'
    rue.stroke_line(x1, y1, x2, y2)

# Tests
affiche(rue)
trait(50, 25, rue.width/2, rue.height/2)

# Autres tests
for x in range (int(rue.width/2), rue.width + 1, 20) :
    trait(x, 0, 3*rue.width/2 - x, rue.height)