import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int("24168862")
API_HASH = "916a9424dd1e58ab7955001ccc0172b3"
BOT_TOKEN = "8234835598:AAEN3fVmhP7PuYIczq8fVDuxhayiMsIItcQ"
OWNER_ID = 7113972959  # apna id

# 👇 group id yaha daal (important for private trigger)
GROUP_ID = -1003421586593

app = Client("banallbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

running = False  # stop control


# 🔹 START BAN (private se)
@app.on_message(filters.command("xban") & filters.private & filters.user(OWNER_ID))
async def ban_all(client: Client, message: Message):
    global running
    running = True

    msg = await message.reply("⚡ Fast Banall start...")

    done = 0
    failed = 0

    async for member in client.get_chat_members(GROUP_ID):
        if not running:
            break

        try:
            if member.user.is_bot or member.status in ["administrator", "creator"]:
                continue

            await client.ban_chat_member(GROUP_ID, member.user.id)
            done += 1

            # ⚡ fast but safe delay
            if done % 10 == 0:
                await asyncio.sleep(2)   # batch delay
            else:
                await asyncio.sleep(0.3)

        except:
            failed += 1

    await message.reply(f"✅ Done\nBanned: {done}\nFailed: {failed}")


# 🔹 STOP COMMAND
@app.on_message(filters.command("stop") & filters.private & filters.user(OWNER_ID))
async def stop_ban(client, message):
    global running
    running = False
    await message.reply("🛑 Banall stopped!")


app.run()
