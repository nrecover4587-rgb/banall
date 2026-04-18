import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int("YOUR_API_ID")
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"
OWNER_ID = 123456789  # apna telegram user id

app = Client("banallbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("xban") & filters.user(OWNER_ID))
async def ban_all(client: Client, message: Message):
    chat_id = message.chat.id

    msg = await message.reply("⚡ Banall start...")

    done = 0
    failed = 0

    async for member in client.get_chat_members(chat_id):
        try:
            if member.user.is_bot or member.status in ["administrator", "creator"]:
                continue

            await client.ban_chat_member(chat_id, member.user.id)
            done += 1
            await asyncio.sleep(1)

        except:
            failed += 1

    await msg.edit(f"✅ Done\nBanned: {done}\nFailed: {failed}")


app.run()
