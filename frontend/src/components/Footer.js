import React, { Component } from 'react';
import {BrandText} from "./NavBar";
import {LinkText} from "./NavBar";
import styled from 'styled-components';


export const LogoText = styled(BrandText)`
    color: #ffffff;
    padding-top: 2em;
    padding-bottom: 1em;
    border-radius: 1.5px;
    letter-spacing: .3em;
`;

const Copyright = styled.p`
     color: silver;
     padding-bottom: 2em;
     list-style-type: none;
`;

export function Footer() {
    return (
        <footer style={{backgroundColor: "grey",
                        textAlign: "center",
                        position: "",
                        bottom: "0",
                        width: "100%"
                        }}>
            <LogoText>RECIPE RECOMMENDER</LogoText>
            <Copyright>&copy; 2020 All rights reserved.</Copyright>
        </footer>
    );
}
