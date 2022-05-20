import discord
from discord.ext.commands import has_permissions, cooldown, BucketType

from modules.randomizer import Randomizer
from modules.parser import Parser
from modules.role_manager import RoleManager

from config import *

bot = discord.Bot(auto_sync_commands=True, intents=discord.Intents.all())
games_parser = Parser(config_channel_name="games-config")
games_randomizer = Randomizer()
role_manager = RoleManager()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(name='games',
                   description="Gets server's games to play with friends",
                   guild_ids=[910065668563533894])
async def gamesToPlay(ctx: discord.commands.context.ApplicationContext):
    games = await games_parser.Games(ctx.guild, asList=False)
    await ctx.respond(games, ephemeral=True)


@bot.slash_command(name='random_game',
                   description="Gets random game to play from server's",
                   guild_ids=[910065668563533894])
async def randomGameToPlay(ctx: discord.commands.context.ApplicationContext):
    games = await games_parser.Games(ctx.guild)
    game = await games_randomizer.randomGame(games)
    await ctx.respond(game, ephemeral=True)


@has_permissions(manage_roles=True)
@bot.slash_command(name='create_roles',
                   description="Creates a role for each game from config-channel",
                   guild_ids=[910065668563533894])
async def createRolesByGames(ctx: discord.commands.context.ApplicationContext):
    games = await games_parser.Games(ctx.guild)
    await role_manager.createRolesByGames(games, ctx.guild)
    await ctx.respond("Roles created!", ephemeral=True)


@cooldown(2, 30, BucketType.user)
@bot.slash_command(name='poll',
                   description="Starts poll for game",
                   guild_ids=[910065668563533894])
async def poll(ctx: discord.commands.context.ApplicationContext,
               game_role: discord.Option(discord.Role, "Game role")):
    games = await games_parser.Games(ctx.guild)
    if game_role.name in games:
        await ctx.respond("✅", ephemeral=True)
        description = await games_parser.Poll(guild=ctx.guild)
        embed = discord.Embed(
            title='!POLL!',
            description=description.format(game_role.mention),
            color=0xffffff)
        message = await ctx.send(game_role.mention, embed=embed)
        await message.add_reaction("🟢"), await message.add_reaction("🔴")
    else:
        await ctx.respond("Not a game role", ephemeral=True)

@bot.slash_command(name='help',
                   description="Help with deployment",
                   guild_ids=[910065668563533894])
async def help(ctx: discord.commands.ApplicationContext):
    await ctx.respond(HELP, ephemeral=True)


@bot.event
async def on_application_command_error(ctx, error):
    await ctx.respond(error, ephemeral=True)

bot.run(TOKEN)
