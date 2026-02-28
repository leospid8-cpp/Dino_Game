import sys
import pygame 

from Impostazzioni import Impostazzioni #dal file impostazzioni importa la classe impostazzioni

class dino_game: 
    
    def __init__(self): 

        pygame.init()  
        self.clock = pygame.time.Clock()  
        self.impostazzione = Impostazzioni() # crea l'oggetto Impostazzioni
        
        self.schermata=pygame.display.set_mode((self.impostazzione.schermata_larghezza, self.impostazzione.schermata_larghezza)) #usa le variabili impostate nella classe impostazzioni

        pygame.display.set_caption("Dino Game") 

    def esegui_gioco(self): 
        while(True): 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    sys.exit() 
            self.schermata.fill(self.impostazzione.bg_color) #usa la variabile creata in impostazzioni
            pygame.display.flip() 
            self.clock.tick(60) 


if __name__ == "__main__": 
    dinoGame = dino_game() 
    dinoGame.esegui_gioco() 







