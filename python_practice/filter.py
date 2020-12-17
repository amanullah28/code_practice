users = [
    {"username": "guddu", "tweets": ["guddu bhaiya", "badla"]},
    {"username": "bablu", "tweets": []},
    {"username": "kaleen", "tweets": ["king of mirzapur", "isbar hua na"]},
    {"username": "munna", "tweets": []},
    {"username": "golu", "tweets": ["badla", "jarurat"]},
]

inactive_user = list(map(lambda user: user["username"].upper(),filter(lambda u: not u["tweets"], users)))
# print(inactive_user)

# using list comprehension
inactive_user2 = [user for user in users if not user["tweets"]]
# print(inactive_user2)

# using list comprehension with map
active_users = [user["username"].upper() for user in users if user["tweets"]]
print(active_users)