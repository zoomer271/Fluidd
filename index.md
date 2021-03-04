## Welcome to Fluidd Chat Package

This is used in python to use Fluidd API and make bots for your chats!

### Setting Up The Bot

Go to www.fluidd.club/developers and get a bot setup!

## Few things that are needed here are
```markdown
Token
The token is the password for the bot! It could be changed if you want to.
Name
The name is the username for the bot! It could be changed if you want to.
Prefix
The prefix is the prefix for the bot! Such as !help if you have that command registered it will respond back!
ID
The ID is needed for certain purposes.
```

## Installing everything needed
### Python 3.7 and above
### Our pip package. you can install it with
`pip3 install fluidd` or `python3 -m pip install fluidd`
### A IDE of your choice such as Visual Studio Code

## Starting to code

* Before we start in the top of `bot.py` you must put: 
```markdown
    ---------------------
    Copyright Information
    ---------------------

    Code given here is made by Fluidd Inc. 
    If getting any other functions from other sources and using it in a commercial use.
    All rights must be given to them.
```


* This is a main part of using our API so follow carefully to not mess up!

`bot.py`
```markdown
from fluidd import Fluidd

bot = Fluidd()

bot.TestConnection()
```

And if connection is successful it should return `Server is up and connection is successfully connected! 200`. If it says something else that means the server is down or you are not connected to Internet.
