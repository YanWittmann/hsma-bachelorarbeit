@echo off

if "%~2"=="" (
    REM one argument
    set "input_file=%~1.md"
    set "output_file=%~1.pdf"
) else (
    REM two arguments
    set "input_file=%~1"
    set "output_file=%~2"
)

wsl pandoc "%input_file%" -o "%output_file%" --pdf-engine=xelatex -V linkcolor=blue