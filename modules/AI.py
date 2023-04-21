import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import json
from datetime import date, time, datetime, timedelta
import aiohttp
import random
import requests
import asyncio
import subprocess

class AI(commands.Cog, name="AI"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()        
    async def ai(self, ctx, *, prompt: str):
        cmd = '''curl --silent --location --request POST 'http://127.0.0.1:8080/api' \
--header 'Content-Type: application/json' \
--data-raw '{
 
        "model": "openai:gpt-3.5-turbo",
        'prompt': f'"{prompt}"\nAI:',
}' | grep -oP '(?<="data":")[^"]*'
        '''
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            await ctx.send(f"```\n{result}\n```")
        except subprocess.CalledProcessError as exc:
            await ctx.send(f"Command failed with exit code {exc.returncode}: ```\n{exc.output}\n```")

def setup(bot):
    bot.add_cog(AI(bot))
