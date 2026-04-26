import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE = os.path.join(BASE_DIR, "data", "diary.csv")


def init_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["username", "date", "title", "content"])


init_file()


def add_diary(username, date, title, content):
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([username, date, title, content])


def get_user_diary(username):
    result = []

    with open(FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for r in reader:
            if r[0] == username:
                result.append(r)

    return result


def delete_diaries(username, selected):
    rows = []

    with open(FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)

        for r in reader:
            key = (r[1], r[2], r[3])

            if r[0] == username and key in selected:
                continue

            rows.append(r)

    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def filter_diaries(diaries, search_text, date_from, date_to):
    from datetime import datetime

    def parse(d):
        try:
            return datetime.strptime(d, "%d-%m-%Y")
        except:
            return None

    result = []

    for d in diaries:
        date = parse(d[1])
        title = d[2].lower()

        match_title = True
        if search_text:
            match_title = search_text.lower() in title

        match_date = True
        if date:
            if date_from:
                match_date &= date >= parse(date_from)
            if date_to:
                match_date &= date <= parse(date_to)

        if match_title and match_date:
            result.append(d)

    return result