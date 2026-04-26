from models.diary_model import get_user_diary, delete_diaries, filter_diaries


def load_diaries(username):
    return get_user_diary(username)


def filter_data(diaries, search_text, date_from, date_to):
    return filter_diaries(diaries, search_text, date_from, date_to)


def delete_selected(username, selected):
    delete_diaries(username, selected)