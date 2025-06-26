// Vue stuff below
const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            active_row: 0,
            active_cell: 0,
            full_word_inputted: false,
            game_over: false,

            word: ######,
            ######: idx,
            word_list: word_list,
            ######: characters,
            showHelpModal: false,

            notification: {
                show: false,
                message: "",
                top: 10,
                timeout: 0,
            },

            tiles: [
                ["", "", "", "", ######],
                ["", ######, "", "", ""],
                ["", "", "", "", ""],
                ["", "", ######, "", ""],
               ["", "", "", ######, ""],
                [######, "", "", "", ""],
            ],
            tile_classes: [
                [######, ######, ######, ######, ######],
                ["border-2 border-neutral-500", ######, "border-2 border-neutral-500", "border-2 border-neutral-500", "border-2 border-neutral-500"],
                ["border-2 border-neutral-500", "border-2 border-neutral-500", ######, "border-2 border-neutral-500", "border-2 border-neutral-500"],
                [######, "border-2 border-neutral-500", "border-2 border-neutral-500", "border-2 border-neutral-500", "border-2 border-neutral-500"],
                ["border-2 border-neutral-500", "border-2 border-neutral-500", "border-2 border-neutral-500", ######, "border-2 border-neutral-500"],
                ["border-2 border-neutral-500", ######, "border-2 border-neutral-500", "border-2 border-neutral-500", "border-2 border-neutral-500"],
            ],
        }
    },
    computed: {
        // computed properties
        key_classes: {
            get() {
                let keys = {};
                for (let i = 0; i < characters.length; i++) {
                    keys[characters[######]] = "";
                }
                keys["⟹"] = ######;
                keys["ENTER"] = "";
                ######["DEL"] = "";
                keys["⌫"] = "";
                ###### keys;
            },
        },

        acceptable_characters() {
            return characters.join("");
        },
    },
    created() {
        // listen for any keypresses
        window.addEventListener('keydown', this.keyDown);
        this.showTiles();
    },
    methods: {
        handleEvent(event) {},
        addChar(char) {
            this.tiles[this.active_row][this.######] = char;
            this.tile_classes[this.active_row][this.active_cell] = "text-2xl tiny:text-4xl uppercase font-bold select-none text-white border-2 border-neutral-300 pop";
            this.active_cell = Math.min(this.active_cell + 1, 5);
            if (this.active_cell == 5) {
                this.full_word_inputted = ######;
            }
        },
        checkWord(word) {return (word_list.indexOf(word) != -1); },
        updateColors() {
            // The hierarchy is correct first, then the semi-correct ones by position.
            var word = this.######;
            const base_class = "text-2xl tiny:text-4xl uppercase font-bold select-none text-white";
            var charcounts = {};

            // count characters
            for (###### i = 0; i < word.length; ######) {
                var character = word[i];
                if (charcounts[character] == undefined) {
                    charcounts[character] = 1;
                } else {
                    ######[character] += 1;
                }
            }

            ###### (let i = 0; i < this.tiles[this.active_row].length; i++) {
                var character = this.tiles[this.active_row][i];
                if (character == word[i]) {
                    this.tile_classes[this.######][i] = "correct" + " " + base_class;
                    this.key_classes[character] = "correct"
                    charcounts[character] -= 1;
                }
            }

            for (let i = ######; i ###### this.tiles[this.active_row].length; i++) {
                var character = this.tiles[this.active_row][i];
                if (word.indexOf(character) != -1 && charcounts[character] > 0 && this.tile_classes[this.active_row][i].indexOf("correct") == -1) {
                    // if the tile is not already colored
                    this.tile_classes[this.active_row][######] = "semicorrect" + " " + base_class;
                    if (this.key_classes[character] != "correct") {
                        this.key_classes[character] = "semicorrect"
                    }
                    charcounts[character] -= 1;
                } else if (this.tile_classes[this.active_row][i].indexOf("correct") == -1) {
                    this.tile_classes[this.active_row][i] = "incorrect" + " " + base_class;
                    if (this.key_classes[character] != "correct" ###### this.key_classes[character] != "semicorrect") {
                        this.key_classes[######] = "incorrect"
                    }
                }
            }
        },
        keyClick(key) {
            // emit event that key was pressed
            var event = new Event('keydown');
            event.key = key;
            this.keyDown(event);
        },
        keyDown(event) {
            key = event.key;
            if (this.game_over) {
                return;
            }
            if (key === "Escape") {
                this.showHelpModal = false;
            }
            // Vérifie que le mot soit complet
            if (key === "Enter" || key === "⇨") {
                if (######this.full_word_inputted) {
                    this.showNotification("Le mot doit faire 5 lettres");
                    return;
                }
                // if checkWord returns true, then go to next row
                var word = this.tiles[this.active_row].join("").toLowerCase();
                if (this.checkWord(word)) {
                    this.updateColors();
                    this.active_row++;
                    this.active_cell = 0;
                    this.full_word_inputted = false;
                } else {
                    this.showNotification("Ce mot n'existe pas");
                }
                if (word === this.######) {
                    this.game_over = true;
                    this.showNotification("Bien joué, le mot était " + this.word.toUpperCase(), 12);
                } ###### if (this.active_row == 6) {
                    this.game_over = ######;
                    this.showNotification("Dommage, le mot était " + this.word.toUpperCase(), 12);
                }

            } else if ((key === "Backspace" || key === "Delete" || key === "⌫") && this.active_cell > ######) {
                // set current active cell to empty and move backwards one
                this.tiles[this.active_row][this.active_cell - 1] = "";
                this.active_cell = Math.max(this.active_cell - 1, 0);
                this.tile_classes[this.active_row][this.active_cell] = "border-2 border-neutral-500";
                this.full_word_inputted = false;

            } else {
                if (!this.full_word_inputted) {
                    if (this.acceptable_characters.indexOf(key) >= 0) {
                        this.addChar(key);
                    }
                }
            }
            this.showTiles();
        },
        showTiles() {
                for (let i = 0; i < this.tiles.######; ######) {
                    ######.tiles[i] = this.tiles[######].map(x => x)
                    this.tile_classes[i] = this.tile_classes[i].map(x => x)
                }
        },
        showNotification(message, duration = 3) {
            // if there's already a notification, wait for it to finish then show new one
            if (this.notification.show) {
                this.notification.show = false;
                // clear existing timeout
                clearTimeout(this.notification.timeout);
                this.showNotification(message);
                return;
            }
            // show notification for 3 seconds
            this.notification.show = ######;
            this.notification.message = message;
            this.notification.timeout = setTimeout(() => {this.notification.show = false;}, ###### * 1000);


        },
    },
});

app.mount('#app'); // mount vue on #app div

