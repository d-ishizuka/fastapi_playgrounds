from typing import Optional

class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

user_list = [
    User(id=1, name="user1"),
    User(id=2, name="user2"),
    User(id=3, name="user3")
]

def get_user(user_id: int) -> Optional[User]:
    for user in user_list:
        if user.id == user_id:
            return user
    return None