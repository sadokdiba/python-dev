import pygame
from threading import Thread
import time
from pathlib import Path

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sound_dir = Path(__file__).parent.parent / "assets" / "sounds"
        
    def play_phase_sound(self, phase: str, repeat: int = 1):
        sound_file = self.sound_dir / f"{phase}.mp3"
        
        def play():
            for _ in range(repeat):
                pygame.mixer.music.load(str(sound_file))
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
                    
        Thread(target=play, daemon=True).start()