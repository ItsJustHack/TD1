from ex1 import check_word_feasibility, available_words
from ex1 import FICHIER

# Score of a letter is represented by a dict {letter : value}


def score_word(word: str, score_dict: dict) -> int:
    """Calculation of the score of a word out of a dict"""
    score = 0
    try:
        # Do not accept a word if a letter is not in the dict
        for letter in word:
            score += dico_score[letter]
        return score
    except KeyError:
        raise ("Lettre invalide dans le word")
    except Exception:
        raise "Unknown error occured, exit"


def max_score(words: list, score_dict: dict) -> (str, int):
    """Returns the highest score among a word list"""
    if len(words) == 0:
        raise "Word list is empty, exit"
    score = score_word(words[0], score_dict)
    current_word = words[0]
    for word in words[1:]:
        if score_word(word, score_dict) > score:
            score = score_word(word, score_dict)
            current_word = word
    return (current_word, score)


def highest_score_dict(words: str, available_letters: list,
                       score_dict: dict, allow_joker=False) -> (str, int):
    """ Search the word that has the highest score with available letters"""
    words_available = available_words(words, available_letters, allow_joker)
    assert "psychophysiologique" not in words_available
    return max_score(words_available, score_dict)


if __name__ == "__main__":
    dico_score = {}
    for lettre in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
        dico_score[lettre] = 1
    for lettre in ['d', 'g', 'm']:
        dico_score[lettre] = 2
    for lettre in ['b', 'c', 'p']:
        dico_score[lettre] = 3
    for lettre in ['f', 'h', 'v']:
        dico_score[lettre] = 4
    for lettre in ['j', 'q']:
        dico_score[lettre] = 8
    for lettre in ['k', 'w', 'x', 'y', 'z']:
        dico_score[lettre] = 10

    assert score_word("kaw", dico_score) == 21
    assert score_word("lettre", dico_score) == 6

    assert max_score(['rte', 'ver', 'ce', 'etc', 'cet', 'ex',
                      'cr', 'et', 'ter', 'te', 'ct'], dico_score) == ('ex', 11)

    assert available_words(['kw', 'rte', 'ver', 'ce', 'etc', 'cet', 'ex'],
                           ['k', 'w', 'c']) == ['kw']

    assert highest_score_dict(['kw', 'rte', 'ver', 'ce', 'etc', 'cet', 'ex',
                               'cr', 'et', 'ter', 'te', 'ct'], ['k', 'w', 'c'], dico_score) == ("kw", 20)

    f = open(FICHIER, "r")
    words = []
    for line in f:
        words.append(line.rstrip("\n"))

    print(highest_score_dict(words, [
          'a', 'n', 't', 'i', 'o', 'n', 's', 't', 'u', 'e', 'l', 'm'], dico_score, True))
