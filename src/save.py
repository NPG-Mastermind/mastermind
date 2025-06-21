import csv
import os

SAVE_DIR = "../data/saves/"
os.makedirs(SAVE_DIR, exist_ok=True)

def load_game(filename: str = "save1.csv") -> dict:
    filepath = os.path.join(SAVE_DIR, filename)
    try:
        with open(filepath, mode="r", newline="") as file:
            reader = csv.DictReader(file)
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
    with open(filepath, mode="w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["code","guesses","max_attempts"])
        writer.writerow([
            ",".join(map(str,state.get("code",[]))),
            ",".join([".".join(map(str,guess)) for guess in state.get("guesses",[])]),
            state.get("max_attempts",5)
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
    except Exception as err:
        print(f"Błąd podczas usuwania pliku: {err}")


def generate_new_save_filename() -> str:
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    existing = list_saves()
    numbers = [
        int(file_name[4:-4]) for file_name in existing
        if file_name.startswith("save") and file_name.endswith(".csv") and file_name[4:-4].isdigit()
    ]
    next_number = max(numbers) + 1 if numbers else 1
    return f"save{next_number}.csv"

