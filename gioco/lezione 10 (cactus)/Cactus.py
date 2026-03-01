from pathlib import Path
import pygame

class Cactus:
    def __init__(self, Dino_Game): #il costruttore della classe Cactus prende come parametro l'istanza del gioco principale (Dino_Game) per accedere alla schermata di gioco e alle impostazioni

        self.schermata = Dino_Game.schermata #accesso alla schermata di gioco tramite l'istanza del gioco principale
        self.schermata_rettangolo = Dino_Game.schermata.get_rect() #ottenimento del rettangolo della schermata per posizionare il cactus correttamente

        base_path = Path(__file__).resolve().parent
        immagine = pygame.image.load(base_path / "immagini" / "cactus.png") #caricamento dell'immagine del cactus dalla cartella "immagini"
        self.immagine = pygame.transform.scale(immagine, (80, 80)) #ridimensionamento dell'immagine del cactus a 80x80 pixel
        self.rettangolo = self.immagine.get_rect() #ottenimento del rettangolo dell'immagine del cactus per posizionarlo correttamente
        self.rettangolo.bottomright = self.schermata_rettangolo.bottomright #posizionamento del cactus in basso a destra della schermata
        
        self.velocita_x = 5 #velocità di movimento del cactus verso sinistra
        
    def aggiorna(self): #metodo per aggiornare la posizione del cactus, chiamato ad ogni ciclo di gioco
        self.rettangolo.x -= self.velocita_x #spostamento del cactus verso sinistra in base alla velocità definita

        if self.rettangolo.right < 0: #se il cactus esce completamente dallo schermo a sinistra, lo riposiziona a destra per farlo ricomparire
            self.rettangolo.left = self.schermata_rettangolo.right #posizionamento del cactus a destra della schermata per farlo ricomparire

    def disegna(self): #metodo per disegnare il cactus sulla schermata di gioco, chiamato ad ogni ciclo di gioco
        self.schermata.blit(self.immagine, self.rettangolo) #disegno del cactus sulla schermata di gioco utilizzando il metodo blit di Pygame, che disegna l'immagine del cactus nella posizione definita dal suo rettangolo
