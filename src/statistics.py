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


def save_stats(data):
    os.makedirs(os.path.dirname(STATS_FILE), exist_ok=True)
    with open(STATS_FILE, mode="w", newline="") as plik:
        writer = csv.writer(plik)
        writer.writerow(["games_played", "games_won", "total_guesses", "average_guesses"])
        writer.writerow([data["games_played"], data["games_won"], data["total_guesses"],])


def update_stats(won,guess_count):
    data=load_stats()
    data["total_guesses"]=data["total_guesses"]+guess_count
    data["games_played"]+=1
    if won:#sprawdza czy jest wygrana, TRUE OR FALSE
        data["games_won"]+=1
    if data["games_played"]>0:
        data["average_guesses"]=data["average_guesses"]/data["games_played"]
    else:
        data["average_guesses"]=0.0
    save_stats(data)


def show_stats():
    data = load_stats()
    print("|==================STATS==================|")
    print(f"Rozegrane gry: {data['games_played']}")
    print(f"Wygrane gry: {data['games_won']}")
    print(f"Średnia liczba prób: {data['average_guesses']}")
    print(f"Próby ogólnie: {data['total_guesses']}")
    print("|==================STATS==================|")