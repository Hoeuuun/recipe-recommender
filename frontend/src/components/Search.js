import React, { useState, useEffect } from 'react';
import {DebounceInput} from "react-debounce-input";
import {restRequest, serverAddress} from "../RestClient";
import StackGrid from "react-stack-grid";
import {SearchResultCard} from "./SearchResultCard";
import CardHeader from "@material-ui/core/CardHeader";
// import StarRatings from 'react-star-ratings';
import {MDBCol, MDBIcon, MDBInput} from "mdbreact";
import Input from "@material-ui/core/Input";
import styled, {css} from "styled-components";
import {Title} from "./Contact";
import Fade from "react-reveal/Fade";

const SearchTitle = styled(Title)`
  background-color: lightgray;
`;

function debounce(fn, wait) {
    var timeout;

    return function exec() {
        var self = this;
        var args = arguments;

        var doIt = () => {
            timeout = null;
            fn.apply(self, args)
        }

        clearTimeout(timeout)
        timeout = setTimeout(doIt, wait);
    }
}

export function Search() {
    // State and setter search input
    const [searchInput, setSearchInput] = useState(false);
    // State and setter for search results
    const [searchResults, setSearchResults] = useState([]);
    // State and setter for search status (loading request)
    const [isSearching, setIsSearching] = useState(false);


    function onInputEntered(input) {
        console.log(input);
        setIsSearching(input);
        setSearchInput(input);

        input = input.split(" ").join(",");
        restRequest(`search?q=${input}`).then(response => {
            // This is executed when request returns data
            setIsSearching(false);
            if (response) {
                setSearchResults(response.data);
            }
        });
    }

    onInputEntered = debounce(onInputEntered, 200)

    function adaptResultToProps(result) {
        result.rating = result.rating / 20.0;
        return result;
    }

    return (
        <div id="Search" style={{padding:"30px 90px 90px 100px"}}>
            <Fade bottom>
                <div
                    style={{
                        width: "50%",
                        marginLeft: "25%"

                    }}>
                    <SearchTitle>Recipes</SearchTitle>
                    <hr
                        style={{
                            width: "150px",
                            border: "1px solid #828282"
                        }}/>
                </div>
                <MDBInput label="Enter ingredients"
                      outline icon color="black"
                      outline icon="search"
                      outline size="lg"
                          onChange={e => onInputEntered(e.target.value)}
                />

            </Fade>

            {/*<DebounceInput*/}
            {/*    placeholder="Enter ingredients"*/}
            {/*    minLength={3}*/}
            {/*    debounceTimeout={200}*/}
            {/*    onChange={e => onInputEntered(e.target.value)}*/}

            {/*/>*/}

            {isSearching && searchInput && <h1 align="center">Searching for: {searchInput}...</h1>}

            {!isSearching && searchInput && <h1 align="center">Results for: {searchInput}</h1>}

            <StackGrid columnWidth={250}>

                {searchResults.map((result) => (

                <SearchResultCard id={result.id}
                                  title={result.title}
                                  image={result.image}
                                  time={result.time}
                                  rating={result.rating}
                                  review_count={result.review_count}
                                  description={result.description}
                                  ingredients={result.ingredients}
                                  directions={result.directions}
                />

                ))}
            </StackGrid>
        </div>
    );
}
