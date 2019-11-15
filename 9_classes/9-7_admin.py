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


class Admin(User):
    """attempt to model an administrator"""
    def __init__(self, first_name, last_name, *privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)


class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("The list of privileges are: " + str(self.privileges))


admin = Admin("Jozef", "Adminski", 'can add post', 'can delete post', 'can ban user')

admin.privileges.show_privileges()
admin.greet_user()