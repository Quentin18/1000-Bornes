from src.interface import Coord
from src.sons import Sons
from src.jeu import Jeu


def listeJoueursTri(listeJoueurs):
    """Retourne la liste des joueurs du plus avancé en km au moins avancé."""
    listeTri = []
    for joueur in listeJoueurs[::-1]:
        i = 0
        while len(listeTri) > i and listeTri[i].km >= joueur.km:
            i += 1
        listeTri.insert(i, joueur)
    return listeTri


class Joueur(object):
    """Crée un joueur de la partie."""
    def __init__(self, nom, orientation, points, pioche):
        """Initialise un joueur."""
        self.nom = nom
        self.orientation = orientation
        self.km = 0
        self.points = points
        self.main = []
        self.distribueJoueur(pioche)
        self.cartesEmplacements = [['feu_rouge'], [], [], [], [], [], []]
        self.bloque = True
        self.limite = False
        self.bottes = []
        if orientation == 'sud':
            self.emplacements_x = 350
            self.emplacements_y = Coord.length - 310
            self.emplacements_width = 110 * 7
            self.emplacements_length = 150
            self.rotation = False
            self.coord_nom = (int(Coord.width / 2) - 50, Coord.length - 340)
        elif orientation == 'nord':
            self.emplacements_x = 350
            self.emplacements_y = 50
            self.emplacements_width = 110 * 7
            self.emplacements_length = 150
            self.rotation = False
            self.coord_nom = (int(Coord.width / 2) - 50, 220)
        elif orientation == 'ouest':
            self.emplacements_x = 50
            self.emplacements_y = 20
            self.emplacements_width = 150
            self.emplacements_length = 110 * 7
            self.rotation = True
            self.coord_nom = (240, int(Coord.length / 2))
        elif orientation == 'est':
            self.emplacements_x = Coord.width - 200
            self.emplacements_y = 20
            self.emplacements_width = 150
            self.emplacements_length = 110 * 7
            self.rotation = True
            self.coord_nom = (Coord.width - 400, int(Coord.length / 2))
        else:
            print('Erreur : mauvaise orientation.')

    def trieMain(self):
        """
        Trie la main prise en paramètre en plaçant de gauche à droite
        les kms, les attaques, les parades puis les bottes."""
        kmMain, attaquesMain, paradesMain, bottesMain = [], [], [], []
        for carte in self.main:
            if carte in Jeu.listeKM:
                i = 0
                while len(kmMain) > i and int(kmMain[i]) >= int(carte):
                    i += 1
                kmMain.insert(i, carte)
            elif carte in Jeu.listeAttaques:
                if carte in attaquesMain:
                    attaquesMain.insert(attaquesMain.index(carte), carte)
                else:
                    attaquesMain.append(carte)
            elif carte in Jeu.listeParades:
                if carte in paradesMain:
                    paradesMain.insert(paradesMain.index(carte), carte)
                else:
                    paradesMain.append(carte)
            elif carte in Jeu.listeBottes:
                bottesMain.append(carte)
        self.main = kmMain + attaquesMain + paradesMain + bottesMain

    def distribueJoueur(self, pioche):
        """Distribue 6 cartes au joueur au début de la partie."""
        for _ in range(6):
            self.main.append(pioche.pop(0))
        self.trieMain()

    def joue(self, listeJoueurs, pioche, pot):
        """Fais joueur un joueur automatiquement."""
        # Pioche une carte
        self.main.append(pioche.pop(0))
        # Choisit l'action
        if not self.bloque:
            for i in Jeu.listeKM:
                # Conditions : vérifie si <= 50 si limité,
                # ne dépasse pas 1000 et 2 * 200 km max
                if (i in self.main and (not self.limite or int(i) <= 50)
                        and int(i) + self.km <= 1000
                        and (i != '200'
                             or len(self.cartesEmplacements[2]) < 2)):
                    # Pose des km
                    self.cartesEmplacements[
                        Jeu.nomsEmplacements.index(i)].append(
                            self.main.pop(self.main.index(i)))
                    self.km += int(i)
                    if i == '200':
                        Sons.woohooSound.play()
                    return self.nom + " a posé " + i + " km.", False
        else:
            if (Jeu.dicoAttaquesBottes[self.cartesEmplacements[0][-1]]
                    in self.main):
                # Contre l'attaque avec une botte
                self.bottes.append(self.main.pop(
                    self.main.index(
                        Jeu.dicoAttaquesBottes[
                            self.cartesEmplacements[0][-1]])))
                pot.append(self.cartesEmplacements[0].pop(-1))
                self.bloque = False
                if self.bottes[-1] == 'vehicule_prioritaire':
                    Sons.sireneSound.play()
                    if self.limite:
                        # Cas de coup fourré avec feu rouge + limite
                        pot.append(self.cartesEmplacements[1].pop(-1))
                        self.limite = False
                else:
                    Sons.winningSound.play()
                self.points += 400
                return ''.join([
                    self.nom,
                    " a posé la botte : ",
                    Jeu.dicoNomsCartes[self.bottes[-1]],
                    " ! 400 points"]), True
            elif (Jeu.dicoAttaquesParades[self.cartesEmplacements[0][-1]]
                    in self.main):
                # Contre l'attaque avec une parade
                self.cartesEmplacements[0].append(
                    self.main.pop(self.main.index(
                        Jeu.dicoAttaquesParades[
                            self.cartesEmplacements[0][-1]])))
                self.bloque = False
                if self.cartesEmplacements[0][-1] == 'feu_vert':
                    Sons.startSound.play()
                return ''.join([
                    self.nom,
                    " a contré l'attaque : ",
                    Jeu.dicoNomsCartes[self.cartesEmplacements[0][-1]],
                    "."]), False
        if (self.limite
                and Jeu.dicoAttaquesBottes[self.cartesEmplacements[1][-1]]
                in self.main):
            # Contre la limite de vitesse avec une botte
            self.bottes.append(self.main.pop(
                self.main.index(
                    Jeu.dicoAttaquesBottes[
                        self.cartesEmplacements[1][-1]])))
            pot.append(self.cartesEmplacements[1].pop(-1))
            self.limite = False
            Sons.sireneSound.play()
            self.points += 400
            return ''.join([
                self.nom,
                " a posé la botte : ",
                Jeu.dicoNomsCartes[self.bottes[-1]],
                " ! 400 points"]), True
        elif (self.limite
                and Jeu.dicoAttaquesParades[self.cartesEmplacements[1][-1]]
                in self.main):
            # Contre la limite de vitesse avec une fin de limite
            self.cartesEmplacements[1].append(
                self.main.pop(self.main.index(
                    Jeu.dicoAttaquesParades[
                        self.cartesEmplacements[1][-1]])))
            self.limite = False
            return self.nom + " a contré la limite de vitesse.", False
        # Regarde si il peut attaquer
        for i in Jeu.listeAttaques:
            if i in self.main:
                for joueur in listeJoueursTri(listeJoueurs):
                    if joueur.orientation != self.orientation:
                        if i != 'limite_de_vitesse':
                            if ((len(joueur.cartesEmplacements[0]) == 0
                                    or joueur.cartesEmplacements[0][-1]
                                    in Jeu.listeParades)
                                    and Jeu.dicoAttaquesBottes[i]
                                    not in joueur.bottes):
                                # Pose une attaque
                                joueur.cartesEmplacements[0].append(
                                    self.main.pop(self.main.index(i)))
                                joueur.bloque = True
                                if (joueur.cartesEmplacements[0][-1]
                                        == 'accident'):
                                    Sons.crashSound.play()
                                elif (joueur.cartesEmplacements[0][-1]
                                        == 'panne_essence'):
                                    Sons.panneSound.play(maxtime=3000)
                                return ''.join([
                                    self.nom,
                                    " a attaqué ",
                                    joueur.nom,
                                    " : ",
                                    Jeu.dicoNomsCartes[
                                        joueur.cartesEmplacements[0][-1]],
                                    "."]), False
                        else:
                            if ((len(joueur.cartesEmplacements[1]) == 0
                                    or joueur.cartesEmplacements[1][-1]
                                    in Jeu.listeParades)
                                    and Jeu.dicoAttaquesBottes[i]
                                    not in joueur.bottes):
                                # Pose une limitation
                                joueur.cartesEmplacements[1].append(
                                    self.main.pop(self.main.index(i)))
                                joueur.limite = True
                                Sons.hornSound.play()
                                return ''.join([
                                    self.nom,
                                    " a attaqué ",
                                    joueur.nom,
                                    " : ",
                                    Jeu.dicoNomsCartes[
                                        joueur.cartesEmplacements[1][-1]],
                                    "."]), False
        # Pose une botte (pas de coup fourré)
        for i in Jeu.listeBottes:
            if i in self.main:
                self.bottes.append(self.main.pop(self.main.index(i)))
                if i == 'vehicule_prioritaire':
                    Sons.sireneSound.play()
                else:
                    Sons.winningSound.play()
                self.points += 100
                return ''.join([
                    self.nom,
                    " a posé la botte : ",
                    Jeu.dicoNomsCartes[i],
                    " ! 100 points"]), True
        # Doit jeter une carte
        for i in self.main:
            if (i in Jeu.listeParades
                    and Jeu.dicoParadesBottes[i] in self.bottes):
                # Jette une parade dont le joueur a la botte correspondante
                pot.append(self.main.pop(self.main.index(i)))
                return ''.join([
                    self.nom,
                    " a jeté la carte : ",
                    Jeu.dicoNomsCartes[i],
                    "."]), False
        listeOrdreAJetter = (['25', '50'] + Jeu.listeParades + ['75', '100']
                             + Jeu.listeAttaques + ['200'])
        for i in listeOrdreAJetter:
            if i in self.main:
                # Jette une carte
                pot.append(self.main.pop(self.main.index(i)))
                return ''.join([
                    self.nom,
                    " a jeté la carte : ",
                    Jeu.dicoNomsCartes[i],
                    "."]), False
        return '', False

    def phaseCritique(self):
        """
        Fais jouer un joueur quand il n'y a plus de pioche.
        """
        if not self.bloque:
            for i in Jeu.listeKM:
                if (i in self.main and (not self.limite or int(i) <= 50)
                        and int(i) + self.km <= 1000
                        and (i != '200'
                             or len(self.cartesEmplacements[2]) < 2)):
                    # Pose des km
                    self.cartesEmplacements[
                        Jeu.nomsEmplacements.index(i)].append(
                            self.main.pop(self.main.index(i)))
                    self.km += int(i)
                    if i == '200':
                        Sons.woohooSound.play()
                    return self.nom + " a posé " + i + " km."
        # Le joueur est bloqué
        self.bloque = True
        return self.nom + " est bloqué."
