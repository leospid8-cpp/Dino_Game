from pathlib import Path
import pygame

class Cactus:
    def __init__(self, Dino_Game): 

        self.incremento = 50 #momento in secondi in cui aumentare la velocità del cactus

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

        if secondi >= self.incremento:  #aumenta la velocità del cactus ogni 50 secondi
            self.incremento += 50 #aggiorna il momento in cui aumentare la velocità
            self.velocita_x += 1 #aumenta la velocità del cactus di 1 ogni 50 secondi

        if self.rettangolo.right < 0: 
            self.rettangolo.left = self.schermata_rettangolo.right 

    def disegna(self): 
        self.schermata.blit(self.immagine, self.rettangolo) 
