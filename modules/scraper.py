import discord.utils


class Scraper:
    async def _getGamesMessage(self, guild: discord.guild, channel_name: str):
        channel = discord.utils.get(guild.channels, name=channel_name)
        messages = await channel.history(limit=200).flatten()
        print(messages[::-1])
        return messages[::-1]
