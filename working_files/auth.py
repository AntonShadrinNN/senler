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
        token='vk1.a.0H7P4WGxHF4gS8BGq9mRvycMxKFfrdZAdeTpcfdaWFzr2LPbQGvtgZaOwgrFx1kMkolBvBDGSWwf4bcs6ZNldu2d'
              'D0CrwwhWWoHbdADyHx3j0iTpeNkS_NLDoavrYDnnJLCpDewMn4IarNGNyehcloiHk2QEVXDpTeu3NJxkUD4CLfrOp-efD0D'
              'bG8ptnwRA1iCASg20LxQJfSjEUKQxIQ')

    return session
