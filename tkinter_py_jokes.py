import tkinter as tk
import pygame.mixer
import random
import pyjokes

class TkinterPyJokes:

    SOUND_EFFECTS_DIRECTORY = "./sounds"
    GAME_SPEED = 125
    MAX_LOOPS = 15
    SOUND_VOLUME = 0.25
    LABEL_COLOR = "#000099"
    LABEL_SELECTED_COLOR = "#990000"
    PY_JOKE_CATEGORIES = ["Neutral", "All", "Chuck", "Chuck", "Neutral", "All", "All", "Chuck", "Neutral"]
    ENDING_SOUNDS = [0,7] #This is in relation to the sound effects stored within the game_tiles list.

    def __init__(self):
        self.root = tk.Tk()
        self.game_tiles = []
        self.joke_label = None
        self.start_button = None
        self.current_tile = None
        self.after_id = None
        self.sound_channel = None
        self.game_loops = 0
        self.initialize()

    def initialize(self):
        self.root.title("Random PyJokes")
        self.root.geometry("570x550")
        self.start_button = tk.Button(self.root, text="Go!", width=20, height=1, command=self.start, font=("Helvetica", 24, "bold"))
        self.start_button.place(x=90, y=450)
        self.joke_label = tk.Label(self.root, text="PyJoke: ......", wraplength=500, font=("Helvetica", 12, "bold"), bg="#FFFFFF")
        self.joke_label.place(x=10, y=380)
        pygame.mixer.init()
        self.sound_channel = pygame.mixer.Channel(0)
        self.sound_channel.set_volume(self.SOUND_VOLUME)
        self.create_game_tiles()
        self.root.mainloop()

    def create_game_tiles(self):
        for row in range(3):
            for col in range(3):
                index = row * 3 + col
                label = tk.Label(
                    self.root,
                    text=self.PY_JOKE_CATEGORIES[index],
                    bg=self.LABEL_COLOR,
                    fg="white",
                    width=15,
                    height=5,
                    font=("Helvetica", 14, "bold")
                )
                label.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                sound_file = f"{self.SOUND_EFFECTS_DIRECTORY}/s{index}.mp3"
                self.game_tiles.append((pygame.mixer.Sound(sound_file), label, self.PY_JOKE_CATEGORIES[index]))

    def reset_tile_color(self):
        if self.current_tile is not None:
            self.game_tiles[self.current_tile][1].config(bg=self.LABEL_COLOR)

    def play_sound(self):
        pygame.mixer.stop()
        if self.game_loops == self.MAX_LOOPS-1: #Play the last note in the sequence
            rand_num = random.randint(0, 1)
            sound_file = self.game_tiles[self.ENDING_SOUNDS[rand_num]][0]
            sound_effect = pygame.mixer.Sound(sound_file)
            self.sound_channel.play(sound_effect)
        else:
            self.sound_channel.play(self.game_tiles[self.current_tile][0])

    def start(self):
        if self.game_loops == self.MAX_LOOPS: #The
            self.root.after_cancel(self.after_id)
            self.start_button.config(state="normal") #Enable the start button
            joke_category = self.game_tiles[self.current_tile][2].lower()
            joke = pyjokes.get_joke(language="en", category=joke_category)
            self.joke_label.config(text=f"PyJoke: {joke}") #Display the joke
            self.game_loops = 0
        else:
            if self.game_loops == 0:
                self.start_button.config(state="disabled") #Disable the start button
                self.joke_label.config(text="PyJoke: ......")
            self.reset_tile_color()
            rand_num = random.randint(0, len(self.game_tiles)-1)
            self.game_tiles[rand_num][1].config(bg=self.LABEL_SELECTED_COLOR)
            self.current_tile = rand_num
            self.play_sound()
            self.game_loops += 1
            self.after_id = self.root.after(self.GAME_SPEED, self.start)

tkinterPyJokes = TkinterPyJokes()
