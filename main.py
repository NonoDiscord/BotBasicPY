import discord
from discord.ext import commands

base = commands.Bot(command_prefix="PREFIX", help_command = None)

token = "TOKEN BOT"

@base.event
async def on_ready():
    print("BOT ON!")

@base.command()
async def exemple(ctx):
  embed = discord.Embed()
  embed.set_author(name='TITRE'),
  embed.add_field(name='FIELD', value='FIELD')
  embed.set_footer(text='FOOTER')
  await ctx.send(embed=embed)
  
base.run(token)