#!/bin/bash
# Linux shell script
# Sets up the python virtual environment for you
# Note: VSCode will not recognize the .venv if generated
# from here on Windows because the structure is entirely different

# Ensures that we’re in the project root
# Create venv, enter venv
cd "$(dirname "$0")"
python3 -m venv ../.venv
. ../.venv/bin/activate

# Ensure pip, setuptools, and wheel are updated
python -m pip install --upgrade pip setuptools wheel
# Install other package helpers
python -m pip install pip-chill
# Install the dependencies described inside of requirements.txt
python -m pip install -r ../requirements.txt

# Enter the venv manually by calling source ./.venv/bin/activate
echo "Python virtual environment successfully created"
