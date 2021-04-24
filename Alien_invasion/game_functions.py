import sys
import pygame
from bullet import Bullet 
from alien import Alien 

def check_events(ai_settings, screen, ship, bullets):
    """Reaction for events generated by keyboard and mouse."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship) 
                    
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Updating images on screen and going to a new screen"""
    
    #Refreshing screen
    screen.fill(ai_settings.bg_color)

    #Redisplay all bullets below layouts of spaceship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    #Display last modified screen
    pygame.display.flip()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """reaction to pressing a key"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """reaction to key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def update_bullets(bullets):
    """Updating bullets position and removing invisible."""
    #updating bullets position
    bullets.update()

   #deleting bullets, that leaves screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
          bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """shooting bullet if its allowed."""
    #making new bullet and adding him to group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """Calculating how much aliens can be in one row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Calculating how much rows of aliens can be fitted in screen"""
    available_space_y =  (ai_settings.screen_height - (3 * alien_height) 
        - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creating alien and putting him to the row"""
    #Creating alien and putting him to the row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height + 2 * alien.rect.height * 
        row_number)
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Creating fleet full of aliens"""
    #Creating alien and defining number of aliens, that will fit in one
    #line. Length between each alien is equal to alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, 
        alien.rect.height)

    #Creating fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)

def check_fleet_edges(ai_settings, aliens):
    """Corrert reaction , when alien arive to the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Moving whole fleet down and changing the direction that
     it's moving"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def update_aliens(ai_settings, aliens):
    """Checking are aliens near to the edge of the screen, and then
    updating position of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
