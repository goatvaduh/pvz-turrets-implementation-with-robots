#menu
import pygame
import sys
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 48)
        self.title_text = self.font.render("Main Menu", True, (255, 255, 255))
        self.start_text = self.font.render("Start Game", True, (255, 255, 255))
        self.quit_text = self.font.render("Quit Game", True, (255, 255, 255))
        self.start_rect = self.start_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
        self.quit_rect = self.quit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    def display(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_rect.collidepoint(event.pos):
                        print("Starting game...")
                        running = False
                    elif self.quit_rect.collidepoint(event.pos):
                        print("Quitting game...")
                        pygame.quit()
                        sys.exit()

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.title_text, (self.screen.get_width() // 2 - self.title_text.get_width() // 2, 100))
            self.screen.blit(self.start_text, self.start_rect.topleft)
            self.screen.blit(self.quit_text, self.quit_rect.topleft)
            pygame.display.flip()

def gggggg():
    print("gggggg")