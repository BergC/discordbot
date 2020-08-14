import discord

# Import our token
def read_token():
    with open("token.txt", "r") as f:
        lines  = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

# Welcome a new member
@client.event # Event decorator
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server {member.mention}""")

# Send messages via user commands
@client.event # Event decorator
async def on_message(message):
    server_id = client.get_guild(743565065252372480)
    server_channels = ["whatever"] # Channels our bot will reply into
    valid_users = ["ocysp#0437"] # Users that are authorized to use bot commands

    if str(message.channel) in server_channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("hi")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {server_id.member_count}""")
    else:
        print(f"""User: {message.author} tried initiate command {message.content}""")

client.run(token)

