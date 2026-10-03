import os
import discord

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
        response = reply(message.content)

    await message.reply(response)

client.run(os.environ["DISCORD_BOT_TOKEN"])