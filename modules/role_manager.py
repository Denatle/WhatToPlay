import discord
import random


class RoleManager:
    def __init__(self) -> None:
        self.random_color = lambda: random.randint(0, 255)

    async def createRolesByGames(self, games: list, guild: discord.Guild):
        for _, game in enumerate(games):
            await guild.create_role(name=game, color=discord.Color.from_rgb(
                self.random_color(),
                self.random_color(),
                self.random_color()))
