from telethon import events, Button, custom
import re, os
from MashaRoBot.events import register
from MashaRoBot import telethn as love
PHOTO = "https://telegra.ph/file/ec7c7881de4fca0bb7484.jpg"
@register(pattern=("/alive"))
async def awake(event):
  LOVELY = event.sender.first_name
  LOVELY = "**ðªðð¢ ðð  ð ð¥ºâ** \n\n"
  LOVELY += "**I'á´ ðµðððððð£ðð¥°, Yá´á´Ê Há´á´Êá´Êá´á´á´â¤ï¸ð¥*\n\n"
  LOVELY += "**I'á´ Wá´Êá´ÉªÉ´É¢ OÉ´ Lá´á´ á´ ð¦**\n\n"
  LOVELY += "**MÊ ÏÏÎ·ÑÑ :**  [ð¤ ð¦ð§ðð¥ððð¥ðð¤ð®ð³â¢](t.me/STA4RGIRL_XD)\n\n"
  LOVELY += "**AÊá´á´á´ MÊ ð¾ð ððð ð¤© :** [ð¤ ð¦ð§ðð¥ððð¥ðð¤ð®ð³â¢](t.me/itzmeehh)\n\n"
  BUTTON = [[Button.url("ð¦ð¨ð£ð£ð¢ð¥ð§ð", "https://t.me/FlorenzaSupport"), Button.url("ð¨ð£ððð§ð", "https://t.me/Starz_bots")]]
  await love.send_file(event.chat_id, PHOTO, caption=LOVELY,  buttons=BUTTON)
