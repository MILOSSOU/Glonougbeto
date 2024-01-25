from pyrogram import Client, filters
import requests
from info import LOG_CHANNEL, GOOGLE_API_KEY, SUPPORT_CHAT_ID
import google.generativeai as genai
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

genai.configure(api_key=GOOGLE_API_KEY)

@Client.on_message(filters.command('ask') & filters.chat(SUPPORT_CHAT_ID))
async def ai_generate(client, message):
   user_input = message.text.split()[1:]

   if not user_input:
       await message.reply_text("Commɑnde incomplète /ask Sɑlut")
       return

   user_input = " ".join(user_input)

   generation_config = {
       "temperature": 0.9,
       "top_p": 1,
       "top_k": 1,
       "max_output_tokens": 2048,
   }

   safety_settings = [
       {
           "category": "HARM_CATEGORY_HARASSMENT",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
       {
           "category": "HARM_CATEGORY_HATE_SPEECH",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
       {
           "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
       {
           "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
   ]

   model = genai.GenerativeModel(
       model_name="gemini-pro",
       generation_config=generation_config,
       safety_settings=safety_settings
   )

   prompt_parts = [user_input]
   response = model.generate_content(prompt_parts)
   await message.reply_text(text=f"🙋Ꭰꭼꮇꭺɴꭰꭼꮜꭱ: {message.from_user.mention}\n🤦Question:- {user_input}\n\n📝Réponse:\n\n{response.text}")         
   await client.send_message(LOG_CHANNEL, text=f"#ask Rᴇϙᴜᴇ̂ᴛᴇ ᴅᴇ {message.from_user.mention}\nQuestion:- {user_input}")
   await s.delete()

@Client.on_message(filters.command("ask"))
async def ai_generate_private(client, message):
  buttons = [[
    InlineKeyboardButton("Support", url="https://t.me/SharVision_Support")
  ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\n𝖴𝗍𝗂𝗅𝗂𝗌𝖾𝗋 𝖼𝖾𝗍𝗍𝖾 𝖿𝗈𝗇𝖼𝗍𝗂𝗈𝗇𝗇𝖺𝗅𝗂𝗍𝖾́ 𝖽𝖺𝗇𝗌 𝗅𝖾 𝗀𝗋𝗈𝗎𝗉𝖾 𝖽𝖾 𝗌𝗎𝗉𝗉𝗈𝗋𝗍 👇 ", reply_markup=reply_markup)
