#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import os

SAVE_DIR = "data/saves/"
os.makedirs(SAVE_DIR, exist_ok=True)

def load_game(filename: str = "save1.csv") -> dict:
    filepath = os.path.join(SAVE_DIR, filename)
    try:
        with open(filepath, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                code = list(map(int, row["code"].split(",")))
                guesses = [list(map(int, g.split("."))) for g in row["guesses"].split(";") if g]
                max_attempts = int(row["max_attempts"])
                print(f"Loaded the game from: {filename}")
                return {"code": code, "guesses": guesses, "max_attempts": max_attempts}
    except FileNotFoundError:
        print("File not found")
        return {}

def save_game(state: dict, filename: str = "save1.csv"):
    os.makedirs(SAVE_DIR, exist_ok=True)
    filepath = os.path.join(SAVE_DIR,filename)
    with open(filepath, mode="w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["code","guesses","max_attempts"])
        writer.writerow([
            ",".join(map(str,state.get("code",[]))),
            ";".join([".".join(map(str,guess)) for guess in state.get("guesses",[])]),
            state.get("max_attempts",0)
        ])
    print(f"Game saved to: {format(filepath)}")

def list_saves():
    if not os.path.exists(SAVE_DIR):
        return []
    return [f for f in os.listdir(SAVE_DIR) if f.endswith(".csv")]

def delete_save(filename: str):
    filepath = os.path.join(SAVE_DIR, filename)
    try:
        os.remove(filepath)
        print(f"Plik {filename} został usunięty.")
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {filename}")
    except Exception as e:
        print(f"Błąd podczas usuwania pliku: {e}")


def generate_new_save_filename() -> str:
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    existing = list_saves()
    numbers = [
        int(f[4:-4]) for f in existing
        if f.startswith("save") and f.endswith(".csv") and f[4:-4].isdigit()
    ]
    next_number = max(numbers) + 1 if numbers else 1
    return f"save{next_number}.csv"

