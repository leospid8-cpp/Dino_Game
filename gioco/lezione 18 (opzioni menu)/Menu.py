import pygame
import sys

class Menu:
    def __init__(self, Dino_Game):
        self.schermata = Dino_Game.schermata
        self.schermata_rettangolo = Dino_Game.schermata.get_rect() 

        self.inpausa = False


    def menu(self, Dino_Game, inpausa):
        while inpausa:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: 
                        inpusa = False
                        return # esce dal menu e torna al gioco

            self.schermata.fill((0, 0, 0)) 
            font = pygame.font.Font(None, 48)
            testo = font.render("Premi ESC per continuare", True, (255, 255, 255))
            testo_rettangolo = testo.get_rect(center=self.schermata_rettangolo.center)
            self.schermata.blit(testo, testo_rettangolo)
            pygame.display.flip()
        sys.exit()
        
