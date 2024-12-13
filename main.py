"""
/bin/crescent - @cups9's open-source utility Discord bot
* this discord bot was intended to be used for Citrine Studios projects, such as TDSMP
* all code here is modifiable so long as you adhere to the GPL-3 license (you must fork this repo to modify the code)
* if this project expands, it will be owned by Citrine Studios and not @cups9
"""
# -- IMPORTS -- #
# `hikari` and `arc` are explained in the README.md
import hikari
import arc
# "import hidden" is disabled in .gitignore for security purposes
import hidden
# required for certain functions
from typing import Any

# -- QUICKSTART -- #
# `bot` and `client` define key variables used within the script
bot = hikari.GatewayBot(token=hidden.TOKEN)
client = arc.GatewayClient(bot)

# Outputs a custom message for when the bot starts, allowing for easy readability
@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('[⭐️] [LOG] /bin/utils is now active.')

# -- COMMANDS -- #
# Test command pulled from the `arc` example repo (thank you!)
@client.include
@arc.slash_command("hi", "Say hi!")
async def test(
    ctx: arc.GatewayContext,
    user: arc.Option[hikari.User, arc.UserParams("The user to say hi to.")]
) -> None:
    await ctx.respond(f"Hey {user.mention}!")

# -- DEBUG -- #
# Defines the slash command group for the next few commands
status = client.include_slash_group("status", "Check the status of the bot")

# Checks the ping of the bot
@status.include
@arc.slash_subcommand("ping", "Check the bot's ping.")
async def ping(
    ctx: arc.GatewayContext
) -> None:
    await ctx.respond(f"Pong! {bot.heartbeat_latency * 1_000:.0f}ms")

# Checks the shard (instances/servers) count of the bot
@status.include
@arc.slash_subcommand("shard-count", "Check the bot's shard count.")
# Checks if the command has the right author
# [#] @cups9 : currently attempting to somehow declare the `author_check` function so it can be used in any command, need help!
async def author_check(ctx: arc.Context[Any]) -> None:
    if ctx.author.id != hidden.AUTHOR_ID: # the author is hidden for privacy purposes
        raise Exception("An unauthorised author attempted to execute this command.")
async def shard_count(
    ctx: arc.GatewayContext
) -> None:
    await ctx.respond(f"This bot currently has: **{bot.shard_count}** shards.", flags=hikari.MessageFlag.EPHEMERAL)

# -- EXTENSIONS -- #
# Loads the extensions required for this project, which can be unloaded later if change is desired
# Imports the module from a different script which in this case, are scripts from the "extensions" folder
client.load_extension("extensions.tdsmp")

# -- LAUNCH -- #
# Launches and starts the bot
# !! PLEASE KEEP THIS AT THE BOTTOM !!
bot.run()
