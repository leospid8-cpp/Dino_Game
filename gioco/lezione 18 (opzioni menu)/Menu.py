import pygame
import sys



class Menu:
    def __init__(self, Dino_Game):
        self.aggiorna_superfici(Dino_Game)
        self.inpausa = False

    def aggiorna_superfici(self, Dino_Game):
        self.trasparenza = pygame.Surface(
            (
                Dino_Game.impostazzione.schermata_larghezza,
                Dino_Game.impostazzione.schermata_altezza,
            ),
            pygame.SRCALPHA,
        )
        self.schermata = Dino_Game.schermata
        self.schermata_rettangolo = Dino_Game.schermata.get_rect() 


    def menu(self, Dino_Game, inpausa):
        while inpausa:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: 
                        inpausa = False
                        return inpausa # esce dal menu e torna al gioco
                    elif event.key == pygame.K_F11:
                        pygame.display.toggle_fullscreen()
                        Dino_Game.aggiorna_display()
                
            

            self.schermata.blit(Dino_Game.sfondo, (0, 0))
            Dino_Game.disegna_cactus()
            Dino_Game.dinosauro.disegna()
            Dino_Game.timer()

            self.trasparenza.fill((0, 0, 0, 150))
            self.schermata.blit(self.trasparenza, (0, 0))

            font = pygame.font.Font(None, 48)
            testo = font.render("Premi ESC per continuare", True, (255, 255, 255))
            testo_rettangolo = testo.get_rect(center=self.schermata_rettangolo.center)
            self.schermata.blit(testo, testo_rettangolo)
            pygame.display.flip()
        return inpausa
        
    def menu_sconfitta(self, Dino_Game, punteggio):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: 
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_RETURN:
                        return True  # segnala restart
                    elif event.key == pygame.K_F11:
                        pygame.display.toggle_fullscreen()
                        Dino_Game.aggiorna_display()

            self.schermata.blit(Dino_Game.sfondo, (0, 0))
            Dino_Game.disegna_cactus()
            Dino_Game.dinosauro.disegna()
            self.trasparenza.fill((0, 0, 0, 170))
            self.schermata.blit(self.trasparenza, (0, 0))
            font1 = pygame.font.Font(None, 48)
            testo_punteggio = font1.render(f"Punteggio: {punteggio}", True, (255, 255, 255))
            testo_punteggio_rettangolo = testo_punteggio.get_rect(left=20, top=20)
            self.schermata.blit(testo_punteggio, testo_punteggio_rettangolo)
            testo = font1.render("Hai perso!", True, (255, 255, 255))
            testo_rettangolo = testo.get_rect(center=self.schermata_rettangolo.center)
            self.schermata.blit(testo, testo_rettangolo)
            font2 = pygame.font.Font(None, 36)
            testo_istruzioni1 = font2.render("Premi ESC per uscire", True, (255, 255, 255))
            testo_istruzioni1_rettangolo = testo_istruzioni1.get_rect(center=(self.schermata_rettangolo.centerx, self.schermata_rettangolo.centery + 50))
            self.schermata.blit(testo_istruzioni1, testo_istruzioni1_rettangolo)
            testo_istruzioni2 = font2.render("Premi INVIO per reiniziare", True, (255, 255, 255))
            testo_istruzioni2_rettangolo = testo_istruzioni2.get_rect(center=(self.schermata_rettangolo.centerx, self.schermata_rettangolo.centery + 100))
            self.schermata.blit(testo_istruzioni2, testo_istruzioni2_rettangolo)
            testo_istruzioni3 = font2.render("Premi F11 per schermo intero", True, (255, 255, 255))
            testo_istruzioni3_rettangolo = testo_istruzioni3.get_rect(center=(self.schermata_rettangolo.centerx, self.schermata_rettangolo.centery + 150))
            self.schermata.blit(testo_istruzioni3, testo_istruzioni3_rettangolo)
            pygame.display.flip()
