import operator
import string
from collections import Counter
from itertools import chain
from pathlib import Path

from sty import fg, ef

path = "C:\\Users\\sidan\\Desktop\\Sidharth\\Python\\ywsidharthanand\\wordlesolver\\data\\words.txt"

legal_char = set(string.ascii_letters)
max_attempt = 6
word_len = 5

words = {
    word.lower()
    for word in Path(path).read_text().splitlines()
    if len(word) == word_len and set(word) < legal_char
}

let_count = Counter(chain.from_iterable(words))
let_freq = {
    character: value / sum(let_count.values())
    for character, value in let_count.items()
}


def commonality_metric(word):
    score = 0.0
    for char in word:
        score += let_freq[char]
    return score / (word_len - len(set(word)) + 1)


def sort_words(words):
    sort_by = operator.itemgetter(1)
    return sorted([(word, commonality_metric(word)) for word in words], key=sort_by, reverse=True)


def get_sorted_words(word_commonality):
    s = ''
    num = 0
    for (word, freq) in word_commonality:
        s += f"{num+1}.  " + fg.li_blue + f"{word:<6}  |  " + ef.bold + f"{freq:<4.3}\n" + fg.rs
        num += 1
    return s
