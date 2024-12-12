# List of Imports
import hikari
import arc
# "import hidden" is ignored in .gitignore for security purposes
import hidden

# Initialisation
bot = hikari.GatewayBot(token=hidden.TOKEN)
client = arc.GatewayClient(bot)

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('/bin/utils is now active.')

# -- COMMANDS -- #

@client.include
@arc.slash_command("hi", "Say hi!")
async def ping(
    ctx: arc.GatewayContext,
    user: arc.Option[hikari.User, arc.UserParams("The user to say hi to.")]
) -> None:
    await ctx.respond(f"Hey {user.mention}!")


# This is queued for moving to an extension instead of being as a base command
@client.include
@arc.slash_command("modpack-ver", "List the current modpack version.")
async def info(
    ctx: arc.GatewayContext
) -> None:
    await ctx.respond(f"**TDSMP**\nThe current modpack version is: **v1.1.0**. (last updated: <t:1734003240:D>)")

bot.run()
