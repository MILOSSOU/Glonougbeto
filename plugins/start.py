from pyrogram import Client, filters, types as t
from bot import StartTime

startText = """
ᴛʜᴇsᴇ ᴀʀᴇ sᴏᴍᴇ ᴀɪ ᴄᴏᴍᴍᴀɴᴅs

 ➻ /draw : ᴄʀᴇᴀᴛᴇ ɪᴍᴀɢᴇs
 ➻ /upscale : ᴜᴘsᴄᴀʟᴇ ʏᴏᴜʀ ɪᴍᴀɢᴇs
 ➻ /gpt : ᴄʜᴀᴛɢᴘᴛ
 ➻ /bard : ʙᴀʀᴅ ᴀɪ ʙʏ ɢᴏᴏɢʟᴇ
 ➻ /mistral : ᴍɪsᴛʀᴀʟ ᴀɪ
 ➻ /llama : ʟʟᴀᴍᴀ ʙʏ ᴍᴇᴛᴀ ᴀɪ
 ➻ /palm : ᴘᴀʟᴍ ʙʏ ɢᴏᴏɢʟᴇ
 ➻ /reverse : ʀᴇᴠᴇʀsᴇ ɪᴍᴀɢᴇ sᴇᴀʀᴄʜ
 ➻ /gemini : ɢᴇᴍɪɴɪ ʙʏ ɢᴏᴏɢʟᴇ
 ➻ /imagine : ᴄʀᴇᴀᴛᴇ ᴀɪ ɪᴍᴀɢᴇs

 ➻ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ - @weebs_support
"""

@Client.on_message(filters.command(["start","help","repo","source"]))
async def start(_: Client, m: t.Message):
    await m.reply_text(
        startText,
        reply_markup=t.InlineKeyboardMarkup(
            [
                [
                    t.InlineKeyboardButton(text="ᴊᴏɪɴ ᴍy ᴜᴩᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ",url="https://t.me/codeflix_bots")
                ]
            ]
        )
    )
