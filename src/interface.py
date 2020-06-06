import pygame
from time import time
from src.images import Images
from src.coord import Coord
from src.couleurs import Couleurs
import src.selection as selection
import src.stats as stats


class Interface:
    """Gère l'interface du jeu."""
    def __init__(self):
        """Crée la fenêtre."""
        self.width = Coord.width
        self.length = Coord.length
        self.bgColor = Couleurs.WHITE
        self.screen = pygame.display.set_mode([self.width, self.length])
        self.font = pygame.font.SysFont('impact', 20)
        pygame.display.set_caption('1000 Bornes')

        # Icône
        icone = pygame.image.load('./images/icone.png')
        pygame.display.set_icon(icone)

        # Noms des emplacements des cartes
        self.nomsEmplacements = ['Attaques', 'Limitations', '200',
                                 '100', '75', '50', '25']

    def afficheTexte(self, texte):
        """Affiche le texte en paramètre en haut de la fenêtre."""
        text = self.font.render(texte, 1, Couleurs.BLUE)
        self.screen.blit(text, (350, 20))

    def afficheNoms(self, listeJoueurs, orientationJoueurQuiJoue):
        """
        Affiche les noms des joueurs.
        Celui du joueur qui joue apparait avec un fond vert.
        """
        for joueur in listeJoueurs:
            if joueur.orientation == orientationJoueurQuiJoue:
                color = Couleurs.GREEN
            else:
                color = Couleurs.RED
            text = self.font.render(joueur.nom + ' : '
                                    + str(joueur.km) + ' km, '
                                    + str(joueur.points) + ' pts',
                                    1, Couleurs.BLUE, color)
            self.screen.blit(text, joueur.coord_nom)

    def afficheBottes(self, listeJoueurs):
        """
        Affiche les bottes des joueurs.
        Celles-ci apparaissent à côté des attaques.
        """
        for joueur in listeJoueurs:
            i = 90
            for botte in joueur.bottes:
                if joueur.orientation == 'sud':
                    self.screen.blit(Images.dicoCartesImages[botte],
                                     (joueur.emplacements_x - 20 - i,
                                     joueur.emplacements_y + 5))
                elif joueur.orientation == 'ouest':
                    imageTourne = pygame.transform.rotate(
                        Images.dicoCartesImages[botte], 90)
                    self.screen.blit(imageTourne,
                                     (joueur.emplacements_x + 20 + i,
                                      joueur.emplacements_y + 5))
                elif joueur.orientation == 'nord':
                    self.screen.blit(Images.dicoCartesImages[botte],
                                     (joueur.emplacements_x + 5,
                                      joueur.emplacements_y + 20 + i))
                elif joueur.orientation == 'est':
                    imageTourne = pygame.transform.rotate(
                        Images.dicoCartesImages[botte], 90)
                    self.screen.blit(imageTourne,
                                     (joueur.emplacements_x - 20 - i,
                                      joueur.emplacements_y + 5))
                i -= 20

    def afficheEmplacementsCartes(self, listeJoueurs):
        """
        Affiche les emplacements où les joueurs posent les cartes,
        ainsi que la carte du dessus sur chaque emplacement.
        """
        for joueur in listeJoueurs:
            j = 0
            for i in range(0, 770, 110):
                if not joueur.rotation:
                    pygame.draw.rect(self.screen, Couleurs.RED,
                                     [joueur.emplacements_x + i,
                                      joueur.emplacements_y, 110,
                                      joueur.emplacements_length], 2)
                    if len(joueur.cartesEmplacements[j]) != 0:
                        carte = joueur.cartesEmplacements[j][-1]
                        self.screen.blit(Images.dicoCartesImages[carte],
                                         (joueur.emplacements_x + i + 5,
                                          joueur.emplacements_y + 5))
                        if j >= 2 and len(joueur.cartesEmplacements[j]) >= 2:
                            text = self.font.render(
                                'x' + str(len(joueur.cartesEmplacements[j])),
                                1, Couleurs.BLACK)
                            self.screen.blit(text,
                                             (joueur.emplacements_x + i + 10,
                                              joueur.emplacements_y + 70))
                    else:
                        text = self.font.render(self.nomsEmplacements[j],
                                                1, Couleurs.BLUE)
                        self.screen.blit(text, (joueur.emplacements_x + i + 10,
                                                joueur.emplacements_y + 70))

                else:
                    pygame.draw.rect(self.screen, Couleurs.RED,
                                     [joueur.emplacements_x,
                                      joueur.emplacements_y + i,
                                      joueur.emplacements_width, 110], 2)
                    if len(joueur.cartesEmplacements[j]) != 0:
                        carte = joueur.cartesEmplacements[j][-1]
                        imageTourne = pygame.transform.rotate(
                            Images.dicoCartesImages[carte], 90)
                        self.screen.blit(imageTourne,
                                         (joueur.emplacements_x + 5,
                                          joueur.emplacements_y + i + 5))
                        if j >= 2 and len(joueur.cartesEmplacements[j]) >= 2:
                            text = self.font.render(
                                'x' + str(len(joueur.cartesEmplacements[j])),
                                1, Couleurs.BLACK)
                            self.screen.blit(text,
                                             (joueur.emplacements_x + 30,
                                              joueur.emplacements_y + i + 20))
                    else:
                        text = self.font.render(self.nomsEmplacements[j],
                                                1, Couleurs.BLUE)
                        self.screen.blit(text,
                                         (joueur.emplacements_x + 30,
                                          joueur.emplacements_y + i + 20))

                j += 1

    def afficheMainJoueur(self, listeJoueurs, numCarteChoisie):
        """Affiche la main du joueur au sud de la fenêtre."""
        i = 0
        numCarte = 0
        for carte in listeJoueurs[0].main:
            if numCarte != numCarteChoisie:
                self.screen.blit(Images.dicoCartesImages[carte],
                                 (Coord.main_x + i, Coord.main_y))
            i += 110
            numCarte += 1

    def affichePioche(self, pioche):
        """
        Affiche la pioche au centre à droite.
        Le dos de la carte est affiché si la pioche est non vide.
        """
        pygame.draw.rect(self.screen, Couleurs.RED,
                         [Coord.pioche_x, Coord.pioche_y,
                          Coord.pioche_width, Coord.pioche_length], 2)
        if len(pioche) != 0:
            self.screen.blit(Images.dos_carte,
                             (Coord.pioche_x + 5,
                              Coord.pioche_y + 5))

    def affichePot(self, pot):
        """Affiche la dernière carte du pot au centre à gauche."""
        pygame.draw.rect(self.screen, Couleurs.RED,
                         [Coord.pot_x, Coord.pot_y,
                          Coord.pot_width, Coord.pot_length], 2)
        if len(pot) != 0:
            self.screen.blit(Images.dicoCartesImages[pot[-1]],
                             (Coord.pot_x + 5, Coord.pot_y + 5))

    def pause(self, listeJoueurs, pioche, pot, statsKm,
              numCarteChoisie, message, orientationJoueurQuiJoue,
              playMusic, temps=2):
        """
        Pause dynamiquement le programme afin qu'il s'arrête sans planter.
        """
        paused = True
        t_start = time()
        while paused:
            t_stop = time()
            if t_stop - t_start >= temps:
                paused = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    # Stat button
                    if selection.clickDansZone(pos, 5, 105, 35, 31):
                        stats.afficheStats(statsKm, listeJoueurs)
                    else:
                        paused = False

                self.update(listeJoueurs, pioche, pot, numCarteChoisie,
                            message, orientationJoueurQuiJoue, playMusic)

    def update(self, listeJoueurs, pioche, pot, numCarteChoisie, message,
               orientationJoueurQuiJoue, playMusic,
               bougeCarte=False, fini=False):
        """Met à jour la fenêtre."""
        self.screen.fill(self.bgColor)
        # Logo
        self.screen.blit(Images.logo,
                         (int(self.width / 2) - 163,
                          int(self.length / 2) - 110))
        if not fini:
            # Pioche
            self.affichePioche(pioche)
            # Pot
            self.affichePot(pot)
            # Noms joueurs
            self.afficheNoms(listeJoueurs, orientationJoueurQuiJoue)
            # Main actuelle
            self.afficheMainJoueur(listeJoueurs, numCarteChoisie)
            # Bottes
            self.afficheBottes(listeJoueurs)
            # Emplacements cartes
            self.afficheEmplacementsCartes(listeJoueurs)
            # Bouton music
            if playMusic:
                self.screen.blit(Images.music_on_button, (5, 5))
            else:
                self.screen.blit(Images.music_off_button, (5, 5))
            # Bouton stat
            self.screen.blit(Images.stat_button, (5, 55))
            # Bouton mode nuit
            self.screen.blit(Images.night_mode_button, (5, 105))
        # Message
        self.afficheTexte(message)
        if bougeCarte:
            # Affiche la carte sélectionnée à l'emplacement de la souris
            pos = pygame.mouse.get_pos()
            carte = listeJoueurs[0].main[numCarteChoisie]
            self.screen.blit(Images.dicoCartesImages[carte],
                             (pos[0] - 50, pos[1] - 71))
        pygame.display.update()
