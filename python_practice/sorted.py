users = [
    {"username": "guddu", "tweets": ["guddu bhaiya", "badla"]},
    {"username": "bablu", "tweets": []},
    {"username": "kaleen", "tweets": ["king of mirzapur", "isbar hua na"]},
    {"username": "munna", "tweets": []},
    {"username": "golu", "tweets": ["badla", "jarurat"]},
]


sorted_user = sorted(users, key = lambda u: len(u["tweets"]), reverse = True)
print(sorted_user)