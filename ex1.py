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


def mot_plus_long_dico(words: list, available_letters: list) -> str:
    """ Search the longest word through a file"""
    max_length = 0
    current_word = ""
    for word in words:
        if len(word) > max_length and check_word_feasibility(word,
                                                             available_letters):
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
    except Exception as e:
        # Not sure about the way to handle any other error
        print(f"An error occured: {e}")
