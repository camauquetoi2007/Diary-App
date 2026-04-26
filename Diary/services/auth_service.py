from models.user_model import add_user, get_all_users


def signup_user(username, password):
    if not username or not password:
        return "empty"

    for u in get_all_users():
        if u[0] == username:
            return "exist"

    add_user(username, password)
    return "success"


def login_user(username, password):
    for u in get_all_users():
        if u[0] == username and u[1] == password:
            return "success"

    return "fail"