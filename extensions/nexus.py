# -- IMPORTS -- #
# Dependencies required
import hikari
import arc
from typing import Any
# "import hidden" is disabled in .gitignore for security purposes
import hidden

# THIS IS CURRENTLY UNDER MAINTENANCE AND HIGHLY EXPERIMENTAL

# -- QUICKSTART --
# Defines the `plugin` variable for other commands
plugin = arc.GatewayPlugin("nexus")
# ** nexus SLASH_GROUP ** #
nexus = plugin.include_slash_group("nexus", "Commands from the Nexus Series from Citrine Studios")

# Uses @plugin.include instead of @client.include
@nexus.include
@arc.slash_subcommand("modpack-ver", "List the current modpack version.")
async def mrpack(
    ctx: arc.GatewayContext
) -> None:
    await ctx.respond(f"**NEXUS**\nThe Nexus modpack is currently in version: `1.0.4`.")

@nexus.include
@arc.slash_subcommand("faq", "Learn about frequently asked or thought-about questions")
async def faq(
    ctx: arc.GatewayContext,
    faq_choices: arc.Option[str, arc.StrParams("What do you want to know?", choices=["invite", "mods", "schedule"])]
) -> None:
    if faq_choices == "invite":
        await ctx.respond("test response to 'invite' command")
    elif faq_choices == "mods":
        await ctx.respond("test response to 'mods' command")
    elif faq_choices == "schedule":
        await ctx.respond("test response to 'schedule' command")

# Adds the plugin to the client (main.py)
@arc.loader
def loader(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)