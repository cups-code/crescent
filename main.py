# List of Imports
import hikari
import arc
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

bot.run()
