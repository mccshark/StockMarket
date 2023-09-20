#!/bin/bash

# Navigate to the target directory

cd ~/Documents/Github/StockMarket

# Create a Python virtual environment named myenv

python3 -m venv venv

# Activate the virtual environment

source myenv/bin/activate

# Output a message indicating success

echo "Python virtual environment 'myenv' has been created and activated."