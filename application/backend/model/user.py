class User:
    ADMIN = 'ADMIN'
    GUEST = 'GUEST'

    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type

    @staticmethod
    def get_allowed_users():
        return [
            User('1', '1', User.ADMIN),
            User('2', '2', User.GUEST),
            User('3', '3', User.GUEST),
        ]

    @classmethod
    def find_user(cls, username, password):
        users = cls.get_allowed_users()
        try:
            return next(user for user in users if user.username == username and user.password == password)
        except StopIteration:
            return None
