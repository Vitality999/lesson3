from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime
import keys



PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
     'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

#PROXY = {'proxy_url': 'socks5://95.215.54.206:39880'}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
solar = [{'planet':'Меркурий'},{'planet':'Венера'}, {'planet':'Земля'}, {'planet':'Марс'},{'planet': 'Юпитер'},
         {'planet':'Сатурн'}, {'planet':'Нептун'}, {'planet':'Плутон'}, {'planet':'Луна' }, {'planet': 'Солнце'}]

constellations = {'Capricornus':'Козерог', 'Gemini': 'Близнецы', 'Aries':'Овен', 'Libra':'Весы',
                  'Sagittarius': 'Стрелец', 'Taurus':'Телец', 'Aquarius': 'Водолей', 'Cancer' : 'Рак',
                  'Leo':'Лев', 'Virgo':'Дева', 'Scorpio': 'Скорпион', 'Pisces': 'Рыбы'}

sysdate = datetime.datetime.now()

numbers = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7,
           'восемь': 8, 'девять': 9, 'десять': 10, 'ноль': 0}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    if user_text == 'Привет':
        print(user_text)
        update.message.reply_text('И тебе привет')
    elif user_text == 'Пока':
        print(user_text)
        update.message.reply_text('До новых встреч')

    else:
        print(user_text)
        update.message.reply_text(user_text)


def question(bot, update):
    while True:
        update.message.reply_text('Введите название планеты с большой буквы, для выхода введите: "Выход"\n')
        if update.message.text() != 'Выход':
            solar_system(bot, update)
        elif update.message.text() == 'Выход':
            update.message.reply_text('Выхода нет')


def solar_system(bot, update):

    for objects in solar:
        if objects['planet'] == update.message.text:
            if update.message.text == 'Марс':
                mars = ephem.Mars(sysdate)
                ma = ephem.constellation(mars)[1]
                if ma in constellations:
                    update.message.reply_text(constellations.get(ma))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Юпитер':
                jupiter = ephem.Jupiter(sysdate)
                ju = ephem.constellation(jupiter)[1]
                if ju in constellations:
                    update.message.reply_text(constellations.get(ju))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Луна':
                moon = ephem.Moon(sysdate)
                mo = ephem.constellation(moon)[1]
                if mo in constellations:
                    update.message.reply_text(constellations.get(mo))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Сатурн':
                saturn = ephem.Saturn(sysdate)
                sa = ephem.constellation(saturn)[1]
                if sa in constellations:
                    update.message.reply_text(constellations.get(sa))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Венера':
                venus = ephem.Venus(sysdate)
                ve = ephem.constellation(venus)[1]
                if ve in constellations:
                    update.message.reply_text(constellations.get(ve))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Солнце':
                sun = ephem.Sun(sysdate)
                sa = ephem.constellation(sun)[1]
                if sa in constellations:
                    update.message.reply_text(constellations.get(sa))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Меркурий':
                mercury = ephem.Mercury(sysdate)
                me = ephem.constellation(mercury)[1]
                if me in constellations:
                    update.message.reply_text(constellations.get(me))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Нептун':
                neptune = ephem.Neptune(sysdate)
                ne = ephem.constellation(neptune)[1]
                if ne in constellations:
                    update.message.reply_text(constellations.get(ne))
                else:
                    update.message.reply_text('Созвезие не обнаружено')

            elif update.message.text == 'Плутон':
                update.message.reply_text('Настолько маленькая, что и планетой назвать нельзя')
            else:
                update.message.reply_text('Планету украли')


def counting_word (bot, update):
    have = update.message.text.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')\
    .replace('!', ' ').replace('\n', ' ').replace('\t', ' ')
    if len(have) > 10:
        if have[11] in '\"\'' and have[-1] in '\"\'':
            counter = str(len(have.split())-1)
            update.message.reply_text('Всего слов: ' + counter  )
        else:
            update.message.reply_text('Введите фразу в кавычках')
    elif len(have) <= 10:
        update.message.reply_text("Вы ничего не ввели")
    else:
        update.message.reply_text('Такое не считаем')

def calculate(bot, update):
    enter = update.message.text
    if enter.endswith('='):
        parse = enter.split()
        replacement = (parse[1].replace('=', ''))
        if '+' in replacement:
            substitution = replacement.replace('+',' ')
            sp = substitution.split()
            update.message.reply_text(int(sp[0]) + int(sp[1]))
        elif '-' in replacement:
            substitution = replacement.replace('-',' ')
            sp = substitution.split()
            update.message.reply_text(int(sp[0]) - int(sp[1]))
        elif '*' in replacement:
            substitution = replacement.replace('*',' ')
            sp = substitution.split()
            update.message.reply_text(int(sp[0]) * int(sp[1]))
        elif '/' in replacement:
            try:
                substitution = replacement.replace('/',' ')
                sp = substitution.split()
                update.message.reply_text(int(sp[0]) / int(sp[1]))
            except ZeroDivisionError:
                update.message.reply_text('На ноль даже на зоне не делят')

#взаимодействие с числами в виде строки:

    elif 'плюс' in enter.split()[2]:
        replaces = enter.lower().replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')
        string = replaces.split()[1:]
        if string[0] in numbers and string[2] in numbers:
            result = int(numbers.get(string[0]) + int(numbers.get(string[2])))
            update.message.reply_text(result)
    elif 'минус' in enter.split()[2]:
        replaces = enter.lower().replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')
        string = replaces.split()[1:]
        if string[0] in numbers and string[2] in numbers:
            result = int(numbers.get(string[0]) - int(numbers.get(string[2])))
            update.message.reply_text(result)
    elif 'умножить' in enter.split()[2]:
        replaces = enter.lower().replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace('на', ' ')
        string = replaces.split()[1:]
        if string[0] in numbers and string[2] in numbers:
            result = int(numbers.get(string[0]) * int(numbers.get(string[2])))
            update.message.reply_text(result)
    elif 'делить' in enter.split()[2] or 'поделить' in enter.split()[2]:
        try:
            replaces = enter.lower().replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace('на', ' ')
            string = replaces.split()[1:]
            if string[0] in numbers and string[2] in numbers:
                result = int(numbers.get(string[0]) / int(numbers.get(string[2])))
                update.message.reply_text(result)
        except ZeroDivisionError:
            update.message.reply_text('На ноль даже на зоне не делят')

#взаимодействие вещественных чисел:

    elif 'и' in enter.lower().split():
        replaces = enter.lower().replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace('на', ' ')
        string = replaces.split()[1:]
        string[1] = '.'
        string[5] = '.'
        if 'умножить' in string:
            x = str(numbers.get(string[0])) + '.' + str(numbers.get(string[2]))
            y = str(numbers.get(string[4])) + '.' + str(numbers.get(string[6]))
            z = round(float(x) * float(y), 2)
            update.message.reply_text(z)
        elif 'делить' in string or 'поделить' in string:
            x = str(numbers.get(string[0])) + '.' + str(numbers.get(string[2]))
            y = str(numbers.get(string[4])) + '.' + str(numbers.get(string[6]))
            z = round(float(x) / float(y), 2)
            update.message.reply_text(z)
        elif 'плюс' in string:
            x = str(numbers.get(string[0])) + '.' + str(numbers.get(string[2]))
            y = str(numbers.get(string[4])) + '.' + str(numbers.get(string[6]))
            z = round(float(x) + float(y), 2)
            update.message.reply_text(z)
        elif 'минус' in string:
            x = str(numbers.get(string[0])) + '.' + str(numbers.get(string[2]))
            y = str(numbers.get(string[4])) + '.' + str(numbers.get(string[6]))
            z = round(float(x) - float(y), 2)
            update.message.reply_text(z)
    else:
        update.message.reply_text('Выражение не содержит в конце знака "="')

def fullmoon(bot, update):
    message = update.message.text
    if message.endswith('?'):
        replaces = message.replace('?', '').replace('-', '/')
        separator = replaces.split()
        next_date = ephem.next_new_moon(separator[-1])
        convert_type = next_date.datetime()
        times = datetime.datetime.strftime(convert_type, '%Y-%m-%d %H:%M:%S')
        update.message.reply_text('Ближайшее полнолуние: ' + times)
    else:
        update.message.reply_text('Вы забыли поставить знак "?"')


def main():
    mybot = Updater(keys.tKey, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", question))
    dp.add_handler(CommandHandler("wordcount", counting_word))
    dp.add_handler(CommandHandler("calculate", calculate))
    dp.add_handler(CommandHandler("newmoon", fullmoon))
    dp.add_handler(MessageHandler(Filters.text, solar_system))



    mybot.start_polling()
    mybot.idle()



if __name__ == '__main__':
    main()