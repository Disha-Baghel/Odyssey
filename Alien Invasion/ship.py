import pygame


class Ship:
    '''A class to manage the ship6'''

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('Images/spaceship.webp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #Movement flag 
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update the ship's position based on the movement flag'''
        if self.moving_right:
            # self.rect.x += 1
            self.x += self.settings.ship_speed

        elif self.moving_left:
            # self.rect.x -= 1
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        '''Draw the ship at its currnet location'''
        self.screen.blit(self.image, self.rect)
        