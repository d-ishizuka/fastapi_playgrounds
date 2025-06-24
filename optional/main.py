from typing import Optional, Mapping

type Profile = dict[str, Optional[str | int]]

def get_profile(
    email: str,
    username: Optional[str] = None,
    age: Optional[int] = None
) -> Profile:
    profile: Profile = {}
    profile["email"] = email
    if username:
        profile["username"] = username
    if age:
        profile["age"] = age
    return profile

user_profile = get_profile(email="test@example.com")
print(user_profile)

complete_profile = get_profile(email="test@example.com", username="testuser", age=25)
print(complete_profile)