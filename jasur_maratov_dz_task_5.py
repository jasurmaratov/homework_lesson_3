from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def gen(from_, used_, unique):
    while True:
        n_nouns = choice(from_)

        if not(unique and n_nouns in used_):
            used_.append(n_nouns)
            break

    return (n_nouns, used_)

def get_jokes(count, unique=False):
    used = []
    answer = []

    if unique and count > max(map(len,[nouns, adverbs, adjectives])):
        return get_jokes(5, True)

    for _ in range(count):

        nons, used_ = gen(nouns, used, unique)
        used.append()

        adv, used_ = gen(adverbs, used, unique)
        used.append(used_)

        adj, used_ = gen(adjectives, used, unique)
        used.append(used_)

        answer.append(f"{nons} {adv} {adj}")

    return answer