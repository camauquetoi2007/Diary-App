import flet as ft
from controllers.diary_controller import load_diaries, filter_data, delete_selected
from views.detail_view import detail_view
from datetime import timedelta


def diary_view(page, username, go_write, go_login):
    page.controls.clear()
    page.bgcolor = "#121212"

    select_mode = False
    selected_items = set()

    search_text = ""
    date_from = ""
    date_to = ""
    current_picker_type = None

    # ======================
    # HEADER (GIỮ NGUYÊN)
    # ======================
    title = ft.Text(
        f"Xin chào {username}",
        size=30,
        weight="bold",
        color="white"
    )

    subtitle = ft.Text(
        "Nhật ký của bạn",
        size=16,
        color="#aaaaaa"
    )

    # ======================
    # SEARCH (GIỮ NGUYÊN)
    # ======================
    def on_search(e):
        nonlocal search_text
        search_text = e.control.value.lower()
        render_list()

    search_field = ft.TextField(
        hint_text="Tìm theo tiêu đề...",
        on_change=on_search,
        bgcolor="#1e1e1e",
        color="white"
    )

    # ======================
    # DATE PICKER (GIỮ NGUYÊN)
    # ======================
    date_from_text = ft.Text("Từ ngày", color="#aaaaaa")
    date_to_text = ft.Text("Đến ngày", color="#aaaaaa")

    def set_date(t, v):
        nonlocal date_from, date_to

        if t == "from":
            date_from = v
            date_from_text.value = v
        else:
            date_to = v
            date_to_text.value = v

        page.update()
        render_list()

    def handle_date_change(e):
        nonlocal current_picker_type
        if e.control.value:
            d = e.control.value + timedelta(days=1)
            set_date(current_picker_type, d.strftime("%d-%m-%Y"))

    date_picker = ft.DatePicker(on_change=handle_date_change)
    page.overlay.append(date_picker)

    def open_picker(t):
        nonlocal current_picker_type
        current_picker_type = t
        date_picker.open = True
        page.update()

    date_from_box = ft.Container(
        content=date_from_text,
        padding=15,
        bgcolor="#1e1e1e",
        border_radius=10,
        width=200,
        alignment=ft.alignment.Alignment(0, 0),
        on_click=lambda e: open_picker("from")
    )

    date_to_box = ft.Container(
        content=date_to_text,
        padding=15,
        bgcolor="#1e1e1e",
        border_radius=10,
        width=200,
        alignment=ft.alignment.Alignment(0, 0),
        on_click=lambda e: open_picker("to")
    )

    # ======================
    # LISTVIEW (GIỮ NGUYÊN)
    # ======================
    diary_list = ft.ListView(expand=True, spacing=12, padding=20)

    # ======================
    # RENDER LIST (GIỮ UI CŨ 100%)
    # ======================
    def render_list():
        diary_list.controls.clear()

        diaries = load_diaries(username)
        filtered = filter_data(diaries, search_text, date_from, date_to)

        if not filtered:
            diary_list.controls.append(
                ft.Text("Không tìm thấy nhật ký", color="#888888")
            )
        else:
            for d in filtered:

                key = (d[1], d[2], d[3])
                selected = key in selected_items

                def toggle(e, d=d):
                    k = (d[1], d[2], d[3])

                    if k in selected_items:
                        selected_items.remove(k)
                    else:
                        selected_items.add(k)

                    render_list()
                    page.update()

                def open_detail(e, d=d):
                    if select_mode:
                        toggle(e, d)
                    else:
                        detail_view(page, username, d,
                            lambda u: diary_view(page, u, go_write, go_login)
                        )

                select_icon = ft.Container(
                    content=ft.Text("X" if selected else "O", color="white"),
                    width=30,
                    height=30,
                    alignment=ft.alignment.Alignment(0, 0),
                    bgcolor="#ff6b6b" if selected else "#555",
                    border_radius=15
                ) if select_mode else None

                # 🔥 GIỮ NGUYÊN CARD UI CŨ 100%
                diary_list.controls.append(
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text(str(d[1]), size=12, color="#aaaaaa"),
                                        ft.Text(str(d[2]), size=18, weight="bold", color="white"),
                                        ft.Text(
                                            str(d[3]),
                                            size=14,
                                            color="#cccccc",
                                            max_lines=2,
                                            overflow="ellipsis"
                                        )
                                    ],
                                    expand=True
                                ),
                                select_icon if select_mode else ft.Container()
                            ]
                        ),
                        padding=15,
                        width=500,
                        bgcolor="#1e1e1e",
                        border=ft.border.all(1, "#333"),
                        border_radius=12,
                        on_click=open_detail
                    )
                )

        page.update()

    render_list()

    # ======================
    # BUTTONS (GIỮ NGUYÊN VỊ TRÍ)
    # ======================
    def open_write(e):
        go_write(username)

    def logout(e):
        go_login()

    def toggle_delete_mode(e):
        nonlocal select_mode

        if select_mode:
            delete_selected(username, selected_items)
            selected_items.clear()
            diary_view(page, username, go_write, go_login)
        else:
            select_mode = True
            render_list()

    add_button = ft.Container(
        content=ft.Text("+", size=40, color="white"),
        width=80,
        height=80,
        bgcolor="#4dabf7",
        border_radius=40,
        alignment=ft.alignment.Alignment(0, 0),
        on_click=open_write
    )

    logout_button = ft.Container(
        content=ft.Text("⎋", size=30, color="white"),
        width=60,
        height=60,
        bgcolor="#ff6b6b",
        border_radius=30,
        alignment=ft.alignment.Alignment(0, 0),
        on_click=logout
    )

    delete_button = ft.Container(
        content=ft.Text("XÓA", color="white"),
        padding=10,
        bgcolor="#ff6b6b",
        border_radius=8,
        on_click=toggle_delete_mode
    )

    # ======================
    # LAYOUT (GIỮ NGUYÊN 100%)
    # ======================
    page.add(
        ft.Stack(
            [
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Row(
                                [title, ft.Container(expand=True), delete_button]
                            ),
                            padding=20
                        ),

                        ft.Container(
                            content=ft.Column([
                                search_field,
                                ft.Row([date_from_box, date_to_box])
                            ]),
                            padding=20
                        ),

                        ft.Container(
                            content=diary_list,
                            expand=True
                        )
                    ],
                    expand=True
                ),

                ft.Container(
                    content=add_button,
                    bottom=20,
                    left=0,
                    right=0,
                    alignment=ft.alignment.Alignment(0, 0)
                ),

                ft.Container(
                    content=logout_button,
                    bottom=20,
                    right=20
                )
            ],
            expand=True
        )
    )

    page.update()