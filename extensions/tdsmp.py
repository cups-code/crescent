# -- IMPORTS -- #
# Dependencies required
import hikari
import arc
from typing import Any
# "import hidden" is disabled in .gitignore for security purposes
import hidden

# -- QUICKSTART --
# Defines the `plugin` variable for other commands
plugin = arc.GatewayPlugin("tdsmp")
# ** TDSMP SLASH_GROUP ** #
tdsmp = plugin.include_slash_group("smp", "Commands from the active SMP from Citrine Studios")
faq = tdsmp.include_subgroup("faq", "Learn about frequently asked or thought-about questions")

# Uses @plugin.include instead of @client.include
@tdsmp.include
@arc.slash_subcommand("modpack-ver", "List the current SMP modpack version.")
async def mrpack(
    ctx: arc.GatewayContext
) -> None:
    await ctx.respond(f"**TDSMP**\nThe current modpack version is: **v1.1.0**. (last updated: <t:1734003240:D>)")

# This is currently **slightly** messy (implemented it as a docstring instead). Thinking of implementing this in an embed instead.
@tdsmp.include
@arc.slash_subcommand("rules", "List the current rules for the SMP.")
async def rules(
    ctx: arc.GatewayContext
) -> None:
    embed = hikari.Embed(
        title="The TDSMP Rules and Amendments",
        description=f"""
            1. Thou shalt not kill or injure those for devious reasons or intentions regarding harm to reputation, the victim, or overall server status

            2. Thou shalt not thieve in one's personal belongings, and must require consent from the other individual or people

            3. Thou shalt not conduct destruction of property regarding self or others in harmful or leisure intentions

            4. Should any rule be broken in the slightest manner, punishment of the individual will be determined by the severity of the incident, along with a server vote.""",
        color="#a6d471"
    )
    # THIS FIELD WILL NOT WORK UNLESS YOU HAVE THE `hidden` MODULE
    # Comment this field if you are NOT using the `hidden` module
    embed.add_field("Last Updated", f"<t:1734082200:D>")
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
        title="How do I join The Dabido SMP??",
        description=f"""
        * To enter The Dabido SMP, you must use the Citrine Studios link to join the main Discord hub.

        * In there, you will be able to fill out an application which will allow you to join the SMP and find the IP. You will also find the required modpacks, as well as some rules (even though you can query it through `/smp rules`.)

        * Contact the current server owner for more details.""",
        color="#a6d471"
    )
    # THIS FIELD WILL NOT WORK UNLESS YOU HAVE THE `hidden` MODULE
    # Comment this field if you are NOT using the `hidden` module
    embed.add_field("Last Updated", f"<t:1734082200:D>")
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

        * The modpacks can be found in a private channel, only available for TDSMP members. All modpack versions will be listed there. Please seek the `/smp faq ip` command if you would like to know more about how to join.""",
        color="#a6d471"
    )
    embed.add_field("Last Updated", f"<t:1734082200:D>")
    await ctx.respond(embed)

# FAQ - MODS-INFO
@faq.include
@arc.slash_subcommand("mods-info", "What are the mods in TDSMP?")
async def faq_mods_info(
    ctx: arc.GatewayContext
) -> None:
    embed = hikari.Embed(
        title="What mods are in TDSMP?",
        description=f"""
        * There are many notable mods that can be found in TDSMP. This includes Origins, Dungeons & Taverns, Knight Quest, Farmer's Delight, Musket Mod, Regions Unexplored, Better Combat, and Small Ships.

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
        title="What are the uptimes for TDSMP?",
        description=f"""
        * Uptimes for TDSMP vary quite heavily, mostly being spontaneous. However, there is a range as to when the server does open. There are also many factors that contribute to the server's uptime, and the server may not run during these times so you will need to regularly check the provided status channel (if you are a member).

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
