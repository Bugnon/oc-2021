""""TRON

Deux motos génèrent des traces derrière eux, et qui ne peut pas être franchi 

La trace est représenter

"""
from dis import dis
import os
import pygame
from datetime import datetime
pygame.init()
os.chdir('assets')
moto1image = pygame.image.load('Player1.png')
moto2image = pygame.image.load('Player2.png')
clock = pygame.time.Clock()
screen_size = 800
base_screen_size = screen_size
target_size = screen_size
screen = pygame.display.set_mode((screen_size, screen_size))
police = pygame.font.Font("dogica.ttf",int(screen.get_width() / 15))
pygame.display.set_caption("TRON","Player1.png")
points = [0,0]

nom1 = "Rouge"
nom2 = "Bleu"

def load_animation(image,scalex,scaley):
    img = []
    for i in range(int(image.get_width() / image.get_height())):
        rect = pygame.Rect(i * image.get_height(),0,image.get_height(),image.get_height())
        i = pygame.transform.scale(image.subsurface(rect),(scalex,scaley))
        img.append(i)
    return img

class transition:
    def __init__(self):
        super().__init__()
        self.anim_in = load_animation(pygame.image.load("transition_in.png"),screen.get_width(),screen.get_height())
        self.anim_out = load_animation(pygame.image.load("transition_out.png"),screen.get_width(),screen.get_height())
        self.anim_speed = 0.2
        self.current_sprite = 0

    def animation_in(self):
        global screen
        self.current_sprite += self.anim_speed
        if int(self.current_sprite) >= len(self.anim_in):
            return True
        screen.blit(self.anim_in[int(self.current_sprite)],pygame.Rect(0,0,screen.get_width(),screen.get_height()))
        return False
    def animation_out(self):
        global screen
        self.current_sprite += self.anim_speed
        if int(self.current_sprite) >= len(self.anim_out):
            return True
        screen.blit(self.anim_out[int(self.current_sprite)],pygame.Rect(0,0,screen.get_width(),screen.get_height()))
        return False
class game:
    def setup(self):
        self.moto1 = moto(moto1image,50 - moto1image.get_width() / 2,screen.get_height() / 2 - moto1image.get_height() / 2,[pygame.K_d,pygame.K_a,pygame.K_s,pygame.K_w],(255,0,0),180,nom1)
        self.moto2 = moto(moto2image,screen.get_width() - 50 - moto1image.get_width() / 2,screen.get_height() / 2 - moto1image.get_height() / 2,[pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP],(0,0,255),0,nom2)
class menu_image(pygame.sprite.Sprite):
    global screen
    def __init__(self):
        super().__init__()
        self.anim_insert_coin = load_animation(pygame.image.load("menu_insert_coin.png"),screen.get_width(),screen.get_height())
        self.anim_coin = load_animation(pygame.image.load("menu_coin.png"),screen.get_width(),screen.get_height())
        self.menu_rect = self.anim_insert_coin[0].get_rect()
        self.menu_rect.width = screen.get_width()
        self.menu_rect.height = screen.get_height()
        self.current_anim = self.anim_insert_coin
        self.current_sprite = 0
        self.image = self.current_anim[self.current_sprite]
    
    def update(self):
        self.current_sprite += 0.2
        if int(self.current_sprite) >= len(self.current_anim):
            self.current_sprite = 0
        self.image = self.current_anim[int(self.current_sprite)]
        screen.blit(self.image,self.menu_rect)
    
    def start_game(self):
        self.current_anim = self.anim_coin
        self.current_sprite = 0
        while True:
            pygame.display.set_caption("TRON","Player1.png")
            self.current_sprite += 0.2
            if int(self.current_sprite) >= len(self.current_anim):
                return
            self.image = self.current_anim[int(self.current_sprite)]
            screen.blit(self.image,self.menu_rect)
            pygame.display.update()
            clock.tick(60)
def reset_game(gagnant,pos):
    global screen
    global police
    global transition
    time_before_restart = 3
    current_time = datetime.now()
    rayon = 80
    while True:
        pygame.display.set_caption("TRON","Player1.png")
        if (datetime.now() - current_time).seconds > time_before_restart - 1:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        fond(bg)
        
        game.moto1.draw_trail()
        game.moto2.draw_trail()
        game.moto1.blit()
        game.moto2.blit()

        text = police.render("{} a gagné !".format(gagnant),True,"white","black")
        text_rect = text.get_rect()
        xtext = screen.get_width() / 2 - text_rect.width / 2
        ytext = screen.get_width() / 4
        text_rect.x = xtext
        text_rect.y = ytext
        screen.blit(text,text_rect)

        if rayon > 10:
            rayon *= 0.96
        pygame.draw.circle(screen,"white",(pos.x,pos.y),rayon,4)
        
        
        pygame.display.update()
        clock.tick(60)
    
    check = check_win()
    if check == "ROUGE":
        transition_in = False
        transition.current_sprite = 0
        while transition_in == False:
            pygame.display.set_caption("TRON","Player1.png")
            transition_in = transition.animation_in()
            if transition_in == True:
                main_menu()
            pygame.display.update()
            clock.tick(60)
    elif check == "BLEU":
        transition_in = False
        transition.current_sprite = 0
        while transition_in == False:
            pygame.display.set_caption("TRON","Player1.png")
            transition_in = transition.animation_in()
            if transition_in == True:
                main_menu()
            pygame.display.update()
            clock.tick(60)
    
    global screen_size
    global target_size
    target_size -= 200
    while True:
        pygame.display.set_caption("TRON","Player1.png")
        pygame.display.set_caption("TRON","Player1.png")
        screen_size += window_size(screen_size,target_size)
        if abs(screen_size - target_size) < 10:
            screen_size = target_size
            screen = pygame.display.set_mode((screen_size, screen_size))
            police = pygame.font.Font("dogica.ttf",int(screen.get_width() / 15))
            break
        screen = pygame.display.set_mode((screen_size, screen_size))
        fond(bg)
        pygame.display.update()
        clock.tick(60)
    game.moto1 = moto(moto1image,50 - moto1image.get_width() / 2,screen.get_height() / 2 - moto1image.get_height() / 2,[pygame.K_d,pygame.K_a,pygame.K_s,pygame.K_w],(255,0,0),180,nom1)
    game.moto2 = moto(moto2image,screen.get_width() - 50 - moto1image.get_width() / 2,screen.get_height() / 2 - moto1image.get_height() / 2,[pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP],(0,0,255),0,nom2)
    main_game()

class moto(pygame.sprite.Sprite):
    def __init__(self,img,posx,posy,touches,couleur,rotation,name):
        super().__init__()
        self.name = name
        self.health = 1
        self.max_health = 1
        self.velocity = 2
        self.base_image = img
        self.image = pygame.transform.rotate(self.base_image,rotation)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.dir = (0,0)
        if rotation == 0:
            self.dir = (-1,0)
        elif rotation == 180:
            self.dir = (1,0)
        self.line_points = [self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2]
        self.line_rect = []
        self.touches = touches
        self.color = couleur

        self.points = [self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2]
        self.maxpoints = 25
        self.d_entre_pts = 1
        self.points_distance = 1
        self.point_connecte = []
    def left(self):
        if self.dir == (-1,0):
            return
        self.line_points += self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2
        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(self.base_image, 0)
        rect_b = self.image.get_rect()
        
        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(0,1),(0,-1))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
        self.dir = (-1,0)

    def down(self):
        if self.dir == (0,-1):
            return
        self.line_points += self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2
        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(self.base_image, 90)
        rect_b = self.image.get_rect()

        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(1,0),(-1,0))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
        self.dir = (0,-1)    

    def right(self):
        if self.dir == (1,0):
            return
        self.line_points += self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2
        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(self.base_image, 180)
        rect_b = self.image.get_rect()

        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(0,1),(0,-1))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
        self.dir = (1,0)

    def up(self):
        if self.dir == (0,1):
            return
        self.line_points += self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2
        rect_a = self.image.get_rect()
        self.image = pygame.transform.rotate(self.base_image, 270)
        rect_b = self.image.get_rect()

        if rect_a != rect_b:
            pos = pos_apres_rot(self.dir,self.image,(1,0),(-1,0))
            self.rect.x += pos[0]
            self.rect.y += pos[1]
            
        self.dir = (0,1)

    def moto_controller(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.touches[0]:
                self.right()
            elif event.key == self.touches[1]:
                self.left()
            elif event.key == self.touches[2]:
                self.down()
            elif event.key == self.touches[3]:
                self.up()        
    def move(self):
        self.rect.x += self.dir[0] * self.velocity
        self.rect.y -= self.dir[1] * self.velocity

    def blit(self):
        screen.blit(self.image, self.rect)
    def draw_trail(self):
        self.line_rect.clear()
        if len(self.line_points) > 2:
            for i in range(0,int(len(self.line_points) - 2),2):
                self.line_rect += pygame.draw.line(screen,self.color,(self.line_points[i],self.line_points[i+1]),(self.line_points[i+2],self.line_points[i+3]),5)
        self.line_rect += pygame.draw.line(screen,self.color,(self.line_points[-2],self.line_points[-1]),(self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_height() / 2),5)
    def get_collision(self):
        collisions.extend(self.line_rect)
    
    def apply_collision(self):
        global points
        collision_size = 0.4
        hit_list = []
        for i in range(0,int(len(collisions)),4):
            rect = pygame.Rect(collisions[(i):(i+4)])
            if self.dir[0] != 0:
                collision = pygame.Rect(self.rect.x + max(0,self.dir[0]) * self.image.get_width() * (1 - collision_size),self.rect.y,self.image.get_width() * collision_size,self.image.get_height())
            else:
                collision = pygame.Rect(self.rect.x,self.rect.y + abs(min(0,self.dir[1])) * self.image.get_height() * (1 - collision_size),self.image.get_width(),self.image.get_height() * collision_size)
            if(collision.colliderect(rect)):
                hit_list.append(rect)
        if len(hit_list) != 0:
            pos = pygame.Rect.clip(self.rect,hit_list[0])
            pos.x += pos.width / 2
            pos.y += pos.height / 2
            if self.name == nom1:
                points[1] += 1
                gagnant = nom2
            else:
                points[0] += 1
                gagnant = nom1
            reset_game(gagnant,pos)
            
def pos_apres_rot(dirbase,image,dir1,dir2):
    pos = [0,0]
    if(dirbase == dir1 or dirbase == dir2):
        pos[0] -= image.get_width() / 2 - image.get_height() / 2
        pos[1] += image.get_width() / 2 - image.get_height() / 2
    return pos

def fond(image):
    # /!\ il faut que la largeur et longueur de la fenetre soit un multiple de 100 car le fond fait 100x100 px
    nb_x = int(screen.get_width() / 100) + 1
    nb_y = int(screen.get_height() / 100) + 1

    for x in range(nb_x):
        for y in range(nb_y):
            screen.blit(image, (x * 100, y * 100))

def window_size(current_size,target_size):
    speed = 5
    size = 0
    if size != target_size:
        if abs(current_size - target_size) < 5:
            size = 0
        elif current_size < target_size:
            size = speed
        elif current_size > target_size:
            size = -speed
    return size

son = pygame.mixer.Sound('music/music_TRON.wav')
son.set_volume(0.1)
son.play(loops=-1, maxtime=0, fade_ms=0)

bg = pygame.image.load('bg.png')

class Button():
    def __init__(self,x,y,image,w,h):
        self.image = image
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = pygame.Rect(x,y,w,h)
        self.clicked = False
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

def start_main_game():
    global transition
    transition.current_sprite = 0
    animation_finie = False
    while animation_finie == False:
        pygame.display.set_caption("TRON","Player1.png")
        pygame.display.set_caption("TRON","Player1.png")
        fond(bg)
        game.moto1.blit()
        game.moto2.blit()
        animation_finie = transition.animation_out()
        pygame.display.update()
        clock.tick(60)
    main_game()

def check_win():
    global points
    if points[0] == 2:
        return "ROUGE"
    elif points[1] == 2:
        return "BLEU"
    return ""
def main_game():
    global screen_size
    global target_size
    global screen
    time_before_start = 3
    current_time = datetime.now()
    while True:
        pygame.display.set_caption("TRON","Player1.png")
        if (datetime.now() - current_time).seconds > time_before_start - 1:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        fond(bg)
        text = police.render(str(time_before_start - (datetime.now() - current_time).seconds),True,"white")
        text_rect = text.get_rect()
        xtext = screen.get_width() / 2 - text_rect.width / 2
        ytext = screen.get_width() / 4
        text_rect.x = xtext
        text_rect.y = ytext
        screen.blit(text,text_rect)

        game.moto1.blit()
        game.moto2.blit()

        

        pygame.display.update()
        clock.tick(60)
    
    global points
    score = pygame.image.load("score.png")
    while True:
        pygame.display.set_caption("TRON","Player1.png")
        screen_size += window_size(screen_size,target_size)
        screen = pygame.display.set_mode((screen_size, screen_size))
        fond(bg)
        for event in pygame.event.get():
            game.moto1.moto_controller(event)
            game.moto2.moto_controller(event)
            if event.type == pygame.QUIT:
                pygame.quit()
        game.moto1.draw_trail()
        game.moto2.draw_trail()
        game.moto1.move()
        game.moto2.move()
        game.moto1.blit()
        game.moto2.blit()
        global collisions
        collisions = []
        game.moto1.get_collision()
        game.moto2.get_collision()
        game.moto1.apply_collision()
        game.moto2.apply_collision()

        current_score = pygame.transform.scale(score,(score.get_width() * screen.get_width() / 200,score.get_height() * screen.get_width() / 200))
        score_rect = pygame.Rect(screen.get_width() / 2 - current_score.get_width() / 2,0,current_score.get_height(),current_score.get_width())
        screen.blit(current_score,score_rect)

        rouge_score = police.render(str(points[0]),True,"white")
        bleu_score = police.render(str(points[1]),True,"white")

        rouge_score_rect = rouge_score.get_rect()
        rouge_score_rect.x = screen.get_width() / 2 - rouge_score_rect.width / 2 - score_rect.height / 4
        rouge_score_rect.y = score_rect.width / 2 - rouge_score_rect.height / 2

        bleu_score_rect = bleu_score.get_rect()
        bleu_score_rect.x = screen.get_width() / 2 - bleu_score_rect.width / 2 + score_rect.height / 4
        bleu_score_rect.y = score_rect.width / 2 - bleu_score_rect.height / 2

        screen.blit(rouge_score,rouge_score_rect)
        screen.blit(bleu_score,bleu_score_rect)

        pygame.display.update()
        clock.tick(60)

def main_menu():
    global points
    global screen
    global menu_image
    global transition
    global base_screen_size
    global screen_size
    transition.current_sprite = 0
    animation_finie = False
    target_size = base_screen_size
    
    while abs(screen_size - target_size) > 5:
        pygame.display.set_caption("TRON","Player1.png")
        screen_size += window_size(screen_size,target_size)
        screen = pygame.display.set_mode((screen_size, screen_size))
    screen = pygame.display.set_mode((base_screen_size,base_screen_size))
    while animation_finie == False:
        pygame.display.set_caption("TRON","Player1.png")
        menu_image.update()
        animation_finie = transition.animation_out()
        pygame.display.update()
        clock.tick(60)
    points = [0,0]
    insert_coin = Button(screen.get_width() / 2 - 100,screen.get_height() / 2 - 50,pygame.image.load('transparent.png'),200,200)
    regles = Button(10, 10, pygame.image.load('livre_regles.png'),100,100)
    back = Button(screen.get_width() - 110, 10, pygame.image.load('back.png'),100,100)
    regles_ouvertes = False
    touches = pygame.image.load("touches.png")
    touches = pygame.transform.scale(touches,(touches.get_width() * 3,touches.get_height() * 3))
    regles_texte = pygame.image.load("regles_texte.png")
    regles_texte = pygame.transform.scale(regles_texte,(regles_texte.get_width() * 3,regles_texte.get_height() * 3))
    regles_texte_rect = pygame.Rect(screen.get_width() / 2 - regles_texte.get_width() / 2,screen.get_width() / 2,regles_texte.get_width(),regles_texte.get_height())
    touches_rect = pygame.Rect(screen.get_width() / 2 - touches.get_width() / 2,screen.get_width() / 4,touches.get_width(),touches.get_height())
    while True:
        pygame.display.set_caption("TRON","Player1.png")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
        if regles_ouvertes == True:
            screen.fill((0,0,0))
            screen.blit(touches,touches_rect)
            screen.blit(regles_texte,regles_texte_rect)
            if back.draw():
                regles_ouvertes = False

        if regles_ouvertes == False:
            menu_image.update()
            if insert_coin.draw():
                menu_image.start_game()
                game.moto1 = moto(moto1image,50 - moto1image.get_width() / 2,screen.get_height() / 2 - moto1image.get_height() / 2,[pygame.K_d,pygame.K_a,pygame.K_s,pygame.K_w],(255,0,0),180,nom1)
                game.moto2 = moto(moto2image,screen.get_width() - 50 - moto1image.get_width() / 2,screen.get_height() / 2 - moto1image.get_height() / 2,[pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP],(0,0,255),0,nom2)
                points = [0,0]
                transition.current_sprite = 0
                menu_image.current_anim = menu_image.anim_insert_coin
                while transition.animation_in() == False:
                    pygame.display.set_caption("TRON","Player1.png")
                    pygame.display.update()
                    clock.tick(60)
                start_main_game()
            elif regles.draw():
                regles_ouvertes = True
            
            
                
        pygame.display.update()
        clock.tick(60)
transition = transition()
menu_image = menu_image()
game = game()
main_menu()