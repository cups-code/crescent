# -- IMPORTS -- #
# Dependencies required
import hikari
import arc
from typing import Any
# "import hidden" is disabled in .gitignore for security purposes
import hidden
import os
import json
import asyncio

# -- QUICKSTART --
# Defines the `plugin` variable for other commands
plugin = arc.GatewayPlugin("polls")



# -- COMMANDS --

pollGroup = plugin.include_slash_group("poll", "Crescent's poll system, currently in maintenance.")


@pollGroup.include
@arc.with_concurrency_limit(arc.channel_concurrency(1))
@arc.slash_subcommand("create", "Creates a user poll.")
async def createPoll(
    ctx: arc.GatewayContext, 
    pollname: arc.Option[str, arc.StrParams("The name of the poll.")],
    polloption: arc.Option[str, arc.StrParams("A poll option idk change this later.")] = "" ):


    #Checks if the polls json file exists yet
    if not os.path.exists("polls.json"):
        print("Generating json file")

        with open("polls.json", 'w') as file:
            json.dump({}, file, indent=4)
                    
    #Reads the polls json file
    with open("polls.json", "r") as file:
        readPoll = json.load(file)

    #await asyncio.sleep(8.0) #test for if it can run mutliple thingies

    if pollname in readPoll: #Poll with name already exists
        await ctx.respond("A poll with this name already exists. Please try again with another name.")
        
    else: #Create the poll
        await ctx.respond("Creating poll")

        readPoll[pollname] = {}

        with open("polls.json", "w") as file:
            json.dump(readPoll, file, indent=4)
    
    print(readPoll)





# -- OTHER STUFF LOL GIVE THIS ANOTHER NAME --

# Adds the plugin to the client (main.py)
@arc.loader
def loader(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)
