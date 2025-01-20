export function getDatosBackend() {
    return fetch('http://127.0.0.1:8000/').then(
        (respose) => {
            return respose.json
        }
    )
}