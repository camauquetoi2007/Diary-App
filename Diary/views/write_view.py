import flet as ft
from datetime import datetime
from models.diary_model import add_diary


def write_view(page, username, go_diary):
    page.controls.clear()
    page.bgcolor = "#0f1c2e"

    now = datetime.now().strftime("%d-%m-%Y")

    title_input = ft.TextField(
        hint_text="Tiêu đề",
        text_size=24,
        color="white"
    )

    content_input = ft.TextField(
        hint_text="Viết nội dung...",
        multiline=True,
        expand=True,
        text_size=16,
        color="#cccccc"
    )

    def save(e):
        add_diary(username, now, title_input.value, content_input.value)
        go_diary(username)

    def back(e):
        go_diary(username)

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.TextButton("< Quay lại", on_click=back),
                    ft.Container(expand=True),
                    ft.ElevatedButton("LƯU", on_click=save)
                ]),
                ft.Text(now, size=30, color="white"),
                title_input,
                content_input,
            ]),
            padding=20,
            expand=True
        )
    )