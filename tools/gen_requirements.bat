@echo off
rem WINDOWS SPECIFIC BAT SCRIPT
rem Pip chill doesn't remove all unnecessary dependencies
rem This tool script ensures some deps are trimmed from reqs.txt

rem Ensures that we’re in the project root and in the venv
rem %~dp0 is the location of the bat script according to Windows
cd /d %~dp0
call ..\.venv\Scripts\activate.bat

rem Generate requirements, filter out unnecessary ones, exit
pip-chill --no-version --no-chill | ^
findstr /v /c:"backports.tarfile" | ^
findstr /v /c:"importlib-metadata" | ^
findstr /v /c:"jaraco.collections" | ^
findstr /v /c:"platformdirs" > ../requirements.txt
deactivate

echo "requirements.txt successfully updated"
