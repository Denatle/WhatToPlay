import random

class Randomizer:
    def __init__(self) -> None:
        pass
    
    def randomGame(self, games: list):
        return random.choice(games)