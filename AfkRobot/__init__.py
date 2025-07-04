import asyncio
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client, idle

import config

loop = asyncio.get_event_loop()
boot = time.time()

mongo = MongoClient(config.MONGO_DB_URI)
db = mongo.AFK

botid = 0
botname = ""
botusername = ""
cleanmode = {}

SUDOERS = config.SUDO_USER

app = Client(
    ":AfkRobotAFKBot:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

async def initiate_bot():
    global botid, botname, botusername
    await app.start()
    getme = await app.get_me()
    botid = getme.id
    botusername = (getme.username).lower()
    botname = f"{getme.first_name} {getme.last_name or ''}".strip()
    
    print(f"✅ Bot Started as @{botusername} (ID: {botid})")
    await idle()  # <- Keep the bot running!
    await app.stop()
    print("❌ Bot Stopped")

if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())