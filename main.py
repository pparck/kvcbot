import discord
from discord.ext import commands
from discord.utils import get
import os

app = commands.Bot(command_prefix='+')

calcResult = 0

@app.event
async def on_ready():
    print("로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("KVC클랜 역할지정중")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    await app.process_commands(message)

@app.command(name="ㅎㅇ")
async def hi(ctx):
    topic = ctx.channel.topic
    if topic is not None and '#역할지정' in topic:
        message = ctx.message
        await message.add_reaction("✅")
    else:
        message = ctx.message
        await message.add_reaction("🚫")
        return None

@app.command(name="역할", pass_context=True)
async def Role(ctx, m1, member: discord.Member, m2):
    topic = ctx.channel.topic
    if topic is not None and '#역할지정' in topic:
        message = ctx.message
        if m1 == "주기":

            member = member or None
            if member == None:
                await message.add_reaction("🚫")
                return None

            if m2 == "매니저":
                await message.add_reaction("🚫")
                return None
            elif m2 == "스태프":
                await message.add_reaction("🚫")
                return None

            elif m2 == '후원우수유저':
                await member.add_roles(get(ctx.guild.roles, name='===[ 후원우수유저  ]==='))
                await message.add_reaction("✅")
            elif m2 == 'VIP':
                await member.add_roles(get(ctx.guild.roles, name='===[ 귀빈(VIP) ]==='))
                await message.add_reaction("✅")
            elif m2 == 'VVIP':
                await member.add_roles(get(ctx.guild.roles, name='===[ A 귀빈(VVIP) ]==='))
                await message.add_reaction("✅")
            elif m2 == '후원자':
                await member.add_roles(get(ctx.guild.roles, name='===[ 후원자 ]==='))
                await message.add_reaction("✅")

            elif m2 == '유튜버':
                await member.add_roles(get(ctx.guild.roles, name='===[ 유튜버(YouTuber) ]==='))
                await message.add_reaction("✅")
            elif m2 == '스트리머':
                await member.add_roles(get(ctx.guild.roles, name='===[ 스트리머(streamer) ]==='))
                await message.add_reaction("✅")

            elif m2 == '1차인증':
                await member.add_roles(get(ctx.guild.roles, name='===[ 1차 인증]==='))
                await message.add_reaction("✅")
            elif m2 == '2차인증':
                await member.add_roles(get(ctx.guild.roles, name='===[ 2차 인증 ]==='))
                await message.add_reaction("✅")
            elif m2 == '유저':
                await member.add_roles(get(ctx.guild.roles, name='===[ 유저(User) ]==='))
                await message.add_reaction("✅")

            elif m2 == '블루팀':
                await member.add_roles(get(ctx.guild.roles, name='===[🔵 블루팀 🔵]==='))
                await message.add_reaction("✅")
            elif m2 == '레드팀':
                await member.add_roles(get(ctx.guild.roles, name='===[🔴 레드팀 🔴]==='))
                await message.add_reaction("✅")

            elif m2 == '영화 관람자':
                await member.add_roles(get(ctx.guild.roles, name='🎫ㅣ영화 관람자'))
                await message.add_reaction("✅")
            elif m2 == '클랜전 참여':
                await member.add_roles(get(ctx.guild.roles, name='클랜전 참여'))
                await message.add_reaction("✅")

            elif m2 == '언랭':
                await member.add_roles(get(ctx.guild.roles, name='===[ 언랭(Uncooled) ]==='))
                await message.add_reaction("✅")
            elif m2 == '아이언':
                await member.add_roles(get(ctx.guild.roles, name='===[ 아이언(Iron) ]==='))
                await message.add_reaction("✅")
            elif m2 == '브론즈':
                await member.add_roles(get(ctx.guild.roles, name='===[ 브론즈(bronze) ]==='))
                await message.add_reaction("✅")
            elif m2 == '실버':
                await member.add_roles(get(ctx.guild.roles, name='===[ 실버(Silver) ]==='))
                await message.add_reaction("✅")
            elif m2 == '골드':
                await member.add_roles(get(ctx.guild.roles, name='===[ 골드(Gold) ]==='))
                await message.add_reaction("✅")
            elif m2 == '플레티넘':
                await member.add_roles(get(ctx.guild.roles, name='===[ 플래티넘(Platinum) ]==='))
                await message.add_reaction("✅")
            elif m2 == '다이아':
                await member.add_roles(get(ctx.guild.roles, name='===[ 다이아(Diamond) ]==='))
                await message.add_reaction("✅")
            elif m2 == '불멸':
                await member.add_roles(get(ctx.guild.roles, name='===[ 불멸(Immortal) ]==='))
                await message.add_reaction("✅")
            elif m2 == '레디언트':
                await member.add_roles(get(ctx.guild.roles, name='===[ 레디언트(Radiant) ]==='))
                await message.add_reaction("✅")



        if m1 == "뺏기":

            member = member or None
            if member == None:
                await message.add_reaction("🚫")
                return None

            if m2 == "매니저":
                await message.add_reaction("🚫")
                return None
            elif m2 == "스태프":
                await message.add_reaction("🚫")
                return None

            elif m2 == '후원우수유저':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 후원우수유저  ]==='))
                await message.add_reaction("✅")
            elif m2 == 'VIP':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 귀빈(VIP) ]==='))
                await message.add_reaction("✅")
            elif m2 == 'VVIP':
                await member.remove_roles(get(ctx.guild.roles, name='===[ A 귀빈(VVIP) ]==='))
                await message.add_reaction("✅")
            elif m2 == '후원자':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 후원자 ]==='))
                await message.add_reaction("✅")

            elif m2 == '유튜버':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 유튜버(YouTuber) ]==='))
                await message.add_reaction("✅")
            elif m2 == '스트리머':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 스트리머(streamer) ]==='))
                await message.add_reaction("✅")

            elif m2 == '1차인증':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 1차 인증]==='))
                await message.add_reaction("✅")
            elif m2 == '2차인증':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 2차 인증 ]==='))
                await message.add_reaction("✅")
            elif m2 == '유저':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 유저(User) ]==='))
                await message.add_reaction("✅")

            elif m2 == '블루팀':
                await member.remove_roles(get(ctx.guild.roles, name='===[🔵 블루팀 🔵]==='))
                await message.add_reaction("✅")
            elif m2 == '레드팀':
                await member.remove_roles(get(ctx.guild.roles, name='===[🔴 레드팀 🔴]==='))
                await message.add_reaction("✅")

            elif m2 == '영화 관람자':
                await member.remove_roles(get(ctx.guild.roles, name='🎫ㅣ영화 관람자'))
                await message.add_reaction("✅")
            elif m2 == '클랜전 참여':
                await member.remove_roles(get(ctx.guild.roles, name='클랜전 참여'))
                await message.add_reaction("✅")

            elif m2 == '언랭':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 언랭(Uncooled) ]==='))
                await message.add_reaction("✅")
            elif m2 == '아이언':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 아이언(Iron) ]==='))
                await message.add_reaction("✅")
            elif m2 == '브론즈':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 실버(Silver) ]==='))
                await message.add_reaction("✅")
            elif m2 == '실버':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 실버(Silver) ]==='))
                await message.add_reaction("✅")
            elif m2 == '골드':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 골드(Gold) ]==='))
                await message.add_reaction("✅")
            elif m2 == '플레티넘':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 플래티넘(Platinum) ]==='))
                await message.add_reaction("✅")
            elif m2 == '다이아':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 다이아(Diamond) ]==='))
                await message.add_reaction("✅")
            elif m2 == '불멸':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 불멸(Immortal) ]==='))
                await message.add_reaction("✅")
            elif m2 == '레디언트':
                await member.remove_roles(get(ctx.guild.roles, name='===[ 레디언트(Radiant) ]==='))
                await message.add_reaction("✅")
    else:
        return None

access_token = os.environ["token"]
    
app.run(access_token)
