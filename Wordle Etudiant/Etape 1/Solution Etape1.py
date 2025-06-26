import json
import random

def charger_caracteres(langue):
    with open(f"data/{langue}/{langue}_characters.txt", "r") as f:
        caracteres = [line.strip() for line in f]
    return caracteres

def charger_mots(langue):
    _5lettres = []
    with open(f"data/{langue}/liste_complete.txt", "r") as f:
        for line in f:
            _5lettres+=line.split()
    return _5lettres


def charger_clavier(langue):
        with open(f"data/{langue}/{langue}_keyboard.json", "r") as f:
            clavier = json.load(f)
        return clavier

def avoir_index():
    index = random.randrange(1,100000,1)
    return index

def main():
    print("En quelle langue créer le wordle ?")
    print("Langues disponibles : fr, en")
    langue = input()
    langue.lower()

    while langue != "fr" and langue != "en":
        print("Langue indisponible.")
        print("En quelle langue créer le wordle ?")
        print("Langues disponibles : fr, en")
        langue = input()
        langue.lower()

    liste_caracteres = charger_caracteres(langue)
    mots_5lettres = charger_mots(langue)
    clavier = charger_clavier(langue)
    index = avoir_index()
    mot_secret = mots_5lettres[index % len(mots_5lettres)]

    print("\n***********************************************")
    print(f"                    INFOS")
    print(f"Le set de caractères est : {liste_caracteres}")
    print(f"- Il y a {len(mots_5lettres)} mots de 5 lettres pour le {langue}")
    print(f"- L'index est {index}")
    print(f"- Le vrai index est {index % len(mots_5lettres)}")
    print(f"- Le mot secret associé est {mot_secret}")
    print(f"Le clavier est : {clavier}")
    print(f"***********************************************\n")
    return


main()
