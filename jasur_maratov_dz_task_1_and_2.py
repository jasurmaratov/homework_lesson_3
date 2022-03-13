"""task 1 and 2"""
DICT_NUM = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четире',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
}
def num_translate(num_world):
    return DICT_NUM.get(num_world)

def num_transtalen(num_world):
    to_key = DICT_NUM.get(num_world.lower())

    if to_key:
        return to_key.capitalize() if num_world[0].isupper() else to_key

    return None

resault = num_transtalen('One')
print(resault)