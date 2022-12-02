import pygame
import random
pygame.init()

#var
WIDTH = 700
HIGHT = 500

display = pygame.display.set_mode((WIDTH,HIGHT))
caption = pygame.display.set_caption("StarShip")

icon_image = pygame.image.load(r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\logo.png")

icon = pygame.display.set_icon(icon_image)

class Player_Sprite():
    Player_image = pygame.image.load(r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\player.png").convert_alpha()
    Player_x = 0
    Player_y = 450
    def __init__(self):
        display.blit(Player_Sprite.Player_image, (Player_Sprite.Player_x - 20, Player_Sprite.Player_y - 15))
        
class Space_Rock_Sprite():
    images_list = [r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\Meteor1.png",
                   r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\Meteor2.png"]
    ran_list = random.choice(images_list)
    rock_image = pygame.image.load(ran_list).convert_alpha()
    Space_Rock_Speed = 10
    Space_Rock_Sprite_x = random.randint(0, 700)
    Space_Rock_Sprite_y = 0
    def __init__(self):
        display.blit(Space_Rock_Sprite.rock_image, (Space_Rock_Sprite.Space_Rock_Sprite_x - 10, Space_Rock_Sprite.Space_Rock_Sprite_y - 10))
        Space_Rock_Sprite.Space_Rock_Sprite_y += Space_Rock_Sprite.Space_Rock_Speed
        if Space_Rock_Sprite.Space_Rock_Sprite_y == HIGHT:
            Space_Rock_Sprite.Space_Rock_Sprite_x = random.randint(0, 700)
            Space_Rock_Sprite.Space_Rock_Sprite_y = 0
            Space_Rock_Sprite.Space_Rock_Sprite_y += Space_Rock_Sprite.Space_Rock_Speed
            Space_Rock_Sprite.ran_list = random.choice(Space_Rock_Sprite.images_list)
            Space_Rock_Sprite.rock_image = pygame.image.load(Space_Rock_Sprite.ran_list).convert_alpha()
            
class Healer_Sprite():
    healer_image = pygame.image.load(r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\energy.png").convert_alpha()
    Healer_Sprite_speed = 5
    Healer_Sprite_x = random.randint(0, 700)
    Healer_Sprite_y = 0
    def __init__(self):
        display.blit(Healer_Sprite.healer_image, (Healer_Sprite.Healer_Sprite_x, Healer_Sprite.Healer_Sprite_y))
        Healer_Sprite.Healer_Sprite_y += Healer_Sprite.Healer_Sprite_speed
        if Healer_Sprite.Healer_Sprite_y == HIGHT:
            Healer_Sprite.Healer_Sprite_x = random.randint(0, 700)
            Healer_Sprite.Healer_Sprite_y = 0
            Healer_Sprite.Healer_Sprite_y += Healer_Sprite.Healer_Sprite_speed
            
class TheTurtle():
    TheTurtle_x = 200
    TheTurtle_y = -30000 #-30000
    TheTurtle_image = pygame.image.load(r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\the turtle ship.png").convert_alpha()
    def __init__(self):
        display.blit(TheTurtle.TheTurtle_image, (TheTurtle.TheTurtle_x, TheTurtle.TheTurtle_y))
        TheTurtle.TheTurtle_y += 2
        TheTurtle.TheTurtle_x += 0

class bg():
    bg_image = pygame.image.load(r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\Bg.png").convert_alpha()
    def __init__(self):
        display.blit(bg.bg_image, (0,0))

def win():
    ron = True
    while ron:
        image2 = pygame.image.load(r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\You Win.png")
        display.blit(image2, (0,-90))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ron = False
                pygame.quit()
                break
        
        try:
            pygame.display.update()
        except:
            pass
  
def game_over():
    ran = True
    while ran:
        image1 = pygame.image.load(r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\You Lose.png")
        display.blit(image1, (0,-90))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ran = False
                pygame.quit()
        
        try:
            pygame.display.update()
        except:
            pass
           
def start():
    ren = True
    while ren:
        image = pygame.image.load(r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\start.png")
        display.blit(image, (0,-90))
            
        for event in pygame.event.get():
            #exit
            if event.type == pygame.QUIT:
                ren = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    ren = False
                    game_run()
                    break
                if event.key == pygame.K_q:
                    ren = False
                    pygame.quit()
                if event.key == pygame.K_a:
                    pass
        
        try:
            pygame.display.update()
        except:
            pass
            

def game_run():
    #vars
    clock = pygame.time.Clock()
    FPS = 100
    speed = 3.5
    run = True
    life = 9
    
    class Life_count():
        numbers =[r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\numeral0.png",
                  r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\numeral1.png",
                  r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\numeral2.png",
                  r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\numeral3.png",
                  r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\numeral4.png",
                  r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\numeral5.png",
                  r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\numeral6.png"]
        def __init__(self):
            if life/3 <= 1:
                image_num = pygame.image.load(Life_count.numbers[round(life/3)]).convert_alpha()
                img_plane = pygame.image.load(r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\playerLife2_blue.png").convert_alpha()
                display.blit(image_num, (45,15))
                display.blit(img_plane, (0,10))
            
            else:
                image_num = pygame.image.load(Life_count.numbers[round(life/3)]).convert_alpha()
                img_plane = pygame.image.load(r"C:\Users\Gianclarence Solas\Desktop\Pygame SpaceX\images\playerLife2_blue.png").convert_alpha()
                display.blit(image_num, (45,15))
                display.blit(img_plane, (0,10))

    while run:
        clock.tick(FPS)
        bg()
        
        #bind
        Life_count()
        
        TheTurtle_rect = pygame.draw.rect(display, "yellow", pygame.Rect(TheTurtle.TheTurtle_x + 100, TheTurtle.TheTurtle_y + 130, 100, 40))
        TheTurtle()
        
        rect_body_sprite_player = pygame.draw.rect(display, "white", pygame.Rect(Player_Sprite.Player_x, Player_Sprite.Player_y, 20, 20), 0, 2)
        Player_Sprite()
        
        rect_body_sprite_rock = pygame.draw.rect(display, "red", pygame.Rect(Space_Rock_Sprite.Space_Rock_Sprite_x, Space_Rock_Sprite.Space_Rock_Sprite_y, 20, 20), 0, 2)
        Space_Rock_Sprite()
        
        Healer_Sprite_rect = pygame.draw.rect(display, "green", pygame.Rect(Healer_Sprite.Healer_Sprite_x, Healer_Sprite.Healer_Sprite_y, 15, 1), 0, 2)
        Healer_Sprite()
        
        for event in pygame.event.get():
            #exit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        pygame.quit()
                        
        try:    
            keys = pygame.key.get_pressed()
        except:
            pass
        
        #key press left right
        if keys[pygame.K_RIGHT] and Player_Sprite.Player_x < WIDTH - 23:
            Player_Sprite.Player_x += speed
        if keys[pygame.K_LEFT] and Player_Sprite.Player_x > WIDTH - WIDTH:
            Player_Sprite.Player_x -= speed
        
        #colision 
        colision1 = pygame.Rect.colliderect(rect_body_sprite_player, rect_body_sprite_rock)
        colision2 = pygame.Rect.colliderect(rect_body_sprite_player, Healer_Sprite_rect)
        colision3 = pygame.Rect.colliderect(rect_body_sprite_player, TheTurtle_rect)
        
        if colision1:
            life -= 1
            
        if colision2:
            life += 1
            
        if colision3:
            win()
        
        #lose    
        if round(life/3) == 0:
            run = False
            game_over()
            
        if round(life/3) >= 6:
            life -= 1
        
        try:    
            pygame.display.update()
        except:
            pass

if __name__ == "__main__":
    start()