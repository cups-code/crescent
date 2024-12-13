# /bin/crescent
A Discord bot developed by cups9 in affiliation with Citrine Studios used for basic utilities, such as outputting information from certain projects. This repository conforms to the GPL-3 license.

## Purpose
Project Crescent, also known as /bin/crescent and Utility Bot, is a bot that allows for easier access to information, as well as having some basic moderation and other tasks that can be found in the Projects section of this repository. This bot is still a work-in-progress, and is fueled by passion and free time.

## Development
If you want to help support the development of this project, please consider writing an issue or PR. Writing an issue doesn't even need coding experience, as you can simply request a feature or report a bug and our contributors can just read through your issue.

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
- **WARNING!** Make sure to make your bot unavailable for User Install in the 'Installation' tab if you wish to not have users using your commands through their own account and private DMs.
- Once you have the token, store it in the `hidden.py` file like so.
```py
# hidden.py
TOKEN="..."
```
- **WARNING!** If you are forking this repository, make sure to make a .gitignore file with its contents containing `hidden.py` only if it does not exist already within your clone.
- The dependencies required are already installed in the `venv`. If you wish to install the dependencies system-wide, use the following command.
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
# Thanks!
Thank you for reading through this README, as well as viewing this repository and taking your time to either just browse or contribute to the repository.

I also thank all the contributors of the past, present, and future of this repository as they have all made an impact to the development of Project Crescent.
