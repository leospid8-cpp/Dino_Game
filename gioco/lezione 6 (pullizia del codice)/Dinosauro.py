from pathlib import Path
import pygame

class Dinosauro:
    def __init__(self, Dino_Game): 

        self.schermata = Dino_Game.schermata 
        self.schermata_rettangolo = Dino_Game.schermata.get_rect() 

        base_path = Path(__file__).resolve().parent
        immagine = pygame.image.load(base_path / "immagini" / "dino.png") 
        self.immagine = pygame.transform.scale(immagine, (110, 110)) 
        self.rettangolo = self.immagine.get_rect() 
        
        self.rettangolo.midbottom = self.schermata_rettangolo.midbottom 

    def disegna(self): 
        self.schermata.blit(self.immagine, self.rettangolo) 
