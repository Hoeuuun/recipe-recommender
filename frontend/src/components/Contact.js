import React, {Component, useState} from 'react';
import Fade from "react-reveal/Fade";
import styled from "styled-components";
import {LogoText} from "./Footer";
import {SearchButton} from "./Header";
import Button from "@material-ui/core/Button";
import LinkedInIcon from '@material-ui/icons/LinkedIn';
import GitHubIcon from '@material-ui/icons/GitHub';
import MailOutlineIcon from '@material-ui/icons/MailOutline';

export const Title = styled(LogoText)`
    color: #282828;
    text-align: center;
    padding: 2rem 1rem 1rem 1rem;
    background-color: white;
    textAlign: center;
    //position: "";
    //bottom: "0";
`;

const SubmitButton = styled(SearchButton)`
    color: dimgrey;
    font-size: 1rem;
    position: relative;
    white-space: nowrap;
    letter-spacing: 2px;
    cursor: pointer;
    //background: transparent;
    font-weight: 700;
    //padding: 12px 26px 12px 26px;
    //margin: 28em 4em 28em 4em;
    border: 2px solid gray;
    align-items: center;
    margin: 5px 5px 5px 5px;   
    justify-content: center; 
    //   padding: 12px 26px 12px 260px;
    background: white;
    textAlign: center;
    color: #202020;
    
    
    &:hover, &:active {
        border-color: #000033;
    }
`;

const CenterButtons = styled.div`
    //position: relative;
    //top: 50%;
    //left: 50%;
    //-webkit-transform: translate(-50%, -50%);
    //transform: translate(-50%, -50%);
    ////marginTop: 100px;
    //width: 100px;
    //height: 100px;
    //margin-top: 30%;
    ////margin-bottom: 5%;
    ////margin-left: -75%;
 
`;


export function Contact() {
    function sendEmail() {
        window.location = "mailto:recipe.recommender.rr@gmail.com"
    }
    function linkLinkedIn() {
        window.open(
            "https://www.linkedin.com/in/hoeun-sim-9b195435/", "_blank");
        // window.location = "https://www.linkedin.com/in/hoeun-sim-9b195435/"
    }
    function linkGitHub() {
        // window.location = "https://github.com/Hoeuuun/recipe-recommender"
        window.open(
            "https://github.com/Hoeuuun/recipe-recommender", "_blank");
    }

    return (
        <div
            id="Contact"
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
                    <Title>Contact</Title>
                    <hr
                        style={{
                            width: "150px",
                            border: "1px solid #828282"
                        }}/>
                        <div className="row">
                            <CenterButtons>
                                <Button variant="primary"
                                        type="submit">
                            <span>
                                <SubmitButton onClick={sendEmail}>
                                    <MailOutlineIcon></MailOutlineIcon>
                                </SubmitButton>
                            </span>
                            <span>
                                <SubmitButton onClick={linkGitHub}>
                                    <GitHubIcon></GitHubIcon>
                                </SubmitButton>
                            </span>
                            <span>
                                <SubmitButton onClick={linkLinkedIn}>
                                    <LinkedInIcon></LinkedInIcon>
                                </SubmitButton>
                            </span>
                                </Button>
                            </CenterButtons>
                        </div>
                </div>
            </Fade>
        </div>
    );
}
