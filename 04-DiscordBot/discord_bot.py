import discord

client = discord.Client()
@client.event
async def on_ready():
    # De bot kan op veel verschillende servers draaien. Met deze regel code pak je de eerste server die deze bot heeft. Als jouw bot maar 1 server heeft is het makkelijk.
    guild = client.guilds[0]
    # De naam van de server printen we gelijk uit.
    print(guild.name, "is the name of the server")

    # We printen de naam van de bot user uit.
    print(client.user, "has connected to the client")
client.run("OTA2MTY0MzAyNDkzNDEzNDI2.YYUpRQ.wBIsHLfvE9aN32H0T1SMfELHvH0")
