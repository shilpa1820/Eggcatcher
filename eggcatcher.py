import pygame
import math
import random
from pygame import mixer

pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 600))

# seting the game name
pygame.display.set_caption("egg catcher", "eggy")

# setting the icon
icon = pygame.image.load("basket.png")
pygame.display.set_icon(icon)

# background music
mixer.music.load("backgroundforfarm.wav")
mixer.music.play(-1)
# loading the player image
playerimg = pygame.image.load("playerbasket.png")
playerx = 350
playery = 500
playery_change = 0
playerx_change = 0

# creating  eggs
number_of_eggs = 6
eggimage = []
eggx = []
eggy = []
eggx_change = []
eggy_change = []
brokenegg = []
for i in range(number_of_eggs):
    eggimage.append(pygame.image.load("egg.png"))
    eggx.append(random.randint(20,770))
    eggy.append(random.randint(2,20))
    eggx_change.append(0)
    eggy_change.append(0.5)
    # loading broken egg
    brokenegg.append(pygame.image.load("brokenegg.png"))

# loading the background
background = pygame.image.load("farmbacground.png")


# to draw the egg
def egg(x, y, i):
    screen.blit(eggimage[i], (x, y))


# function to draw the player
def player(x, y):
    screen.blit(playerimg, (x, y))

# loading egg drop sound
eggdrop = mixer.Sound("eggcrash.wav")
# creating a function to blit broken egg


def broken(x,y,i):
    if eggy[i]>=495:
        eggdrop.play()
        screen.blit(brokenegg[i],(x,y))


# loading basket moving sound
basket=mixer.Sound("basketmove.wav")


global score
score = 0

# loading the font
font_score = pygame.font.Font("freesansbold.ttf",32)
font_over = pygame.font.Font("freesansbold.ttf",100)


#  function to blit the score
def display_score():
   sscore = font_score.render("score : "+ str(score),True,(0,0,0))
   screen.blit(sscore,(5,5))

def display_over():
    over_txt = font_over.render("GAME OVER",True,(250,0,0))
    screen.blit(over_txt,100,100)




def iscollusion(eggx, eggy, playerx, playery):
    distance = math.sqrt((math.pow(eggx - playerx, 2)) + (math.pow(playery - eggy, 2)))
    if distance <= 25:
        return True
    else:
        return False


running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # key down is pressing the key
            if event.key == pygame.K_LEFT:
                playerx_change = -1
                basket.play()
            if event.key == pygame.K_RIGHT:
                playerx_change = 1
                basket.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    # creating boundaries
    if playerx >= 730:
        playerx = 730
    if playerx <= 10:
        playerx = 10



    playerx += playerx_change




    player(playerx, playery)
    for i in range(number_of_eggs):
        collusion = iscollusion(eggx[i], eggy[i], playerx, playery)
        if collusion:
            score += 1
            eggy[i] = 20
            print(score)
        # creating boundaries for egg2
        if eggy[i] >= 500:
            eggy[i] = random.randint(2,20)
            eggx[i]=random.randint(20,770)
        # egg movemnt
        eggy[i] += eggy_change[i]
        egg(eggx[i], eggy[i], i)
        # broken egg
        broken(eggx[i],eggy[i],i)
    # to display the score
    display_score()


    pygame.display.update()
