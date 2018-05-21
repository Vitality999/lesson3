# Задание
#
#Скачайте файл по ссылке: https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
#Прочитайте его и подсчитайте количество слов в тексте


with open('referat.txt', 'r', encoding='utf-8')as file:
    count = 0
    for line in file:
        print(line)
        l = len(line.split())
        count += l
    print('\nВ тексте:'.upper(), count, 'слова\n'.upper())
    file.close()
