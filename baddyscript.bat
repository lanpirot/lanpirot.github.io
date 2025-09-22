@echo off
:: Define the directory name
set DIR_NAME=baddyfiles

:: Create the directory if it doesn't exist
if not exist "%DIR_NAME%" mkdir "%DIR_NAME%"


:: Create a file named badstuff.txt
type nul > "%DIR_NAME%\badstuff.txt"
