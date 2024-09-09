import random
import os
from dotenv import load_dotenv

import nextcord
from nextcord.ext import commands

import discord
from discord.ext import commands
from utils import generate_puzzle_embed

load_dotenv()

bot = commands.Bot(command_prefix=[], intents = discord.Intents.all())

GUILD_IDS=(
    [int(guild_id) for guild_id in os.getenv("GUILD_IDS").split(",")]
    if os.getenv("GUILD_IDS", None)
    else nextcord.utils.MISSING
)

@bot.event
async def on_ready():
    print("Bot running")

@bot.slash_command()
async def character(ctx):
    with open("characterList.txt","r") as f:
        random_response = f.readlines()
        answer = random.choice(random_response)
    await ctx.send(answer)

@bot.slash_command(description="Play a game of ZZZ wordle!", guild_ids=GUILD_IDS)
async def play(interaction: nextcord.Interaction):
    embed = generate_puzzle_embed()
    await interaction.send(embed = embed)

bot.run(os.getenv("TOKEN"))