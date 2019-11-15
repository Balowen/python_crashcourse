class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("User: " + self.first_name.title() + " " + self.last_name.title())

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Bart", "Nawoj")
user2 = User("Kam", "King")

user1.describe_user()
user2.greet_user()

for value in range(1, 11):
    user1.increment_login_attempts()

user1.describe_user()
print("Attempted " + str(user1.login_attempts) + " login attempts.")