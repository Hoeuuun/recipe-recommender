import React, { useState, useEffect } from 'react';
import { Autocomplete } from '@material-ui/lab';
import TextField from "@material-ui/core/TextField";
import SortIcon from '@material-ui/icons/Sort';
import MailOutlineIcon from "@material-ui/icons/MailOutline";
import Button from "@material-ui/core/Button";
import {classes} from "istanbul-lib-coverage";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import MenuItem from "@material-ui/core/MenuItem";
import FormHelperText from "@material-ui/core/FormHelperText";
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
            {props.title}:
            <FormControl className={classes.formControl}>
                <Select
                    onChange={e => onSelect(e.target.value)}
                    className={classes.selectEmpty}
                    inputProps={{ 'aria-label': 'Without label' }}>

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