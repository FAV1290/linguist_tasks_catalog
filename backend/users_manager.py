from werkzeug.security import check_password_hash


from db.models import User


def check_user_password(target_user: User | None, password: str | None) -> bool:
    if not target_user or not password:
        return False
    return check_password_hash(target_user.password, str(password))
