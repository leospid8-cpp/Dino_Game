import sys
import pygame 
from pathlib import Path

from Impostazzioni import Impostazzioni 
from Dinosauro import Dinosauro
from Cactus import Cactus #importazione della classe Cactus dal file Cactus.py

class dino_game: 
    
    def __init__(self): 

        pygame.init()  
        self.clock = pygame.time.Clock()  
        self.impostazzione = Impostazzioni()

        base_path = Path(__file__).parent
        self.immagineSfondo = pygame.image.load(base_path / "immagini" / "sfondo.jpg")
        self.sfondo = pygame.transform.scale(self.immagineSfondo, (self.impostazzione.schermata_larghezza, self.impostazzione.schermata_altezza)) 
        self.schermata = pygame.display.set_mode(
            (self.impostazzione.schermata_larghezza, self.impostazzione.schermata_altezza)
        ) 

        pygame.display.set_caption("Dino Game") 

        self.dinosauro = Dinosauro(self) 
        self.cactus = Cactus(self) #creazione di un'istanza della classe Cactus

    def esegui_gioco(self): 
        while(True): 

            self.controlla_eventi() 
            self.dinosauro.aggiorna()
            self.cactus.aggiorna() #aggiornamento del cactus
            self.aggiorna_schermo() 
            self.clock.tick(60) 

    def controlla_eventi(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP:

                    if not self.dinosauro.saltando: 
                        self.dinosauro.saltando = True
                        self.dinosauro.velocita_y = self.dinosauro.forza_salto
                elif event.key == pygame.K_ESCAPE: 
                    sys.exit()
                elif event.key == pygame.K_F11: 
                    pygame.display.toggle_fullscreen()
    
    def aggiorna_schermo(self): 
        self.schermata.blit(self.sfondo, (0, 0))
        self.dinosauro.disegna()
        self.cactus.disegna() #disegno del cactus
        pygame.display.flip()

if __name__ == "__main__": 
    dinoGame = dino_game() 
    dinoGame.esegui_gioco() 







