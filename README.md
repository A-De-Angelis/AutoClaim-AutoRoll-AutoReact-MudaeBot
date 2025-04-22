# Mudae AutoRoll AutoClaim AutoReact [Broken for now]
### Original by GDiazFentanes, Updated by Ray

## Introduction
Auto Rolling, Auto Claiming and Auto Reacting, for Mudae's waifus, kakeras or husbandos every hour automatically. Uses slash rolling with given parameters for a better botting experience.
These files make it possible to use the Mudae Discord Bot 24/7 without any human input. It is supported by the Discord API to send and receive messages from any account. After extensive research into the existing bots in late 2023, I realized that none of them are actually working/supported. In order to use it you only need basic knowledge about Discord and Python (If you don't have it, read this document completely and you will easily achieve it).

## Features
- **Auto roll** every hour with the command you want (wa, wx, ha, etc...)
- **Auto Claim** cards that belong to the series you like, or that are above a certain kakera threshold (default 200)
- **Stop** rolling after claiming a card
- **Auto React** only to the kakera you prefer
- **Repeat** all the functionalities above each hour the minute you prefer
- **Uses slash commands** in order to benefit from the **native slash boosts (10% extra Kakera)**

## Files
This repository contains 3 different files:
| File Name | File Purpose | File Purpose |
| ------ | ------ |------ |
| Vars.py | Where the variables that you need to change are stored | Edit this!
| Bot.py | The bot is launched from here | Execute this!
| Function.py | Contains the function and code for the bot to work | Keep this in same directory!

## Requirements
This bot requires the following libraries in order to work correctly. Make sure Python 3 is installed along with the 2 required pip libraries (Discum and Schedule).
If you don't know how to do it, read here → [How to install a Python package](https://packaging.python.org/en/latest/tutorials/installing-packages/)

### Using Arch Linux (with pacman and pip)
```bash
sudo pacman -S python-pip
pip install discum
pip install schedule
```

### Using Ubuntu/Debian (with apt and pip)
```bash
sudo apt update
sudo apt install python3-pip
pip install discum
pip install schedule
```

### Using Other Linux Distributions
Ensure `pip` is installed for your distribution, then run:
```bash
pip install discum
pip install schedule
```

## Variables (Vars)
Time to edit Vars.py. Here you decide what settings the bot will have. In this section we will see what each variable does and what are the possibilities to fill them out. 
You will also choose what Discord account is used and on what channel you want the bot to execute the Mudae commands. These decisions are  reflected in these mandatory variables:

**Mandatory variables** : Needed for the bot to work:
+ `token` - The discord Token of the account you want to bot with → [How to get a Discord Token](https://www.androidauthority.com/get-discord-token-3149920/)
+ `channelId` - ID of the channel you want to roll in → [How to get a channel ID](https://docs.statbot.net/docs/faq/general/how-find-id/)  
+ `serverId` - ID of the server/guild you want to roll in → [How to get a server/guild ID](https://docs.statbot.net/docs/faq/general/how-find-id/)  

**Optional variables** : These are already filled by default, but you can change them if you want (setting desiredSeries and whether to pokeRoll))

+ `rollCommand` - Choose what command (only one) will the bot use to roll (mx, ma, mg, wx, wg, wa, hx, ha or hg)
+ `desiredKakeras` - **Case-sensitive** - Array of kakera types between single quotes separated by comas (see example below)
+ `desiredSeries` - **Case-sensitive** - Array of series between single quotes separated by comas (see example below)
+ `pokeRoll` - If you want to also roll the Mudae´s Pokeslot (True or False)
+ `repeatMinute` - Which minute of the hour the bot will roll at (value between 00 and 59, set to 25 by default)

##### Example of correctly filled variables
Each variable type (boolean, string, int, or array) requires specific formatting. Strings and arrays must be enclosed in quotes, while booleans and integers should not. Below is an example of properly configured variables. Note that the `token`, `channelId`, and `serverId` values are placeholders.

```python
token = 'MTE4MDIyNzU4NTUzNjQzNDMxNw.GDXjNH.YqGhIq7GwyVHSk9sf9zod3AACAffJeZiynTexc' 
channelId = '1182144443902599230'                 
serverId = '816317249082097684'                  
rollCommand= 'wa'
desiredKakeras= ['kakeraP','kakeraY','kakeraO','kakeraR','kakeraW','kakeraL']
desiredSeries = ['One Piece','Dragon Ball Z','Dumbbell Nan Kilo Moteru?']
pokeRoll = True
repeatMinute = '25'
```

##### Execution
![image](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2023/assets/152492889/b39973db-35b7-4de4-a111-95c40de5c04d)

Once you have completed all the previous steps, you will be able to safely execute Bot.py
This will open the file and start the Bot, logging all the rolls and actions made. The console should look like the image
(note that the bot won't roll until the set miniute time every hour)
- Red heart -> already claimed cards
- White heart -> not claimed yet cards

## Possible Errors
- Mudae has no access/write/read permission to the channel you decided
- Your Discord Token may have changed
- Your Mudae settings always have a button on each character roll
- Series and Characters are case-sensitive
- Your account must have a DM (at any time) with the mudae bot (try $help to make sure)
