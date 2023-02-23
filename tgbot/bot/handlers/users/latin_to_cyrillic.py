from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.bot.loader import dp, Form
from tgbot.bot.utils.to_cyrillic import to_cyrillic
from tgbot.bot.filters.sentence_callback_data import sentence_cd


@dp.message_handler(state=Form.latin_to_cyrillic)
async def latin_to_cyrillic(message: Message, state: FSMContext):
    text = to_cyrillic(message.text)

    await message.answer(
        text=f'`{text}`',
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='To latin',
                        callback_data=sentence_cd.new(action='to-latin')
                    ),
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
