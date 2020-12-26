import React, {Component} from 'react';
import {NavBar} from "./components/NavBar";
import {Header} from "./components/Header";
import {Search} from "./components/Search";
import {Contact} from "./components/Contact";
import {Footer} from "./components/Footer";
import {LoginButton} from "./components/LoginButton";
import {Auth0Provider} from "@auth0/auth0-react";

export default function App() {
  return (
    <div>
        <Auth0Provider
            domain="dev-degk2yc5.us.auth0.com"
            clientId="tRrtNJsbjsTHkJ7vzZLZiFs13jEBhFdA"
            redirectUri={window.location.origin}
        >
            <LoginButton/>
        </Auth0Provider>
        <NavBar/>
        <Header/>
        <Search/>
        <Contact/>
        <Footer/>
    </div>
  );
}
