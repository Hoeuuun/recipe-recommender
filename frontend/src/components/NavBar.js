import React from 'react';
import { Navbar, Nav } from "react-bootstrap";
import styled from 'styled-components';


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
        <Navbar collapseOnSelect expand="md" bg="secondary" variant="dark">
            <Navbar.Brand href="#home"><BrandText>Recipe Recommender</BrandText></Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
            <Navbar.Collapse className="responsive-navbar-nav">
                <Nav className="ml-auto">
                    <Nav.Link href="#home"><LinkText>HOME</LinkText></Nav.Link>
                    <Nav.Link href="#recipes"><LinkText>RECIPES</LinkText></Nav.Link>
                    <Nav.Link href="#contact"><LinkText>CONTACT</LinkText></Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}