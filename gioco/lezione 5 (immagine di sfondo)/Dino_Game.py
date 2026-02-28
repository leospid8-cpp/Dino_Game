import sys
import pygame 

from pathlib import Path
from Impostazzioni import Impostazzioni 
from Dinosauro import Dinosauro

class dino_game: 
    
    def __init__(self): 

        pygame.init()  
        self.clock = pygame.time.Clock()  
        self.impostazzione = Impostazzioni()
        base_path = Path(__file__).parent
        self.immagineSfondo = pygame.image.load(base_path / "immagini" / "sfondo.jpg") #caricamento del immagine di sfondo
        self.sfondo = pygame.transform.scale(self.immagineSfondo, (self.impostazzione.schermata_larghezza, self.impostazzione.schermata_altezza)) #scala l'immagine per addattarla allo schermo
        self.schermata = pygame.display.set_mode(
            (self.impostazzione.schermata_larghezza, self.impostazzione.schermata_altezza)
        ) 

        pygame.display.set_caption("Dino Game") 

        self.dinosauro = Dinosauro(self) 

    def esegui_gioco(self): 
        while(True): 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    sys.exit() 
            self.schermata.blit(self.sfondo, (0, 0))  #disegna l'immagine di sfondo sulla schermata
            self.dinosauro.disegna() 
            pygame.display.flip() 
            self.clock.tick(60) 


if __name__ == "__main__": 
    dinoGame = dino_game() 
    dinoGame.esegui_gioco() 







