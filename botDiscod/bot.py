import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        async with message.channel.typing():
            await asyncio.sleep(2)
        await message.channel.send('Hello!')

client.run(
    'MTIwMTQ1NDYyOTkxMzkwNzI2MA.GVoEgN.0F2RKsTu0GDn2U7ISj1toQrCFdqQDdU_BPTTAQ')
