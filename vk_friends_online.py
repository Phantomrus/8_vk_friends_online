import vk
from getpass import getpass

APP_ID = 5834484


def get_user_login():
    return input("Please enter login: ")


def get_user_password():
    return getpass("Please enter password: ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends' # Тут вопрос
    )
    api = vk.API(session)
    friends_online_id = api.friends.getOnline()
    friends_online_list = api.users.get(user_ids=friends_online_id)

    return friends_online_list


def output_friends_to_console(friends_online_list):
    print("Online now:")
    for num, friend in enumerate(friends_online_list, start=1):
            print('%s \t %s %s' % (num, friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)