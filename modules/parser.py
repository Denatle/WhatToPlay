import discord


class Parser:
    def __init__(self, config_channel_name: "str"):
        self.channel_name = config_channel_name

    async def _getConfigs(self, guild: discord.Guild):
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        messages = await channel.history(limit=float("inf")).flatten()
        return messages[::-1]

    async def _parseGamesFromConfig(self, messages: list):
        games = messages[1].content.split(",")
        for i, game in enumerate(games):
            games[i] = game.strip()
        return games

    async def Games(self, guild: discord.Guild, *, asList: bool = False):
        messages = await self._getConfigs(guild)
        games = await self._parseGamesFromConfig(messages)
        return games if asList else messages[0].content + " " + ", ".join(games)
