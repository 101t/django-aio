set ENVIROO=.\\env\\bin\\python
set MANAGER=manage.py
IF "%1" == "--reset" (
	del -rf db.sqlite3
	%ENVIROO% %MANAGER% reseter
	%ENVIROO% %MANAGER% makemigrations
	%ENVIROO% %MANAGER% migrate
)
%ENVIROO% %MANAGER% load_new

set RUN_PROJECT="%ENVIROO% %MANAGER% runserver 0.0.0.0:8000"
echo %RUN_PROJECT%
%
%RUN_PROJECT%