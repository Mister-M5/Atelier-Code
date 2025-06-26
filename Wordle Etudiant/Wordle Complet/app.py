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
lang = lang.lower()

while lang!="fr" and lang!="en":
    print("Langue incorecte.")
    print("En quelle langue créer le wordle ?")
    print("langues disponibles : fr, en")
    lang = input()
    lang = lang.lower()

data_dir = "data/"

def load_characters(lang):
    with open(f"{data_dir}/{lang}/{lang}_characters.txt", "r") as f:
        characters = [line.strip() for line in f]
    return characters

def load_words(lang):
    #loads the words and does some basic QA
    _5words = []
    with open(f"{data_dir}/{lang}/liste_complete.txt", "r") as f:
        for line in f:
            _5words+=line.split()
    # QA
    _5words = [word.lower() for word in _5words if len(word) == 5 and word.isalpha()]
    # remove words without correct characters
    _5words = [word for word in _5words if all([char in language_characters for char in word])]

    # we don't want words in order, so shuffle
    random.shuffle(_5words)
    print(f"Les mots {lang} sont désormais mélangés")
    return _5words

def load_language_config(lang):
        with open(f"{data_dir}/{lang}/language_config.json", "r") as f:
            language_config = json.load(f)
        return language_config

def load_keyboard(lang):
        with open(f"{data_dir}/{lang}/{lang}_keyboard.json", "r") as f:
            keyboard = json.load(f)
        return keyboard

def get_idx():
    idx = random.randrange(1,100000,1)
    return idx

language_characters = load_characters(lang)
language_codes_5words = load_words(lang)
language_configs = load_language_config(lang)
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
        self.config = language_configs
        self.keyboard = keyboards
        print("\n***********************************************")
        print(f"                    INFOS")
        print(f"- Il y a {len(word_list)} mots pour le {lang}")
        print(f"- L'index est {idx}")
        print(f"- Le mot associé est {self.word}")
        print(f"***********************************************\n")
        if len(keyboards[-1])<=7:
            self.keyboard[-1].insert(0, "⇨")
            self.keyboard[-1].append("⌫")



@app.route("/")
def language(lang_c=lang):
    word_list = language_codes_5words
    language = Language(lang_c, word_list)
    return render_template("game.html", language=language, img=Logo)

if __name__ == "__main__":
    app.run()
