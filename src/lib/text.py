# 1

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    text = ' '.join(text.split())

    return text

# 2

import re

def tokenize(text: str) -> list[str]:
    reg = r'\w+(?:-\w+)*'
    l = []

    for x in re.finditer(reg, text):
        l.append(x.group())

    return l

# 3
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}

    for x in tokens:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
            
    return dict(sorted(freq.items()))

# 4 

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    
    words = list(freq.items())
    words.sort(key=lambda x: (-x[1], x[0]))

    return words[:n]

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто" ))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))

# print(count_freq(["a", "b", "a", "c", "b", "a"]))
# print(top_n(count_freq(["a", "b", "a", "c", "b", "a"]), 2))

# print(count_freq(["bb","aa","bb","aa","cc"]))
# print(top_n(count_freq(["bb","aa","bb","aa","cc"]), 2))