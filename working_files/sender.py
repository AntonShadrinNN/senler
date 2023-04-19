from vk_api import VkUpload
from vk_api.exceptions import ApiError
from warnings import warn
import functools


def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception:
                pass
    return wrapper


@retry
def send(session, user_id: str, message: str, *args, img=None):
    vk = session.get_api()
    if img:
        upload = VkUpload(vk)
        photo = upload.photo_messages(img)
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        img = f'photo{owner_id}_{photo_id}_{access_key}'
    try:
        vk.messages.send(
            user_id=user_id,
            message=message,
            random_id='0',
            attachment=img,
        )
    except ApiError:
        warn(f'\n\nПользователю {args[0]} нельзя отправить сообщение!\nВероятно переписка с ним отсутствует')

