import discord
from discord.commands import OptionChoice
import random


class RoleManager:
    def __init__(self) -> None:
        self.random_color = lambda: random.randint(0, 255)

    async def createRolesByGames(self, games: list, guild: discord.Guild):
        for _, game in enumerate(games):
            role = discord.utils.get(guild.roles, name=game)
            if role:
                continue
            await guild.create_role(name=game, color=discord.Color.from_rgb(
                self.random_color(),
                self.random_color(),
                self.random_color()))
            
    async def getGameRoles(self, games: list, guild: discord.Guild):
        roles = []
        for _, game in enumerate(games):
            role = discord.utils.get(guild.roles, name=game)
            if role:
                roles += role
    
    async def clearGameRoles(self, games: list, guild: discord.Guild):
        for _, game in enumerate(games):
            role = discord.utils.get(guild.roles, name=game)
            if role:
                await role.delete()
