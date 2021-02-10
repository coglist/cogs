import discord
from discord.ext import commands
import aiohttp


class AnimeCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="hug")
  async def huguser(self, ctx: commands.Context, user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/hug') as r:
        res = await r.json()
        if user == ctx.author: 
         embed = discord.Embed(
           description=f"**{ctx.author.name}** hugs themselves! (somehow)",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           description=f"**{ctx.author.name}** hugs **{user.name}**",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

  @commands.command(name="kiss")
  async def kissuser(self, ctx: commands.Context, user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/kiss') as r:
        res = await r.json()
        if user == ctx.author:
         embed = discord.Embed(
           description=f"**{ctx.author.name}** kisses themselves (i guess?)",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           description=f"**{ctx.author.name}** kisses **{user.name}**",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

  @commands.command(name="pat")
  async def patuser(self, ctx: commands.Context, user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/pat') as r:
        res = await r.json()
        if user == ctx.author:
         embed = discord.Embed(
           description=f"**{ctx.author.name}** pats themselves!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           description=f"**{ctx.author.name}** pats **{user.name}**",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
    
  @commands.command(name="avatar")
  async def anime_avatar(self, ctx: commands.Context):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/avatars') as r:
        res = await r.json()
        embed = discord.Embed(
         description="**Here's your anime avatar!**",
         color=discord.Colour.random()
         )
        embed.set_image(url=res['url'])
        await ctx.reply(embed=embed)

  @commands.command(name="wallpaper")
  async def anime_wallpaper(self, ctx: commands.Context):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/wallpapers') as r:
        res = await r.json()
        embed = discord.Embed(
          description="**Here's your wallpaper!**",
          color=discord.Colour.random()
        )
        embed.set_image(url=res['url'])
        await ctx.reply(embed=embed)


def setup(bot):
  bot.add_cog(AnimeCog(bot))
