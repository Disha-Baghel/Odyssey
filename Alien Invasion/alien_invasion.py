import sys
import pygame

from settings import Settings 
from ship import Ship

class AlienInvasion:     

    '''Overall class to manage game assets and behaviour'''

    def __init__(self):
        '''Initialize the game, and create game resources'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))   #surface
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Imvasion")
        self.ship = Ship(self)

        self.bg_color = (17, 24, 39)


        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

    def run_game(self):
        
        '''Start the main loop for the game'''
        while(True):
            # watch the keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        '''Respond to keypresses and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                        
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        #Respond to keypresses
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
                
        elif event.key == pygame.K_LEFT:
            #Move the ship to the left
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        #Respond to key releases
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = False
                
        elif event.key == pygame.K_LEFT:
            #Move the ship to the left
            self.ship.moving_left = False

        elif event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()