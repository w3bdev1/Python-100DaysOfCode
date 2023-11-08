class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.following = 0
        self.followers = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("007", "James Bond")
user_2 = User("045", "John Doe")
user_2.follow(user_1)

print(f"{user_1.username} has {user_1.followers} follower(s).")
print(f"{user_2.username} is following {user_2.following} person(s).")
