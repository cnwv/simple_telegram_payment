from aiogram.types import LabeledPrice, Message
from aiogram.types import PreCheckoutQuery, CallbackQuery

from keyboards.payment import payment_keyboard


async def send_invoice_handler(message: Message):
    await message.answer(
        "Выберите сумму поддержки:",
        reply_markup=payment_keyboard()
    )


async def handle_payment_button(callback: CallbackQuery):
    amount = int(callback.data.split('_')[1])  # Получаем число из callback_data
    prices = [LabeledPrice(label=f"{amount} XTR", amount=amount)]

    await callback.message.answer_invoice(
        title=f"Поддержка канала - {amount} XTR",
        description=f"Поддержать канал на {amount} звёзд!",
        prices=prices,
        provider_token="",
        payload=f"channel_support_{amount}",
        currency="XTR",
    )
    await callback.answer()


async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)


async def success_payment_handler(message: Message):
    # there is logic for adding payment for your database
    user_id = message.from_user.id
    amount = message.successful_payment.total_amount
    print(f"Payment received - User ID: {user_id}, Amount: {amount} stars")
    await message.answer(text="🥳Спасибо за вашу поддержку!🤗")


async def pay_support_handler(message: Message):
    await message.answer(
        text="Добровольные пожертвования не подразумевают возврат средств, "
             "однако, если вы очень хотите вернуть средства - свяжитесь с нами."
    )