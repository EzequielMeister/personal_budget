import json
import os

def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    # Si no existe, inicializa estructura
    return {"incomes": [], "expenses": []}

def save_data(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)
