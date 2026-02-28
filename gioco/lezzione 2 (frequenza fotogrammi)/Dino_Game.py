import sys
import pygame 


class dino_game: 
    
    def __init__(self): 

        pygame.init()  
        self.clock = pygame.time.Clock()   #crea un oggetto che serve a gestire il frame rate
        self.schermata = pygame.display.set_mode((1200, 800)) 

        pygame.display.set_caption("Dino Game") 
        self.bg_color = (230, 230, 230)  #imposta il colore di sfondo della schermata

    def esegui_gioco(self): 
        while(True): 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    sys.exit() 
            self.schermata.fill(self.bg_color)
            pygame.display.flip() 
            self.clock.tick(60) #va ad impostare nel oggetto clock un frame rate pari a 60


if __name__ == "__main__": 
    dinoGame = dino_game() 
    dinoGame.esegui_gioco() 







