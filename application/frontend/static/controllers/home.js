class Home {
    constructor() {
        this.sweetAlert = new SweetAlertWrapper();

        this.registerButton = document.getElementById('registroButton');
        this.loginButton = document.getElementById('loginButton');

        this.registerButton.addEventListener('click', this.handleRegisterClick.bind(this));
        this.loginButton.addEventListener('click', this.handleLoginClick.bind(this));
    }

    async handleRegisterClick() {
        this.sweetAlert.showInfo('Registro', 'Haz clic en el botón de registro');
    }

    async handleLoginClick() {
        this.sweetAlert.showInfo('Login', 'Haz clic en el botón de login');
    }
}

document.addEventListener('DOMContentLoaded', function () {
    new Home();
});
