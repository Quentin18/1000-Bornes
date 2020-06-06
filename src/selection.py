from src.coord import Coord


def carteSelectionnee(listeJoueurs, pos):
    """Retourne la carte sélectionnée dans la main du joueur sud."""
    if clickDansZone(pos, Coord.main_x, Coord.main_y,
                     Coord.main_width, Coord.main_length):
        numCarte = 0
        for i in range(0, 770, 110):
            if clickDansZone(pos, Coord.main_x + i, Coord.main_y,
                             Coord.carte_width, Coord.main_length):
                return listeJoueurs[0].main[numCarte], numCarte
            numCarte += 1
    return 'aucune', -1


def clickDansZone(pos, x, y, width, length):
    """
    Teste si le click (pos) se trouve dans le rectangle défini par
    son coin haut-gauche (x, y), sa longueur (width) et sa largeur (length).
    """
    return ((pos[0] >= x and pos[0] <= x + width)
            and (pos[1] >= y and pos[1] <= y + length))


def endroitSelectionne(listeJoueurs, pos):
    """
    Retourne l'endroit sélectionné où poser
    la carte sélectionnée préalablement.
    """
    if clickDansZone(pos, Coord.pot_x, Coord.pot_y,
                     Coord.pot_width, Coord.pot_length):
        return 'pot'
    else:
        for joueur in listeJoueurs:
            if clickDansZone(pos, joueur.emplacements_x,
                             joueur.emplacements_y, joueur.emplacements_width,
                             joueur.emplacements_length):
                return 'emplacements' + joueur.nom
    return 'aucun'
