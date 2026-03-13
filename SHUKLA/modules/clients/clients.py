import asyncio

from pyrogram import Client
from pyrogram.types import ChatPrivileges
from pytgcalls import PyTgCalls
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram.errors import BadRequest  # Import BadRequest for error handling

from ..clients.vars import Config
from ...console import LOGGER

ass_power = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
    can_manage_video_chats=True,
    can_promote_members=True,    
    can_invite_users=True
)

bot_power = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
    can_manage_video_chats=True,
    can_promote_members=True,    
    can_invite_users=True
)

try:
    LOGGER.info("Connecting To Mongo Database ...")
    MONGO_DB_URL = Config.MONGO_DATABASE
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URL)
    mongodb = _mongo_async_.Genius
    LOGGER.info("Succesfully Connected.")
except Exception as e:
    print(f"Error: {e}")
    LOGGER.error("Failed To Connect To Your Mongo Database.")
    exit()

class Shukla(Client, PyTgCalls):
    def __init__(self):
        self.app = Client(
            name="ShuklaUserbot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            session_string=Config.STRING_SESSION,
        )
        self.ass = Client(
            name="ShuklaPlayer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            session_string=Config.SESSION_STRING,
        )
        self.bot = Client(
            name="ShuklaServer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
        )
        if Config.SESSION_STRING:
            self.call = PyTgCalls(self.ass)
        else:
            self.call = PyTgCalls(self.app)

    async def start(self):
        LOGGER.info("Starting Userbot")
        await self.app.start()
        self.app.name = self.app.me.first_name + "" + (self.app.me.last_name or "")
        self.app.username = self.app.me.username if self.app.me.username else self.app.me.mention
        self.app.mention = self.app.me.mention
        self.app.id = self.app.me.id
        if self.app.id not in Config.SUDOERS:
            Config.SUDOERS.add(int(self.app.id))
        try:
            await self.app.join_chat("ITSZSHUKLA")
            await self.app.join_chat("mastiwithfriendsxd")
            await self.app.join_chat("strangerassociation")
        except:
            pass
        await self.app.send_message(Config.LOG_GROUP_ID, "**Userbot Started**")
        LOGGER.info(f"Userbot Started as {self.app.name}")
        LOGGER.info("Starting PyTgCalls")
        if Config.SESSION_STRING:
            await self.ass.start()
            self.ass.name = self.ass.me.first_name + "" + (self.ass.me.last_name or "")
            self.ass.username = self.ass.me.username
            self.ass.mention = self.ass.me.mention
            self.ass.id = self.ass.me.id
            try:
                await self.ass.join_chat("ITSZSHUKLA")
                await self.ass.join_chat("mastiwithfriendsxd")
                await self.ass.join_chat("strangerassociation")
            except:
                pass
            try:
                await self.ass.send_message(Config.LOG_GROUP_ID, "**Vc Assistant Started.**")
            except:
                pass
            LOGGEtry:
    await self.ass.send_message(Config.LOG_GROUP_ID, "**Vc Assistant Started.**")
except Exception as e:
    LOGGER.warning(f"Assistant log error: {e}")
