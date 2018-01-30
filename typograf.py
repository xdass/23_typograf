import re

# замена кавычек ' и " на « »
# todo в нужных местах заменить дефисы на тире (деф -    тире — )
# замена дефисов на короткое тире в номерах телефонов   ‐   &ndash;
# связывание чисел с последующими словами неразрывным пробелом
# удаление лишних пробелов и переносов строк  +
# связывание союзов и любых слов из 1-2 символов с последующими словами

actions = [
    (r'[ \t]+', ' '),
    (r'\n+', '\n'),
    (r'[\"\'](.+)[\"\']', r'«\1»'),
    (r'(\d+)‐(\d+)', r'\1&ndash;\2'),
    (r'(\d+)\s+(\w+)', r'\1&nbsp;\2'),
    (r'([^-]\b[а-яА-Я]{1,2}\b)\s+(\w+)', r'\1&nbsp;\2')
]
test_string = """Так-вот это 'Заголовок', потом идут  лишние     пробелы(табы). А наш номер +700-233-22-11111 который


мы купили за 1000 рублей. Во во говорил я тогда
"""
test_str2 = """Вчера 33 китайца позвонили по телефону: +7900-900-22-11  тут пробелы и		табы.


Тут "что-то в кавычках". Это - нормально!
"""
for expr, replace in actions:
    test_str2 = re.sub(expr, replace, test_str2)

print(test_str2)


def beautify_text(text):
    for expr, replace in actions:
        text = re.sub(expr, replace, text)
    return text
