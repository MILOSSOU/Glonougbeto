from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages
import asyncio
        
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
# https://t.me/GetTGLink/4178
async def verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Diffusion de vos messɑges...'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"Diffusion en cours:\n\nNombre total d’utilisateurs {total_users}\nComplète: {done} / {total_users}\nSuccès: {success}\nBlσqués: {blocked}\nSuppɾimés: {deleted}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Diffusion teɾminée:\nTeɾminé en {time_taken} secondes.\n\nNombɾe totɑl d'utilisɑteuɾs {total_users}\nComplète: {done} / {total_users}\nSuccès: {success}\nBlσqués: {blocked}\nSuppɾimés: {deleted}")


@Client.on_message(filters.command("grp_broadcast") & filters.user(ADMINS) & filters.reply)
async def grp_brodcst(bot, message):
    chats = await db.get_all_chats()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Diffusion en cours:...'
    )
    start_time = time.time()
    total_chats = await db.total_chat_count()
    done = 0
    failed =0

    success = 0
    async for chat in chats:
        pti, sh = await broadcast_messages(int(chat['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"Diffusion en cours:\n\nTotal Chats {total_chats}\nComplète: {done} / {total_chats}\nSuccès: {success}\nÉchoué: {failed}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Diffusion teɾminée:\nTeɾminé en {time_taken} secondes.\n\nTotal Chats {total_chats}\nComplète: {done} / {total_chats}\nSuccès: {success}\nÉchoué: {failed}")
