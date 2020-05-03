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
import {Sort} from "./Sort";

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

const TIME_SORT_OPTION_TO_REST_ARGS = {
    '< 15': [0, 15],
    '< 30': [0, 30],
    '< 60': [0, 60]
}

const RATING_SORT_OPTION_TO_RES_ARGS = {
    'Highest': 'DESC',
    'Lowest': 'ASC'
}

const REVIEW_SORT_OPTION_TO_RES_ARGS = {
    'Highest': 'DESC',
    'Lowest': 'ASC'
}
export function Search() {
    // State and setter search input
    const [searchInput, setSearchInput] = useState(false);
    // State and setter for search results
    const [searchResults, setSearchResults] = useState([]);
    // State and setter for search status (loading request)
    const [isSearching, setIsSearching] = useState(false);

    const [minTime, setMinTime] = useState(null);
    const [maxTime, setMaxTime] = useState(null);

    const [review, setReview] = useState(null);

    const [rating, setRating] = useState(null);

    function doSearch() {
        let searchQuery = searchInput;
        if (!searchQuery){
            console.log(`Not doing search because there is no text query.`)
            return;
        }
        console.log(searchQuery);
        setIsSearching(searchQuery);
        setSearchInput(searchQuery);

        searchQuery = searchQuery.split(" ").join(",");

        // construct the url with sort options
        var url = `search?q=${searchQuery}`

        if (minTime !== null)  {
            url += `&minTime=${minTime}`;
        }
        if (maxTime !== null) {
            url += `&maxTime=${maxTime}`;
        }

        if (review !== null) {
            url += `&review=${review}`;
        }

        if (rating !== null) {
            url += `&rating=${rating}`;
        }


        restRequest(url).then(response => {
            // This is executed when request returns data
            setIsSearching(false);
            if (response) {
                setSearchResults(response.data);
            }
        });
    }

    useEffect(() => {
        // Do search
        doSearch()
    }, [searchInput, minTime, maxTime, review, rating])

    const debouncedSetSearchInput = debounce(value => setSearchInput(value), 200)

    // functions to handle sorts
    function handleRatingSortChange(value) {
        console.log(`Rating sort changed to ${value}`)
        setRating(RATING_SORT_OPTION_TO_RES_ARGS[value]);
    }
    function handleReviewSortChange(value) {
        console.log(`Review sort changed to ${value}`)
        setReview(REVIEW_SORT_OPTION_TO_RES_ARGS[value]);
    }
    function handleTimeSortChange(value) {
        console.log(`Cooking time sort changed to ${value}`);
        const minMaxTimes = TIME_SORT_OPTION_TO_REST_ARGS[value];
        setMinTime(minMaxTimes[0]);
        setMaxTime(minMaxTimes[1]);
    }
    // var a = 5;
    // var b = handleRatingSortChange;
    // b('hello');
    // handleRatingSortChange('hello');


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
                          onChange={e => debouncedSetSearchInput(e.target.value)}
                />
                <Sort
                    title="Rating"
                    options={['Highest', 'Lowest']}
                    onItemSelected={handleRatingSortChange}
                />

                <Sort
                    title="Review"
                    options={['Highest', 'Lowest']}
                    onItemSelected={handleReviewSortChange}
                />

                <Sort
                    title="Time"
                    options={['< 15', '< 30', '< 60']}
                    onItemSelected={handleTimeSortChange}
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
