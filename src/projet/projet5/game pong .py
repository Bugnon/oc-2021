import pygame
import math
import random
import sys

pygame.init()
pygame.display.set_caption('Pong') 
screen = pygame.display.set_mode((1200, 800))

# classe game
class Game:
    
    def __init__(self):
        # definir si notre jeu a commencé
        # charger la palette de gauche
        self.palet1 = Palet1()
        # charger la palette de droite
        self.palet2 = Palet2()
        # charger la balle
        self.ball = Ball(self)
        # charger le texte
        self.label = Text('pong', (10, 10))
        self.label1 = Text('0',  (450, 350))
        self.label2 = Text('0',  (685, 350))
        
        # charger la bannière
        self.banner = Button('images2.0/Pong.jpg', (600, 300), (500, 200))
        # charger le boutton
        self.button = Button('images2.0/play.jpg', (600, 500), (400, 150))

        # charger le score
        self.score1 = 0 
        self.score2 = 0
        
        self.running = True
        self.playing = False
        
        # charger le fond d'écran
        self.background = pygame.image.load('images2.0/background.png')
        self.background = pygame.transform.scale(self.background, (1200, 800))
        self.rect = self.background.get_rect()

    def run(self):
        # boucle tant que la condition est vrai
        while self.running:
            
            # appliquer l'arriere plan du jeu
            screen.blit(self.background, (0, 0))
            
            # si le joueur ferme la fenetre
            for event in pygame.event.get():
                # evenement est la fermeture de la fenetre
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                
                # evenement est appuyer sur "q"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.playing = False
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.rect.collidepoint(event.pos):
                        self.playing = True

                self.palet1.do_event(event)
                self.palet2.do_event(event)
                
            if self.score1 == 10 or self.score2 == 10:
                    self.playing = False
                    screen.blit(self.background, (0, 0))
                
            # si le jeu a commencé
            if self.playing:
                # les sprites bougent
                self.palet1.move()
                self.palet2.move()
                self.ball.move()
            
            # si le jeu a commencé
            if self.playing:
                # les éléments se dessinent
                self.palet1.draw()
                self.palet2.draw()
                self.ball.draw()
                self.label.draw()
                self.label1.draw()
                self.label2.draw()
            # si le jeu n'a pas commencé
            else:
                # les élément bannière et boutton se dessinent
                self.button.draw()
                self.banner.draw()
                
            # mettre a jour l'ecran
            pygame.display.flip()
        
    def start(self):
        self.is_playing = True
        
    def game_over(self):
        self.is_playing = False
        self.score = 0


# classe texte
class Text:
    def __init__(self, text, pos=(0, 0)):
        self.font = pygame.font.Font(None, 100)
        self.color = (255, 255, 255)
        self.text = text
        self.pos = pos
        self.render(text)

    def render(self, text):
        self.image = self.font.render(text, 1, self.color)

    def draw(self):
        screen.blit(self.image, self.pos)


# classe boutton
class Button(pygame.sprite.Sprite):

    def __init__(self, path, pos, size):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def draw(self):
        screen.blit(self.image, self.rect)


# classe palette de gauche
class Palet1(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.image = pygame.image.load('images2.0/palet.png')
        self.image = pygame.transform.scale(self.image, (20, 150))
        self.rect = self.image.get_rect()
        self.rect.topleft = 50, 100
        self.mask = pygame.mask.from_surface(self.image)

    def do_event(self, event):
        # la palette sait comment bouger
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                self.speed = -10
            elif event.key == pygame.K_x:
                self.speed = 10
        elif event.type == pygame.KEYUP:
            self.speed = 0
        
    def move(self):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 800:
            self.rect.bottom = 800
        
    def draw(self):
        screen.blit(self.image, self.rect)


# classe palette de droite
class Palet2(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.image = pygame.image.load('images2.0/palet.png')
        self.image = pygame.transform.scale(self.image, (20, 150))
        self.rect = self.image.get_rect()
        self.rect.topleft = 1135, 100
        self.mask = pygame.mask.from_surface(self.image)
        
    def do_event(self, event):
        # la palette sait comment bouger
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                self.speed = -10
            elif event.key == pygame.K_m:
                self.speed = 10
        elif event.type == pygame.KEYUP:
            self.speed = 0
        
    def move(self):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 800:
            self.rect.bottom = 800
        
    def draw(self):
        screen.blit(self.image, self.rect)


# classe balle
class Ball(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = [5, 5]
        self.image = pygame.image.load('images2.0/ball02.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.init()

    def init(self):
        self.rect.center = 600, 400

    def move(self):
        self.rect.move_ip(self.velocity)

        # collision en bas
        if self.rect.bottom > self.game.rect.bottom:
            self.velocity[1] = -5

        # collision à droite
        if self.rect.right > self.game.rect.right:
            self.game.score1 += 1
            self.game.label1.render(str(self.game.score1))
            self.init()
    
        # collision en haut
        if self.rect.top < self.game.rect.top:
            self.velocity[1] = 5

        # collision à gauche
        if self.rect.left < self.game.rect.left:
            self.game.score2 += 1
            self.game.label2.render(str(self.game.score2))
            self.init()

        # collision palette gauche
        if self.rect.colliderect(self.game.palet1.rect):
            self.velocity[0] = 5

        # collision palette droite
        if self.rect.colliderect(self.game.palet2.rect):
            self.velocity[0] = -5

    def draw(self):
        screen.blit(self.image, self.rect)


# charger le jeu
game = Game()
game.run()