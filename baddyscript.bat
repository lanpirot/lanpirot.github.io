@echo off
:: Define the directory name
set DIR_NAME=baddyfiles

:: Create the directory if it doesn't exist
if not exist "%DIR_NAME%" mkdir "%DIR_NAME%"

:: Get today's date and time in YYYY-MM-DD_HH:MM:SS format
for /f "tokens=2 delims==" %%G in ('wmic os get localdatetime /value') do set datetime=%%G
set DATE=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2%_%datetime:~8,2%:%datetime:~10,2%:%datetime:~12,2%

:: Create a file named after today inside the directory
type nul > "%DIR_NAME%\bad_stuff%DATE%.txt"

:: Print confirmation
echo Baddy script successfully executed at: %DIR_NAME%\bad_stuff%DATE%.txt
