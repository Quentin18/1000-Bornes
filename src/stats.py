import matplotlib.pyplot as plt


def afficheStats(statsKm, listeJoueurs):
    """
    Affiche le graphique des kms parcourus par
    chaque joueur en fonction du temps.
    """
    i = 0
    for liste in statsKm:
        plt.plot(liste, label=listeJoueurs[i].nom)
        i += 1
    plt.title("Evolution de la partie")
    plt.xlabel("Tour")
    plt.ylabel("Km")
    plt.legend()
    plt.show()
