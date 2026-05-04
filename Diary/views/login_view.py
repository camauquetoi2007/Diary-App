import flet as ft
from services.auth_service import signup_user, login_user


def login_view(page, go_diary):
    page.controls.clear()
    page.bgcolor = "#121212"

    title = ft.Text("Đăng nhập / Đăng ký", size=36, weight="bold", color="white")

    username = ft.TextField(
        label="Username",
        width=500,
        bgcolor="#1e1e1e",
        color="white"
    )

    password = ft.TextField(
        label="Password",
        password=True,
        width=500,
        bgcolor="#1e1e1e",
        color="white"
    )

    result = ft.Text(color="red")

    def handle_signup(e):
        result.value = signup_user(username.value, password.value)
        page.update()

    def handle_login(e):
        if login_user(username.value, password.value) == "success":
            go_diary(username.value)
        else:
            result.value = "Sai tài khoản hoặc mật khẩu"
            page.update()

    page.add(
        ft.Container(
            content=ft.Column([
                title,
                username,
                password,
                ft.Row([
                    ft.ElevatedButton("Login", on_click=handle_login),
                    ft.OutlinedButton("Sign up", on_click=handle_signup),
                ], alignment="center"),
                result
            ], horizontal_alignment="center"),
            expand=True,
            padding=50,
            alignment=ft.alignment.Alignment(0, 0),
            bgcolor="#1e1e1e"
        )
    )