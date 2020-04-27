export const serverAddress = 'http://localhost:5000'

export function restRequest(endpoint) {
    const url = `${serverAddress}/${endpoint}`;
    return fetch(url, {
        method: 'GET',
    }).
        then(response => response.json()).
        catch(error => console.error(error));
}