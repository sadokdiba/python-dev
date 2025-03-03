from tkinter import Tk
from .components import TimerDisplay
from ..timer import PomodoroTimer
from ..utils.sound_manager import SoundManager
from ..config import TimerConfig, ThemeConfig

class PomodoroApp:
    def __init__(self):
        self.window = Tk()
        self._setup_window()