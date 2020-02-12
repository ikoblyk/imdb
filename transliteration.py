from collections import defaultdict
from pprint import pprint
from regex import regex

russian_alphabet_upper = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
]

russian_alphabet_lower = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def create_alp(a, b, index):
    d = defaultdict()
    for i in range(a.__len__()):
        d[a[i]] = b[i][index]
    return d



eng_upper = [
['A', 'a'],
['B',	'b'],
['V',	'v'],
['G',	'g'],
['D',	'd'],
['E',	'e'],
['Yo',	'yo'],
['Zh',	'zh'],
['Z',	'z'],
['I','i'],
['Y',	'y'],
['K',	'k'],
['L',	'l'],
['M',	'm'],
['N',	'n'],
['O',	'o'],
['P',	'p'],
['R',	'r'],
['S',	's'],
['T',	't'],
['U',	'u'],
['F',	'f'],
['Kh',	'kh'],
['Ts',	'ts'],
['Ch',	'ch'],
['Sh',	'sh'],
['Shch',	'shch'],
[''	,''],
['Y',	'y'],
[''	,''],
['E',	'e'],
['Yu',	'yu'],
['Ya',	'ya']
]


d_upper = create_alp(russian_alphabet_upper, eng_upper, 0)
d_lower = create_alp(russian_alphabet_lower, eng_upper, 1)


def cyrrylic_check(strr):
    return bool(regex.search('[а-яА-Я]', strr))


def transalte(fromm):
    transaltion = ''
    for char in fromm:
        if cyrrylic_check(char):
            if char.islower():
                transaltion+=d_lower[char]
            elif char.isupper():
                transaltion += d_upper[char]

            else:
                transaltion += char
        else:
            transaltion+=char
    return transaltion





