# /bin/crescent
A Discord bot developed by cups9 in affiliation with Citrine Studios used for basic utilities, such as outputting information from certain projects.

## Development
If you want to help support the development of this project, please consider writing an issue or PR.

### APIs and Libraries Used
- Hikari: https://github.com/hikari-py/hikari/
> `hikari-py` is the foundation of the entire bot, as it serves as the base library as a microframework.
- Arc: https://github.com/hypergonial/hikari-arc
> `hikari-arc` is a command handler that allows the establishment of commands.

### Local Development
- To run this bot locally, make sure to clone this repository in the folder you want by typing this command.
```
git clone https://github.com/cups-code/utils-bot
```
- Then, you will need to create a file called `hidden.py` which will store your token in a variable called `TOKEN`.
- You will need to use your own token by making an application on [discord.dev](https://discord.dev/) and going to the 'Bot' section. Reset the bot token to receive it.
- Once you have the token, store it in the `hidden.py` file like so.
```py
# hidden.py
TOKEN="..."
```
- The dependencies are already installed in the `venv`. If you wish to install the dependencies system-wide, use the following command.
```
pip install hikari hikari-arc
```
or
```
pip3 install hikari hikari-arc
```
or
```
python3 -m pip install hikari hikari-arc
```
- **WARNING!** If you are forking this OR making your own repository public, make sure to make a .gitignore file with its contents containing `hidden.py` only if it does not exist already within your clone.

## Roadmap
- [x] Move all projects into singular extensions for easier management
- [ ] Complete the 'TDSMP' information extension
- [ ] Get more contributors to allow easier development
- [ ] Find a host OR self-host the bot for prod
