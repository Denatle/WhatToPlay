import random

class Randomizer:
    async def randomGame(self, games: list):
        return random.choice(games)