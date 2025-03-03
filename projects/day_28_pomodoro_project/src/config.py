from dataclasses import dataclass
from typing import Dict

@dataclass
class TimerConfig:
    work_minutes: int = 25
    short_break_minutes: int = 5
    long_break_minutes: int = 20
    long_break_interval: int = 4
    sound_repeat: int = 3

@dataclass
class ThemeConfig:
    PINK: str = "#e2979c"
    RED: str = "#e7305b"
    GREEN: str = "#9bdeac"
    YELLOW: str = "#f7f5dd"
    FONT_NAME: str = "Courier"
    
    def get_phase_colors(self) -> Dict[str, str]:
        return {
            "work": self.GREEN,
            "short_break": self.PINK,
            "long_break": self.RED
        }