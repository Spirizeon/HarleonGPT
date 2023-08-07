#!/bin/bash
echo "enter your openai API key:"
read KEY1
echo "openai='${KEY1}'" > .env 
echo "enter your discord bot token:"
read KEY2
echo "TOKEN='${KEY2}'" >> .env
echo "successfully added!"
