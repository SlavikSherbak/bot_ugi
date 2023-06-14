import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open("static/bot.png", "rb")
    bot.send_photo(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Розклад 🗓")
    item2 = types.KeyboardButton("Фінансові питання 😄")
    item3 = types.KeyboardButton("Документи 📜")
    item4 = types.KeyboardButton("Мої оцінки 😃")
    item5 = types.KeyboardButton("Ресурси 📚")
    item6 = types.KeyboardButton("Не знайшов відповідь 😔")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(
        message.chat.id,
        "Привіт, {0.first_name}!\nЯ - <b>{1.first_name}</b>, телеграм бот 😊.Я створений для того, щоб допомогти тобі знайти відповіді на деякі твої питання. Для того щоб побачити, що я вмію, натискай на відповідні кнопки.".format(
            message.from_user, bot.get_me()
        ),
        parse_mode="html",
        reply_markup=markup,
    )
    bot.send_message(message.chat.id, " ©Viacheslav Shcherbak, 2021")


@bot.message_handler(content_types=["text"])
def lalala(message):
    keyboardDovid = types.InlineKeyboardMarkup(row_width=1)
    url_button0 = types.InlineKeyboardButton(
        text="Довідка про навчання 😄",
        url="https://docs.google.com/forms/d/e/1FAIpQLSe1GkemCU8rEvjHlEtb0Ep9MrkCB7m3pOvggh3kCgoAJkHUMQ/viewform",
    )
    url_button1 = types.InlineKeyboardButton(
        text="Виклик на сесію 😌",
        url="https://docs.google.com/forms/d/e/1FAIpQLSfO2z8-sxg29Hr97teQ1aG7QUBfoDYE1YkQVYjz-N567DtkLQ/viewform",
    )
    url_button2 = types.InlineKeyboardButton(
        text="Зразки заяв 📃",
        url="https://docs.google.com/document/d/18F_6UDjEkrdRCfMyvSq6ma1y65nqg5uyLvTVfBv5IZQ/edit?usp=sharing",
    )
    keyboardDovid.add(url_button0, url_button1, url_button2)

    keyboardMoney = types.InlineKeyboardMarkup()
    url_button0 = types.InlineKeyboardButton(
        text="Вартість ☹️", url="https://ugi.edu.ua/abiturients/vartist-navchannya/"
    )
    url_button1 = types.InlineKeyboardButton(
        text="Реквізити ☺️", callback_data="recvizutu"
    )
    url_button2 = types.InlineKeyboardButton(text="Зв'язок 🤫", callback_data="zvazok")
    keyboardMoney.add(url_button0, url_button1, url_button2)

    keyboardNoAnswer = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(
        text="Контакти на сайті 😄", url="https://ugi.edu.ua/contacts/"
    )
    url_button1 = types.InlineKeyboardButton(
        text="Анонімне запитання 🤫",
        url="https://docs.google.com/forms/d/e/1FAIpQLScUbU2LbJv4uRc7fpoiPv4b_MSDnVyBvI9LuloE5Xq2oeTnvA/viewform",
    )
    keyboardNoAnswer.add(url_button, url_button1)

    keyboardResource = types.InlineKeyboardMarkup()
    url_button0 = types.InlineKeyboardButton(text="Сайт УГІ", url="https://ugi.edu.ua/")
    url_button1 = types.InlineKeyboardButton(
        text="Moodle", url="https://learn.ugi.edu.ua/login/index.php"
    )
    url_button2 = types.InlineKeyboardButton(
        text="Бібліотека", url="https://lib.ugi.edu.ua/"
    )
    keyboardResource.add(url_button0, url_button1, url_button2)

    keyboardMyMark = types.InlineKeyboardMarkup()
    url_button0 = types.InlineKeyboardButton(
        text="Особистий кабінет 😇",
        url="https://education.ugi.edu.ua/cgi-bin/classman.cgi?n=2",
    )
    url_button1 = types.InlineKeyboardButton(
        text="Інструкція 🙂",
        url="https://www.youtube.com/watch?v=AOVqxdhu0JQ&t=22s&ab_channel=%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B8%D0%B9%D0%B3%D1%83%D0%BC%D0%B0%D0%BD%D1%96%D1%82%D0%B0%D1%80%D0%BD%D0%B8%D0%B9%D1%96%D0%BD%D1%81%D1%82%D0%B8%D1%82%D1%83%D1%82%2FUkrainianinstituteofartsandsciences",
    )
    keyboardMyMark.add(url_button0, url_button1)

    if message.chat.type == "private":
        if message.text == "Документи 📜":
            bot.send_message(
                message.chat.id,
                "Ось довідки та заяви, з якими я можу допомогти, натискай на потрібну кнопку!",
                reply_markup=keyboardDovid,
            )

            # bot.send_message(message.chat.id, "Посилання на зразки заяв нижче", reply_markup=keyboardDeclare)

        elif message.text == "Фінансові питання 😄":
            bot.send_message(
                message.chat.id,
                "Вартість навчання, реквізити для оплати та дані для зв'язку з бухгалтерією нижче 🙂",
                reply_markup=keyboardMoney,
            )

        elif message.text == "Розклад 🗓":
            markup = types.InlineKeyboardMarkup()
            item0 = types.InlineKeyboardButton("Денна форма", callback_data="day")
            item1 = types.InlineKeyboardButton("Заочна форма", callback_data="night")
            markup.add(item0, item1)
            bot.send_message(
                message.chat.id, "Обери форму навчання 😉", reply_markup=markup
            )

        elif message.text == "Мої оцінки 😃":
            bot.send_message(
                message.chat.id,
                "Обирай потрібний варіант, якщо не знаеш як користуватися, натисни __інструкція__ 🙂",
                reply_markup=keyboardMyMark,
                parse_mode="MarkdownV2",
            )

        elif message.text == "Ресурси 📚":
            bot.send_message(
                message.chat.id, "Усе необхідне нижче! 😎", reply_markup=keyboardResource
            )

        elif message.text == "Не знайшов відповідь 😔":
            bot.send_message(message.chat.id, "Деканат - @dekanat_ugi ❤️")
            bot.send_message(message.chat.id, "Приймальня ректора - @office_ugi ❤️")
            bot.send_message(
                message.chat.id,
                "Усі інші контакти ти можеш знайти на сайті. Також ти можеш задати анонімне запитання адміністративній  раді УАЦВО",
                reply_markup=keyboardNoAnswer,
            )

        else:
            bot.send_message(message.chat.id, "Я не знаю что ответить 😢")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        # Очная форма обучения кнопки всех групп
        keyboardGF = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="ГФ-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=140",
        )
        url_button1 = types.InlineKeyboardButton(
            text="ГФ-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=141",
        )
        url_button2 = types.InlineKeyboardButton(
            text="ГФ-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=232",
        )
        url_button3 = types.InlineKeyboardButton(
            text="ГФ-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=457",
        )
        keyboardGF.add(url_button0, url_button1, url_button2, url_button3)

        keyboardDZ = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="ДЗ-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=110",
        )
        url_button1 = types.InlineKeyboardButton(
            text="ДЗ-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=225",
        )
        url_button3 = types.InlineKeyboardButton(
            text="ДЗ-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=444",
        )
        keyboardDZ.add(url_button0, url_button1, url_button2, url_button3)

        keyboardEK = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="ЕК-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=127",
        )
        url_button1 = types.InlineKeyboardButton(
            text="ЕК-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=114",
        )
        url_button2 = types.InlineKeyboardButton(
            text="ЕК-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=226",
        )
        url_button3 = types.InlineKeyboardButton(
            text="ЕК-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=446",
        )
        keyboardEK.add(url_button0, url_button1, url_button2, url_button3)

        keyboardGR = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="ЖР-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=131",
        )
        url_button1 = types.InlineKeyboardButton(
            text="ЖР-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=115",
        )
        url_button2 = types.InlineKeyboardButton(
            text="ЖР-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=227",
        )
        url_button3 = types.InlineKeyboardButton(
            text="ЖР-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=448",
        )
        keyboardGR.add(url_button0, url_button1, url_button2, url_button3)

        keyboardMT = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="МТ-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=134",
        )
        url_button1 = types.InlineKeyboardButton(
            text="МТ-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=116",
        )
        url_button2 = types.InlineKeyboardButton(
            text="МТ-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=228",
        )
        url_button3 = types.InlineKeyboardButton(
            text="МТ-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=450",
        )
        keyboardMT.add(url_button0, url_button1, url_button2, url_button3)

        keyboardPO = types.InlineKeyboardMarkup(row_width=2)
        url_button2 = types.InlineKeyboardButton(
            text="ПО-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=236",
        )
        url_button3 = types.InlineKeyboardButton(
            text="ПО-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=452",
        )
        keyboardPO.add(url_button2, url_button3)

        keyboardPS = types.InlineKeyboardMarkup(row_width=2)
        url_button1 = types.InlineKeyboardButton(
            text="ПС-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=117",
        )
        url_button2 = types.InlineKeyboardButton(
            text="ПС-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=229",
        )
        url_button3 = types.InlineKeyboardButton(
            text="ПС-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=454",
        )
        keyboardPS.add(url_button1, url_button2, url_button3)

        keyboardFV = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="ФВ-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=137",
        )
        url_button1 = types.InlineKeyboardButton(
            text="ФВ-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=118",
        )
        url_button2 = types.InlineKeyboardButton(
            text="ФВ-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=230",
        )
        url_button3 = types.InlineKeyboardButton(
            text="ФВ-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=456",
        )
        keyboardFV.add(url_button0, url_button1, url_button2, url_button3)

        keyboardFK = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="ФК-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=144",
        )
        url_button1 = types.InlineKeyboardButton(
            text="ФК-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=145",
        )
        url_button2 = types.InlineKeyboardButton(
            text="ФК-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=231",
        )
        url_button3 = types.InlineKeyboardButton(
            text="ФК-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=459",
        )
        keyboardFK.add(url_button0, url_button1, url_button2, url_button3)

        # Заочная форма обучения кнопки всех групп
        keyboardZGF = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="зГФ-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=354",
        )
        url_button1 = types.InlineKeyboardButton(
            text="зГФ-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=336",
        )
        url_button2 = types.InlineKeyboardButton(
            text="зГФ-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=337",
        )
        url_button3 = types.InlineKeyboardButton(
            text="зГФ-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=458",
        )
        keyboardZGF.add(url_button0, url_button1, url_button2, url_button3)

        keyboardZDZ = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="зДЗ-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=325",
        )
        url_button1 = types.InlineKeyboardButton(
            text="зДЗ-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=326",
        )
        url_button3 = types.InlineKeyboardButton(
            text="зДЗ-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=445",
        )
        keyboardZDZ.add(url_button0, url_button1, url_button2, url_button3)

        keyboardZEK = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="зЕК-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=523",
        )
        url_button1 = types.InlineKeyboardButton(
            text="зЕК-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=327",
        )
        url_button2 = types.InlineKeyboardButton(
            text="зЕК-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=547",
        )
        url_button3 = types.InlineKeyboardButton(
            text="зЕК-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=447",
        )
        keyboardZEK.add(url_button0, url_button1, url_button2, url_button3)

        keyboardZGR = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="зЖР-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=349",
        )
        url_button1 = types.InlineKeyboardButton(
            text="зЖР-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=324",
        )
        url_button2 = types.InlineKeyboardButton(
            text="зЖР-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=328",
        )
        url_button3 = types.InlineKeyboardButton(
            text="зЖР-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=449",
        )
        keyboardZGR.add(url_button0, url_button1, url_button2, url_button3)

        keyboardZMT = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="зМТ-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=351",
        )
        url_button1 = types.InlineKeyboardButton(
            text="зМТ-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=329",
        )
        url_button2 = types.InlineKeyboardButton(
            text="зМТ-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=330",
        )
        url_button3 = types.InlineKeyboardButton(
            text="зМТ-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=451",
        )
        keyboardZMT.add(url_button0, url_button1, url_button2, url_button3)

        keyboardZPO = types.InlineKeyboardMarkup(row_width=2)
        url_button2 = types.InlineKeyboardButton(
            text="зПО-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=331",
        )
        url_button3 = types.InlineKeyboardButton(
            text="зПО-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=453",
        )
        keyboardZPO.add(url_button2, url_button3)

        keyboardZPS = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="зПС-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=363",
        )
        url_button1 = types.InlineKeyboardButton(
            text="зПС-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=332",
        )
        url_button2 = types.InlineKeyboardButton(
            text="зПС-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=333",
        )
        url_button3 = types.InlineKeyboardButton(
            text="зПС-19(д)",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=567",
        )
        url_button4 = types.InlineKeyboardButton(
            text="зПС-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=442",
        )
        url_button5 = types.InlineKeyboardButton(
            text="зПС-20(д)",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=568",
        )
        keyboardZPS.add(
            url_button0, url_button1, url_button2, url_button3, url_button4, url_button5
        )

        keyboardZFV = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="зФВ-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=353",
        )
        url_button1 = types.InlineKeyboardButton(
            text="зФВ-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=334",
        )
        url_button2 = types.InlineKeyboardButton(
            text="зФВ-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=335",
        )
        url_button3 = types.InlineKeyboardButton(
            text="зФВ-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=455",
        )
        keyboardZFV.add(url_button0, url_button1, url_button2, url_button3)

        keyboardZFK = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(
            text="зФК-17",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=524",
        )
        url_button1 = types.InlineKeyboardButton(
            text="зФК-18",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=431",
        )
        url_button2 = types.InlineKeyboardButton(
            text="зФК-19",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=339",
        )
        url_button3 = types.InlineKeyboardButton(
            text="зФК-20",
            url="https://education.ugi.edu.ua/cgi-bin/timetable.cgi?n=700&group=460",
        )
        keyboardZFK.add(url_button0, url_button1, url_button2, url_button3)

        if call.message:
            if call.data == "dovidka":
                bot.send_message(
                    call.message.chat.id,
                    "[Форма для подання заявки на отримання довідки](https://docs.google.com/forms/d/e/1FAIpQLSe1GkemCU8rEvjHlEtb0Ep9MrkCB7m3pOvggh3kCgoAJkHUMQ/viewform)",
                    parse_mode="MarkdownV2",
                )
            elif call.data == "vukluck":
                bot.send_message(
                    call.message.chat.id,
                    "[Виклик на сесію](https://google.com)",
                    parse_mode="MarkdownV2",
                )
            elif call.data == "recvizutu":
                photo = open("static/photo.jpg", "rb")
                bot.send_photo(call.message.chat.id, photo)
                bot.send_message(
                    call.message.chat.id, "Ці данні в текстовому вигляду 😉"
                )
                bot.send_message(
                    call.message.chat.id,
                    "✅ __Найменування організації:__ ",
                    parse_mode="MarkdownV2",
                )
                bot.send_message(
                    call.message.chat.id, "УКРАЇНСЬКИЙ ГУМАНІТАРНИЙ Інститут ПBH3"
                )
                bot.send_message(
                    call.message.chat.id,
                    "✅ __Код отримувача:__ ",
                    parse_mode="MarkdownV2",
                )
                bot.send_message(call.message.chat.id, "30366752")
                bot.send_message(
                    call.message.chat.id, "✅ __Назва банку:__ ", parse_mode="MarkdownV2"
                )
                bot.send_message(call.message.chat.id, 'АТ КБ "ПРИВАТБАНК"')
                bot.send_message(
                    call.message.chat.id,
                    "✅ __Рахунок отримувача у форматі IBAN:__ ",
                    parse_mode="MarkdownV2",
                )
                bot.send_message(call.message.chat.id, "UA933052990000026006020114768")
                bot.send_message(
                    call.message.chat.id, "✅ __Валюта:__ ", parse_mode="MarkdownV2"
                )
                bot.send_message(call.message.chat.id, "UAH")
            elif call.data == "vartist":
                bot.send_message(
                    call.message.chat.id,
                    "[Вартість навчання](https://ugi.edu.ua/abiturients/vartist-navchannya/)",
                    parse_mode="MarkdownV2",
                )
            elif call.data == "zvazok":
                bot.send_message(
                    call.message.chat.id, "Телефон бугалтерії +38 (093) 321 22 00 "
                )
            elif call.data == "statementsEviction":
                bot.send_message(
                    call.message.chat.id, "Заява на виселення з гуртожитку"
                )
            elif call.data == "day":
                # Очная форма выбор категории групп
                markup = types.InlineKeyboardMarkup()
                item1 = types.InlineKeyboardButton("ГФ", callback_data="gf")
                item2 = types.InlineKeyboardButton("ДЗ", callback_data="dz")
                item3 = types.InlineKeyboardButton("ЕК", callback_data="ek")
                item4 = types.InlineKeyboardButton("ЖР", callback_data="gr")
                item5 = types.InlineKeyboardButton("МТ", callback_data="mt")
                item7 = types.InlineKeyboardButton("ПО", callback_data="po")
                item8 = types.InlineKeyboardButton("ПС", callback_data="ps")
                item9 = types.InlineKeyboardButton("ФВ", callback_data="fv")
                item10 = types.InlineKeyboardButton("ФК", callback_data="fk")

                markup.add(
                    item1, item2, item3, item4, item5, item7, item8, item9, item10
                )
                bot.send_message(
                    call.message.chat.id,
                    "Обирай потрібну группу 😉",
                    reply_markup=markup,
                )
            elif call.data == "night":
                # Заочная форма выбор категории групп
                markup = types.InlineKeyboardMarkup()
                item1 = types.InlineKeyboardButton("зГФ", callback_data="zgf")
                item2 = types.InlineKeyboardButton("зДЗ", callback_data="zdz")
                item3 = types.InlineKeyboardButton("зЕК", callback_data="zek")
                item4 = types.InlineKeyboardButton("зЖР", callback_data="zgr")
                item5 = types.InlineKeyboardButton("зМТ", callback_data="zmt")
                item7 = types.InlineKeyboardButton("зПО", callback_data="zpo")
                item8 = types.InlineKeyboardButton("зПС", callback_data="zps")
                item9 = types.InlineKeyboardButton("зФВ", callback_data="zfv")
                item10 = types.InlineKeyboardButton("зФК", callback_data="zfk")

                markup.add(
                    item1, item2, item3, item4, item5, item7, item8, item9, item10
                )
                bot.send_message(
                    call.message.chat.id,
                    "Обирай потрібну группу 😉",
                    reply_markup=markup,
                )
            # Очная форма обучения ответ на выбор категории групп
            elif call.data == "gf":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп ГФ",
                    reply_markup=keyboardGF,
                )
            elif call.data == "dz":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп ДЗ",
                    reply_markup=keyboardDZ,
                )
            elif call.data == "ek":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп ЕК",
                    reply_markup=keyboardEK,
                )
            elif call.data == "gr":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп ГР",
                    reply_markup=keyboardGR,
                )
            elif call.data == "mt":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп МТ",
                    reply_markup=keyboardMT,
                )
            elif call.data == "po":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп ПО",
                    reply_markup=keyboardPO,
                )
            elif call.data == "ps":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп ПС",
                    reply_markup=keyboardPS,
                )
            elif call.data == "fv":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп ФВ",
                    reply_markup=keyboardFV,
                )
            elif call.data == "fk":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп ФК",
                    reply_markup=keyboardFK,
                )

            # Заочная форма обучения ответ на выбор категории групп
            elif call.data == "zgf":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп зГФ",
                    reply_markup=keyboardZGF,
                )
            elif call.data == "zdz":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп зДЗ",
                    reply_markup=keyboardZDZ,
                )
            elif call.data == "zek":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп зЕК",
                    reply_markup=keyboardZEK,
                )
            elif call.data == "zgr":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп зГР",
                    reply_markup=keyboardZGR,
                )
            elif call.data == "zmt":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп зМТ",
                    reply_markup=keyboardZMT,
                )
            elif call.data == "zpo":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп зПО",
                    reply_markup=keyboardZPO,
                )
            elif call.data == "zps":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп зПС",
                    reply_markup=keyboardZPS,
                )
            elif call.data == "zfv":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп зФВ",
                    reply_markup=keyboardZFV,
                )
            elif call.data == "zfk":
                bot.send_message(
                    call.message.chat.id,
                    "Розклад для групп зФК",
                    reply_markup=keyboardZFK,
                )

            # remove inline buttons
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Ось відповідь на ваше запитання 👍",
                reply_markup=None,
            )

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
