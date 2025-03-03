from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Callable, Optional
import math

@dataclass
class TimerState:
    current_phase: str = "work"
    reps: int = 0
    is_running: bool = False
    time_remaining: int = 0
    
class PomodoroTimer:
    def __init__(self, config, on_tick: Callable, on_phase_change: Callable):
        self.config = config
        self.state = TimerState()
        self.on_tick = on_tick
        self.on_phase_change = on_phase_change
        self._timer_id: Optional[str] = None
        
    def start(self):
        if not self.state.is_running:
            self.state.is_running = True
            self._start_phase()
    
    def _start_phase(self):
        self.state.reps += 1
        phase_durations = {
            "work": self.config.work_minutes * 60,
            "short_break": self.config.short_break_minutes * 60,
            "long_break": self.config.long_break_minutes * 60
        }
        
        if self.state.reps % (self.config.long_break_interval * 2) == 0:
            self.state.current_phase = "long_break"
        elif self.state.reps % 2 == 0:
            self.state.current_phase = "short_break"
        else:
            self.state.current_phase = "work"
            
        self.state.time_remaining = phase_durations[self.state.current_phase]
        self.on_phase_change(self.state.current_phase)
        self._count_down()
    
    def _count_down(self):
        if self.state.time_remaining > 0 and self.state.is_running:
            self.on_tick(self.state.time_remaining)
            self.state.time_remaining -= 1
            self._timer_id = window.after(1000, self._count_down)
        elif self.state.is_running:
            self._start_phase()
    
    def pause(self):
        self.state.is_running = False
        if self._timer_id:
            window.after_cancel(self._timer_id)
            
    def reset(self):
        self.pause()
        self.state = TimerState()
        self.on_tick(0)
        self.on_phase_change("work")