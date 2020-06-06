import pygame


class Sons:
    """Importe les sons du jeu."""
    pygame.mixer.init()
    winningSound = pygame.mixer.Sound(
        './sounds/Winning-brass-fanfare-sound-effect.wav')
    hornSound = pygame.mixer.Sound('./sounds/Horn-sound.wav')
    crashSound = pygame.mixer.Sound('./sounds/Car-crash-sound-effect.wav')
    tadaSound = pygame.mixer.Sound('./sounds/Ta-da-orchestra-fanfare.wav')
    woohooSound = pygame.mixer.Sound('./sounds/Cartoon-woohoo.wav')
    clickSound = pygame.mixer.Sound('./sounds/Button-click-sound-effect.wav')
    panneSound = pygame.mixer.Sound('./sounds/Panne-sound.wav')
    startSound = pygame.mixer.Sound('./sounds/Car-start-sound.wav')
    sireneSound = pygame.mixer.Sound('./sounds/Sirene-sound.wav')
