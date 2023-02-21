from aiogram.types import Message, ParseMode
from tgbot.bot.loader import dp


@dp.message_handler()
async def latin_to_cyrillic(message: Message):
    text = message.text

    text = text.replace("o'", "ў")
    text = text.replace("oʻ", "ў")
    text = text.replace("o’", "ў")
    text = text.replace("O'", "Ў")
    text = text.replace("Oʻ", "Ў")
    text = text.replace("O’", "Ў")

    text = text.replace("gʻ", "ғ")
    text = text.replace("g'", "ғ")
    text = text.replace("g’", "ғ")
    text = text.replace("Gʻ", "Ғ")
    text = text.replace("G'", "Ғ")
    text = text.replace("G’", "Ғ")

    text = text.replace("sh", "ш")
    text = text.replace("sH", "ш")
    text = text.replace("Sh", "Ш")
    text = text.replace("SH", "Ш")

    text = text.replace("ch", "ч")
    text = text.replace("cH", "ч")
    text = text.replace("Ch", "Ч")
    text = text.replace("CH", "Ч")

    text = text.replace("yo", "ё")
    text = text.replace("yO", "ё")
    text = text.replace("Yo", "Ё")
    text = text.replace("YO", "Ё")

    text = text.replace("ya", "я")
    text = text.replace("yA", "я")
    text = text.replace("Ya", "Я")
    text = text.replace("YA", "Я")

    text = text.replace("yu", "ю")
    text = text.replace("yU", "ю")
    text = text.replace("Yu", "Ю")
    text = text.replace("YU", "Ю")

    text = text.replace("ee", "эе")
    text = text.replace("EE", "ЭE")
    text = text.replace("Ee", "ЭE")
    text = text.replace("eE", "эе")

    text = text.replace("Ye", "E")
    text = text.replace("YE", "E")
    text = text.replace("ye", "е")
    text = text.replace("yE", "е")

    text = text.replace("Ts", "Ц")
    text = text.replace("TS", "Ц")
    text = text.replace("ts", "ц")
    text = text.replace("tS", "ц")

    text = text.replace("a", "а")
    text = text.replace("b", "б")
    text = text.replace("c", "ц")
    text = text.replace("d", "д")
    text = text.replace("e", "е")
    text = text.replace("f", "ф")
    text = text.replace("g", "г")
    text = text.replace("h", "ҳ")
    text = text.replace("i", "и")
    text = text.replace("j", "ж")
    text = text.replace("k", "к")
    text = text.replace("l", "л")
    text = text.replace("m", "м")
    text = text.replace("n", "н")
    text = text.replace("o", "о")
    text = text.replace("p", "п")
    text = text.replace("q", "қ")
    text = text.replace("r", "р")
    text = text.replace("s", "с")
    text = text.replace("t", "т")
    text = text.replace("u", "у")
    text = text.replace("v", "в")
    text = text.replace("x", "х")
    text = text.replace("y", "й")
    text = text.replace("z", "з")

    text = text.replace("A", "А")
    text = text.replace("B", "Б")
    text = text.replace("D", "Д")
    text = text.replace("C", "С")
    text = text.replace("E", "Э")
    text = text.replace("F", "Ф")
    text = text.replace("G", "Г")
    text = text.replace("H", "Ҳ")
    text = text.replace("I", "И")
    text = text.replace("J", "Ж")
    text = text.replace("K", "К")
    text = text.replace("L", "Л")
    text = text.replace("M", "М")
    text = text.replace("N", "Н")
    text = text.replace("O", "О")
    text = text.replace("P", "П")
    text = text.replace("Q", "Қ")
    text = text.replace("R", "Р")
    text = text.replace("S", "С")
    text = text.replace("T", "Т")
    text = text.replace("U", "У")
    text = text.replace("V", "В")
    text = text.replace("Y", "Й")
    text = text.replace("X", "Х")
    text = text.replace("Z", "З")

    text = text.replace("'", "ъ")

    await message.answer(
        text=f'`{text}`',
        parse_mode=ParseMode.MARKDOWN_V2
    )
