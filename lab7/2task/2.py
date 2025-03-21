import pygame
import os

pygame.init()
pygame.mixer.init()


w, h = 300, 545

screen = pygame.display.set_mode((w, h))

COL_BACKGROUND = (128, 0, 32)  # Burgundy (deep red)



#image = pygame.image.load()

path1 = "/Users/tanzilya/Documents/new_folder/labs/lab7/2task"
songs = [file for file in os.listdir(path1) if file.endswith(".mp3")]

screen.fill(COL_BACKGROUND)

#geometric drawings
pygame.draw.circle(screen, (50, 45, 50), (150, 345), 131)
pygame.draw.circle(screen, (255, 255, 245), (150, 345), 130)
pygame.draw.circle(screen, (50, 45, 50), (150, 345), 51)
pygame.draw.circle(screen, (255, 255, 245), (150, 345), 50)
pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(40, 22, 220, 176))

#icons
next_img = pygame.image.load("next.png")
next_img = pygame.transform.scale(next_img, (50, 50))
prev_img = pygame.image.load("previous.png")
prev_img = pygame.transform.scale(prev_img, (50, 50))
play_img = pygame.image.load("play.png")
play_img = pygame.transform.scale(play_img, (50, 50))
pause_img = pygame.image.load("pause.png")
pause_img = pygame.transform.scale(pause_img, (50, 50))


screen.blit(next_img, (215, 320))
screen.blit(prev_img, (35, 320))
screen.blit(play_img, (125, 320))
#screen.blit(this_love, (62, 22))

play_btn = False
skip_btn = False
prev_btn = False
current_song = 0
paused = False

def play_song():
    pygame.mixer.music.load(os.path.join(path1, songs[current_song]))
    pygame.mixer.music.play()
    song_name = songs[current_song]  
    cover = pygame.image.load(song_name[:-4]+".jpeg")
    cover = pygame.transform.scale(cover, (176, 176))
    screen.blit(cover, (62, 22))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    play_song()

            elif event.key == pygame.K_RIGHT:
                current_song = (current_song + 1) % len(songs)  
                paused = False 
                play_song()

            elif event.key == pygame.K_LEFT:
                current_song = (current_song - 1) % len(songs)  
                paused = False 
                play_song()

    if not pygame.mixer.music.get_busy() and not paused:
        current_song = (current_song + 1) % len(songs)  
        play_song()
        
    if pygame.mixer.music.get_busy():
        pygame.draw.circle(screen, (255, 182, 255), (150, 345), 50)

        screen.blit(pause_img, (125, 320))
    else:
        pygame.draw.circle(screen, (255, 255, 245), (150, 345), 50)
        screen.blit(play_img, (125, 320))
    

    
    

    pygame.display.flip()


        