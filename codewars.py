text = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'


def remove_consecutive_duplicates(text: str) -> str:
    text = text.split()
    for i in range(len(text) - 1, 0, -1):
        if text[i] == text[i - 1]:
            del text[i]
    return ' '.join(text)


# print(remove_consecutive_duplicates(text))


year = {
    'January': {
        '1': 'Naughty', '2': 'Naughty', '31': 'Nice'
    },
    'February': {
        '1': 'Nice', '2': 'Naughty', '28': 'Nice'
    },
    'December': {
        '1': 'Nice', '2': 'Nice', '31': 'Naughty'
    }
}


def naughty_or_nice(data: dict) -> str:
    naughty = 0
    nice = 0
    for month in data.values():
        for day in month.values():
            if day == 'Naughty':
                naughty += 1
            else:
                nice += 1
    if naughty > nice:
        return 'Naughty!'
    else:
        return 'Nice!'


def keep_order(numbers: list[int], num: int) -> int:
    for i in range(len(numbers)):
        if numbers[i] >= num:
            return i
    return len(numbers)


def vowel_one(s):
    res = ''
    for i in s.lower():
        if i in 'eyuioa':
            res += '1'
        else:
            res += '0'
    return res
