import unittest
import os
import csv
from src.stats import *
from unittest.mock import patch

class TestStatistics(unittest.TestCase):

    def setUp(self):
        # Usuń plik statystyk przed każdym testem
        if os.path.exists(STATS_FILE):
            os.remove(STATS_FILE)

    def tearDown(self):
        # Usuń plik statystyk po każdym teście
        if os.path.exists(STATS_FILE):
            os.remove(STATS_FILE)

    def test_load_stats_no_file(self):
        stats = load_stats()
        self.assertEqual(stats['games_played'], 0)
        self.assertEqual(stats['games_won'], 0)
        self.assertEqual(stats['total_guesses'], 0)
        self.assertEqual(stats['average_guesses'], 0.0)

    def test_save_and_load_stats(self):
        test_data = {
            'games_played': 5,
            'games_won': 3,
            'total_guesses': 20,
            'average_guesses': 4.0
        }
        save_stats(test_data)
        loaded_data = load_stats()
        self.assertEqual(loaded_data, test_data)

    def test_update_stats_win(self):
        update_stats(True, 5)
        stats = load_stats()
        self.assertEqual(stats['games_played'], 1)
        self.assertEqual(stats['games_won'], 1)
        self.assertEqual(stats['total_guesses'], 5)
        self.assertEqual(stats['average_guesses'], 5.0)

    def test_update_stats_loss(self):
        update_stats(False, 5)
        stats = load_stats()
        self.assertEqual(stats['games_played'], 1)
        self.assertEqual(stats['games_won'], 0)
        self.assertEqual(stats['total_guesses'], 5)
        self.assertEqual(stats['average_guesses'], 5.0)

    def test_multiple_updates(self):
        update_stats(True, 3)
        update_stats(False, 5)
        update_stats(True, 4)
        stats = load_stats()
        self.assertEqual(stats['games_played'], 3)
        self.assertEqual(stats['games_won'], 2)
        self.assertEqual(stats['total_guesses'], 12)
        self.assertAlmostEqual(stats['average_guesses'], 4.0)

    @patch('builtins.print')
    def test_show_stats(self, mock_print):
        update_stats(True, 3)
        show_stats()
        self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()
