import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!bot') or client.user.mention:
        server_name = "@" + message.guild.name
        await message.channel.send('HELLO WORLD, {}'.format(server_name))


client.run(YOUR_BOT_TOKEN)
