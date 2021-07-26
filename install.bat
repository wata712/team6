@echo off

echo ========================================================
echo.
echo        システムに必要なライブラリをインストールします
echo.
echo ========================================================

call powershell -command "pip install -r requirements.txt"

pause