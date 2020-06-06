from typing import List
import requests

AUTH_TOKEN = ''
API_VERSION = '5.107'
UNCHANGED_REQUIRED_PARAMETERS = '?access_token={0}&v={1}'.format(AUTH_TOKEN, API_VERSION)
API_URL = 'https://api.vk.com/method/{}' + UNCHANGED_REQUIRED_PARAMETERS


class User:

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id
        user_data = requests.get(API_URL.format('users.get')).json()['response'][0]
        self.first_name = user_data['first_name']
        self.second_name = user_data['last_name']
        self.own_link = 'https://vk.com/id{}'.format(self.user_id)

    def __and__(self, user: "User") -> List["User"]:
        parameters = {
            "target_uid": user.user_id
        }
        common_friends_ids = requests.get(API_URL.format('friends.getMutual'), params=parameters).json()['response']
        common_friends = []
        for id in common_friends_ids:
            common_friends.append(User(id))
        return common_friends

    def __str__(self) -> str:
        return self.own_link


if __name__ == '__main__':
    user1 = User(40297500)
    user2 = User(571404144)
    common_friends = user1 & user2
    for friend in common_friends:
        print(friend)
