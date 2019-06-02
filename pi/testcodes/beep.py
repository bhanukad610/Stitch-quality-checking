import pygame
def alert():
	pygame.mixer.init()
	pygame.mixer.music.load("Smoke Alarm-SoundBible.com-1551222038.wav")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue


alert()


