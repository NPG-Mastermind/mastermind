#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import os

STATS_FILE = "data/stats.csv"

def load_stats():
    default_stats = {
        "games_played": 0,
        "games_won": 0,
        "total_guesses": 0,
        "average_guesses": 0.0
    }
    if not os.path.exists(STATS_FILE):
        return default_stats
    try:
        with open(STATS_FILE, mode="r", newline="") as plik:
            reader = csv.DictReader(plik)
            for row in reader:
                return {
                    "games_played": int(row["games_played"]),
                    "games_won": int(row["games_won"]),
                    "total_guesses": int(row["total_guesses"]),
                    "average_guesses": float(row["average_guesses"]),
                }
    except (FileNotFoundError, KeyError, ValueError):
        return default_stats


def save_stats():
    pass


def update_stats():
    pass


def show_stats():
    data = load_stats()
    print("|==================STATS==================|")
    print(f"Rozegrane gry: {data['games_played']}")
    print(f"Wygrane gry: {data['games_won']}")
    print(f"Średnia liczba prób: {data['average_guesses']}")
    print(f"Próby ogólnie: {data['total_guesses']}")
    print("\==================STATS==================|")

