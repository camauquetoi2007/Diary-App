import os

def init_db():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists("data/users.csv"):
        with open("data/users.csv", "w", encoding="utf-8") as f:
            f.write("username,password\n")

    if not os.path.exists("data/diary.csv"):
        with open("data/diary.csv", "w", encoding="utf-8") as f:
            f.write("username,date,title,content\n")