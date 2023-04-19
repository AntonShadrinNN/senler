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
        # Flash
        token='vk1.a.JnsaR86Cl62h78PL9Jjf8f-Ybiz6zSFgciCk3idlqox9_iLN4hippHSkZOrSJM5rj8beoDufziMR5S5TuVbxn6zjn2qKeNkvErTKprdk7xxgsnRpaltgJS2LpofkZ1246fnIm9WdzgkJBeB_l3yIblZIQmhE9FAffD5_DqUMkghJObs73Y9cgxmrgw5gMrAp0Vo5IS4A4wS2Fa5q-VUM4Q'
        # Matrix
        # token='vk1.a.r7DmWlS0ca5KcfSsJsR5-lesMg6n5kY_eIblWH4CT6jmrXvi_nR6aNlfJBxcKHTKF1ljC9Q1KVNdlADu0ZniLzEY55gZyh-DJ0kWTXg1NZcXPK_vJWP5PavMG1GaBGwffh4US7HXbLSnwAZp-N30I3RzUs1D4JWNuFeyXhElpLgyM7J6V20BcgbiQnLm3rBhTrCHyiZMdYUZ_2xRDKGU5Q'
    )
    return session
