# The Kryte Team
# Copyright (C) 2025

import requests
import json
import os.path
import os
import subprocess
from pymsgbox import alert

print("Checking if Discord is installed...")

if (not os.path.isfile("/usr/share/discord/resources/build_info.json")):
	print("Discord is not installed!")
	alert("Discord is not yet installed! Please install it first.", "DiscordAutoupdate")
	exit(1)

print("Checking for updates...")

r = requests.get("https://discord.com/api/updates?platform=linux")

if r.status_code == 200:
	print("Got result from Discord")
	
	dapi_jayson = json.loads(r.text)
	
	print("Latest version from Discord: {0}".format(dapi_jayson["name"]))
	
	d_jayson = {}
	
	with open("/usr/share/discord/resources/build_info.json", "r") as f:
		d_jayson = json.loads(f.read())
	
	print("Version installed is: {0}".format(d_jayson["version"]))
	
	if (dapi_jayson["name"] == d_jayson["version"]):
		print("Already on the latest version!")
		print("Launching Discord...")
		
		subprocess.Popen(["/usr/share/discord/Discord"])
		
		print("Goodbye! - DiscordAutoupdate")
	else:
		print("Update time!")
		
		alert("There is a new version of Discord available!\nDiscordAutoupdate will install it as soon as you press Ok.", "DiscordAutoupdate")
		
		dreq = requests.get("https://discord.com/api/download/stable?platform=linux&format=deb")
		
		if dreq.status_code == 200:
			with open("/tmp/discord.deb","wb") as f:
				f.write(dreq.content)
		else:
			print("Failed with {0}".format(r.status_code))
			alert("We couldn't reach Discord's servers\nThis could have happened because:\nYour internet connection isn't working.\nDiscord's servers are down.\n\n{0}".format(r.status_code), "DiscordAutoupdate")
			exit(1)

		
		
		subprocess.Popen(["/usr/share/discord/Discord"])
		
		print("Goodbye! - DiscordAutoupdate")
else:
	print("Failed with {0}".format(r.status_code))
	alert("We couldn't reach Discord's servers\nThis could have happened because:\nYour internet connection isn't working.\nDiscord's servers are down.\n\n{0}".format(r.status_code), "DiscordAutoupdate")
