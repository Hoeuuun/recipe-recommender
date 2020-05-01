import React, { useState, useEffect } from 'react';
import {DebounceInput} from "react-debounce-input";
import {restRequest, serverAddress} from "../RestClient";
import StackGrid from "react-stack-grid";
import {SearchResultCard} from "./SearchResultCard";
import CardHeader from "@material-ui/core/CardHeader";
import StarRatings from 'react-star-ratings';


export function Search() {
    // State and setter search input
    const [searchInput, setSearchInput] = useState(false);
    // State and setter for search results
    const [searchResults, setSearchResults] = useState([]);
    // State and setter for search status (loading request)
    const [isSearching, setIsSearching] = useState(false);



    function onInputEntered(input) {
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

    function adaptResultToProps(result) {
        result.rating = result.rating / 20.0;
        return result;
    }

// Call hook with current search input, but
    // wait 500ms since it was last called to return the latest value
    // UI with search box and results
    return (
        <div>
            <DebounceInput
                placeholder="Enter ingredients"
                minLength={3}
                debounceTimeout={200}
                onChange={e => onInputEntered(e.target.value)}
            />

            {isSearching && searchInput && <h1>Searching for: {searchInput}...</h1>}

            {!isSearching && searchInput && <h1>Results for: {searchInput}</h1>}

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
