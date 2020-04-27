import React, { useState, useEffect } from 'react';
import {DebounceInput} from "react-debounce-input";
import {restRequest} from "../RestClient";

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

        restRequest(`search?q=${input}`).then((response) => {
            setIsSearching(false);
            if (response) {
                setSearchResults(response.data);
            }
        });

        // fetch()
    }

    // Call hook with current search input, but
    // wait 500ms since it was last called to return the latest value
    /// const debouncedSearchInput = useDebounce(searchInput, 500);

    // UI with search box and results
    return (
        <div>
            <DebounceInput
                placeholder="Enter ingredients"
                minLength={3}
                debounceTimeout={200}
                onChange={e => onInputEntered(e.target.value)}
            />

            {isSearching && searchInput && <h1>Searching for: {searchInput}</h1>}
            {!isSearching && searchInput && <h1>Results for: {searchInput}</h1>}

            {searchResults.map(result => (
                <div key={result.id}>
                    <h4>{result.title}</h4>
                    {/*<img*/}
                    {/*    src={`${result.thumbnail.path}/portrait_incredible.${*/}
                    {/*        result.thumbnail.extension*/}
                    {/*    }`}*/}
                    {/*/>*/}
                </div>
            ))}
        </div>
    );
}
