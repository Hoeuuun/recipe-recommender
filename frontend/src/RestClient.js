export const serverAddress = 'https://hoeunsim.com/rr'

export function restRequest(endpoint) {
    const url = `${serverAddress}/${endpoint}`;
    return fetch(url, {
        method: 'GET',
    }).
        then(response => {
            console.log(`Got response ${JSON.stringify(response)}`);
            return response;
        }).
        then(response => response.json()).
        catch(error => console.error(error));
}


