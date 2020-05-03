import React from 'react';
import {classes} from "istanbul-lib-coverage";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import MenuItem from "@material-ui/core/MenuItem";
import SortIcon from "@material-ui/icons/Sort";

/**
 * General drop down sort widget.
 *
 * Props are:
 *  * title: What to show as title
 *  * options: Array of strings for Options to display
 *  * onItemSelected: A callback function taking a single string argument - value, which is what the user selected.
 */
export function Sort(props) {
    function onSelect(value) {
        props.onItemSelected(value);
    }

    return (
        <div style={{
            padding: "1px 90px 90px 10px"
            }}>
            <SortIcon></SortIcon>
            {props.title}:
            <FormControl style={{
                    paddingLeft: "20px"
            }}>
                <Select
                    onChange={e => onSelect(e.target.value)}>
                    {props.options.map(option =>
                        <MenuItem value={option}>
                            {option}
                        </MenuItem>
                    )}

                </Select>
            </FormControl>
        </div>
    );
}