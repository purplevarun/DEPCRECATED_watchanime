@echo off
echo Welcome to Watch Anime ! by Varun Kedia && ^
echo Visit - https://github.com/purplevarun/watchanime && ^
echo Press enter to Watch Anime ! && ^
echo Consider starring the repo if you like this application ! && ^
pause && ^
echo installation started && ^
if exist "installed.txt" (
watchanime-env\scripts\activate && ^
watchanime-env\scripts\activate && ^
python main.py %* && ^
pause
exit
)
else (
echo hey > installed.txt && ^
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
echo. && ^
python main.py %* && ^
deactivate && ^
echo watchanime virtual environment deactivated
)
