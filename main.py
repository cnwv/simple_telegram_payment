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

dp.message.register(payment.send_invoice_handler, Command(commands="donate"))
dp.pre_checkout_query.register(payment.pre_checkout_handler)
dp.message.register(payment.success_payment_handler, F.successful_payment)
dp.message.register(payment.pay_support_handler, Command(commands="paysupport"))


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
