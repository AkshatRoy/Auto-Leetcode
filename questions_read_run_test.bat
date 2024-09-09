@echo off
setlocal enabledelayedexpansion

:: Set the file path and URL base
set "filepath=question.txt"
set "tempfile=tempfile.txt"
set "urlbase=https://leetcode.com/problems/"

:: Check if the file exists
if not exist "%filepath%" (
    echo File not found: %filepath%
    cmd /k
    exit /b 1
)

:: Read the first line from the file
set "problem="
for /f "usebackq delims=" %%a in ("%filepath%") do (
    set "problem=%%a"
    goto :break
)
:break

:: Construct the URL
set "url=%urlbase%%problem%/description"

:: Open the URL in the default web browser
start brave.exe "%url%"


python "python_script_final.py"


:: Process the file to move the first line to the end 
> "%tempfile%" (
    for /f "usebackq delims=" %%a in ("%filepath%") do (
        if "%%a" neq "!problem!" (
            echo %%a
        )
    )
    echo %problem%
)

:: Replace the original file with the modified one
move /y "%tempfile%" "%filepath%"

:: cmd /k

endlocal
