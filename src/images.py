import pygame


class Images:
    """Importe les images du jeu."""
    image_25km = pygame.image.load('./images/25km.png')
    image_50km = pygame.image.load('./images/50km.png')
    image_75km = pygame.image.load('./images/75km.png')
    image_100km = pygame.image.load('./images/100km.png')
    image_200km = pygame.image.load('./images/200km.png')
    image_feu_rouge = pygame.image.load('./images/feu_rouge.png')
    image_limite_de_vitesse = pygame.image.load(
        './images/limite_de_vitesse.png')
    image_panne_essence = pygame.image.load('./images/panne_essence.png')
    image_creve = pygame.image.load('./images/creve.png')
    image_accident = pygame.image.load('./images/accident.png')
    image_feu_vert = pygame.image.load('./images/feu_vert.png')
    image_fin_limite_de_vitesse = pygame.image.load(
        './images/fin_limite_de_vitesse.png')
    image_essence = pygame.image.load('./images/essence.png')
    image_roue_de_secours = pygame.image.load('./images/roue_de_secours.png')
    image_reparations = pygame.image.load('./images/reparations.png')
    image_vehicule_prioritaire = pygame.image.load(
        './images/vehicule_prioritaire.png')
    image_citerne = pygame.image.load('./images/citerne.png')
    image_increvable = pygame.image.load('./images/increvable.png')
    image_as_du_volant = pygame.image.load('./images/as_du_volant.png')
    dos_carte = pygame.image.load('./images/dos_carte.png')
    logo = pygame.image.load('./images/logo.png')
    music_on_button = pygame.image.load('./images/music_on_button.png')
    music_off_button = pygame.image.load('./images/music_off_button.png')
    stat_button = pygame.image.load('./images/stat_button.png')
    night_mode_button = pygame.image.load('./images/night_mode_button.png')

    dicoCartesImages = {'25': image_25km,
                        '50': image_50km,
                        '75': image_75km,
                        '100': image_100km,
                        '200': image_200km,
                        'feu_rouge': image_feu_rouge,
                        'limite_de_vitesse': image_limite_de_vitesse,
                        'panne_essence': image_panne_essence,
                        'creve': image_creve,
                        'accident': image_accident,
                        'feu_vert': image_feu_vert,
                        'fin_limite_de_vitesse': image_fin_limite_de_vitesse,
                        'essence': image_essence,
                        'roue_de_secours': image_roue_de_secours,
                        'reparations': image_reparations,
                        'vehicule_prioritaire': image_vehicule_prioritaire,
                        'citerne': image_citerne,
                        'increvable': image_increvable,
                        'as_du_volant': image_as_du_volant}
