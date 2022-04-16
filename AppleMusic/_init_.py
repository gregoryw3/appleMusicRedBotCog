from .AppleMusic import AppleMusic


def setup(bot):
    bot.add_cog(AppleMusic(bot))