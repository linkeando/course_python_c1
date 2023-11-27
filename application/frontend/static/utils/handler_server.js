class ServerHandler {
    ALERT = new SweetAlertWrapper()

    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    async fetchData(endpoint, method = 'GET', queryParams = {}, body = null) {
        const url = `${this.baseUrl}/${endpoint}`;

        const options = {
            method: method.toUpperCase(),
            headers: {
                'Content-Type': 'application/json',
            },
            body: body ? JSON.stringify(body) : null,
        };

        try {
            const response = await fetch(url, options);

            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.statusText}`);
            }

            return response.json();
        } catch (error) {
            this.ALERT.showError('Error al realizar la solicitud', error);
        }
    }

    getData = (endpoint, queryParams = {}) => this.fetchData(endpoint, 'GET', queryParams);
    postData = (endpoint, data) => this.fetchData(endpoint, 'POST', {}, data);
    updateData = (endpoint, data) => this.fetchData(endpoint, 'PUT', {}, data);
    deleteData = (endpoint) => this.fetchData(endpoint, 'DELETE');
    readAllData = (endpoint, queryParams = {}) => this.fetchData(endpoint, 'GET', queryParams);
}