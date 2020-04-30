import React, { Component } from 'react';
import {serverAddress} from "../RestClient";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardMedia from "@material-ui/core/CardMedia";
import makeStyles from "@material-ui/core/styles/makeStyles";
import {red} from "@material-ui/core/colors";

const useStyles = makeStyles((theme) => ({
    root: {
        maxWidth: 345,
    },
    media: {
        height: 0,
        paddingTop: '56.25%', // 16:9
    },
    expand: {
        transform: 'rotate(0deg)',
        marginLeft: 'auto',
        transition: theme.transitions.create('transform', {
            duration: theme.transitions.duration.shortest,
        }),
    },
    expandOpen: {
        transform: 'rotate(180deg)',
    },
    avatar: {
        backgroundColor: red[500],
    },
}));

export function SearchResultCard(props) {
    const classes = useStyles();
    return (
        <Card className={classes.root}>
            <CardHeader
                title={props.title}
                subheader=""
            />
            <CardMedia className={classes.media} image={`${serverAddress}/images/userphotos/${props.image}`}
            />

        </Card>
    );
}