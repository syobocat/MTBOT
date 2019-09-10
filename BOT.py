import discord
from discord.ext import commands

# 設定
bot = commands.Bot(command_prefix='!!')
bot.remove_command('help')

# コマンド
@bot.command()
async def help(ctx, tohelp='all'):
    if tohelp == 'all':
        embed = discord.Embed(title='現在利用可能なコマンドは以下のとおりです。', description='', color=0xffffff)
        embed.add_field(name='!!help', value='この一覧を表示します。', inline=False)
        await ctx.send(embed=embed)

# 接続
bot.run('NjIwOTYxMTQ0NjU5NzcxMzky.XXeaXw.Li_xIVO4nh8KtT0rlkvFskyRhoE')
