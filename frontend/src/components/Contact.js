import React, { Component } from 'react';
import Form from "react-bootstrap/Form";
import Col from "react-bootstrap/Col";
import Fade from "react-reveal/Fade";
import styled from "styled-components";
import {LogoText} from "./Footer";
import {SearchButton} from "./Header";
import Button from "@material-ui/core/Button";


export const Title = styled(LogoText)`
    color: grey;
    text-align: center;
    padding: 2rem 1rem 1rem 1rem;
    background-color: white;
    textAlign: center;
    //position: "";
    //bottom: "0";
`;

const SubmitButton = styled(SearchButton)`
    color: grey;
    font-size: 1rem;
    position: relative;
    white-space: nowrap;
    letter-spacing: 5px;
    cursor: pointer;
    background: transparent;
    font-weight: 700;
    //padding: 12px 26px 12px 26px;
    //margin: 28em 4em 28em 4em;
    border: 2px solid gray;
    align-items: center;
    margin: 2px 2px 2px 2px;   
    //justify-content: center; 
    //   padding: 12px 26px 12px 260px;
    
    
    &:hover, &:active {
        border-color: grey;
    }
     
`;


export function Contact() {
    return (
        <div
            style={{
                backgroundColor: "#f9f9f9",
                borderColor: "#ffffff",
                padding: "30px 90px 90px 100px"
            }}>

            <Fade bottom>
                <div
                    style={{
                        width: "50%",
                        marginLeft: "25%"

                    }}>
                    <Title>Contact Me</Title>
                    <hr
                        style={{
                            width: "150px",
                            border: "1px solid #828282"
                        }}/>
                </div>

                <Form>
                    <Form.Row>
                        <Form.Group as={Col} controlId={"formGridName"}>
                            <Form.Control type="name" placeholder={"Name"} />
                        </Form.Group>

                        <Form.Group as={Col} controlId={"formGridEmail"}>
                            <Form.Control type="email" placeholder={"Email"} />
                        </Form.Group>
                    </Form.Row>

                    <Form.Group controlId={"formGridMessage"} >
                        <Form.Control as={"textarea"} rows={"6"} placeholder={"Message"} />
                    </Form.Group>
                    <Button variant="primary" type="submit" className={"float-right"}>
                        <SubmitButton>Send Message</SubmitButton>
                    </Button>
                </Form>

                </Fade>
        </div>



    );
}
