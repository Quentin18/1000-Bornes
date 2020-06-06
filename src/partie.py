from src.joueur import Joueur
from src.jeu import Jeu
from src.sons import Sons
from random import shuffle
import src.selection as selection


class Partie:
    """Gère une partie."""
    def __init__(self, listePoints, nom):
        """Initialise une partie."""
        # Initialisation de la liste de stats des kms
        self.statsKm = [[], [], [], []]
        # Préparation de la pioche
        self.pioche = (
            Jeu.listeAttaques * 3
            + ['feu_rouge'] * 2
            + ['limite_de_vitesse']
            + Jeu.listeParades * 6
            + ['feu_vert'] * 8
            + Jeu.listeBottes
            + Jeu.listeKM * 4
            + ['100'] * 8
            + ['25', '50', '75'] * 6)
        shuffle(self.pioche)
        self.pot = []
        self.listeJoueurs = self.creationJoueurs(listePoints, nom)

    def creationJoueurs(self, listePoints, nom):
        """Crée les 4 joueurs et les place dans une liste."""
        listeNoms = [nom, 'Ouest', 'Nord', 'Est']
        listeOrientations = ['sud', 'ouest', 'nord', 'est']
        liste = []
        for i in range(4):
            liste.append(Joueur(
                listeNoms[i],
                listeOrientations[i],
                listePoints[i],
                self.pioche))
        return liste

    def tousBloque(self):
        """Retourne True si tous les joueurs sont bloqués."""
        for i in self.listeJoueurs:
            if not i.bloque:
                return False
        return True

    def listeJoueursTri(self):
        """
        Retourne la liste des joueurs du plus avancé en km
        au moins avancé.
        """
        listeTri = []
        for joueur in self.listeJoueurs[::-1]:
            i = 0
            while len(listeTri) > i and listeTri[i].km >= joueur.km:
                i += 1
            listeTri.insert(i, joueur)
        return listeTri

    def joueJoueurSud(self, pos, pot, carteChoisie, endroitChoisi):
        """
        Fait jouer le joueur sud en fonction de la carte et de
        l'endroit choisi.
        """
        if endroitChoisi == 'pot':
            # Jette une carte
            pot.append(self.listeJoueurs[0].main.pop(
                self.listeJoueurs[0].main.index(carteChoisie)))
            return ''.join([
                self.listeJoueurs[0].nom,
                " a jeté la carte : ",
                Jeu.dicoNomsCartes[carteChoisie],
                "."])
        else:
            for joueur in self.listeJoueurs:
                if endroitChoisi == 'emplacements' + joueur.nom:
                    j = 0
                    if joueur.rotation:
                        borneSup = joueur.emplacements_length
                    else:
                        borneSup = joueur.emplacements_width
                    for i in range(0, borneSup, 110):
                        if ((not joueur.rotation
                                and selection.clickDansZone(
                                    pos,
                                    joueur.emplacements_x + i,
                                    joueur.emplacements_y,
                                    110,
                                    joueur.emplacements_length))
                                or (joueur.rotation
                                    and selection.clickDansZone(
                                        pos,
                                        joueur.emplacements_x,
                                        joueur.emplacements_y + i,
                                        joueur.emplacements_width,
                                        110))):
                            if joueur.orientation == 'sud':
                                if (carteChoisie
                                        in Jeu.dicoEmplacementsCartesValides[
                                            Jeu.nomsEmplacements[j]]):
                                    if (j >= 2 and (not joueur.bloque and (
                                        not joueur.limite
                                        or int(carteChoisie) <= 50)
                                        and int(
                                            carteChoisie) + joueur.km <= 1000)
                                        and (carteChoisie != '200'
                                        or len(
                                            joueur.cartesEmplacements[2])
                                            < 2)):
                                        # Pose un km
                                        joueur.cartesEmplacements[j].append(
                                            joueur.main.pop(
                                                joueur.main.index(
                                                    carteChoisie)))
                                        joueur.km += int(carteChoisie)
                                        if carteChoisie == '200':
                                            Sons.woohooSound.play()
                                        return ''.join([
                                            joueur.nom,
                                            " a posé ",
                                            carteChoisie,
                                            " km."])
                                    else:
                                        if (len(joueur.cartesEmplacements[j])
                                                != 0 and carteChoisie
                                                in Jeu.listeParades
                                                and carteChoisie
                                                == Jeu.dicoAttaquesParades[
                                                    joueur.cartesEmplacements[
                                                        j][-1]]):
                                            # Pose une parade
                                            joueur.cartesEmplacements[
                                                j].append(joueur.main.pop(
                                                    joueur.main.index(
                                                        carteChoisie)))
                                            if j == 0:
                                                joueur.bloque = False
                                            elif j == 1:
                                                joueur.limite = False
                                            if carteChoisie == 'feu_vert':
                                                Sons.startSound.play()
                                            return ''.join([
                                                joueur.nom,
                                                " a contré l'attaque : ",
                                                Jeu.dicoNomsCartes[
                                                    carteChoisie],
                                                "."])
                                elif carteChoisie in Jeu.listeBottes:
                                    # Pose une botte
                                    joueur.bottes.append(joueur.main.pop(
                                        joueur.main.index(carteChoisie)))
                                    nbPoints = 100
                                    # Cas de coup fourré
                                    # (remise de l'attaque dans le pot)
                                    if (joueur.bloque and carteChoisie
                                            == Jeu.dicoAttaquesBottes[
                                                joueur.cartesEmplacements[
                                                    0][-1]]):
                                        pot.append(
                                            joueur.cartesEmplacements[
                                                0].pop(-1))
                                        joueur.bloque = False
                                        nbPoints += 300
                                    if (joueur.limite and carteChoisie
                                            == Jeu.dicoAttaquesBottes[
                                                joueur.cartesEmplacements[
                                                    1][-1]]):
                                        pot.append(
                                            joueur.cartesEmplacements[
                                                1].pop(-1))
                                        joueur.limite = False
                                        nbPoints += 300
                                    if (joueur.bottes[-1]
                                            == 'vehicule_prioritaire'):
                                        Sons.sireneSound.play()
                                    else:
                                        Sons.winningSound.play()
                                    joueur.points += nbPoints
                                    return ''.join([
                                        joueur.nom,
                                        " a posé la botte : ",
                                        Jeu.dicoNomsCartes[joueur.bottes[-1]],
                                        " ! ",
                                        str(nbPoints),
                                        " points"])
                            else:
                                if ((j < 2 and carteChoisie
                                        in Jeu.dicoEmplacementsCartesValides[
                                            Jeu.nomsEmplacements[j]])
                                        and (carteChoisie in Jeu.listeAttaques)
                                        and (len(joueur.cartesEmplacements[j])
                                             == 0 or (
                                        len(joueur.cartesEmplacements[j])
                                        != 0 and joueur.cartesEmplacements[j][
                                            -1]
                                        in Jeu.listeParades))
                                        and Jeu.dicoAttaquesBottes[
                                            carteChoisie]
                                        not in joueur.bottes):
                                    # Pose une attaque
                                    joueur.cartesEmplacements[j].append(
                                        self.listeJoueurs[0].main.pop(
                                            self.listeJoueurs[0].main.index(
                                                carteChoisie)))
                                    if j == 0:
                                        joueur.bloque = True
                                        if carteChoisie == 'accident':
                                            Sons.crashSound.play()
                                        elif (carteChoisie
                                                == 'panne_essence'):
                                            Sons.panneSound.play(maxtime=3000)
                                    elif j == 1:
                                        joueur.limite = True
                                        Sons.hornSound.play()
                                    return ''.join([
                                        self.listeJoueurs[0].nom,
                                        " a attaqué ",
                                        joueur.nom,
                                        " : ",
                                        Jeu.dicoNomsCartes[carteChoisie],
                                        "."])
                        j += 1
        return ''
