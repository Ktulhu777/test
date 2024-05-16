import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext

import service
from config import TOKEN_BOT
from state_bot import StateTask

storage = MemoryStorage()

bot = Bot(token=TOKEN_BOT, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)


@dp.message(Command('start'))
async def start(message: types.Message):
    try:
        await service.add_user(user_id=int(message.from_user.id), username=message.from_user.username)
        await message.answer(text="Здравствуйте, я бот созданный для ежедневных заданий")
    except Exception as e:
        print(e)


@dp.message(Command('tasks'))
async def get_tasks(message: types.Message):
    tasks = await service.read_tasks(int(message.from_user.id))
    if tasks:
        for item in tasks:
            await message.answer(
                "Название задачи - {title}\n Описание задачи: {body}".format(title=item.title, body=item.body))
    else:
        await message.answer("Список задач пуст")


@dp.message(Command('add'))
async def start_add_task(message: types.Message, state: FSMContext):
    """Начало FSM для добавления задачи"""
    await message.answer("Введите название задачи")
    await state.set_state(StateTask.title)


@dp.message(StateTask.title)
async def get_title(message: types.Message, state: FSMContext):
    """Добавление title"""
    await state.update_data(title=message.text)
    await state.set_state(StateTask.description)
    await message.answer("Введите описание задачи")


@dp.message(StateTask.description)
async def get_description(message: types.Message, state: FSMContext):
    """Добавление description и запись в БД с очищением FSM"""
    await state.update_data(description=message.text)
    data = await state.get_data()
    await service.add_task(user_id=int(message.from_user.id), title=data['title'], body=data['description'])
    await message.answer("Задача добавлена")
    await state.clear()


async def main() -> None:
    dp.message.register(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
