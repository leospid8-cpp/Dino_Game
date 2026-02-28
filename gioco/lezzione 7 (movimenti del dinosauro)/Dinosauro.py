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
        self.saltando = False #variabile per gestire la fase in cui si trova inizzializzata a falso 

    def aggiorna(self):
        if self.saltando:
            self.velocita_y += self.gravita
            self.rettangolo.y += self.velocita_y

            # Controllo se è tornato a terra
            if self.rettangolo.bottom >= self.posizione_terra:
                self.rettangolo.bottom = self.posizione_terra
                self.saltando = False
                self.velocita_y = 0

    def disegna(self): 
        self.schermata.blit(self.immagine, self.rettangolo) 
