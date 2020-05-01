import React, { Component } from 'react';
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

import clsx from 'clsx';

const useStyles = makeStyles((theme) => ({
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

export function SearchResultCard(props) {
    const classes = useStyles();
    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };

    function convertMinsToHrs(mins) {
        let h = Math.floor(mins/60);
        let m = mins % 60;

        h = h < 1 ? '' : h + ' hr ';
        m = m < 1 ? '' : m + ' min';

        return `${h} ${m}`;
    }

    // in DB, rating = int((data['rating_stars'] / 5) * 100)
    // convert int to 5-star rating
    const rating = props.rating / 20.0;
    // console.log("rating: " + rating);

    const description = props.description
    console.log(description);

    return (
        <Card className={classes.root}>
            <CardHeader
                title={props.title}
                // subheader={`Rating: ${props.rating}/100  |  Time: ${props.time} `}
                subheader={`Time: ${convertMinsToHrs(props.time)}`}
            />
            <CardMedia className={classes.media}
                       image={`${serverAddress}/images/userphotos/${props.image}`}
            />
            <CardContent>
                <Typography variant="body2" color="textSecondary" component="p">
                    {description}
                </Typography>
            </CardContent>
                <CardActions disableSpacing>
                    <StarRatings
                        rating={rating}
                        starDimension="1.3em"
                        starSpacing=".2em"
                    />
                    <Typography color="textSecondary" component="p">
                        <div style={{fontSize:"1em",
                                    position:"relative",
                                    paddingTop:".5em",
                                    paddingLeft:".5em"
                                    }}>({props.review_count})</div>
                    </Typography>

                    {/*<IconButton aria-label="add to favorites">*/}
                    {/*    <FavoriteIcon />*/}
                    {/*</IconButton>*/}
                    {/*<IconButton aria-label="share">*/}
                    {/*    <ShareIcon />*/}
                    {/*</IconButton>*/}
                    <IconButton
                        className={clsx(classes.expand, {
                            [classes.expandOpen]: expanded,
                        })}
                        onClick={handleExpandClick}
                        aria-expanded={expanded}
                        aria-label="show more"
                    >
                        <ExpandMoreIcon />
                    </IconButton>
                </CardActions>
                <Collapse in={expanded} timeout="auto" unmountOnExit>
                    <CardContent>
                        <Typography paragraph>Directions:</Typography>
                        <Typography paragraph>
                            Heat 1/2 cup of the broth in a pot until simmering, add saffron and set aside for 10
                            minutes.
                        </Typography>
                    </CardContent>
                </Collapse>
        </Card>
    );
}