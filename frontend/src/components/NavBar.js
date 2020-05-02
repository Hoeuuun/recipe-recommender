import React from 'react';
import { Navbar, Nav } from "react-bootstrap";
import styled from 'styled-components';
import { Link, animateScroll as scroll } from "react-scroll";


export const LinkText = styled.li`
      font-size: 12px;
      letter-spacing: 1px;
`;

export const BrandText = styled.h1`
      font-size: 24px;
      letter-spacing: 2px;
      font-weight: bold;
`;

export function NavBar() {
    return (
        <Navbar collapseOnSelect expand="lg"
                bg=""
                variant="light"
                id="Navbar"
                sticky="op">
            <Navbar.Brand href="#home"><BrandText>Recipe Recommender</BrandText></Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
            <Navbar.Collapse className="responsive-navbar-nav">
                <Nav className="ml-auto">
                    <Nav.Link href="#Header" smooth={true}><LinkText>HOME</LinkText></Nav.Link>
                    <Nav.Link href="#Search" smooth={true}><LinkText>RECIPES</LinkText></Nav.Link>
                    <Nav.Link href="#Contact" smooth={true}><LinkText>CONTACT</LinkText></Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}