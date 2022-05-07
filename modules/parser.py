import discord.utils


class Parser:
    def __init__(self, config_channel_name: "str"):
        self.channel_name = config_channel_name

    async def _getGamesMessage(self, guild):
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        messages = await channel.history(limit=float("inf")).flatten()
        return (messages[-1].content, messages[-2].content)

    async def _parseGamesFromMessage(self, messages: tuple):
        games = messages[1].split(",")
        for i, game in enumerate(games):
            games[i] = game.strip()

        return (messages[0], games)

    async def Games(self, guild, *, asList: bool = False):
        messages = await self._getGamesMessage(guild)
        games = await self._parseGamesFromMessage(messages)
        return games[1] if asList else games[0] + " " + ", ".join(games[1])
