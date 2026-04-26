import flet as ft
from utils.db_init import init_db
from views.login_view import login_view
from views.diary_view import diary_view
from views.write_view import write_view


def main(page: ft.Page):
    page.title = "Diary App"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212"

    init_db()

    def go_login():
        login_view(page, go_diary)

    def go_diary(username):
        diary_view(page, username, go_write, go_login)

    def go_write(username):
        write_view(page, username, go_diary)

    go_login()


ft.app(target=main)