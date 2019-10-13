import React, {Component} from 'react';
//import './App.css';
import {SearchPage} from "./components/SearchPage";
import {Header} from "./components/Header";

export default function App() {
    return (
        <div>
            <Header/>
            <SearchPage/>
        </div>);
}