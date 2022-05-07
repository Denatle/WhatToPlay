import discord
from modules import parser, randomizer

bot = discord.Bot(sync_commands=True, intents=discord.Intents.all())
games_parser = parser.Parser(config_channel_name="games-config")
games_randomizer = randomizer.Randomizer()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(name='Games')
async def gamesToPlay(ctx):
    games = await games_parser.Games(ctx.guild)
    await ctx.respond(games)

@bot.slash_command(name='Random game')
async def randomGameToPlay(ctx):
    games = await games_parser.Games(ctx.guild)
    await ctx.respond(games_randomizer.randomGame(games))
    
bot.run("OTcxNzI3NTQ5NDEzNTkzMTI4.GW1RQu.VBrZctP9RicDuXbQvhI6oOrWfRhoQ3hYOuCN9Y")
