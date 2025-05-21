class User():
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __str__(self):
        return f"Login: {self.login}, Password: {self.password}"

users = [
    User("user1", "qwe"),
    User("user2", "asd"),
    User("user3", "zxc"),
    User("user4", "rty"),
    User("user5", "fgh"),
]

input_login = input("Введите логин -> ")
input_password = input("Введите пароль -> ")

found_user = None

for user in users:
    if user.login == input_login and user.password == input_password:
        found_user = user
        break

if found_user:
    print(f"Пользователь найден. {found_user}")
else:
    print(f"Пользователя с логином {input_login} и паролем {input_password} в базе не обнаружено.")