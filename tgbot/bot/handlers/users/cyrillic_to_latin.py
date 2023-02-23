import typing
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from tgbot.bot.loader import dp, Form
from tgbot.bot.utils.to_latin import to_latin
from tgbot.bot.filters.sentence_callback_data import sentence_cd


@dp.message_handler(state=Form.cyrillic_to_latin)
async def cyrillic_to_latin_message_handler(message: Message, state: FSMContext):
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


@dp.callback_query_handler(sentence_cd.filter(action='to-latin'), state='*')
async def cyrillic_to_latin_callback_handler(callback_query: CallbackQuery, callback_data: typing.Dict[str, str]):
    await callback_query.answer()
    text = to_latin(callback_query.message.text)

    try:
        await callback_query.message.edit_text(
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
    except:
        await callback_query.message.answer(
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
