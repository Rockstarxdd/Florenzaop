from telethon import events, Button, custom
import re, os
from MashaRoBot.events import register
from MashaRoBot import telethn as love
PHOTO = "https://telegra.ph/file/ec7c7881de4fca0bb7484.jpg"
@register(pattern=("/alive"))
async def awake(event):
  LOVELY = event.sender.first_name
  LOVELY = "**𝗪𝗛𝗢 𝗔𝗠 𝗜 🥺❓** \n\n"
  LOVELY += "**I'ᴍ 𝙵𝚕𝚘𝚛𝚎𝚗𝚣𝚊🥰, Yᴏᴜʀ Hᴇᴀʀᴛʙᴇᴀᴛ❤️🔥*\n\n"
  LOVELY += "**I'ᴍ Wᴏʀᴋɪɴɢ Oɴ Lᴏᴠᴇ 🦋**\n\n"
  LOVELY += "**Mʏ σωηєя :**  [🖤 𝗦𝗧𝗔𝗥𝗚𝗜𝗥𝗟🖤🇮🇳™](t.me/STA4RGIRL_XD)\n\n"
  LOVELY += "**Aʙᴏᴜᴛ Mʏ 𝙾𝚠𝚗𝚎𝚛 🤩 :** [🖤 𝗦𝗧𝗔𝗥𝗚𝗜𝗥𝗟🖤🇮🇳™](t.me/itzmeehh)\n\n"
  BUTTON = [[Button.url("𝗦𝗨𝗣𝗣𝗢𝗥𝗧🙂", "https://t.me/FlorenzaSupport"), Button.url("𝗨𝗣𝗗𝗔𝗧𝗘", "https://t.me/Starz_bots")]]
  await love.send_file(event.chat_id, PHOTO, caption=FLORENZA,  buttons=BUTTON)
