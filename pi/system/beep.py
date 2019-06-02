import pygame
def alert(clip):
	pygame.mixer.init()
	if(clip == 0):
		pygame.mixer.music.load("voiceClips/booting.mp3")
		
		
	if(clip == 1):
		pygame.mixer.music.load("voiceClips/modelcreating.mp3")
		
	if(clip == 2):
		pygame.mixer.music.load("voiceClips/modelcreated.mp3")
		
	if(clip == 3):
		pygame.mixer.music.load("voiceClips/ready.mp3")
		
		
	if(clip == 4):
		pygame.mixer.music.load("voiceClips/beep.wav")
		
	if(clip == 5):
		pygame.mixer.music.load("voiceClips/wait.mp3")
	
	if(clip == 6):
		pygame.mixer.music.load("voiceClips/noimages.mp3")
		
		
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue





