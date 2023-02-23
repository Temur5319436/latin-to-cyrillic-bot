from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from tgbot.bot.loader import dp, Form
from tgbot.bot.utils.to_latin import to_latin
from tgbot.bot.filters.sentence_callback_data import sentence_cd


@dp.message_handler(state=Form.cyrillic_to_latin)
async def cyrillic_to_latin(message: Message, state: FSMContext):
    text = to_latin(message.text)

    await message.answer(
            text=f'`{text}`',
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text='To cyrillic',
                            callback_data=sentence_cd.new(action='to-cyrillic')
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text='❌',
                            callback_data=sentence_cd.new(action='delete')
                        )
                    ]
                ]
            )
        )
