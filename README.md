# ctr4ever_Discord_bot_parser
A text parser that converts the messages of the Records Bot on ctr4ever discord server into usable data.

Ctr4ever is a highschore leaderboard website for the ps1 game Crash Team Racing.
The database storage system broke down in 2019 and many submissions since then were lost.
However, our discord server has a bot that posts time updates regularly, and the bot started in eary 2019.

This program is used to transform data from the bot into a usable form for re-creating a database in the future.

Example:

Original messages:

 — 03/03/2022
New record in Coco Park
Niklas Nyberg 🇫🇮, with a time of 1'14''64, has achieved 23rd place in Coco Park

Data conversion result as [line number, username, unix date, ctr4ever trackID, time in centiseconds]:

[585, 'Niklas Nyberg', 1646319600, 7, 7424]
