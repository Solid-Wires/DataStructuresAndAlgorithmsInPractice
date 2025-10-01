@echo off
rem WINDOWS SPECIFIC BAT SCRIPT
rem Sets up the python virtual environment for you

rem Ensures that we’re in the project root
rem Create venv, enter venv
cd /d %~dp0
python -m venv ../.venv
call ..\.venv\Scripts\activate.bat

rem Ensure pip, setuptools, and wheel are updated
python -m pip install --upgrade pip setuptools wheel
rem Install other package helpers
python -m pip install pip-chill
rem Install the dependencies described inside of requirements.txt
python -m pip install -r ../requirements.txt

rem Exits. Enter the venv manually by calling .\.venv\Scripts\activate.bat
deactivate

echo "Python virtual environment successfully created"
