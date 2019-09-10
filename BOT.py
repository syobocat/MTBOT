'''
ルールなど
Python上級者の方で「ここはこうしたほうがいい」というものがありましたら追記・変更ご自由にどうぞ。


'''

# 設定　よほどのことがなければ変更しないこと
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!!')
bot.remove_command('help')

# ここからコマンド

#ヘルプコマンド。コマンドを追加した場合、周りに従って追記すること。
@bot.command()
async def help(ctx, tohelp='all'): #tohelpにはヘルプを表示するコマンド名が入る
    if tohelp == 'all':
        embed = discord.Embed(title='現在利用可能なコマンドは以下のとおりです。', description='', color=0xffffff)
        embed.add_field(name='!!say', value='任意のテキストを送信します。', inline=False)

        #!!helpの説明は一番最後に
        embed.add_field(name='!!help', value='この一覧を表示します。', inline=False)
        await ctx.send(embed=embed)
    if tohelp == 'say':
        embed = discord.Embed(title='使用方法 ： `!!say <文字列>`', description='任意のテキストを送信します。', color=0xffffff)
        await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, message='使用方法 ： `!!say 文字列`'):
    await ctx.send(message)
    await ctx.delete()

# 接続　絶対に書き換えない。
bot.run('NjIwOTYxMTQ0NjU5NzcxMzky.XXesQA.aIDTt3LD_pbt7-rBgW-281v9CZk')