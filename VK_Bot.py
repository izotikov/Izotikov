import vk_api
import datetime
from time import sleep
from random import choice

limit = datetime.timedelta(seconds=1)


def getLatestPosts(groupsIds: list):
    comma = []
    for id in groupsIds:
        com = ['API.wall.get({', '})']
        com.insert(1, f'"owner_id": -{id}, "count": 2')
        comma.append(''.join(com))

    if len(groupsIds) != 1:
        code = 'return {};'.format(', '.join(comma))
    else:
        code = 'return {};'.format(comma)
    latestPosts = []
    for group in api.execute(code=code.replace("'", '')):
        try:
            group['items'][0]['is_pinned']
            postIndex = 1
        except KeyError:
            postIndex = 0

        post = group['items'][postIndex]
        latestPosts.append((post['owner_id'], post['id'], post['date']))
    return latestPosts

def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device

def main(groupsIds: list):
    while True:
        for owner_id, post_id, unix_date in getLatestPosts(groupsIds):
            delta = (datetime.datetime.utcnow() - (datetime.datetime.utcfromtimestamp(unix_date)))
            if delta <= limit:
                api.wall.createComment(owner_id=owner_id,
                                       post_id=post_id,
                                       message=choice(messages).strip())
                api.wall.closeComments(owner_id=owner_id,
                                       post_id=post_id)
                print('[INFO] Бот ответил на пост {} в паблике {}'.format(post_id, -owner_id))
        sleep(1)


if __name__ == "__main__":
    print('\tby shakeless\nЕсли вы уже успешно заходили в аккаунт, можете ввести только логин')
    groups = input('Введите ид групп через пробел(Пример: 195007647 195007647...): ').split()
    messages = input(
        'Введите сообщения через запятые (Пример: всем привет, спам, как дела?): ').split(
        ',')
    login = input('Введите логин:  ')
    password = input('Введите пароль: ')
    try:
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth(token_only=True)
    except vk_api.exceptions.BadPassword as error:
        while True:
            print('Неправильный пароль, попробуйте ещё раз')
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            vk_session = vk_api.VkApi(
                login, password,
                # функция для обработки двухфакторной аутентификации
                auth_handler=auth_handler
            )

            try:
                vk_session.auth()
            except vk_api.AuthError as error_msg:
                print(error_msg)
            try:
                vk_session = vk_api.VkApi(login, password)
                vk_session.auth(token_only=True)
                break
            except vk_api.exceptions.BadPassword:
                pass
    api = vk_session.get_api()
    print(
        'Успешный запуск, чтобы остановить работу программы нажмите Ctrl + C или закройте консоль')
    main(groups)