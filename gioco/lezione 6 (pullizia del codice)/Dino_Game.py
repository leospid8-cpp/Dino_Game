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
        self.immagineSfondo = pygame.image.load(base_path / "immagini" / "sfondo.jpg")
        self.sfondo = pygame.transform.scale(self.immagineSfondo, (self.impostazzione.schermata_larghezza, self.impostazzione.schermata_altezza)) 
        self.schermata = pygame.display.set_mode(
            (self.impostazzione.schermata_larghezza, self.impostazzione.schermata_altezza)
        ) 

        pygame.display.set_caption("Dino Game") 

        self.dinosauro = Dinosauro(self) 

    def esegui_gioco(self): 
        while(True): 

            self.controlla_eventi() #chiamiamo la funzione per controllare gli eventi
            self.aggiorna_schermo() #chiamiamo la funzione per aggiornare lo schermo
            self.clock.tick(60) 

    def controlla_eventi(self): #trasferiamo il controllo degli eventi in una funzione separata per mantenere il codice più pulito
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
    
    def aggiorna_schermo(self): #trasferiamo la logica di aggiornamento dello schermo in una funzione separata per mantenere il codice più pulito
        self.schermata.blit(self.sfondo, (0, 0))
        self.dinosauro.disegna()
        pygame.display.flip()

if __name__ == "__main__": 
    dinoGame = dino_game() 
    dinoGame.esegui_gioco() 







