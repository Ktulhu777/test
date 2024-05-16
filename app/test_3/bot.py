from aiogram import Bot
from app.config import DB_NAME, DB_PASS, DB_USER, DB_HOST, TOKEN_BOT

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
bt = Bot(token=TOKEN_BOT)
