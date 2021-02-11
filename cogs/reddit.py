import discord
from discord.ext import commands
import aiohttp
import random

class RedditCog(commands.Cog):
  def __init__(self, bot):
        self.bot = bot

  default_subreddit = "h" # The subreddit that is displayed when using the command without any arguments.
  @commands.command(name="reddit")
  async def subreddit(self, ctx : commands.Context, subreddit=default_subreddit):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://www.reddit.com/r/{subreddit}/hot.json') as r:
            res = await r.json()
            random_post = random.randint(1, 25)
            
            if res["data"]["children"][random_post]['data']["over_18"] == True:
              res["data"]["children"][random_post]['data']["url"] = "https://media4.giphy.com/media/10kABVanhwykJW/giphy.gif"
              res["data"]["children"][random_post]['data']["title"] = "This post is marked as NSFW, therefore it will not be displayed, sorry!"
              res["data"]["children"][random_post]['data']["permalink"] = "/r/olzieisabaddev"
            
            embed = discord.Embed(
              description = res['data']['children'][random_post]['data']['selftext'],
              color = discord.Colour.orange())

            embed.set_author(name=res['data']['children'][random_post]['data']['title'], url=f"https://reddit.com{res['data']['children'][random_post]['data']['permalink']}")
            
            embed.set_image(url=res["data"]["children"][random_post]['data']["url"])
            
            embed.set_footer(text=f"👍 {res['data']['children'][random_post]['data']['ups']} 💬 {res['data']['children'][random_post]['data']['num_comments']}")
            
            await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(RedditCog(bot))
