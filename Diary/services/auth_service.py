from models.user_model import add_user, get_all_users


def signup_user(username, password):
    if not username or not password:
        return "Vui lòng nhập đủ thông tin"

    elif len(username) < 6:
        return "Tên tài khoản phải có ít nhất 6 ký tự"

    elif username[0].isdigit():
        return "Tên tài khoản không được bắt đầu bằng số"

    else:
        pass

    for u in get_all_users():
        if u[0] == username:
            return "Tên tài khoản đã tồn tại. Vui lòng sử dụng tên khác."

    add_user(username, password)
    return "Đã đăng kí thành công"


def login_user(username, password):
    for u in get_all_users():
        if u[0] == username and u[1] == password:
            return "success"

    return "fail"