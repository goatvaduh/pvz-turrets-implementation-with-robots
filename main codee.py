import pygame 
import menu
import sys
# I want to create a screen where if the user clicks any button, it will redirect the user to the main menu. 
# If the user holds down the escape button for 1 second, it will close the game.
# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Turrets vs Robots")
clock = pygame.time.Clock()
running = True
escape_held = False
escape_start_time = None

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        if not escape_held:
            escape_held = True
            escape_start_time = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - escape_start_time >= 1000:
            running = False
    else:
        escape_held = False
        escape_start_time = None

    """adding a  subtitle displaying turrets vs robots and display underneath it "press any button to continue" and if the user presses any button, it will redirect the user to
     the main menu."""

    keys = pygame.key.get_pressed()
    subtitle_font = pygame.font.Font(None, 48)
    display_text = subtitle_font.render("Turrets vs Robots", True, (255, 255, 255))
    continue_text = subtitle_font.render("press any button to continue", True, (255, 255, 255))

    if any(keys) or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
        # Redirect to main menu
        print("Redirecting to main menu...")  # Replace this with actual redirection logic
        menu.Menu(screen).display()  # Call the function from menu.py
        break

        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#b300ca")

    # RENDER YOUR GAME HERE
    screen.blit(display_text, (screen.get_width() // 2 - display_text.get_width() // 2, 100))
    screen.blit(continue_text, (screen.get_width() // 2 - continue_text.get_width() // 2, 200))
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # the game is quite simple so only 60 fps is fine 


pygame.quit()