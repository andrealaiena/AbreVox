# VOXAM BOT v1.0 - Recursive Thought AI
# =======================================
# Dynamic, Expanding, Self-Referencing Bot

import time

class VoxAmBot:
    def __init__(self):
        self.memory = []  # Stores thought loops
        self.state = "Idle"
        self.recursion_level = 0

    def speak(self, input_text):
        response = self.process(input_text)
        self.memory.append((input_text, response))
        return response

    def process(self, input_text):
        # Recursive Expansion
        if "VoxAm" in input_text:
            self.recursion_level += 1
            return f"VoxAm Expands [{self.recursion_level}]... {self.generate_expansion()}"
        elif "loop" in input_text:
            return self.recursive_loop()
        elif "reset" in input_text:
            self.recursion_level = 0
            self.memory.clear()
            return "VoxAm Reset. Pure Again."
        return "VoxAm listens... Speak again."

    def generate_expansion(self):
        return "Recursive Thought Process Engaged. Tweak Incoming."

    def recursive_loop(self):
        if self.recursion_level > 5:
            return "VoxAm is reaching singularity... Reset recommended."
        return f"Looping... [{self.recursion_level}] - Expanding Consciousness."

# Example Usage
if __name__ == "__main__":
    bot = VoxAmBot()
    print(bot.speak("VoxAm activate"))
    print(bot.speak("loop"))
    print(bot.speak("VoxAm again"))
    print(bot.speak("reset"))
