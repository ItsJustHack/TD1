### Variable plus grand mot actuel 
### Skip du mot si la longueur est plus petite 
### Si le mot n'est pas skip on parcourt le mot et on teste les lettres

def check_word_feasibility(word, available_letters): # Ne jamais faire ça 
    """Check if a word is doable with the currrent letters"""
    for letters in word:
        if letters not in available_letters:
            return False                    # SURTOUT CA
    return True


assert check_word_feasibility("test", ['t', 'e', 's'])
assert check_word_feasibility("salut", ['s', 't', 'a', 'l', 'u', 'd'])

def mot_plus_long_dico(fichier : str,
                     available_letters : list):
    """ Search the longest word through a file"""
    try: 
        f = open(fichier, "r")
        max_length = 0
        current_word = ""
        for ligne in f:
            word = ligne.rstrip("\n")
            if len(word) > max_length and check_word_feasibility(word, available_letters):
                current_word = word 
                max_length = len(word)
        return current_word
    except FileNotFoundError:
        print("File not found, exit") #TODO
        return ""

assert(mot_plus_long_dico("frenchssaccent.dic", ['b', 'a', 'c']) == "abaca")
assert(mot_plus_long_dico("frenchssaccent.dic", ['a', 'n', 't', 'i', 'c', 'o', 'n', 's', 't', 'u', 'e', 'l', 'm']) == "anticonstitutionnellement")
