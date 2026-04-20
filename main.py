import flet as ft
import csv
import os

FILE = "user.csv"

def main(page):
    title = ft.Text(
        "Đăng nhập / Đăng ký", 
        size = 24, 
        weight = "bold"
    )
    
    username = ft.TextField(
        label = "Username",
        password = False
    )

    password = ft.TextField(
        label = "Password",
        password = True
    )

    result = ft.Text()
    
    def login(e):
        result.value = "Đã đăng nhập thành công"
        page.update()

    login_button = ft.ElevatedButton(
        "Login",
        on_click = login
    )

    def signup(e):
        user = username.value
        pw = password.value
        
        if user == "" or pw == "":
            result.value = "Không được để trống"
            page.update()
            return
        
        with open(FILE, "a", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow([user, pw])


        result.value = "Đã đăng ký thành công"
        page.update()

    signup_button = ft.ElevatedButton(
        "Sign up",
        on_click = signup
    )

    button_row = ft.Row(
        controls = [login_button, signup_button]
    )
    
    page.add(
        title,
        username,
        password,
        button_row,
        result,
    )

ft.app(target=main)
print(os.getcwd())