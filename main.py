import asyncio
from pyrogram import Client, filters

API_ID = int("24168862")
API_HASH = "916a9424dd1e58ab7955001ccc0172b3")
BOT_TOKEN = "8234835598:AAEN3fVmhP7PuYIczq8fVDuxhayiMsIItcQ"
OWNER_ID = 7113972959

# 👇 ONLY ONE GROUP
GROUP_ID = -1003421586593

app = Client("banallbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

running = False


@app.on_message(filters.command("xban") & filters.private & filters.user(OWNER_ID))
async def ban_all(client, message):

    global running
    running = True

    await message.reply("⚡ Target group ban start...")

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

            await asyncio.sleep(0.3)

        except:
            failed += 1

    await message.reply(f"✅ Done\nBanned: {done}\nFailed: {failed}")


@app.on_message(filters.command("stop") & filters.private & filters.user(OWNER_ID))
async def stop(client, message):
    global running
    running = False
    await message.reply("🛑 Stopped")


app.run()
