from pathlib import Path
import pygame

class Dinosauro:
    def __init__(self, Dino_Game): 

        self.schermata = Dino_Game.schermata 
        self.schermata_rettangolo = Dino_Game.schermata.get_rect() 

        base_path = Path(__file__).resolve().parent
        immagineSalto = pygame.image.load(base_path / "immagini" / "dino4.png")  
        immagineCorsa1 = pygame.image.load(base_path / "immagini" / "dino1.png")
        immagineCorsa2 = pygame.image.load(base_path / "immagini" / "dino2.png") 
        immagineCorsa3 = pygame.image.load(base_path / "immagini" / "dino3.png") 
        self.immagineSalto = pygame.transform.scale(immagineSalto, (110, 110))  
        self.immagineCorsa1 = pygame.transform.scale(immagineCorsa1, (110, 110))  
        self.immagineCorsa2 = pygame.transform.scale(immagineCorsa2, (110, 110)) 
        self.immagineCorsa3 = pygame.transform.scale(immagineCorsa3, (110, 110))  

        self.framesCorsa = [self.immagineCorsa1, self.immagineCorsa2, self.immagineCorsa3]  
        self.indiceFrame = 0  
        self.timerAnimazione = 0  
        self.velocitaAnimazione = 6 
        self.immagine = self.framesCorsa[self.indiceFrame]  

        self.rettangolo = self.immagine.get_rect() 
        self.rettangolo.midbottom = self.schermata_rettangolo.midbottom 
        
        self.saltando = False 

        self.forza_salto = -18 
        self.velocita_y = 0 
        self.gravita = 1.2 

        self.posizione_terra = self.rettangolo.bottom 

    def aggiorna(self): 

        if self.saltando == False: 
            keys = pygame.key.get_pressed() 
            self.timerAnimazione += 1  
            if self.timerAnimazione >= self.velocitaAnimazione:  
                self.timerAnimazione = 0  
                self.indiceFrame = (self.indiceFrame + 1) % len(self.framesCorsa) 
            self.immagine = self.framesCorsa[self.indiceFrame] 
            

        if self.saltando: 
            self.immagine = self.immagineSalto  
            self.velocita_y += self.gravita 
            self.rettangolo.y += self.velocita_y 

            
            if self.rettangolo.bottom >= self.posizione_terra:
                self.rettangolo.bottom = self.posizione_terra
                self.saltando = False
                self.velocita_y = 0

    def disegna(self): 
        self.schermata.blit(self.immagine, self.rettangolo) 
