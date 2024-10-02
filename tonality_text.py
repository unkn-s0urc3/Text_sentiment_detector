import re

import array_of_aggressive_words


def find_aggressive_words_by_parts(text, aggressive_words):
    text_words = re.findall(r'\w+', text.lower())

    aggressive_roots = [word[:len(word) * 2 // 3] for word in aggressive_words]

    found_words = [word for word in text_words if any(root in word for root in aggressive_roots)]

    return found_words

text = "Я тебя ненавижу!"
found_words = find_aggressive_words_by_parts(text, array_of_aggressive_words.words)

if found_words:
    print(f"Агрессивные слова найдены: {', '.join(found_words)}")
else:
    print("Агрессивных слов не найдено.")