import React, {Component} from 'react';
import {serverAddress} from "../RestClient";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardMedia from "@material-ui/core/CardMedia";
import makeStyles from "@material-ui/core/styles/makeStyles";
import {red} from "@material-ui/core/colors";
import Typography from "@material-ui/core/Typography";
import CardContent from "@material-ui/core/CardContent";
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import CardActions from "@material-ui/core/CardActions";
import IconButton from "@material-ui/core/IconButton";
import Collapse from "@material-ui/core/Collapse";
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share';
import StarRatings from 'react-star-ratings';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import Modal from 'react-modal';

import clsx from 'clsx';

const useCardStyle = makeStyles((theme) => ({
    root: {
        maxWidth: 345,
    },
    media: {
        height: 0,
        paddingTop: '106.25%', // 16:9
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

const useModalStyle = makeStyles((theme) => ({
    root: {
        maxWidth: '80%',
    },
    media: {
       // width: '80%',
       // maxHeight: '40%',
     //   paddingTop: '106.25%', // 16:9
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

const customStyles = {
    content: {
        top: '50%',
        left: '50%',
        right: 'auto',
        bottom: 'auto',
        marginRight: '-50%',
        transform: 'translate(-50%, -50%)',
        maxWidth: '70%',
        maxHeight: '70%'

    },
    overlay: {zIndex: 1000}
};

function convertMinsToHrs(mins) {
    let h = Math.floor(mins / 60);
    let m = mins % 60;

    h = h < 1 ? '' : h + ' hr ';
    m = m < 1 ? '' : m + ' min';

    return `${h} ${m}`;
}

function SearchResultBrief(props) {
    const classes = props.classes;
    return (
        <div onClick={props.onClick}>
            <CardHeader
                title={props.title}
                subheader={`Time: ${convertMinsToHrs(props.time)}`}
            />
            <CardMedia className={classes.media}
                       image={`${serverAddress}/images/userphotos/${props.image}`}
            />
            <CardContent>
                <Typography variant="body2" color="textSecondary" component="p">
                    {props.description}
                </Typography>
            </CardContent>
            <CardActions disableSpacing>
                <StarRatings
                    rating={props.rating}
                    starDimension="1.3em"
                    starSpacing=".2em"
                />
                <Typography color="textSecondary" component="p">
                    <div style={{
                        fontSize: "1em",
                        position: "relative",
                        paddingTop: ".5em",
                        paddingLeft: ".5em"
                    }}>({props.review_count})
                    </div>
                </Typography>

            </CardActions>


        </div>
    );
}

export function SearchResultCard(props) {
    const classes = useCardStyle();
    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };


    // in DB, rating = int((data['rating_stars'] / 5) * 100)
    // convert int to 5-star rating
    const rating = props.rating / 20.0;

    const description = props.description

    const [modalIsOpen, setIsOpen] = React.useState(false);

    function openModal() {
        setIsOpen(true);

    }

    function closeModal() {
        setIsOpen(false);
    }

    return (
        <Card className={classes.root}>
            <SearchResultBrief {...props}
                              onClick={openModal}
                              classes={useCardStyle()}/>
            <Modal
                isOpen={modalIsOpen}
                // onAfterOpen={afterOpenModal}
                onRequestClose={closeModal}
                style={customStyles}
            >
                <SearchResultBrief {...props}
                                  onClick={closeModal}
                                  classes={useModalStyle()}/>

                <CardContent>
                    <h2>Ingredients</h2>
                    <ul>
                        {props.ingredients.map(ingredient => <li>{ingredient}</li>)}
                    </ul>
                    <h2>Directions</h2>
                    <ol>
                        {props.directions.map(direction => <li>{direction}</li>)}
                    </ol>
                </CardContent>
            </Modal>

        </Card>
    );
}

