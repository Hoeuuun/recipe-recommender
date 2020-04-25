import React, {Component} from 'react';
import {NavBar} from "./components/NavBar";
import {Header} from "./components/Header";
import {Search} from "./components/Search";
import {Contact} from "./components/Contact";
import {Footer} from "./components/Footer";


export default function App() {
  return (
    <div>
        <NavBar/>
        <Header/>
        <Search/>
        <Contact/>
        <Footer/>
    </div>
  );
}
