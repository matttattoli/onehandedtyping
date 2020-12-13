@echo off

echo Copying main.py to "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\"
copy main.py "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\onehandedtyping.pyw"

echo Copying ohtremaps.json to "%USERPROFILE%\.ohtremaps.json"
copy ohtremaps.json "%USERPROFILE%\.ohtremaps.json"
