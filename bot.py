import discord
from modules import parser

bot = discord.Bot(sync_commands=True, intents=discord.Intents.all())
games_parser = parser.Parser(config_channel_name="games-config")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command()
async def games(ctx):
    games = await games_parser.Games(ctx.guild)
    await ctx.respond(games)

bot.run("OTcxNzI3NTQ5NDEzNTkzMTI4.GW1RQu.VBrZctP9RicDuXbQvhI6oOrWfRhoQ3hYOuCN9Y")
