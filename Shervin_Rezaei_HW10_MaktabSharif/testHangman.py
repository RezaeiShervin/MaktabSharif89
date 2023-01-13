import unittest
import Hangman


class NetworkError(Exception):
    pass


class TestHangman(unittest.TestCase):

    def setUp(self) -> None:
        self.Bank = Hangman.Bank()
        self.Player = Hangman.Player()
        self.Processes = Hangman.Processes()

    def test_pick_topic(self):
        self.Bank.pick_topic()
        self.assertIn(self.Bank.current_topic, Hangman.Bank.topic_names)

    def test_get_word(self):
        try:
            self.Bank.get_word()
        except Exception:
            print("(I need Internet Connection)")
        if not self.Bank.api_response_status:
            pass
        else:
            self.assertIsNotNone(self.Bank.current_word)

    def test_pick_word(self):
        self.Bank.pick_topic()
        self.Bank.pick_word()
        words = ['red', 'blue', 'cat', 'dog']
        self.assertIn(self.Bank.current_word, words)

    def test_display_maker(self):
        self.Bank.current_word = 'king'
        display = ["_", "_", "_", "_"]
        # display for "king"
        self.Bank.display_maker()
        self.assertEqual(self.Bank.current_word_display, display)

    def test_check_answer_update_lives(self):
        self.Bank.current_word = 'monkey'
        self.Bank.current_word_display = ['m', '_', 'n', 'k', 'e', 'y']
        self.Player.lives = 18
        self.Bank.letters_already_guessed = ['m', 'n', 'k', 'e', 'y']
        self.Bank.letters_guessed_counter = 5
        self.Player.guess('o')
        self.Processes.check_answer_update_lives(self.Bank, self.Player)
        self.Bank.check_solve()
        self.assertEqual(False, self.Bank.not_solved)
        self.assertEqual(['m', 'o', 'n', 'k', 'e', 'y'], self.Bank.current_word_display)
        self.assertEqual(self.Player.lives, 18)

    def test_check_lost_lives(self):
        self.Bank.current_word = 'love'
        self.Bank.current_word_display = ['_', '_', '_', 'e']
        self.Player.lives = 1
        self.Bank.letters_already_guessed = ['e', 'a', 'g', 'h', 'k', 'b', 'q', 'c', 'x', 'z', 't']
        self.Bank.letters_guessed_counter = 11
        self.Player.guess('m')
        self.Processes.check_answer_update_lives(self.Bank, self.Player)
        self.Bank.check_solve()
        self.assertEqual(self.Bank.not_solved, True)
        self.assertEqual(self.Player.lives, 0)

    def test_validate_user_input(self):
        self.Bank.current_word = 'monkey'
        self.Bank.current_word_display = ['m', '_', 'n', 'k', 'e', 'y']
        self.Player.lives = 18
        self.Bank.letters_already_guessed = ['m', 'n', 'k', 'e', 'y']
        self.Bank.letters_guessed_counter = 5
        self.Player.guess('sdfjh')
        self.assertEqual(None, self.Processes.validate_user_input(self.Player))