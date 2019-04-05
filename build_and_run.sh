#!/usr/bin/env bash
docker build -t recipe-recommender .
docker run -p 5000:5000 recipe-recommender
