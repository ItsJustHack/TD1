from ex1 import check_word_feasibility
from ex1 import FICHIER

# On représente les points des lettres par un dico


def score_word(word: str, score_dict: dict) -> int:
    """Calculation of the score of a word out of a dict"""
    score = 0
    try:
        for letter in word:
            score += dico_score[letter]
        return score
    except KeyError:
        raise ("Lettre invalide dans le word")
    except Exception:
        raise "Unknown error occured, exit"


def highest_score_dict(fichier: str,
                         lettres_possibles: list):
    """ Search the word that has the highest score with available letters"""
    try:
        max_score = 0
        mot_actuel = ""
        for word in words:
            score_mot_actuel = score_word(word)
            if score_mot_actuel > max_score and check_word_feasibility(word, lettres_possibles):
                mot_actuel = word
                score_max = score_mot_actuel
        return mot_actuel
    except FileNotFoundError:
        raise ("File not found")


def mot_faisable_plus_joker(word, available_letters):
    """Check if a word is doable with the available letters and 1 joker"""
    isJokerUsed = False
    for letters in word:
        if letters not in available_letters and isJokerUsed:
            return False
        elif letters not in available_letters and not isJokerUsed:
            available_letters.append(letters)
            isJokerUsed = True
    return True


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

    assert (score_word("kaw", dico_score) == 21)

    f = open(FICHIER, "r")
    words = []
    for line in f:
        words.append(line.rstrip("\n"))

print(score_plus_haut_dico("frenchssaccent.dic", ['b', 'a', 'c']))
