@echo off
echo installation started && ^
7za e mpv.7z && ^
echo mpv player extracted successfully && ^
python -m pip install --upgrade pip wheel virtualenv && ^
virtualenv watchanime-env && ^
watchanime-env\scripts\activate && ^
watchanime-env\scripts\activate && ^
cls && ^
echo virtual environment created.... && ^
python -m pip install --upgrade pip bs4 requests html5lib && ^
cls && ^
echo watchanime was successfully installed... && ^
python main.py %* && ^
deactivate && ^
echo watchanime virtual environment deactivated
