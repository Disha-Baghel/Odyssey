import pygame

class Ship:
    '''A class to manage the ship6'''

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screem_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('Images/spaceship.webp')
        self.rect = self.image.get_rect()

        # Start each ship at its current location
        self.screen.blit(self.image, self.rect)

    def blitme(self):
        '''Draw the ship at its currnet location'''
        self.screen.blit(self.image, self.rect)