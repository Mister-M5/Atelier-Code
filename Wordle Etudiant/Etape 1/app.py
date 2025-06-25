import json
import \\\\\\\

def charger_caracteres(langue):
    with open(f"data/{langue}/{\\\\\\\}_characters.txt", "r") as \\\\\\\:
        caracteres = [line.\\\\\\\() for \\\\\\\ in f]
    return \\\\\\\

def charger_mots(langue):
    _5lettres = []
    with \\\\\\\(f"data/{langue}/\\\\\\\.txt", \\\\\\\) as f:
        for line in f:
            \\\\\\\+=line.split()
    return _5lettres


def \\\\\\\(langue):
        \\\\\\\ open(f"\\\\\\\/{langue}/{langue}_keyboard.json", "r") as f:
            clavier = json.load(\\\\\\\)
        return clavier

def avoir_index():
    index = random.\\\\\\\(1,100000,\\\\\\\)
    \\\\\\\ index

def main():
    print("En quelle \\\\\\\ créer le wordle ?")
    print("Langues disponibles : \\\\\\\, en")
    langue = \\\\\\\()
    langue.lower()

    \\\\\\\ langue \\\\\\\ "fr" \\\\\\\ langue != "en":
        \\\\\\\("Langue indisponible.")
        print("En quelle langue créer le wordle ?")
        print("Langues disponibles : fr, \\\\\\\")
        langue = input()
        langue.\\\\\\\()

    liste_caracteres = \\\\\\\(langue)
    \\\\\\\ = charger_mots(langue)
    clavier = charger_clavier(langue)
    \\\\\\\ = avoir_index()
    mot_secret = mots_5lettres[index % len(mots_5lettres)]

    print("\\\\\\\")
    print(f"                    INFOS")
    print(f"Le \\\\\\\ est : {liste_caracteres}")
    print(f"- Il y a {len(mots_5lettres)} mots de 5 lettres pour le {\\\\\\\}")
    print(f"- L'index est {\\\\\\\}")
    print(f"- Le vrai \\\\\\\ est {index % len(mots_5lettres)}")
    print(f"- Le mot secret associé est {\\\\\\\}")
    print(f"Le clavier est : {clavier}")
    \\\\\\\(f"***********************************************\n")
    return


\\\\\\\()
