# -- IMPORTS -- #
# Dependencies required
import arc
from typing import Any

# -- QUICKSTART --
# Defines the `plugin` variable for other commands
plugin = arc.GatewayPlugin("tdsmp")
tdsmp = plugin.include_slash_group("smp", "Commands from the active SMP from Citrine Studios")

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
    await ctx.respond("""
        # The TDSMP Rules and Amendments
        1. Thou shalt not kill or injure those for devious reasons or intentions regarding harm to reputation, the victim, or overall server status
        2. Thou shalt not thieve in one's personal belongings, and must require consent from the other individual or people
        3. Thou shalt not conduct destruction of property regarding self or others in harmful or leisure intentions
        4. Should any rule be broken in the slightest manner, punishment of the individual will be determined by the severity of the incident, along with a server vote.
(Originally written by DavidPlanks)
        """)

# Adds the plugin to the client (main.py)
@arc.loader
def loader(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)
