from typing import List
import requests

auth_token = ''


# https://api.vk.com/method/users.get?user_ids=210700286&fields=bdate&access_token=533bacf01e11f55b536a565b57531ac114461ae8736d6506a3&v=5.107
class User:
    API_URL = 'https://api.vk.com/method/{0}?access_token={1}&v=5.107'

    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        user_data = requests.get(self.API_URL.format('users.get', auth_token)).json()['response'][0]
        self.first_name = user_data['first_name']
        self.second_name = user_data['second_name']
        self.own_link = 'https://vk.com/id{}'.format(self.user_id)

    def __and__(self, user: "User") -> List["User"]:
        common_friends_ids = requests.get(self.API_URL.format('friends.getMutual', auth_token)).json()
        common_friends = []
        for id in common_friends_ids:
            common_friends.append(User(id))
        return common_friends

    def __str__(self) -> str:
        return self.own_link


if __name__ == '__main__':
    pass
