import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
friend_random = random.choice(friends)
print(friend_random)

friend_random_index = random.randint(0,4)
print(friends[friend_random_index])
