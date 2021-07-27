chcp 65001
@echo off

echo =========================================
echo.
echo        システムを起動します
echo                          Auther team6
echo =========================================

cd /d %~dp0
cd .\MainProject
start .\dist\main\main.exe

pause