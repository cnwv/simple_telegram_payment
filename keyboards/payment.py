from aiogram.utils.keyboard import InlineKeyboardBuilder


def payment_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="подписка на 1 месяц - 1 ⭐️", callback_data="pay_1")
    builder.button(text="подписка на 6 месяцев - 2 ⭐️", callback_data="pay_2")
    builder.button(text="подписка на 1 год - 3 ⭐️", callback_data="pay_3")
    builder.adjust(1)
    return builder.as_markup()
