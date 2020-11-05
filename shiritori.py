class Shiritori(object):

    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, next_word: str):

        if self.game_over:
            return "game over"

        if next_word in self.words:
            self.game_over = True
            return "game over"

        next_word_first_character = next_word[0]
        if len(self.words) == 0:
            self.words.append(next_word)
            return self.words
        else:
            last_word_last_character = self.words[len(self.words) - 1][-1]
        if next_word_first_character == last_word_last_character:
            self.words.append(next_word)
            return self.words
        else:
            self.game_over = True
            return "game_over"

    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"


if __name__ == '__main__':
    sh = Shiritori()
    sh.play("word")
    sh.play("dowry")
    sh.play("yodel")
    sh.play("leader")
    sh.play("righteous")
    sh.play("serpent")
    if sh.game_over:
        print("invalid")
    else:
        print("valid")

    sh.restart()
    sh.play("motive")
    sh.play("beach")
    if sh.game_over:
        print("invalid")
    else:
        print("valid")

    sh.restart()
    sh.play("hive")
    sh.play("eh")
    sh.play("hive")
    if sh.game_over:
        print("invalid")
    else:
        print("valid")
