from tkinter import Frame, Label, Button, Canvas, PhotoImage
from pathlib import Path

class TimerDisplay(Frame):
    def __init__(self, parent, theme_config, **kwargs):
        super().__init__(parent, **kwargs)
        self.theme = theme_config
        
        self._setup_ui()
        
    def _setup_ui(self):
        self.canvas = Canvas(self, width=200, height=224, 
                           bg=self.theme.YELLOW, highlightthickness=0)
        
        img_path = Path(__file__).parent.parent / "assets" / "images" / "tomato.png"
        self.img = PhotoImage(file=str(img_path))
        self.canvas.create_image(100, 112, image=self.img)
        
        self.timer_text = self.canvas.create_text(
            100, 130, text="00:00", 
            fill="white", 
            font=(self.theme.FONT_NAME, 35, "bold")
        )
        self.canvas.pack()
        
    def update_time(self, seconds: int):
        minutes = math.floor(seconds / 60)
        secs = seconds % 60
        self.canvas.itemconfig(
            self.timer_text, 
            text=f"{minutes:02d}:{secs:02d}"
        )