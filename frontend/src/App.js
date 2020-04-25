import React, {Component} from 'react';
// import './index.css';
import {SearchPage} from "./components/SearchPage";
import {Header} from "./components/Header";
import {Home} from "./components/Home";
import {Footer} from "./components/Footer";

export default function App() {
    return (
        <div>
            <Header/>
            <Home/>>
            <SearchPage/>
            <Footer/>
        </div>);
}