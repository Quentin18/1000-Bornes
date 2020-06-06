"""
Jeu du 1000 Bornes
Quentin Deschamps
2020
"""
import pygame
from src.interface import Interface
from src.sons import Sons
from src.couleurs import Couleurs
from src.jeu import Jeu
import src.selection as selection
import src.stats as stats
from src.partie import Partie
from random import shuffle

if __name__ == "__main__":
    nom = input("Votre nom : ")

    pygame.init()

    # Création de la fenêtre
    fenetre = Interface()

    # Lancement de la musique
    pygame.mixer.music.load('./sounds/Chill-house-music-loop-116-bpm.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    # Initialisation de la carte choisie
    numCarteChoisie = -1
    carteChoisie = 'aucune'
    endroitChoisi = 'aucun'

    # Création de la partie
    mancheSuivante = False
    numManche = 0
    playMusic = True
    numJoueur = 0
    listePoints = [0, 0, 0, 0]

    partie = Partie(listePoints, nom)

    # Mainloop
    run = True
    while run:
        if not mancheSuivante:
            # Renversement pioche
            if len(partie.pioche) == 0:
                partie.pioche = partie.pot[:]
                shuffle(partie.pioche)
                partie.pot = []
            # Sélection du joueur
            joueurQuiJoue = partie.listeJoueurs[numJoueur]
            if joueurQuiJoue.orientation == 'sud':
                # Le joueur sud joue.
                if len(partie.pioche) != 0:
                    # Cas où la pioche est non vide
                    if len(joueurQuiJoue.main) < 7:
                        joueurQuiJoue.main.append(partie.pioche.pop(0))
                        joueurQuiJoue.trieMain()
                        fenetre.update(
                            partie.listeJoueurs,
                            partie.pioche,
                            partie.pot,
                            numCarteChoisie,
                            'À vous de jouer ! Choisissez une carte.',
                            joueurQuiJoue.orientation,
                            playMusic)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        elif event.type == pygame.MOUSEBUTTONUP:
                            Sons.clickSound.play()
                            pos = pygame.mouse.get_pos()
                            # Music button
                            if selection.clickDansZone(pos, 5, 5, 35, 33):
                                if playMusic:
                                    # Arrête la musique
                                    pygame.mixer.music.stop()
                                    playMusic = False
                                else:
                                    # Remet la musique
                                    pygame.mixer.music.play(-1)
                                    playMusic = True
                                fenetre.update(
                                    partie.listeJoueurs,
                                    partie.pioche,
                                    partie.pot,
                                    numCarteChoisie,
                                    'À vous de jouer ! Choisissez une carte.',
                                    joueurQuiJoue.orientation,
                                    playMusic)
                            # Stat button
                            elif selection.clickDansZone(pos, 5, 55, 35, 31):
                                stats.afficheStats(
                                    partie.statsKm,
                                    partie.listeJoueurs)
                            # Night mode button
                            elif selection.clickDansZone(pos, 5, 105, 35, 35):
                                # Change la couleur de fond
                                if fenetre.bgColor == Couleurs.WHITE:
                                    fenetre.bgColor = Couleurs.BLACK
                                else:
                                    fenetre.bgColor = Couleurs.WHITE
                                fenetre.update(
                                    partie.listeJoueurs,
                                    partie.pioche,
                                    partie.pot,
                                    numCarteChoisie,
                                    'À vous de jouer ! Choisissez une carte.',
                                    joueurQuiJoue.orientation,
                                    playMusic)
                            if carteChoisie == 'aucune':
                                carteChoisie, numCarteChoisie = selection.carteSelectionnee(
                                    partie.listeJoueurs, pos)
                            if (carteChoisie != 'aucune'
                                    and endroitChoisi == 'aucun'):
                                fenetre.update(
                                    partie.listeJoueurs,
                                    partie.pioche, partie.pot,
                                    numCarteChoisie,
                                    'Vous avez choisi la carte : '
                                    + Jeu.dicoNomsCartes[carteChoisie]
                                    + '.',
                                    joueurQuiJoue.orientation,
                                    playMusic)
                                endroitChoisi = selection.endroitSelectionne(
                                    partie.listeJoueurs, pos)
                                if endroitChoisi == 'aucun':
                                    carteChoisie, numCarteChoisie = selection.carteSelectionnee(
                                        partie.listeJoueurs, pos)
                                    if carteChoisie != 'aucune':
                                        fenetre.update(
                                            partie.listeJoueurs,
                                            partie.pioche,
                                            partie.pot,
                                            numCarteChoisie,
                                            'Vous avez choisi la carte : '
                                            + Jeu.dicoNomsCartes[carteChoisie]
                                            + '.',
                                            joueurQuiJoue.orientation,
                                            playMusic)
                                    else:
                                        fenetre.update(
                                            partie.listeJoueurs,
                                            partie.pioche,
                                            partie.pot,
                                            numCarteChoisie,
                                            'À vous de jouer ! Choisissez une carte.',
                                            joueurQuiJoue.orientation,
                                            playMusic)
                            if (carteChoisie != 'aucune'
                                    and endroitChoisi != 'aucun'):
                                message = partie.joueJoueurSud(
                                    pos, partie.pot,
                                    carteChoisie,
                                    endroitChoisi)
                                if message != '':
                                    # Le joueur sud rejoue si
                                    # une botte est posée
                                    if carteChoisie not in Jeu.listeBottes:
                                        # Mise à jour de la liste des
                                        # stats de km
                                        partie.statsKm[numJoueur].append(
                                            joueurQuiJoue.km)
                                        numJoueur = (numJoueur + 1) % 4
                                    numCarteChoisie = -1
                                    carteChoisie = 'aucune'
                                    endroitChoisi = 'aucun'
                                    fenetre.update(
                                        partie.listeJoueurs,
                                        partie.pioche,
                                        partie.pot,
                                        numCarteChoisie,
                                        message,
                                        joueurQuiJoue.orientation,
                                        playMusic)
                                    fenetre.pause(
                                        partie.listeJoueurs,
                                        partie.pioche,
                                        partie.pot,
                                        partie.statsKm,
                                        numCarteChoisie,
                                        message,
                                        joueurQuiJoue.orientation,
                                        playMusic)
                                else:
                                    numCarteChoisie = -1
                                    carteChoisie = 'aucune'
                                    endroitChoisi = 'aucun'
                                    fenetre.update(
                                        partie.listeJoueurs,
                                        partie.pioche,
                                        partie.pot,
                                        numCarteChoisie,
                                        'À vous de jouer ! Choisissez une carte.',
                                        joueurQuiJoue.orientation,
                                        playMusic)

                    if carteChoisie != 'aucune':
                        # Bouge la carte choisie
                        fenetre.update(
                            partie.listeJoueurs,
                            partie.pioche,
                            partie.pot,
                            numCarteChoisie,
                            'Vous avez choisi la carte : '
                            + Jeu.dicoNomsCartes[carteChoisie]
                            + '.',
                            joueurQuiJoue.orientation,
                            playMusic,
                            bougeCarte=True)
                else:
                    # Cas où la pioche est vide
                    message = joueurQuiJoue.phaseCritique()
                    partie.statsKm[numJoueur].append(joueurQuiJoue.km)
                    numJoueur = (numJoueur + 1) % 4
                    fenetre.update(
                        partie.listeJoueurs,
                        partie.pioche,
                        partie.pot,
                        numCarteChoisie,
                        message,
                        joueurQuiJoue.orientation,
                        playMusic)
                    fenetre.pause(
                        partie.listeJoueurs,
                        partie.pioche,
                        partie.pot,
                        partie.statsKm,
                        numCarteChoisie,
                        message,
                        joueurQuiJoue.orientation,
                        playMusic)
            else:
                # Les autres joueurs jouent.
                # print(joueurQuiJoue.nom, joueurQuiJoue.main)
                if len(partie.pioche) != 0:
                    # Cas où la pioche est non vide
                    message, rejoue = joueurQuiJoue.joue(
                        partie.listeJoueurs,
                        partie.pioche,
                        partie.pot)
                    fenetre.update(
                        partie.listeJoueurs,
                        partie.pioche,
                        partie.pot,
                        numCarteChoisie,
                        message,
                        joueurQuiJoue.orientation,
                        playMusic)
                    fenetre.pause(
                        partie.listeJoueurs,
                        partie.pioche,
                        partie.pot,
                        partie.statsKm,
                        numCarteChoisie,
                        message,
                        joueurQuiJoue.orientation,
                        playMusic)
                    if not rejoue:
                        # Mise à jour de la liste des stats de km
                        partie.statsKm[numJoueur].append(joueurQuiJoue.km)
                        numJoueur = (numJoueur + 1) % 4
                else:
                    # Cas où la pioche est vide
                    message = joueurQuiJoue.phaseCritique()
                    partie.statsKm[numJoueur].append(joueurQuiJoue.km)
                    numJoueur = (numJoueur + 1) % 4
                    fenetre.update(
                        partie.listeJoueurs,
                        partie.pioche,
                        partie.pot,
                        numCarteChoisie,
                        message,
                        joueurQuiJoue.orientation,
                        playMusic)
                    fenetre.pause(
                        partie.listeJoueurs,
                        partie.pioche,
                        partie.pot,
                        partie.statsKm,
                        numCarteChoisie,
                        message,
                        joueurQuiJoue.orientation,
                        playMusic)

            # Condition de fin de partie
            if (joueurQuiJoue.km == 1000 or (
                len(partie.pioche) == 0
                    and len(partie.pot) == 0 and partie.tousBloque())):
                gagnant = partie.listeJoueursTri()[0]
                # Ajout des points de fin de manche
                gagnant.points += 400
                for i in partie.listeJoueurs:
                    i.points += i.km
                if 0 in [i.km for i in partie.listeJoueurs]:
                    # Cas où capot d'un ou plusieurs joueurs
                    for i in partie.listeJoueurs:
                        if i.km != 0:
                            i.points += 500
                    fenetre.update(
                        partie.listeJoueurs,
                        partie.pioche,
                        partie.pot,
                        numCarteChoisie,
                        "Capot ! 500 points pour les autres !",
                        gagnant.orientation,
                        playMusic)
                    fenetre.pause(
                        partie.listeJoueurs,
                        partie.pioche,
                        partie.pot,
                        partie.statsKm,
                        numCarteChoisie,
                        "Capot ! 500 points pour les autres !",
                        gagnant.orientation,
                        playMusic,
                        temps=5)
                fenetre.update(
                    partie.listeJoueurs,
                    partie.pioche,
                    partie.pot,
                    numCarteChoisie,
                    gagnant.nom + " a gagné la manche ! 400 points",
                    gagnant.orientation, playMusic)
                Sons.tadaSound.play()
                fenetre.pause(
                    partie.listeJoueurs,
                    partie.pioche,
                    partie.pot,
                    partie.statsKm,
                    numCarteChoisie,
                    gagnant.nom + " a gagné la manche ! 400 points",
                    gagnant.orientation,
                    playMusic,
                    temps=10)
                mancheSuivante = True

        else:
            listePoints = [i.points for i in partie.listeJoueurs]
            partie = Partie(listePoints, nom)
            numJoueur = numManche % 4
            numManche += 1
            mancheSuivante = False

    pygame.quit()
