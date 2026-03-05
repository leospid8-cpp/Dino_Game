from pathlib import Path
import pygame

class Dinosauro:
    def __init__(self, Dino_Game): 

        self.schermata = Dino_Game.schermata 
        self.schermata_rettangolo = Dino_Game.schermata.get_rect() 

        base_path = Path(__file__).resolve().parent
        immagineSalto = pygame.image.load(base_path / "immagini" / "dino4.png")  #carica l'immagine del dinosauro in salto
        immagineCorsa1 = pygame.image.load(base_path / "immagini" / "dino1.png") #carica l'immagine del dinosauro in corsa1
        immagineCorsa2 = pygame.image.load(base_path / "immagini" / "dino2.png") #carica l'immagine del dinosauro in corsa2
        immagineCorsa3 = pygame.image.load(base_path / "immagini" / "dino3.png") #carica l'immagine del dinosauro in corsa3
        self.immagineSalto = pygame.transform.scale(immagineSalto, (110, 110))  # Ridimensiona il frame del salto alla stessa misura del personaggio.
        self.immagineCorsa1 = pygame.transform.scale(immagineCorsa1, (110, 110))  # Ridimensiona il 1° frame di corsa.
        self.immagineCorsa2 = pygame.transform.scale(immagineCorsa2, (110, 110))  # Ridimensiona il 2° frame di corsa.
        self.immagineCorsa3 = pygame.transform.scale(immagineCorsa3, (110, 110))  # Ridimensiona il 3° frame di corsa.

        self.framesCorsa = [self.immagineCorsa1, self.immagineCorsa2, self.immagineCorsa3]  # Lista ordinata dei frame per l'animazione di corsa.
        self.indiceFrame = 0  # Indice del frame attuale nella lista (parte dal primo frame).
        self.timerAnimazione = 0  # Contatore dei frame di gioco usato per rallentare l'animazione.
        self.velocitaAnimazione = 6  # Ogni 6 frame di gioco passa all'immagine successiva.
        self.immagine = self.framesCorsa[self.indiceFrame]  # Inizializza l'immagine corrente (evita errore su self.immagine non definita).

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
            self.timerAnimazione += 1  # A ogni aggiornamento incrementa il timer dell'animazione di corsa.
            if self.timerAnimazione >= self.velocitaAnimazione:  # Quando il timer raggiunge la soglia, cambia frame.
                self.timerAnimazione = 0  # Reset del timer per ricominciare il conteggio.
                self.indiceFrame = (self.indiceFrame + 1) % len(self.framesCorsa)  # Avanza al frame successivo e torna al primo alla fine.
            self.immagine = self.framesCorsa[self.indiceFrame]  # Mostra il frame di corsa selezionato.
            

        if self.saltando: 
            self.immagine = self.immagineSalto  # Durante il salto forza sempre il frame dedicato al salto.
            self.velocita_y += self.gravita 
            self.rettangolo.y += self.velocita_y 

            
            if self.rettangolo.bottom >= self.posizione_terra:
                self.rettangolo.bottom = self.posizione_terra
                self.saltando = False
                self.velocita_y = 0

    def disegna(self): 
        self.schermata.blit(self.immagine, self.rettangolo) 
