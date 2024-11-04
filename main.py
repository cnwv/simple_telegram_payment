import asyncio
import logging
import sys

from aiogram import F, Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command

from config import settings
from handlers import payment

TOKEN = settings.telegram.token
dp = Dispatcher()

# Регистрируем обработчики
dp.message.register(payment.send_invoice_handler, Command(commands="donate"))
dp.callback_query.register(payment.handle_payment_button, F.data.startswith("pay_"))
dp.pre_checkout_query.register(payment.pre_checkout_handler)
dp.message.register(payment.success_payment_handler, F.successful_payment)
dp.message.register(payment.pay_support_handler, Command(commands="paysupport"))


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
