# Задание

#1.Напечатайте в консоль даты: вчера, сегодня, месяц назад

from datetime import datetime, timedelta

dt_now = datetime.now()
delta_day = timedelta(days=1)
delta_month = timedelta(days=30)
dt_yesterday = dt_now - delta_day
dt_last_month = dt_now - delta_month
print('Дата сегодня: ', dt_now.strftime('%Y-%m-%d'), '\n',\
      'Дата вчерашнего дня: ', dt_yesterday.strftime('%Y-%m-%d'), '\n',\
      'Дата прошлого месяца: ', dt_last_month.strftime('%Y-%m-%d'))

#2.Превратите строку "01/01/17 12:10:03.234567" в объект datetime

date_str = '01/01/17 12:10:03.234567'
d_s = datetime.strptime(date_str, '%d/%m/%y %H:%M:%S.%f')
print(d_s, '- объект datetime')

