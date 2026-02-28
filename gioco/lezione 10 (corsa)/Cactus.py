from pathlib import Path
import pygame

class Cactus:
    def __init__(self, Dino_Game): 

        self.schermata = Dino_Game.schermata 
        self.schermata_rettangolo = Dino_Game.schermata.get_rect() 

        base_path = Path(__file__).resolve().parent
        immagine = pygame.image.load(base_path / "immagini" / "cactus.png") 
        self.immagine = pygame.transform.scale(immagine, (80, 80)) 
        self.rettangolo = self.immagine.get_rect() 
        self.rettangolo.right = self.schermata_rettangolo.right
        
        self.velocita_x = 5
        
    def aggiorna(self): 
        self.rettangolo.x -= self.velocita_x 

        if self.rettangolo.right < 0: 
            self.rettangolo.left = self.schermata_rettangolo.right

    def disegna(self): 
        self.schermata.blit(self.immagine, self.rettangolo) 
