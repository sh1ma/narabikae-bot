from discord.ext.commands import Bot, Cog, Context, command


class Narabikae(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def narabikae(self, ctx: Context) -> None:
        await ctx.channel.edit(position=0)


def setup(bot: Bot) -> None:
    bot.add_cog(Narabikae(bot))
