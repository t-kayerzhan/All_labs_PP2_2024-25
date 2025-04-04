import pygame
import random
import time
from pygame.locals import *

#Pygame initialization
pygame.init()

#Frames per second
clock = pygame.time.Clock()


#Colors 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLDEN = (187, 165, 61)

#Font
font_small = pygame.font.SysFont("Verdana", 20)

#Images
player_img = pygame.image.load("Player.png")
enemy_img = pygame.image.load("Enemy.png")
background_img = pygame.image.load("AnimatedStreet.png")
gameover_img = pygame.image.load("gameover.png")
gameover_img = pygame.transform.scale(gameover_img, (350, 281))
coin_size = 40
coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (coin_size, coin_size))
twocoins_img = pygame.image.load("2coins.png")
twocoins_img = pygame.transform.scale(twocoins_img, (coin_size, coin_size))
fivecoins_img = pygame.image.load("5coins.png")
fivecoins_img = pygame.transform.scale(fivecoins_img, (coin_size, coin_size))

#Sounds:
crash_sound = pygame.mixer.Sound("crash.wav")
coin_sound = pygame.mixer.Sound("coin.mp3")
background_song = pygame.mixer.music.load("bc.mp3")
pygame.mixer.music.play(-1)


#Screen
w, h = 400, 600
screen = pygame.display.set_mode((w, h))
screen.blit(background_img, (0, 0))

#Speeds
player_speed = 5
enemy_speed = 6

#Score and coins variables
score = 0
coins_cnt = 0

#Coin class
class Coin():
    def __init__(self):
        self.x, self.y = 5, h - coin_size - 10
        self.weight = 0
        #Setting Rect of our coin
        self.rect = (self.x, self.y, coin_size, coin_size)
    
    #Generates random position of the coins so they don't appear on the car itself
    def random_pos(self):
        while True:
            self.x = random.randint(5, w - player.rect.w - 5)
            #Generates weight of our coin
            self.weight = random.randint(0, 2)
            self.rect = pygame.Rect(self.x, self.y, coin_size, coin_size) 

            if player.rect.colliderect(self.rect):
                pass
            else:
                break

    def draw(self):
        #Draws a coin based on generated position and weight
        coins = [coin_img, twocoins_img, fivecoins_img]
        screen.blit(coins[self.weight], (self.x, self.y))


#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = w // 2 - self.rect.w // 2
        self.rect.y = h - self.rect.h 
    
    def moving(self):
        #Controlling Player by arrow keys
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-player_speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(player_speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > w:
            self.rect.right = w

    #Checks if tha player touched a coin
    def coin_collision(self, coin):
        global coins_cnt, enemy_speed
        if self.rect.colliderect(coin.rect):
            #Plays a coin sound
            coin_sound.play()
            #Adds up coin's weight, 1, 2 or 5
            if coin.weight == 0:
                coins_cnt += 1
            elif coin.weight == 1:
                coins_cnt += 2
            else:
                coins_cnt += 5
            #Generates the next coin
            coin.random_pos()

        
#Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.random_rect()

    #Enemy moves downsides with current speed
    def moving(self):
        global score
        self.rect.move_ip(0, enemy_speed)
        if self.rect.bottom > h:
            #Score increases by every enemy
            score += 1
            self.random_rect()

    #Generates random position for Enemy
    def random_rect(self):
        self.rect.x = random.randint(0, w - self.rect.w)
        self.rect.y = 0

#Sprites
player = Player()
enemy = Enemy()
coin = Coin()

#Grouping sprites
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

all_sprites.add([player, enemy])
enemy_sprites.add([enemy])

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    #Filling background, printing score and coins counter
    screen.blit(background_img, (0, 0))
    scores = font_small.render(str(score), True, BLACK)
    screen.blit(scores, (10, 10))
    coins_scr = font_small.render(str(coins_cnt), True, GOLDEN)
    screen.blit(coins_scr, (365, 10))

    player.moving()
    enemy.moving()
    #Checking collision of player with a coin
    player.coin_collision(coin)
    #Increasing enemy's cpeed every 10 coins by 1
    enemy_speed = 6 + (coins_cnt // 10) * 0.7
    #Drawing the coins, Enemy and Player
    coin.draw()

    for sprt in all_sprites:
        screen.blit(sprt.image, sprt.rect)

    #Checking the collision with an Enemy
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        #Playing the car crash cound
        crash_sound.play()
        time.sleep(1.5)

        #Game Over screen
        screen.fill(WHITE)
        screen.blit(gameover_img, (25, 100))
        
        #Updating the screen
        pygame.display.flip()

        time.sleep(2)

        running = False

    pygame.display.flip()
    clock.tick(60) #FPS = 60