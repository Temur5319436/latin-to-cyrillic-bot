import typing

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

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


@dp.callback_query_handler(sentence_cd.filter(action='to-cyrillic'), state='*')
async def latin_to_cyrillic_callback_handler(callback_query: CallbackQuery, callback_data: typing.Dict[str, str]):
    await callback_query.answer()
    text = to_cyrillic(callback_query.message.text)

    try:
        await callback_query.message.edit_text(
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
    except:
        await callback_query.message.answer(
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
