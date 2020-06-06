# 1000 Bornes

Jeu du 1000 Bornes en Python avec [pygame](https://www.pygame.org/news)

![](https://github.com/Quentin18/1000-Bornes/blob/master/images/logo.png)

## Présentation
Ce projet est une simulation du célèbre jeu du **1000 Bornes** en Python avec la bibliothèque pygame. Le jeu se joue seul contre 3 ordinateurs, programmés pour jouer comme des humains. L'interface graphique utilise les images des cartes officielles du jeu. Des effets sonores ont aussi été ajoutés afin de rendre le jeu plus ludique.

![](https://github.com/Quentin18/1000-Bornes/blob/master/capture/jeu.gif)

## Règles du jeu
Vous trouverez les règles du jeu [ici](https://www.jeuxdujardin.fr/sites/dujardin/files/notices/MB%20Luxe.pdf).

## Installation
Vous devez installer [pygame](https://www.pygame.org/news) pour l'interface du jeu et [matplotlib](https://matplotlib.org/index.html) pour les statistiques :
```bash
pip3 install pygame
pip3 install matplotlib
```

Clonez ensuite le projet :
```bash
git clone https://github.com/Quentin18/1000-Bornes.git
```

## Lancement
Pour lancer le jeu, tapez la commande :
```bash
python3 1000-bornes.py
```
Entrez ensuite votre nom et la partie démarre.

## Jeu
L'objectif est d'être le premier joueur à atteindre les 1000 bornes. Lorsque c'est votre tour, sélectionnez une carte de votre jeu en cliquant dessus et effectuez une action parmi les suivantes :

- **Jouer un km** : cliquez sur la zone correspondant à la carte choisie.
- **Attaquer un joueur** : cliquez sur la zone correspondant au tas des attaques de l'adversaire. Si vous voulez posez une limite de vitesse, cliquez sur la zone des limitations de votre adversaire.
- **Contrer une attaque** : cliquez sur l'attaque à contrer sur votre tas des attaques.
- **Jouer une botte** : cliquez sur votre zone de cartes.
- **Jeter une carte** : cliquez sur la zone de défausse au milieu de la fenêtre.

Pour changer de cartes, cliquez sur une autre carte de votre jeu. Vous pouvez aussi relâcher une carte en appuyant dans un espace vide. Lorsqu'il n'y a plus de pioche, le jeu se termine automatiquement en jouant les derniers km des joueurs (dont vous).

Une manche est relancée automatiquement lorsqu'une partie se termine. Le score cumulé des manches apparaît à côté du nombre de km pour chaque joueur. Regardez le descriptif des points dans la règle du jeu.

## Stats
Vous pouvez voir les statistiques de la partie grâce à matplotlib en appuyant sur le second icône en haut à gauche. Cela vous montre les km parcourus par chaque joueur en fonction du nombre de tours joués.

![](https://github.com/Quentin18/1000-Bornes/blob/master/capture/stats.png)

## Options
- **Musique** : vous pouvez activer ou désactiver la musique de fond avec le premier icône en haut à gauche.
- **Fond** : vous pouvez mettre le fond en noir ou blanc avec le troisième icône en haut à gauche.

## Contact
Quentin Deschamps: quentindeschamps18@gmail.com

## License
[MIT](https://choosealicense.com/licenses/mit/)
