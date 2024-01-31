import discord
import asyncio
import discord.ext as commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


await_response = False
await_hexa = False


async def ask_help(message):
    async with message.channel.typing():
        await asyncio.sleep(2)
    await message.channel.send('comment je peut t\'aider ?')
    return


async def hex_help(message):
    async with message.channel.typing():
        await asyncio.sleep(2)
    await message.channel.send('tu as trouver une chaîne hexadecimal tu dois surement pouvoir en faire quelque chose... Peut tu me la donner ?')

    def check(m):
        return m.author == message.author and m.channel == message.channel

    try:
        hexadecimal = "69703a3139322e3136382e3138302e3130"
        hexadecimal_splited = "69 70 3a 31 39 32 2e 31 36 38 2e 31 38 30 2e 31 30"
        hexadecimal_splited = hexadecimal_splited.split()
        response = await client.wait_for('message', check=check, timeout=10.0)
        mots_de_response = response.content.lower().split()

        if hexadecimal in mots_de_response or all(hex_part in mots_de_response for hex_part in hexadecimal_splited):
            async with message.channel.typing():
                await asyncio.sleep(2)
            await message.channel.send('tu as essayer de convertir ?')
            return
        else:
            async with message.channel.typing():
                await asyncio.sleep(2)
            await message.channel.send(
                'je pense pas que ce soit la bonne chaine hexa...')

            return

    except asyncio.TimeoutError:
        return


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    general_channel = discord.utils.get(
        client.guilds[0].channels, name='test')
    print(general_channel)

    if general_channel:
        async with general_channel.typing():
            await asyncio.sleep(2)
        await general_channel.send("Salut, je suis là pour t'aider si tu as besoin et si tu veux poser une question")
        async with general_channel.typing():
            await asyncio.sleep(2)
        await general_channel.send("Pour le moment, je te conseil de regarder ce site : http://192.168.71.2:3000 , c'est un site que le PDG a dev, et il est truffer de vulnerabilitées, tu devrais pouvoir trouver le mot de passe de son ordi !")


@client.event
async def on_message(message):
    mots_du_message = message.content.lower().split()

    aide = ["aide", "aider", "aidez", "aides", "aident", "m'aider"]
    hexadecimal = "69703a3139322e3136382e3138302e3130"
    hexadecimal_splited = "69 70 3a 31 39 32 2e 31 36 38 2e 31 38 30 2e 31 30"
    hexadecimal_splited = hexadecimal_splited.split()
    mdp = ["mdp", "passe", "motdepasse", "mot-de-passe"]
    user = ["user", "utilisateur", "utilisateurs", "users", "utilisatrices"]
    hexa = ["hexadecimal", "hexa", "hexadécimal", "hexadécimale"]

    if message.author == client.user:
        return

    if hexadecimal in mots_du_message or all(hex_part in mots_du_message for hex_part in hexadecimal_splited):
        async with message.channel.typing():
            await asyncio.sleep(2)
        await message.channel.send('tu as essayer de convertir ?')
        return

    def check(m):
        return m.author == message.author and m.channel == message.channel

    if any(mot in mots_du_message for mot in hexa):
        await hex_help(message)
        return

    if any(mot in mots_du_message for mot in mdp):
        async with message.channel.typing():
            await asyncio.sleep(2)
        await message.channel.send('malheureusement je ne connais aucun des mot de passe...')
        async with message.channel.typing():
            await asyncio.sleep(2)
        await message.channel.send('mais peut etre qui existe un moyen de recuperer un mot de passe en forcant les requttes...')
        return

    if any(mot in mots_du_message for mot in user):
        async with message.channel.typing():
            await asyncio.sleep(2)
        await message.channel.send('malheureusement je ne connais aucun des utilisateurs...')
        async with message.channel.typing():
            await asyncio.sleep(2)
        await message.channel.send("mais la personne qu'on attaque s'appel Fabrice, peut etre qu'il c'est pas creuser le cerveau pour sont nom d'utilisateur...")
        return

    if message.content.startswith('!send'):
        general_channel = discord.utils.get(
            client.guilds[0].channels, name='test')
        await general_channel.send(message.content[6:])
        return


client.run(
    'MTIwMTQ1NDYyOTkxMzkwNzI2MA.GfXtHn.N3i70xykNW_MobcQ2lFpjo9tdDJOVJ38TBKBrg')
