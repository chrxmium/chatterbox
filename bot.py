import os
import discord
import asyncio
import random

from brain import reply

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    async with message.channel.typing():
        await asyncio.sleep(random.uniform(3, 7))
        response = reply(message.content, user_id=message.author.id)

    await message.reply(response)

client.run(os.environ["DISCORD_BOT_TOKEN"])