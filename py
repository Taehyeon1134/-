py
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user}이(가) 준비되었습니다.')

@bot.command()
async def 환영(ctx, member: discord.Member):
    await ctx.send(f'{member.mention}, 안녕하세요. FRANCE 오신걸 환영하며 규칙 숙지 부탁드립니다.')
@bot.command()
async def 늅(ctx, member: discord.Member):
    await ctx.send(f'{member.mention}, 적응이 힘드시다면 백서아 멘션 부탁드려요.')

bot.run('token')

