import discord
import asyncio

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents, fetch_offline_members = True )


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	server = client.guilds[0]
	greetChannel = discord.utils.get(client.get_all_channels() , name='welcome-and-rules')
	msg = await greetChannel.fetch_message('764755625053126696')
	react = msg.reactions[0]

	async def scanMsg():
		while True:
			await asyncio.sleep(1)
			loop = asyncio.get_running_loop()
			end_time = loop.time() + 3.0
			print("Checking...")
			async for user2 in react.users():
				user2 = server.get_member(user2.id)
				print(user2)
				role = discord.utils.get(server.roles, name="juicyturkeylegger")
				if user2.id == 759379169045118976:
					print(user2.display_name + " is the bot.")
				else:
					if role in user2.roles:
						print(user2.display_name + " is already in.")
						await react.remove(user2)
					else:
						await user2.add_roles(role)
						print(user2.display_name + " is now in.")
						await react.remove(user2)
	task = asyncio.create_task(scanMsg())
	
	

	


client.run(os.environ['botToken'])
