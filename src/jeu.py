class Jeu:
    """Listes et dictionnaires pour gérer les cartes."""
    # Préparation du jeu
    dicoAttaquesParades = {
        'feu_rouge': 'feu_vert',
        'limite_de_vitesse': 'fin_limite_de_vitesse',
        'panne_essence': 'essence',
        'creve': 'roue_de_secours',
        'accident': 'reparations'}
    dicoAttaquesBottes = {
        'feu_rouge': 'vehicule_prioritaire',
        'limite_de_vitesse': 'vehicule_prioritaire',
        'panne_essence': 'citerne',
        'creve': 'increvable',
        'accident': 'as_du_volant'}
    dicoParadesBottes = {
        'feu_vert': 'vehicule_prioritaire',
        'fin_limite_de_vitesse': 'vehicule_prioritaire',
        'essence': 'citerne',
        'roue_de_secours': 'increvable',
        'reparations': 'as_du_volant'}
    listeAttaques = [
        'feu_rouge',
        'limite_de_vitesse',
        'panne_essence',
        'creve',
        'accident']
    listeParades = [
        'feu_vert',
        'fin_limite_de_vitesse',
        'essence',
        'roue_de_secours',
        'reparations']
    listeBottes = [
        'vehicule_prioritaire',
        'citerne',
        'increvable',
        'as_du_volant']
    listeKM = ['200', '100', '75', '50', '25']

    # Pour emplacements des cartes et affichages
    nomsEmplacements = [
        'Attaques',
        'Limitations',
        '200',
        '100',
        '75',
        '50',
        '25']
    dicoEmplacementsCartesValides = {
        'Attaques': [
            'feu_rouge',
            'panne_essence',
            'creve',
            'accident',
            'feu_vert',
            'essence',
            'roue_de_secours',
            'reparations'],
        'Limitations': [
            'limite_de_vitesse',
            'fin_limite_de_vitesse'],
        '200': ['200'],
        '100': ['100'],
        '75': ['75'],
        '50': ['50'],
        '25': ['25']}
    dicoNomsCartes = {
        'feu_rouge': 'Feu rouge',
        'limite_de_vitesse': 'Limite de vitesse',
        'panne_essence': "Panne d'essence",
        'creve': 'Crevé',
        'accident': 'Accident',
        'feu_vert': 'Feu vert',
        'fin_limite_de_vitesse': 'Fin de limite de vitesse',
        'essence': 'Essence',
        'roue_de_secours': 'Roue de secours',
        'reparations': 'Réparations',
        'vehicule_prioritaire': 'Véhicule prioritaire',
        'citerne': 'Citerne',
        'increvable': 'Increvable',
        'as_du_volant': 'As du volant',
        '200': '200 km',
        '100': '100 km',
        '75': '75 km',
        '50': '50 km',
        '25': '25 km'}
