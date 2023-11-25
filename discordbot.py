from me import *
import random, requests, datetime, sys
import os
from typing import Any
import os
import BCSFE_Python
import http.client
import urllib.parse
import json
import string
import io
import discord
import yaml
import time
import json
from discord import app_commands
import zlib
from discord.ext import commands
cooltime = 86400
user_dict = {}
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())
points = {}
admin_ids = [1117808934011555855, 1119864305895084052, 1122291140515872808, 819436785998102548, 887622983852642314, 1080459282044166184, 1066271383744696400] #1066271383744696400 : james
TOKEN = ''
bot_cmd_channel = 1130128084562096260
bc_edit_log_channel = 1130128211141988362
account_error_chanel = 1130128244289585272
free_sling_channel = 1130128281253986385
ticket_channel = 1130128309716525187
review_channel = 1130128328708345916
def convert_time(seconds):
    hours = minutes = 0
    if seconds >= 3600:
        hours, seconds = divmod(seconds, 3600)
    if seconds >= 60:
        minutes, seconds = divmod(seconds, 60)
    time_format = f"{hours}시간{minutes}분{seconds}초"
    return time_format

# def save_save_stats(in_username, save_stats):
#     webhook_url = ''
#     save_stats = json.dumps(save_stats).encode('utf-8')
#     temp_file = io.BytesIO(save_stats)
#     temp_file.seek(0)
#     files = {'file': (f'{in_username}.json', temp_file)}
#     response = requests.post(webhook_url, files=files)
#     if response.status_code == 200:
#         print("Message sent successfully!")
#     else:
#         print(f"Error sending message: {response.status_code}")
#     temp_file.close()
def get_all_cats(in_username, in_gamever, in_transfer_code, in_confirmation_code):
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)
        save_stats = edits.cats.get_remove_cats.get_all_cat__(save_stats)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def cat_food(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_value):
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["cat_food"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def edit_xp(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_value):
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["xp"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def edit_np(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_value):
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["np"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def normal_tickets(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_value):
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["normal_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass

def rare_tickets(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_value):
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["rare_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def platinum_tickets(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_value):
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["platinum_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def legend_tickets(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_value):
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["legend_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def re_inquiry_code(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_value):
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["inquiry_code"] = in_value
        save_stats["token"] = "0" * 40
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def gold_pass(in_username, in_gamever, in_transfer_code, in_confirmation_code):
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)
        officer_id = edits.other.get_gold_pass.get_random_officer_id
        save_stats = edits.other.get_gold_pass.get_gold_pass_val(save_stats, 30, officer_id)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.event
async def on_ready():
	print("Bot is ready!")
	try:
		synced = await bot.tree.sync()
		print(f"Synced {len(synced)} commands(s)")

	except Exception as e:
		print(e)


@bot.tree.command(name="rare_tickets", description="계정에 레어티켓 충전 [1COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력", item_value = "레어티켓 갯수[MAX:299]")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str, item_value: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == bot_cmd_channel:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"레어티켓 {item_value}개 충전이 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = rare_tickets(author_name, gamever, transfer_code, confirmation_code, item_value)
                embedVar = discord.Embed(title="레어티켓 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 레어티켓 {item_value}개 충전을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="레어티켓 충전", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 레어티켓 {item_value}개 충전 성공했습니다.",inline=False)
                e_channel = bot.get_channel(bc_edit_log_channel)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#{ticket_channel}>", ephemeral=True)
        else:
            await interaction.response.send_message(f"티켓 충전 요청은 <#{bot_cmd_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 코인은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(account_error_chanel)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
######################################################################################
@bot.tree.command(name="all_cats", description="모든 캐릭터 얻기 [1COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == bot_cmd_channel:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"모든캐릭터 추가가 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = get_all_cats(author_name, gamever, transfer_code, confirmation_code)
                embedVar = discord.Embed(title="캐릭터추가 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 모든 캐릭터추가 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="캐릭터 추가", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 모든 캐릭터추가 성공했습니다.",inline=False)
                e_channel = bot.get_channel(bc_edit_log_channel)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#{ticket_channel}>", ephemeral=True)
        else:
            await interaction.response.send_message(f"충전 요청은 <#{bot_cmd_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 코인은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(account_error_chanel)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="cat_food", description="계정에 통조림 충전 [1COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력", item_value = "통조림 갯수[MAX:45000]")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str, item_value: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == bot_cmd_channel:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"통조림 {item_value}개 충전이 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = cat_food(author_name, gamever, transfer_code, confirmation_code, item_value)
                embedVar = discord.Embed(title="통조림 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 통조림 {item_value}개 충전을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="통조림 충전", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 통조림 {item_value}개 충전 성공했습니다.",inline=False)
                e_channel = bot.get_channel(bc_edit_log_channel)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#{ticket_channel}>", ephemeral=True)
        else:
            await interaction.response.send_message(f"충전 요청은 <#{bot_cmd_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 코인은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(account_error_chanel)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="xp", description="계정에 XP 충전 [1COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력", item_value = "XP 갯수[MAX:99999999]")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str, item_value: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == bot_cmd_channel:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"XP {item_value}개 충전이 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = edit_xp(author_name, gamever, transfer_code, confirmation_code, item_value)
                embedVar = discord.Embed(title="XP 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 XP {item_value}개 충전을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="XP 충전", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 XP {item_value}개 충전 성공했습니다.",inline=False)
                e_channel = bot.get_channel(bc_edit_log_channel)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#{ticket_channel}>", ephemeral=True)
        else:
            await interaction.response.send_message(f"충전 요청은 <#{bot_cmd_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 코인은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(account_error_chanel)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="np", description="계정에 np 충전 [1COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력", item_value = "np 갯수[MAX:9999]")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str, item_value: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == bot_cmd_channel:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"np {item_value}개 충전이 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = edit_np(author_name, gamever, transfer_code, confirmation_code, item_value)
                embedVar = discord.Embed(title="np 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 np {item_value}개 충전을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="np 충전", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 np {item_value}개 충전 성공했습니다.",inline=False)
                e_channel = bot.get_channel(bc_edit_log_channel)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#{ticket_channel}>", ephemeral=True)
        else:
            await interaction.response.send_message(f"충전 요청은 <#{bot_cmd_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 코인은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(account_error_chanel)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="normal_tickets", description="계정에 냥코티켓 충전 [1COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력", item_value = "냥코티켓 갯수[MAX:299]")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str, item_value: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == bot_cmd_channel:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"냥코티켓 {item_value}개 충전이 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = normal_tickets(author_name, gamever, transfer_code, confirmation_code, item_value)
                embedVar = discord.Embed(title="냥코티켓 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 냥코티켓 {item_value}개 충전을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="냥코티켓 충전", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 냥코티켓 {item_value}개 충전 성공했습니다.",inline=False)
                e_channel = bot.get_channel(bc_edit_log_channel)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#{ticket_channel}>", ephemeral=True)
        else:
            await interaction.response.send_message(f"충전 요청은 <#{bot_cmd_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 코인은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(account_error_chanel)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="platinum_tickets", description="계정에 플레티넘티켓 충전 [1COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력", item_value = "플레티넘티켓 갯수[MAX:9]")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str, item_value: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == bot_cmd_channel:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"플레티넘티켓 {item_value}개 충전이 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = platinum_tickets(author_name, gamever, transfer_code, confirmation_code, item_value)
                embedVar = discord.Embed(title="플레티넘티켓 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 플레티넘티켓 {item_value}개 충전을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="플레티넘티켓 충전", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 플레티넘티켓 {item_value}개 충전 성공했습니다.",inline=False)
                e_channel = bot.get_channel(bc_edit_log_channel)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#{ticket_channel}>", ephemeral=True)
        else:
            await interaction.response.send_message(f"충전 요청은 <#{bot_cmd_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 코인은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(account_error_chanel)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="legend_tickets", description="계정에 레전드티켓 충전 [1COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력", item_value = "레전드티켓 갯수[MAX:4]")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str, item_value: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == bot_cmd_channel:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"레전드티켓 {item_value}개 충전이 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = legend_tickets(author_name, gamever, transfer_code, confirmation_code, item_value)
                embedVar = discord.Embed(title="레전드티켓 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 레전드티켓 {item_value}개 충전을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="레전드티켓 충전", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 레전드티켓 {item_value}개 충전 성공했습니다.",inline=False)
                e_channel = bot.get_channel(bc_edit_log_channel)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#{ticket_channel}>", ephemeral=True)
        else:
            await interaction.response.send_message(f"충전 요청은 <#{bot_cmd_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 코인은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(account_error_chanel)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="re_inquiry_code", description="문의코드 재발급 [1COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == bot_cmd_channel:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"문의코드 재발급 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = re_inquiry_code(author_name, gamever, transfer_code, confirmation_code)
                embedVar = discord.Embed(title="문의코드 재발급 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 문의코드 재발급 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="문의코드 재발급", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 문의코드 재발급 성공했습니다.",inline=False)
                e_channel = bot.get_channel(bc_edit_log_channel)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#{ticket_channel}>", ephemeral=True)
        else:
            await interaction.response.send_message(f"충전 요청은 <#{bot_cmd_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 코인은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(account_error_chanel)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="gold_pass", description="계정에 골드패스 적용 [1COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == bot_cmd_channel:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"골드패스 적용 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = gold_pass(author_name, gamever, transfer_code, confirmation_code)
                embedVar = discord.Embed(title="골드패스 적용 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 골드패스 적용을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="골드패스 적용", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 골드패스 적용 성공했습니다.",inline=False)
                e_channel = bot.get_channel(bc_edit_log_channel)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#{ticket_channel}>", ephemeral=True)
        else:
            await interaction.response.send_message(f"충전 요청은 <#{bot_cmd_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 코인은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(account_error_chanel)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="my_coin", description="내 코인 확인하기")
async def hello(interaction: discord.Interaction):
    try:
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        await interaction.response.send_message(f"{interaction.user.name}님의 보유 코인은 **{point}c**입니다.", ephemeral=True)
    except Exception as e:
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
@bot.tree.command(name="free_coin", description="무료 코인 받기")
async def hello(interaction: discord.Interaction):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        if m_channel == {free_sling_channel}:
            if author_id in user_dict and time.time() - user_dict[author_id] < cooltime:
                cool_time = round(user_dict[author_id] + cooltime - time.time())
                wait_time = convert_time(cool_time)        
                await interaction.response.send_message(f"무료코인 요청 재대기시간이 {wait_time} 남았습니다.", ephemeral=True)
                return
            else:
                user_dict[author_id] = time.time()
                points[interaction.user.id] = points.get(interaction.user.id, 0) + 1
                await interaction.response.send_message(f"무료코인이 요청되었습니다.", ephemeral=False)
        else:
            await interaction.response.send_message(f"무료코인 요청은 <#{free_sling_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")

@bot.event
async def on_message(message):
    try:
        if message.author == bot.user:
            return
        if message.content.startswith('&s') and message.author.id in admin_ids:
            p_user = message.author
            point = points.get(p_user.id, 0)
            points[p_user.id] =+ 100
            await message.delete()
        if message.content.startswith('&data') and message.author.id in admin_ids:
            await message.author.send(f"```{points}```")
        if message.content.startswith('!a') and message.author.id in admin_ids:
            p_user = message.author
            point = points.get(p_user.id, 0)
            member = message.mentions[0]
            points[member.id] = points.get(member.id, 0) + 1
            embedVar = discord.Embed(title="코인 추가", color=0x00ff26)
            embedVar.add_field(name="",value=f"{member.name}님에게 **1sl**를 추가하였습니다.\n**잔여 :{points[member.id]}sl**",inline=False)
            await message.channel.send(embed=embedVar)
            await message.delete()
        if message.content.startswith('!d') and message.author.id in admin_ids:
            p_user = message.author
            point = points.get(p_user.id, 0)
            member = message.mentions[0]
            points[member.id] = points.get(member.id, 0) - 1
            embedVar = discord.Embed(title="코인 차감", color=0x00ff26)
            embedVar.add_field(name="",value=f"{member.name}님에게 **1sl**를 차감하였습니다.\n**잔여 :{points[member.id]}sl**",inline=False)
            await message.channel.send(embed=embedVar)
            await message.delete()
        if message.channel.id == bot_cmd_channel and message.author != bot.user:
            await message.delete()
        if message.channel.id == free_sling_channel and message.author != bot.user:
            await message.delete()
    except Exception as e:
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
if __name__ == "__main__":
access_tocken-os.environ"["BOT_TOCKEN"]
    bot.run(access_tocken)
