from models.auth import User


def get_user_by_email(email):
    user = User.objects.get(email=email)
    return user


def maybe_get_user_by_email(email):
    try:
        return get_user_by_email(email)
    except User.DoesNotExist:
        return None


def get_user(user_id):
    return User.objects.get(id=user_id)
