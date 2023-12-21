import tkinter as tk
from tkinter import messagebox
import time
import pygame

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        self.minutes = 0
        self.seconds = 5  # Modificado para pruebas, puedes ajustar a 25 minutos
        self.is_running = False

        self.label = tk.Label(master, text="")
        self.label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack()
        self.stop_button["state"] = "disabled"

        self.update_display()

        # Configuración de pygame para la reproducción de audio
        pygame.init()
        self.sound_file = "path/to/your/song.mp3"  # Reemplaza con la ruta de tu canción
        self.sound = pygame.mixer.Sound(self.sound_file)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button["state"] = "disabled"
            self.stop_button["state"] = "normal"
            self.run_timer()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.start_button["state"] = "normal"
            self.stop_button["state"] = "disabled"

    def run_timer(self):
        if self.is_running:
            if self.minutes == 0 and self.seconds == 0:
                self.is_running = False
                self.play_sound()
                messagebox.showinfo("Pomodoro Timer", "¡Tiempo completado!")
                self.reset_timer()
            else:
                if self.seconds == 0:
                    self.minutes -= 1
                    self.seconds = 59
                else:
                    self.seconds -= 1

                self.update_display()
                self.master.after(1000, self.run_timer)

    def update_display(self):
        time_str = f"{self.minutes:02d}:{self.seconds:02d}"
        self.label.config(text=time_str)

    def reset_timer(self):
        self.minutes = 0
        self.seconds = 5  # Modificado para pruebas, puedes ajustar a 25 minutos
        self.update_display()
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"

    def play_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.sound_file)
        pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    timer = PomodoroTimer(root)
    root.mainloop()
