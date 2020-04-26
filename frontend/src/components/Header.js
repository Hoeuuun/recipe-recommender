import React, { Component } from 'react';
import styled from "styled-components";


/* Header image */
const HeroImage = styled.div`
    width: 100vw;
    height: 100vh; 
    background-image: linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.3)), url("olive_oil_small.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
    position: relative;
    z-index: -1;
`;

/* Hero text */
const MainHeader = styled.div`
  font-size: 3em;
  letter-spacing: 9px;
  font-style: normal;
  background: #ffffff;
  color: #202020;
  position: absolute;
  padding: 1rem;
  font-weight: bold;
  margin: 4em 1em 4em 1em;
  padding: 5px 16px 5px 16px;
  z-index: 1;

  
 
`;

export const SubHeader= styled.div`
  background: #ffffff;
  letter-spacing: 3px;
  color: #202020;
  font-size: 25px;
  position: absolute;
  font-weight: bold;
  margin: 15em 1em 15em 1em;
  padding: 5px 16px 5px 16px;
  white-space: nowrap;
  z-index: 1;
`;

/* Recipe search button */
export const SearchButton = styled.button`
    color: #fff;
    font-size: 1rem;
    position: relative;
    white-space: nowrap;
    letter-spacing: 5px;
    cursor: pointer;
    background: transparent;
    margin: 2em 5em 5em 5em;
    font-weight: 700;
    padding: 12px 26px 12px 26px;
    margin: 28em 4em 28em 4em;
    border: 2px solid #fff;
    z-index: 0;
   
    &:hover, &:active {
        color: #000033;
        border-color: white;
        background-color: white;
    }
     
`;

export function Header() {
    return (
        <HeroImage>
        <div class="col-12 col-md-8 text-center justify-content-md-center offset-2">
            <MainHeader>RECIPE RECOMMENDER</MainHeader>
        </div>
        <div class="col-6 col-md-4 text-center offset-4">
            <SubHeader>Search 87k+ Recipes</SubHeader>
            <SearchButton href="#search">Find a Recipe</SearchButton>
        </div>
        </HeroImage>
    );
}