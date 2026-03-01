import sys
import pygame 

from Impostazzioni import Impostazzioni 
from Dinosauro import Dinosauro #importa la classe Dinosauro dal file Dinosauro.py

class dino_game: 
    
    def __init__(self): 

        pygame.init()  
        self.clock = pygame.time.Clock()  
        self.impostazzione = Impostazzioni()
        
        self.schermata = pygame.display.set_mode(
            (self.impostazzione.schermata_larghezza, self.impostazzione.schermata_altezza)
        ) 

        pygame.display.set_caption("Dino Game") 

        self.dinosauro = Dinosauro(self) #crea un'istanza del dinosauro e gli passa il gioco come argomento

    def esegui_gioco(self): 
        while(True): 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    sys.exit() 
            self.schermata.fill(self.impostazzione.bg_color)
            self.dinosauro.disegna() #disegna il dinosauro sulla schermata
            pygame.display.flip() 
            self.clock.tick(60) 


if __name__ == "__main__": 
    dinoGame = dino_game() 
    dinoGame.esegui_gioco() 







