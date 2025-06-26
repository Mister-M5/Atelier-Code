from flask import (Flask, render_template)
import json
import random
import os

IMG_FOLDER = os.path.join("static", "images")
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = IMG_FOLDER
Logo = os.path.join(app.config["UPLOAD_FOLDER"], "logo.png")

print("En quelle langue créer le wordle ?")
print ("langues disponibles : fr, en")
lang = input()
lang.lower()

while lang!="fr" and lang!="en":
    print("Langue incorecte.")
    print("En quelle langue créer le wordle ?")
    print("langues disponibles : fr, en")
    lang = input()
    lang.lower()

data_dir = "data/"

def load_characters(lang):
    with open(f"{data_dir}/{lang}/{lang}_characters.txt", "r") as f:
        characters = [line.strip() for line in f]
    return characters

def load_words(lang):
    _5words = []
    with open(f"{data_dir}/{lang}/liste_complete.txt", "r") as f:
        for line in f:
            _5words+=line.split()
    _5words = [word.lower() for word in _5words]
    return _5words


def load_keyboard(lang):
        with open(f"{data_dir}/{lang}/{lang}_keyboard.json", "r") as f:
            keyboard = json.load(f)
        return keyboard

def get_idx():
    idx = random.randrange(1,100000,1)
    return idx

language_characters = load_characters(lang)
language_codes_5words = load_words(lang)
keyboards = load_keyboard(lang)

class Language:
    """Holds the attributes of a language"""

    def __init__(self, language_code, word_list):
        self.language_code = language_code
        self.word_list = word_list
        idx = get_idx()
        self.word = word_list[idx % len(word_list)]
        self.idx = idx
        self.characters = language_characters
        self.keyboard = keyboards
        if len(keyboards[-1])<=7:
            self.keyboard[-1].insert(0, "⇨")
            self.keyboard[-1].append("⌫")
        print("\n***********************************************")
        print(f"                    INFOS")
        print(f"- Il y a {len(word_list)} mots pour le {lang}")
        print(f"- L'index est {idx}")
        print(f"- Le mot associé est {self.word}")
        print(self.keyboard)
        print(f"***********************************************\n")

@app.route("/")
def language(lang_c=lang):
    word_list = language_codes_5words
    language = Language(lang_c, word_list)
    return render_template("Modele.html", language=language, img=Logo)

if __name__ == "__main__":
    app.run()
