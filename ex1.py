# Variable plus grand mot actuel
# Skip du mot si la longueur est plus petite
# Si le mot n'est pas skip on parcourt le mot et on teste les lettres

FICHIER = "frenchssaccent.dic"


def check_word_feasibility(word, available_letters):
    """Check if a word is doable with the currrent letters"""
    for letters in word:
        if letters not in available_letters:
            return False
    return True


assert check_word_feasibility("test", ['t', 'e', 's'])
assert check_word_feasibility("salut", ['s', 't', 'a', 'l', 'u', 'd'])


def available_words(words: list, available_letters: list, joker=False) -> list:
    """Returns the words list without the unavailable words"""
    # This function makes the overall execution slower but the code is easier to read
    # (and it's python, who cares about speed)
    words_available = []
    if joker:  # I'm absolutely sure there is a better way to do this
        for word in words:
            if check_word_feasibility_with_joker(word, available_letters):
                words_available.append(word)
    else:
        for word in words:
            if check_word_feasibility(word, available_letters):
                words_available.append(word)
    return words_available


def check_word_feasibility_with_joker(word: str, available_letters: list) -> bool:
    # This function is required for exercice 4
    """Check if a word is doable with the available letters and 1 joker"""
    letter_added = ''
    is_joker_used = False
    for letters in word:
        if letters not in available_letters + [letter_added] and is_joker_used:
            return False
        elif letters not in available_letters + [letter_added] and not is_joker_used:
            #  available_letters.append(letters) # MODIFIE LA LISTE EN ARGUMENT ??????
            letter_added = letters
            is_joker_used = True
    return True


assert available_words(["test", "voila", "papier"], [
                       't', 'e', 's', 't']) == ["test"]

assert not check_word_feasibility_with_joker("psychophysiologique",
                                             ['a', 'n', 't', 'i', 'o', 'n', 's', 't', 'u', 'e', 'l', 'm'])


assert check_word_feasibility_with_joker("test", ['t', 's'])
assert check_word_feasibility_with_joker("test", ['t', 'e', 's'])
assert not check_word_feasibility_with_joker("anaconda", ['t', 's'])
assert not check_word_feasibility_with_joker("testr", ['t', 's'])


def mot_plus_long_dico(words: list, available_letters: list) -> str:
    """ Search the longest word through a list"""
    max_length = 0
    current_word = ""
    words_available = available_words(words, available_letters)
    for word in words_available:
        if len(word) > max_length:
            current_word = word
            max_length = len(word)
    return current_word


if __name__ == "__main__":
    try:
        f = open(FICHIER, "r")
        words = []
        for line in f:
            words.append(line.rstrip("\n"))  # Reads through the file

        assert mot_plus_long_dico(words, ['b', 'a', 'c']) == "abaca"
        assert mot_plus_long_dico(words, [
            'a', 'n', 't', 'i', 'c', 'o', 'n', 's', 't', 'u', 'e', 'l', 'm']) == "anticonstitutionnellement"
        assert mot_plus_long_dico(['sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base',
                                  'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a'], ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']) == "sacre"

        print("If this runs, the function seems to work")
    except FileNotFoundError:
        raise "File not found, exit"
    except AssertionError:
        raise "Un test a échoué"
    except Exception as e:
        # Not sure about the way to handle any other error
        print(f"An error occured: {e}")
