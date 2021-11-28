#creating a user window for the game
import sys
import pygame

#user defined module
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #bg_color = (230, 230, 230)

    #make Play Button
    play_button = Button(ai_settings,screen,'PLAY')

    #Create an instance to stre game statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #make a ship
    ship = Ship(ai_settings,screen)

    #make a alien
    alien = Alien(ai_settings,screen)
    
    #make a bullet
    bullets=Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()  
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets)    
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)


#MAIN FUNCTION      
run_game()
