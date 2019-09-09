#!/bin/bash

echo "++++++++++ TRAINING MODELS ++++++++++"
rasa train


echo "++++++++++ STARTING SERVER ++++++++++"
rasa run --port 5001 --credentials credentials.yml --endpoints endpoints.yml --debug