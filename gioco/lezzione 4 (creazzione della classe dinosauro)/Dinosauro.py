from pathlib import Path
import pygame

class Dinosauro:
    def __init__(self, Dino_Game): #inizzializza il dinosauro e ne imposta la posizzione inizziale

        self.schermata = Dino_Game.schermata #prende la schermata dal gioco
        self.schermata_rettangolo = Dino_Game.schermata.get_rect() #prende il rettangolo della schermata

        base_path = Path(__file__).resolve().parent
        immagine = pygame.image.load(base_path / "immagini" / "dino.png") #carica l'immagine del dinosauro
        self.immagine = pygame.transform.scale(immagine, (80, 80)) #ridimensiona l'immagine del dinosauro
        self.rettangolo = self.immagine.get_rect() #prende il rettangolo dell'immagine
        
        self.rettangolo.midbottom = self.schermata_rettangolo.midbottom #posiziona il dinosauro al centro in basso della schermata

    def disegna(self): #disegna il dinosauro sulla schermata
        self.schermata.blit(self.immagine, self.rettangolo) #disegna l'immagine del dinosauro sulla schermata
