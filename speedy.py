import tkinter as tk
from tkinter import messagebox
from random_word import RandomWords

class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Game")
        self.root.geometry("600x400")
        self.root.configure(bg='#F0F0F0')

        self.score = 0
        self.max_attempts = 3
        self.attempts_left = self.max_attempts
        self.current_word = ""
        self.time_limit = 60

        self.label_word = tk.Label(root, text="", font=("Arial", 24), bg='#F0F0F0')
        self.label_word.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 20))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)

        self.label_feedback = tk.Label(root, text="", font=("Arial", 16), fg='green', bg='#F0F0F0')
        self.label_feedback.pack(pady=10)

        self.label_attempts = tk.Label(root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 16), bg='#F0F0F0')
        self.label_attempts.pack(pady=10)

        self.label_timer = tk.Label(root, text=f"Time left: {self.time_limit} seconds", font=("Arial", 16), bg='#F0F0F0')
        self.label_timer.pack(pady=10)

        self.r = RandomWords()

        self.start_game()

    def start_game(self):
        self.score = 0
        self.label_feedback.config(text="")
        self.label_word.config(text="")
        self.entry.delete(0, "end")
        self.attempts_left = self.max_attempts
        self.label_attempts.config(text=f"Attempts left: {self.attempts_left}")
        self.update_word()
        self.start_timer()

    def update_word(self):
        self.current_word = self.r.get_random_word()
        self.label_word.config(text=self.current_word)

    def check_word(self, event):
        user_input = self.entry.get()
        if user_input == self.current_word:
            self.score += 1
            self.label_feedback.config(text="Correct!", fg='green')
        else:
            self.attempts_left -= 1
            self.label_attempts.config(text=f"Attempts left: {self.attempts_left}")
            if self.attempts_left == 0:
                self.end_game()
            else:
                self.label_feedback.config(text="Incorrect", fg='red')
        self.entry.delete(0, "end")
        self.update_word()

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.timer_running:
            self.label_timer.config(text=f"Time left: {self.time_limit} seconds")
            if self.time_limit > 0:
                self.time_limit -= 1
                self.root.after(1000, self.update_timer)
            else:
                self.end_game()

    def end_game(self):
        self.timer_running = False
        messagebox.showinfo("Game Over", f"Your score: {self.score}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    typing_game = TypingGame(root)
    root.mainloop()
