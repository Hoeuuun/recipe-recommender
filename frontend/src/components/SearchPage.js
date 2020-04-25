import React, {Component, useState} from 'react';
import PropTypes from 'prop-types';
import '../index.css';
import {RecipeSearch} from './RecipeSearch';
import {debounce} from 'debounce';

const DIET_OPTIONS = {
    PROMPT: "Diet",
    GLUTEN_FREE: "Gluten Free",
    LACTOSE_FREE: "lactose free",
    PALEO: "Paleo",
    PESCATARIAN: "Pescatarian",
    VEGAN: "Vegan",
    VEGATARIAN: "Vegetarian"
};

const RATING_OPTION = {
    PROMPT: "Rating",
    HIGHEST: "Highest",
    LOWEST: "Lowest"
};

const REVIEWS_OPTION = {
    PROMPT: "Reviews",
    HIGHEST: "Highest",
    LOWEST: "Lowest"
};

const TIME_OPTION = {
    PROMPT: "Time",
    LESS_30: "< 30 mins",
    LESS_60: "< 60 mins",
    MORE_60: "60+ mins"
};

function DropDownButton(props) {
    const options = props.options;
    const onSelected = props.onSelected;

    return (
        <select onChange={event => {onSelected(event.target.value)}}>
            {Object.entries(options).map(entry => {return (<option value={entry[0]}> {entry[1]} </option>)})}
        </select>
        );
}

export function SearchPage(props) {
    const [query, setQuery] = useState('');

    const [dietOption, setDietOption] = useState(DIET_OPTIONS.PROMPT);
    const [ratingOption, setRatingOption] = useState(RATING_OPTION.PROMPT);
    const [reviewsOption, setReviewsOption] = useState(RATING_OPTION.PROMPT);
    const [timeOption, setTimeOption] = useState(RATING_OPTION.PROMPT);

    const [updateQuery] = useState(() => debounce(text => setQuery(text), 500));

    const label = "Enter some ingredients.";

    const onQueryEntered = (event) => {
        updateQuery(event.target.value)
    };

   return (
       <div>
           <div className="field">
               <label> Recipe Search Section. </label>
           </div>
           <input
               type="text"
               placeholder={label}
               onChange={onQueryEntered}
           />
           <DropDownButton options={DIET_OPTIONS} onSelected={selectedValue => {
               console.log(selectedValue);
               setDietOption(selectedValue);
           }} />

           <RecipeSearch query={query} dietOption={dietOption} />
       </div>);

}
