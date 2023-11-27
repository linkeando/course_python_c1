class SweetAlertWrapper {
    showAlert(type, title, text) {
        const options = {
            icon: type,
            title,
            text,
        };
        Swal.fire(options);
    }

    showError(title, text) {
        this.showAlert('error', title, text);
    }

    showWarning(title, text) {
        this.showAlert('warning', title, text);
    }

    showInfo(title, text) {
        this.showAlert('info', title, text);
    }

    showSuccess(title, text) {
        this.showAlert('success', title, text);
    }


    showConfirmation(title, text) {
        return Swal.fire({
            icon: 'question',
            title,
            text,
            showCancelButton: true,
            confirmButtonText: 'Aceptar',
            cancelButtonText: 'Cancelar',
        });
    }
}