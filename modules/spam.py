#              Send spam to people using bots (Python3) and (Discord.py)
import discord
import ast
import io
import random
import time
import json
import sys
import inspect
import os
import asyncio
import asyncpg
import logging
import aiohttp
import traceback
import requests
import subprocess
import textwrap
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands import Bot, Greedy
from discord.ext.tasks import loop
from discord import User
from asyncio import sleep
from discord.ext import commands
from datetime import datetime
from os import listdir
from os.path import isfile, join
from contextlib import redirect_stdout

class spam(commands.Cog, name="spam"):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def dmspam(self, ctx, users: Greedy[User], * message: str):
		time = 1
		for user in users:
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await user.send(message)
			await asyncio.sleep(time)
			await ctx.message.add_reaction('👌')

	@commands.command()
	async def chspam(self, ctx, channel_id: str, *, message: str):
		if channel_id == channel:
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await self.bot.get_channel(channel).send(message)
		await asyncio.sleep(time)
		await ctx.message.add_reaction('👌')

def setup(bot):
	bot.add_cog(spam(bot))
