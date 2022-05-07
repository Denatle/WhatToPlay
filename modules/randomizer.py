import random

class Randomizer:
    def __init__(self) -> None:
        pass
    
    async def randomGame(self, games: list):
        return random.choice(games)