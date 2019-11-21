import React, {Component} from 'react';

export function RecipeSearch(props) {
    const query = props.query;
    const dietOption = props.dietOption;

    return (
        <div>
            Searching for "{query}".  Diet option "{dietOption}"
        </div>)
}