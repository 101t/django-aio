@ECHO OFF
set ENVIROO=python

set MANAGER=manage.py

CALL env\Scripts\activate

if "%~1"=="-i" GOTO INTIAL
if "%~1"=="--init" GOTO INTIAL

:INTIAL
    del /F db.sqlite3

    %ENVIROO% %MANAGER% reseter
    %ENVIROO% %MANAGER% makemigrations core
    %ENVIROO% %MANAGER% makemigrations users
    %ENVIROO% %MANAGER% makemigrations notify
    %ENVIROO% %MANAGER% makemigrations
    %ENVIROO% %MANAGER% migrate

    %ENVIROO% %MANAGER% load_new
GOTO DONE

set RUN_PROJECT=%ENVIROO% %MANAGER% runserver 0.0.0.0:8000
CALL %RUN_PROJECT%