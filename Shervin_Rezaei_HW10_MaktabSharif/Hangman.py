from random import choice
import re
import requests
import json


class Bank:
    colours = ['red', 'blue']
    animals = ['dog', 'cat']
    topic_names = ['Colours', 'Animals']
    topics = {'Colours': colours, 'Animals': animals}
    api = 'https://api.api-ninjas.com/v1/randomword'
    api_key = 'FRkfTIwrgLLk+4TIMd+NMA==m6isKOfXzCLPgdGz'

    def __init__(self):
        self.current_topic = ''
        self.current_word = ''
        self.current_word_display = []
        self.letters_guessed_counter = 0
        self.not_solved = True
        self.letters_already_guessed = []
        self.api_response_status = False

    def pick_topic(self) -> None:
        self.current_topic = choice(self.topic_names)

    def get_word(self) -> None:
        response = requests.get(f"{self.api}", headers={'X-Api-Key': f"{self.api_key}"}, params={type: 'noun'})
        if response.status_code == 200:
            word = json.loads(response.text)
            self.api_response_status = True
            self.current_word = word['word'].lower()

    def pick_word(self) -> None:
        self.current_word = choice(self.topics[self.current_topic])

    # this method is to access the current_word_display easier
    def display_maker(self) -> None:
        for i in range(len(self.current_word)):
            self.current_word_display.append('_')

    def check_solve(self):
        self.not_solved = "_" in self.current_word_display


class Player:
    def __init__(self):
        self.lives = 0
        self.answer = ''
        self.guess_validation_incomplete = True

    def guess(self, guess_input: str) -> None:
        self.answer = guess_input


class Processes:
    def __init__(self):
        pass

    @staticmethod
    def validate_user_input(player: Player):
        expression = re.match('(?i)[a-z]', player.answer)
        player.answer = player.answer.lower()
        if expression is None or len(player.answer) > 1:
            return None
        else:
            player.guess_validation_incomplete = False
            return True

    @staticmethod
    def check_answer_update_lives(bank: Bank, player: Player) -> str:
        if player.answer in bank.letters_already_guessed:
            return "repeated"

        elif player.answer not in bank.current_word:
            player.lives -= 1
            bank.letters_already_guessed.append(player.answer)
            return "False"

        else:
            for i in range(len(bank.current_word)):
                if player.answer == bank.current_word[i]:
                    bank.current_word_display[i] = player.answer
                    bank.letters_guessed_counter += 1
                    bank.letters_already_guessed.append(player.answer)
            return "True"


class Main:
    def __init__(self):
        self.word_bank = Bank()
        self.player = Player()
        self.game = Processes()

    def set_word(self):
        try:
            self.word_bank.get_word()
        except requests.exceptions.RequestException as e:
            print(f"there was an error: {e}")

        if not self.word_bank.api_response_status:
            self.word_bank.pick_topic()
            print(f'Topic: {self.word_bank.current_topic}')
            self.word_bank.pick_word()
        print(f'Word is {len(self.word_bank.current_word)} letters long.')
        self.word_bank.display_maker()
        print(self.word_bank.current_word_display)

    def set_player_lives(self):
        self.player.lives = len(self.word_bank.current_word) * 3

    def check_win(self):
        if not self.word_bank.not_solved:
            print('\nYou win!')

        else:
            print('\nYou lose')
            print('Word was {}'.format(self.word_bank.current_word))

    def run(self):
        self.set_word()
        self.set_player_lives()
        while self.word_bank.not_solved and self.player.lives > 0:
            while self.player.guess_validation_incomplete:
                self.player.guess(input('Guess a letter: '))
                if self.game.validate_user_input(self.player) is None:
                    print('\nPlease guess a single alphabet')
            info = self.game.check_answer_update_lives(self.word_bank, self.player)
            if info == "repeated":
                print('\nLetter already guessed.')
            elif info == "False":
                print('\nNope!')
            elif info == "True":
                print('\nNice!')
            print('Lives remaining: {}'.format(self.player.lives))
            print(self.word_bank.current_word_display)
            self.player.guess_validation_incomplete = True
            self.word_bank.check_solve()

        self.check_win()
pl = Main()

