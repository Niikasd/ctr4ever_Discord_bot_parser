<h2># ctr4ever_Discord_bot_parser</h2>
A text parser that converts the messages of the Records Bot on ctr4ever discord server into usable data.

Ctr4ever is a highschore leaderboard website for the ps1 game Crash Team Racing.
The database storage system broke down in 2019 and many submissions since then were lost.
However, our discord server has a bot that posts time updates regularly, and the bot started in eary 2019.

This program is used to transform data from the bot into a usable form for re-creating a database in the future.

Example:

Original messages

![imgur](https://i.imgur.com/WG0vSZu.png)

Data conversion result as [line number, username, unix date, ctr4ever trackID, time in centiseconds]:

```[585, 'Niklas Nyberg', 1646319600, 7, 7424]```

<h2>How to Use</h2>

Prerequisities: Python3

1. Download the program and place messages.txt into the same folder.
2. Open a command prompt.
3. Type in or copy: ```python discord_parser.py```
If step 3 does not work, it may be you need to type one of the following instead of ```python```: ```py```, ```py3```, ```python3```.
