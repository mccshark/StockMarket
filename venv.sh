#!/bin/bash

# Navigate to the target directory

cd ~/Documents/Git/StockMarket

# Create a Python virtual environment named myenv

python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Output a message indicating success
echo "Python virtual environment 'myenv' has been created and activated."