# -- IMPORTS -- #
# Dependencies required
import hikari
import arc
from typing import Any
# "import hidden" is disabled in .gitignore for security purposes
import hidden

# -- QUICKSTART --
# Defines the `plugin` variable for other commands
plugin = arc.GatewayPlugin("anthurium")
# ** anthurium SLASH_GROUP ** #
anthurium = plugin.include_slash_group("anthurium", "Commands from the Anthurium SMP from Citrine Studios")
faq = anthurium.include_subgroup("faq", "Learn about frequently asked or thought-about questions")

# Uses @plugin.include instead of @client.include
@anthurium.include
@arc.slash_subcommand("modpack-ver", "List the current SMP modpack version.")
async def mrpack(
    ctx: arc.GatewayContext
) -> None:
    await ctx.respond(f"**Anthurium**\nThe current modpack version is: **v1.1.0**. (last updated: <t:1735279380:D>)")

# This is currently **slightly** messy (implemented it as a docstring instead). Thinking of implementing this in an embed instead.
@anthurium.include
@arc.slash_subcommand("rules", "List the current rules for the SMP.")
async def rules(
    ctx: arc.GatewayContext
) -> None:
    embed = hikari.Embed(
        title="The Anthurium Rules and Amendments",
        description=f"""
        > **Registered by The High Court**
        > 1. Do not kill, injure, or murder any person with any malicious intent or to harm the victim's reputation and/or server status.
        > 2. Do not steal from anyone. You must always ask for consent in order to take resources from another player's containers (e.g. chests, barrels, etc.)
        > 3. Do not conduct destruction of *any* property to some other person with harmful or malicious intentions
        > 4. Do not create any lag machines that would cause havoc to the server, or other people's instances of the game.
        > 5. Cheating is not allowed on this server. Cheating is tolerated as an immediate ban, as it gives you a severe advantage over players.
        > 6. Farms must be moderated and each type is approved by The High Court. For instance, entity tests and super-high entity-based farms are not allowed. See rule number 4.
        > 7. Any instance of declared and registered warfare on the server will disregard all of these rules except rules that give an immediate ban. See rule number 5. This will not apply if you are not involved in war.
        > 8. Should any rule be broken in even the slightest manner, the punishment of the individual will be determined by many factors such as the severity of the incident and a public vote.
        > [+] Originally written by DavidPlanks, modified by cupstv""",
        color="#a6d471"
    )
    # THIS FIELD WILL NOT WORK UNLESS YOU HAVE THE `hidden` MODULE
    # Comment this field if you are NOT using the `hidden` module
    embed.add_field("Last Updated", f"<t:1735279380:D>")
    embed.set_author(
        name="DavidPlanks"
    )
    await ctx.respond(embed)

# FAQ - JOIN
@faq.include
@arc.slash_subcommand("join", "How do I enter the SMP?")
async def faq_join(
    ctx: arc.GatewayContext
) -> None:
    embed = hikari.Embed(
        title="How do I join The Anthurium SMP?",
        description=f"""
        * To enter The Anthurium SMP, you must use the Citrine Studios link to join the main Discord hub.

        * In there, you will be able to fill out an application which will allow you to join the SMP and find the IP. You will also find the required modpacks, as well as some rules (even though you can query it through `/smp rules`.)

        * Contact the current server owner for more details.""",
        color="#a6d471"
    )
    # THIS FIELD WILL NOT WORK UNLESS YOU HAVE THE `hidden` MODULE
    # Comment this field if you are NOT using the `hidden` module
    embed.add_field("Last Updated", f"<t:1735279380:D>")
    embed.add_field("Invite Link", f"{hidden.CITRINE_DISCORD_LINK}")
    await ctx.respond(embed)

# FAQ - MODS
@faq.include
@arc.slash_subcommand("mods", "What mods do I need for the SMP?")
async def faq_mods(
    ctx: arc.GatewayContext
) -> None:
    embed = hikari.Embed(
        title="What mods do I need?",
        description=f"""
        * All mods are included in a modpack on a release cycle, with no usual schedule, and is semantically versioned.

        * You do **NOT** need to install any additional mods unless you know what you are doing. Adding additional mods may break your instance and we *may* not be able to assist you.

        * The modpacks can be found in a private channel, only available for The Anthurium SMP members. All modpack versions will be listed there. Please seek the `/smp faq ip` command if you would like to know more about how to join.""",
        color="#a6d471"
    )
    embed.add_field("Last Updated", f"<t:1734082200:D>")
    await ctx.respond(embed)

# FAQ - MODS-INFO
@faq.include
@arc.slash_subcommand("mods-info", "What are the mods in Anthurium?")
async def faq_mods_info(
    ctx: arc.GatewayContext
) -> None:
    embed = hikari.Embed(
        title="What mods are in Anthurium?",
        description=f"""
        * There are many notable mods that can be found in The Anthurium SMP. This includes Origins, Dungeons & Taverns, Knight Quest, Farmer's Delight, Musket Mod, Regions Unexplored, Better Combat, and Small Ships.

        * These can all be found through the modpacks that have been admin and community curated.

        * You can find out how to download the modpacks with the `/smp faq mods` command.
        """,
        color="#a6d471"
    )
    embed.add_field("Last Updated", f"<t:1734082200:D>")
    await ctx.respond(embed)

# FAQ - UPTIMES
@faq.include
@arc.slash_subcommand("uptimes", "During what times is the SMP up?")
async def faq_uptimes(
    ctx: arc.GatewayContext
) -> None:
    embed = hikari.Embed(
        title="What are the uptimes for Anthurium?",
        description=f"""
        * Uptimes for The Anthurium SMP vary quite heavily, mostly being spontaneous. However, there is a range as to when the server does open. There are also many factors that contribute to the server's uptime, and the server may not run during these times so you will need to regularly check the provided status channel (if you are a member).

        * On Weekdays, the server opens from 5pm-9pm. Holiday times vary, with the uptime being extended to 9am-9pm.

        * On Weekends, the server opens from 9am-9pm.
        """,
        color="#a6d471"
    )
    embed.add_field("Last Updated", f"<t:1734082200:D>")
    await ctx.respond(embed)

# END OF SLASH GROUP #

# Adds the plugin to the client (main.py)
@arc.loader
def loader(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)
