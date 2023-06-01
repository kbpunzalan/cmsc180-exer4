#!/bin/bash

# Set the number of terminals to open
num_terminals=3

for ((i=1; i<=num_terminals; i++))
do
    start cmd /c python main.py
done