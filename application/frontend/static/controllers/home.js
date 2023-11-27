class Home {
    SERVER = '/home'
    ENDPOINT_REGISTER = 'add_user'
    ENDPOINY_LOGIN = 'login_user'


    constructor() {
        this.ALERT = new SweetAlertWrapper();

        this.registerButton = document.getElementById('registroButton');
        this.loginButton = document.getElementById('loginButton');

        this.registerButton.addEventListener('click', this.handleRegisterClick.bind(this));
        this.loginButton.addEventListener('click', this.handleLoginClick.bind(this));
    }

    async handleRegisterClick() {
        const data = {name: 'John', age: 30};
        const serverHandler = new ServerHandler(this.SERVER);

        const response = await serverHandler.postData(this.ENDPOINT_REGISTER, data);

        if (response) {
            this.ALERT.showSuccess('Entro al server', response.message);
        }
    }


    async handleLoginClick() {
        this.ALERT.showInfo('Login', 'Haz clic en el botón de login');
    }
}

document.addEventListener('DOMContentLoaded', function () {
    new Home();
});
