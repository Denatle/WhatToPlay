import discord
from modules import scraper

bot = discord.Bot(debug_guilds=[910065668563533894])
games_scraper = scraper.Scraper()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command()
async def hello(ctx):
    await ctx.respond("Hello!")

bot.run("OTcxNzI3NTQ5NDEzNTkzMTI4.GW1RQu.VBrZctP9RicDuXbQvhI6oOrWfRhoQ3hYOuCN9Y")
