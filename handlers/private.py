from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**🏷️ Hᴇʏ, ɪ ᴀᴍ [𝗠𝘂𝘀𝗶𝗰 𝗡𝗲𝘅𝘁 😎](https://telegra.ph/file/89d4135199d1d2a98596e.jpg).
ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴘʀᴇᴍɪᴜᴍ sᴜᴘᴇʀ
ғᴀsᴛ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴍᴜsɪᴄ
ᴘʟᴀʏᴇʀ ʙᴏᴛ..!
┏━━━━━━━━━━━━━━━━━┓
┣★ ʀᴜɴ ᴏɴ ᴘʀɪᴠᴀᴛᴇ ᴠᴘꜱ ꜱᴇʀ. 
┣★ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴍᴜꜱɪᴄ.
┣★ ɴᴏ ʟᴀɢ ɪɴ ɪɴ ᴠᴏɪᴄᴇ.
┣★ ꜱᴜᴘᴇʀꜰᴀꜱᴛ ꜱᴘᴇᴇᴅ.
┗━━━━━━━━━━━━━━━━━┛
 ᴄʀᴇᴀᴛᴇᴅ ʙʏ : [ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ](https://t.me/Pavanmagar)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💽 𝗥𝗘𝗣𝗢", url="https://t.me/CreatorPavanRepo"
                    ),
                    InlineKeyboardButton(
                        "𝗕𝗢𝗦𝗦 😎", url="https://t.me/Pavanmagar")
                ],[ 
                    InlineKeyboardButton(
                        "😀 𝗔𝗗𝗗 𝗠𝗘 😀", url="https://t.me/CrepanRobot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲 𝗡𝗼𝘄\n🌠𝗛𝗲𝘅𝗼𝗿 𝗫𝗗 <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌼𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/Prayagraj_Op")
                ]
            ]
        )
   )
