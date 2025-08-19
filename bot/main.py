import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from faststream.rabbit import RabbitBroker
from .config import TOKEN

bot = Bot(token=TOKEN)

broker = RabbitBroker()

dp = Dispatcher()

@broker.subscriber("orders")
async def orders_answer(data: str):
    await bot.send_message(
        chat_id='-- your chat id --',
        text=data
    )


@dp.message()
async def get_chat_id(msg: Message):
    await msg.answer(f"{msg.chat.id}")

async def main():
    async with broker:
        await broker.start()
        await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())