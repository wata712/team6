@echo off

echo =========================================
echo.
echo        システムを起動します
echo                          Auther team6
echo =========================================

rem server起動

cd ..\MainProject
start powershell -command "python main.py"

echo.
echo システムを終了する際には Control+C で終了してください。
pause