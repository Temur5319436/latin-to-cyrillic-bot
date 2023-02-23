import typing
from aiogram.types import CallbackQuery

from tgbot.bot.loader import dp
from tgbot.bot.filters.sentence_callback_data import sentence_cd


@dp.callback_query_handler(sentence_cd.filter(action='delete'), state='*')
async def delete_sentence(callback_query: CallbackQuery, callback_data: typing.Dict[str, str]):
    try:
        await callback_query.message.delete()

    except:
        await callback_query.answer(
                text='Sorry!',
                show_alert=True
            )
        
