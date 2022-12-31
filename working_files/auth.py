from vk_api import VkApi, AuthError


# Для авторизации на личной странице
def auth_handler() -> tuple:

    key = input("Введите код авторизации: ")
    remember_device = True

    return key, remember_device


def auth(login: str, password: str):
    session = VkApi(login, password, auth_handler=auth_handler)
    try:
        session.auth()
    except AuthError as err:
        print(err)
        return

    return session


# Для авторизации в группе
def auth_public():
    session = VkApi(
        # токен для API группы
        token='#')

    return session
