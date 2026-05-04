import csv
import os

FILE = os.path.join("data", "users.csv")


def add_user(username, password):
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([username, password])


def get_all_users():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            return list(reader)
    except:
        return []