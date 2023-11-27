from flask import render_template

from application.backend.model.user import User


class LoginService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        found_user = User.find_user(self.username, self.password)
        if found_user:
            return self._render_home(found_user)
        else:
            return self._render_login_failure()

    @staticmethod
    def _render_home(user: User):
        if user.user_type == User.ADMIN:
            print()
        return render_template('home.html', user=user)

    @staticmethod
    def _render_login_failure():
        template_args = {'message': 'Usuario No Encontrado'}
        return render_template('home.html', **template_args)
