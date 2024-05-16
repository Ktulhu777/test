from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from models import TelegramUser, Tasks
from config import DB_NAME, DB_PASS, DB_USER, DB_HOST

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def add_user(user_id, username):
    async with async_session_maker() as session:
        exampl = await session.execute(select(TelegramUser).where(TelegramUser.username == username))
        username_exampl = exampl.scalar().username
        if not username_exampl:
            new_user = TelegramUser(user_id=user_id, username=username)
            session.add(new_user)
            await session.commit()
            return new_user


async def add_task(user_id: int, title: str, body: str):
    async with async_session_maker() as session:
        new_task = Tasks(user_id=user_id, title=title, body=body)
        session.add(new_task)
        await session.commit()
        return new_task


async def read_tasks(user_id: int):
    async with async_session_maker() as session:
        task_read = await session.execute(select(Tasks).where(Tasks.user_id == user_id))
        return task_read.scalars().all()
