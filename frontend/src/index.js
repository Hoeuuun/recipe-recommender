import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

import "@fortawesome/fontawesome-free/css/all.min.css";
import "bootstrap-css-only/css/bootstrap.min.css";
import "mdbreact/dist/css/mdb.css";
import { Auth0Provider } from '@auth0/auth0-react';


ReactDOM.render(
    <Auth0Provider
        domain="dev-degk2yc5.us.auth0.com"
        clientId="tRrtNJsbjsTHkJ7vzZLZiFs13jEBhFdA"
        redirectUri={window.location.origin}
    >
        <App />
    </Auth0Provider>,
    document.getElementById('root')
);


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
