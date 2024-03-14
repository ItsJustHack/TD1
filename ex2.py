from ex1 import check_mot_faisable 

### On représente les points des lettres par un dico 

dico_score = {}

for lettre in ['a','e','i','l','n','o','r','s','t','u']:
    dico_score[lettre] = 1

for lettre in ['d','g','m']:
    dico_score[lettre] = 2

for lettre in ['b','c','p']:
    dico_score[lettre] = 3

for lettre in ['f','h','v']:
    dico_score[lettre] = 4

for lettre in ['j', 'q']:
    dico_score[lettre] = 8

for lettre in ['k','w','x','y','z']:
    dico_score[lettre] = 10

def score_mot(mot : str):
    score = 0
    try : 
        for lettre in mot:
            score += dico_score[lettre] 
        return score # Encore une mauvaise pratique, un classique cependant
    except KeyError:
        raise("Lettre invalide dans le mot")

assert(score_mot("kaw") == 21)

def score_plus_haut_dico(fichier : str,
                     lettres_possibles : list):
    """ Search the word that has the highest score with available letters"""
    try: 
        f = open(fichier, "r")
        score_max = 0
        mot_actuel = ""
        for ligne in f:
            mot = ligne.rstrip("\n")
            score_mot_actuel = score_mot(mot)
            if score_mot_actuel > score_max and check_mot_faisable(mot, lettres_possibles):
                mot_actuel = mot 
                score_max = score_mot_actuel
        return mot_actuel
    except FileNotFoundError:
        raise("File not found")


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

print(score_plus_haut_dico("frenchssaccent.dic", ['b', 'a', 'c']))