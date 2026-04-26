import flet as ft


def detail_view(page, username, diary, go_diary):
    page.controls.clear()
    page.bgcolor = "#121212"

    def back(e):
        go_diary(username)

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.TextButton("< Quay lại", on_click=back),
                    ft.Container(expand=True),
                ]),

                ft.Text(diary[1], size=14, color=ft.Colors.WHITE70),
                ft.Text(diary[2], size=28, weight="bold", color=ft.Colors.WHITE),
                ft.Divider(color="#333"),
                ft.Text(diary[3], size=16, color=ft.Colors.WHITE),
            ],
            spacing=10,
            expand=True,
            scroll=ft.ScrollMode.AUTO),
            padding=20,
            expand=True
        )
    )