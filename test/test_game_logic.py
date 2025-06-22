import unittest
from unittest.mock import patch
from src.game_logic import *

class TestGameLogic(unittest.TestCase):

    def setUp(self):
        global LENGTH, COUNT
        LENGTH = 4
        COUNT = 6

    def test_GenerateCode(self):
        code = GenerateCode()
        self.assertEqual(len(code), LENGTH)
        self.assertTrue(all(c in NUMBERS[:COUNT] for c in code))

    def test_CheckGuess_perfect_match(self):
        secret = ['1', '2', '3', '4']
        guess = ['1', '2', '3', '4']
        black, white = CheckGuess(secret, guess)
        self.assertEqual(black, 4)
        self.assertEqual(white, 0)

    def test_CheckGuess_all_wrong(self):
        secret = ['1', '2', '3', '4']
        guess = ['5', '6', '5', '6']
        black, white = CheckGuess(secret, guess)
        self.assertEqual(black, 0)
        self.assertEqual(white, 0)

    def test_CheckGuess_some_correct(self):
        secret = ['1', '2', '3', '4']
        guess = ['1', '5', '3', '6']
        black, white = CheckGuess(secret, guess)
        self.assertEqual(black, 2)
        self.assertEqual(white, 0)

    def test_CheckGuess_white_pegs(self):
        secret = ['1', '2', '3', '4']
        guess = ['4', '3', '2', '1']
        black, white = CheckGuess(secret, guess)
        self.assertEqual(black, 0)
        self.assertEqual(white, 4)

    def test_CheckGuess_mixed(self):
        secret = ['1', '2', '3', '4']
        guess = ['1', '3', '2', '5']
        black, white = CheckGuess(secret, guess)
        self.assertEqual(black, 1)
        self.assertEqual(white, 2)

    def test_Validate_correct(self):
        guess = ['1', '2', '3', '4']
        self.assertTrue(Validate(guess))

    def test_Validate_wrong_length(self):
        guess = ['1', '2', '3']
        self.assertFalse(Validate(guess))

    def test_Validate_invalid_numbers(self):
        guess = ['1', '2', '9', '4']
        self.assertFalse(Validate(guess))

    @patch('builtins.input', side_effect=['4'])
    def test_SetLength_valid(self, mock_input):
        result = SetLength()
        self.assertEqual(result, 4)

    @patch('builtins.input', side_effect=['0', '7', 'abc', '3'])
    def test_SetLength_invalid_then_valid(self, mock_input):
        result = SetLength()
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=['6'])
    def test_NumberOfColors_valid_6(self, mock_input):
        result = NumberOfColors()
        self.assertEqual(result, 6)

    @patch('builtins.input', side_effect=['9', '8'])
    def test_NumberOfColors_invalid_then_valid(self, mock_input):
        result = NumberOfColors()
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()
