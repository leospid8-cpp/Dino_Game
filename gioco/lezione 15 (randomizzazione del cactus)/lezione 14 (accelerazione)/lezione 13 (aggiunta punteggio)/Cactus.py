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

        if self.rettangolo.right < 0: 

            if self.Bmomento: #prende il momento in cui il cactus esce dallo schermo
                self.momento = 0+secondi #prende i secondi in cui il cactus esce dallo schermo
                self.Bmomento = False #imposta Bmomento a False per evitare che il momento venga aggiornato continuamente
            elif secondi > self.momento+random.randint(1, 40): #aggiunge un nuovo cactus dopo un intervallo di tempo casuale tra 1 e 40 secondi
                self.rettangolo.left = self.schermata_rettangolo.right 
                self.Bmomento = True

    def disegna(self): 
        self.schermata.blit(self.immagine, self.rettangolo) 
