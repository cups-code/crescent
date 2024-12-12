import arc

plugin = arc.GatewayPlugin("tdsmp")

@plugin.include
@arc.slash_command("modpack-ver", "List the current modpack version.")
async def mrpack(
    ctx: arc.GatewayContext
) -> None:
    await ctx.respond(f"**TDSMP**\nThe current modpack version is: **v1.1.0**. (last updated: <t:1734003240:D>)")

# This is currently **very** messy. Thinking of implementing this in an embed instead.
# --DELETE WHEN FINISHED-- Queued for testing outside of codespace and on local machine.
@plugin.include
@arc.slash_command("rules", "List the current rules for TDSMP.")
async def rules(
    ctx: arc.GatewayContext
) -> None:
    await ctx.respond(
        f"# The TDSMP Rules and Amendments\nThou shalt not kill or injure those for devious reasons or intentions regarding harm to reputation, the victim, or overall server status\nThou shalt not thieve in one's personal belongings, and must require consent from the other individual or people\nThou shalt not conduct destruction of property regarding self or others in harmful or leisure intentions\nShould any rule be broken in the slightest manner, punishment of the individual will be determined by the severity of the incident, along with a server vote.")

@arc.loader
def loader(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)