from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.callback_data import CallbackData

from tgbot.bot.loader import dp
from tgbot.bot.filters.state_callback_data import set_state_cd


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: Message):
    text = f'👋 Hi {message.from_user.first_name}!\n\n'\
            '🤖 I am bot which can help you to translate latin to cyrillic or cyrillic to latin!\n\n'\
            '✅ You should select one option!'

    await message.answer(
            text=text,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text='Latin to cyrillic',
                            callback_data=set_state_cd.new(action='to-cyrillic')
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text='Cyrillic to latin',
                            callback_data=set_state_cd.new(action='to-latin')
                        )
                    ]
                ]
            )
        )


@dp.message_handler(state=None)
async def restart(message: Message):
    text = f'👋 Hi {message.from_user.first_name}!\n\n'\
            '🤖 I am bot which can help you to translate latin to cyrillic or cyrillic to latin!\n\n'\
            '✅ You should select one option!'

    await message.answer(
            text=text,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text='Latin to cyrillic',
                            callback_data=set_state_cd.new(action='to-cyrillic')
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text='Cyrillic to latin',
                            callback_data=set_state_cd.new(action='to-latin')
                        )
                    ]
                ]
            )
        )
