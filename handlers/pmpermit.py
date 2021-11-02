from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"🤟 𝗔𝗯𝗲𝗲 𝗬𝗮𝗵𝗮 𝗽𝗲𝗿 𝗠𝗦𝗚 𝗸𝘂𝗲𝗲 𝗸𝗶𝘆𝗮 🤧 𝗘 𝗮𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝘁 𝗵𝗮𝗶. 🥱 𝗔𝗴𝗮𝗿 𝗞𝗼𝗶 𝗣𝗿𝗼𝗯𝗹𝗲𝗺 𝗛𝗮𝗶 𝘁𝗼 💪 𝗠𝗲𝗿𝗲 𝗕𝗼𝘀𝘀 😎 𝗸𝗼 𝗗𝗠 𝗸𝗿")
  return                        
