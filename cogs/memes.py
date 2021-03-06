import random
from discord.ext import commands
from utils import commands as command


class Memes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        if command.if_command_disabled(ctx.command.name, ctx.guild):
            return
        memes_submissions = self.client.reddit.subreddit('memes').new()
        post_to_pick = random.randint(1, 10)
        for _ in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url) # noqa

    @commands.command()
    async def dankmeme(self, ctx):
        if command.if_command_disabled(ctx.command.name, ctx.guild):
            return
        memes_submissions = self.client.reddit.subreddit('dankmemes').new()
        post_to_pick = random.randint(1, 10)
        for _ in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url)  # noqa


def setup(client):
    client.add_cog(Memes(client))


if __name__ == "__main__":
    import sys
    import os
    import pathlib
    os.chdir(f"{pathlib.Path(__file__).parent.absolute()}/..")
    os.system(f"{sys.executable} {pathlib.Path(__file__).parent.absolute()}/../main.py")
