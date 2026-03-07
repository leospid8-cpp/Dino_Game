from pathlib import Path
import pygame
import random 

class Cactus:
    def __init__(self, Dino_Game): 

        self.incremento = 50 
        self.Bmomento = True
        self.schermata = Dino_Game.schermata 
        self.schermata_rettangolo = Dino_Game.schermata.get_rect() 

        base_path = Path(__file__).resolve().parent
        immagine = pygame.image.load(base_path / "immagini" / "cactus.png") 
        self.immagine = pygame.transform.scale(immagine, (80, 80)) 
        self.rettangolo = self.immagine.get_rect() 
        self.rettangolo.bottomright = self.schermata_rettangolo.bottomright 
        
        self.velocita_x = 5
        
    def aggiorna(self, secondi):
        self.rettangolo.x -= self.velocita_x

        if secondi >= self.incremento:
            self.incremento += 50
            self.velocita_x += 1

        

    def disegna(self): 
        self.schermata.blit(self.immagine, self.rettangolo) 
        
