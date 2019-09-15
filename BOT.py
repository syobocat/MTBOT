'''
ルールなど
Python上級者の方で「ここはこうしたほうがいい」というものがありましたら追記・変更ご自由にどうぞ。


'''

# 設定　よほどのことがなければ変更しないこと
import io
import sys
import subprocess
import discord
import numpy as np
from discord.ext import commands
bot = commands.Bot(command_prefix='!!')
bot.remove_command('help')
token = 'NjIwOTYxMTQ0NjU5NzcxMzky'
token += '.XXetZQ.6xDmzGmjS21b_30fQLMqRgjWJPA'

# ここからコマンド

#ヘルプコマンド。コマンドを追加した場合、周りに従って追記すること。
@bot.command()
async def help(ctx, tohelp='all'): #tohelpにはヘルプを表示するコマンド名が入る
    if tohelp == 'all':
        embed = discord.Embed(title='現在利用可能なコマンドは以下のとおりです。', description='', color=0xffffff)
        embed.add_field(name='!!say', value='任意のテキストを送信します。', inline=False)
        embed.add_field(name='!!isprime', value='素数かどうか判定します。数値以外の入力には対応していません。', inline=False)
        embed.add_field(name='!!calc', value='BOTに計算させることができます。Pythonの標準機能を使用するため、高度なことはできません。', inline=False)
        embed.add_field(name='!!python', value='Pythonのコマンドを実行し、実行結果を返します。', inline=False)

        #!!helpの説明は一番最後に
        embed.add_field(name='!!help', value='この一覧を表示します。', inline=False)
        await ctx.send(embed=embed)
    if tohelp == 'say':
        embed = discord.Embed(title='使用方法 ： `!!say (delete) <文字列>`', description='BOTに任意の文字列を送信させることができます。\n文字列の前にdeleteを入れることにより、本当にBOTが話しているように見せることもできます。', color=0xffffff)
        await ctx.send(embed=embed)

    if tohelp == 'isprime':
        embed = discord.Embed(title='使用方法 ： `!!isprime <数値>`', description='素数かどうか判定します。数値以外の入力には対応していません。', color=0xffffff)
        await ctx.send(embed=embed)

    if tohelp == 'calc':
        embed = discord.Embed(title='使用方法 ： `!!calc <式>`', description='BOTに計算させることができます。', color=0xffffff)
        await ctx.send(embed=embed)

    if tohelp == 'python':
        embed = discord.Embed(title='使用方法 ： `!!python <コマンド>', description='Pythonのコマンドを実行し、実行結果を返します。', color=0xffffff)
        await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, message='使用方法 ： `!!say 文字列`'):
    if message.startswith('delete') == True:
        await discord.ext.commands.bot.discord.message.Message.delete(ctx.message)
        message = message.split()
        message[0] = ''
        message = ' '.join(message)
        message = message.strip()

    await ctx.send(message)

@bot.command()
async def isprime(ctx, *, message='0'):
    returning = "入力が不適切です"
    is_composite = False

    num = int(message)
    if num == 57:
        returning = "#57は素数"
    elif num < 2 or (num % 2 == 0 and num > 2) :
        returning = str(num) + "は素数ではありません"
    else:
        lim = int(np.sqrt(num)) + 1
        for i in range(3, lim, 2):
            if num % i == 0:
                is_composite = True
                break
        if is_composite:
            returning = str(num) + "は素数ではありません"
        else:
            returning = str(num) + "は素数です"
    await ctx.send(returning)

@bot.command()
async def calc(ctx, *, formula):
    await ctx.send(eval(formula))

@bot.command()
async def python(ctx, *, toexe):
    DoAlthoughOver2000 = toexe.startswith('over2000')
    if DoAlthoughOver2000 == True:
        toexe = toexe.split()
        toexe[0] = ''
        toexe = ' '.join(toexe)
        toexe = toexe.strip()

    with open("temp.py", "w") as f:
        print(toexe, file=f)

    result = subprocess.check_output(['python', 'temp.py']).decode('utf-8')
    if len(result) + 6 >= 2000:
        if DoAlthoughOver2000 == True:
            result = '```\n' + result
            result = splitlines(result)
            i = 1
            startline = 0
            for i in range(1, len(result)):
                temp = result[startline:i]
                temp = '\n'.join(temp)
                if len(temp) + 3 >= 2000:
                    endline = i - 1
                    content = result[startline:endline]
                    content = '\n'.join(content) + '\n```'
                    startline = endline + 1
                    await ctx.send(content)
                else:
                    endline = i
            content = result[startline:endline]
            content = '\n'.join(content) + '\n```'
            await ctx.send(content)
        else:
            await ctx.send('出力された文字数が2000を超えています。続行するには`over2000`オプションをつけてください。')
    else:
        result = '```\n' + result + '\n```'
        await ctx.send(result)


# 接続
bot.run(token)
