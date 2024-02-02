# Dépendances
from ma_rue import rue, affiche
from toit1 import toit1
from toit2 import toit2

# Définitions
import random

#Fonction toits
def toits(x, y_sol, niveau):
    '''
    Dessine aléatoirement un toit plat ou un toit en pointe
    à l'ordonnée du niveau passé en paramètre
    Paramètres
        x : abscisse du centre de l'étage
        y_sol: ordonnée du sol
        niveau : numéro de l'étage en partant de 0 pour le rdc
    '''
    # On a le choix entre deux type de toits
    type_toit = random.choice(['plat', 'pointe'])
    
    if type_toit == 'plat':
        # Dessiner un toit plat
        toit2(x, niveau)
    elif type_toit == 'pointe':
        # Dessiner un toit en pointe
        toit1(x, niveau)

