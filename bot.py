import discord
from modules.randomizer import Randomizer
from modules.parser import Parser
from modules.visualizer import Visualizer

bot = discord.Bot(sync_commands=True, intents=discord.Intents.all())
games_parser = Parser(config_channel_name="games-config")
games_randomizer = Randomizer()
visuals = Visualizer("visuals/visuals.json")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(name='games',
                   description="Gets server's games to play with friends",
                   guild_ids=[910065668563533894])
async def gamesToPlay(ctx):
    games = await games_parser.Games(ctx.guild)
    await ctx.respond(games)


@bot.slash_command(name='random_game',
                   description="Gets random game to play from server's",
                   guild_ids=[910065668563533894])
async def randomGameToPlay(ctx):
    games = await games_parser.Games(ctx.guild, asList=True)
    await ctx.respond(await games_randomizer.randomGame(games))


bot.run("OTcxNzI3NTQ5NDEzNTkzMTI4.GW1RQu.VBrZctP9RicDuXbQvhI6oOrWfRhoQ3hYOuCN9Y")
