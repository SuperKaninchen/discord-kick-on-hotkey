import discord
import keyboard
from discord.ext import commands

bot = commands.Bot(command_prefix='koh:')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    channel = discord.utils.get(bot.get_all_channels(), name='general')
    await channel.send("Bot online")


async def kick(member: discord.Member):
    await member.move_to(None)


def key_pressed():
    kick(user)


hotkey = "alt+k"
user = "USER_TO_KICK"
keyboard.add_hotkey(hotkey, key_pressed)
bot.run(token)
