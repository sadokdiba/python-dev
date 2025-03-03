from tkinter import Tk
from .components import TimerDisplay
from ..timer import PomodoroTimer
from ..utils.sound_manager import SoundManager
from ..config import TimerConfig, ThemeConfig

class PomodoroApp:
    def __init__(self):
        self.window = Tk()
        self.config = TimerConfig()
        self.theme = ThemeConfig()
        self.sound = SoundManager()
        
        self._setup_window()
        self._setup_components()
        self._setup_timer()
        
    def _setup_window(self):
        self.window.title("Enhanced Pomodoro Timer")
        self.window.config(padx=100, pady=50, bg=self.theme.YELLOW)
        
    def _setup_components(self):
        self.timer_display = TimerDisplay(self.window, self.theme)
        self.timer_display.grid(column=1, row=1)
        
        # Add more UI components here...
        
    def _setup_timer(self):
        self.timer = PomodoroTimer(
            self.config,
            on_tick=self._handle_tick,
            on_phase_change=self._handle_phase_change
        )
        
    def _handle_tick(self, remaining: int):
        self.timer_display.update_time(remaining)
        
    def _handle_phase_change(self, phase: str):
        self.sound.play_phase_sound(phase, self.config.sound_repeat)
        # Update UI for new phase...
        
    def run(self):
        self.window.mainloop()