from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tgbot.bot.loader import dp, Form
from tgbot.bot.filters.state_callback_data import set_state_cd


@dp.callback_query_handler(set_state_cd.filter(action='to-latin'), state='*')
async def set_state_to_latin(callback_query: CallbackQuery, state: FSMContext):
    await Form.cyrillic_to_latin.set() 

    try:
        await callback_query.message.delete()

        await callback_query.answer(
                text='✅ Answer accepted!\nSend me any message and I can translate it!',
                show_alert=True
            )
    except:
        await callback_query.answer(
                text='✅ Answer accepted!\nSend me any message and I can translate it!',
                show_alert=True
            )


@dp.callback_query_handler(set_state_cd.filter(action='to-cyrillic'), state='*')
async def set_state_to_cyrillic(callback_query: CallbackQuery, state: FSMContext):
    await Form.latin_to_cyrillic.set() 

    try:
        await callback_query.message.delete()


        await callback_query.answer(
                text='✅ Answer accepted!\nSend me any message and I can translate it!',
                show_alert=True
            )
    except:
        await callback_query.answer(
                text='✅ Answer accepted!\nSend me any message and I can translate it!',
                show_alert=True
            )

