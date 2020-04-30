import React, { useState, useEffect } from 'react';
import {DebounceInput} from "react-debounce-input";
import {restRequest, serverAddress} from "../RestClient";
import StackGrid from "react-stack-grid";
import {SearchResultCard} from "./SearchResultCard";


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

    const Columns = () =>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gridGap: 20 }}>
            <div>Column 1</div>
            <div>Column 2</div>
            <div>Column 3</div>
        </div>


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

            {/*<StackGrid columnWidth={150}>*/}
            {/*    <div key="key1">Item 1</div>*/}
            {/*    <div key="key2">Item 2</div>*/}
            {/*    <div key="key3">Item 3</div>*/}
            {/*</StackGrid>*/}

            <StackGrid columnWidth={250}>
                {searchResults.map((result) => (

                <SearchResultCard id={result.id % 3}
                                  title={result.title}
                                  image={result.image}
                />
                ))}
            </StackGrid>
        </div>
    );
}
