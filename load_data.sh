ENVIROO=./env/bin/python
MANAGER=manage.py

if [ "$1" == "--init" ] || [ "$1" == "-i" ]; then
	rm -rf db.sqlite3

	$ENVIROO $MANAGER reseter
	$ENVIROO $MANAGER makemigrations
	$ENVIROO $MANAGER migrate

	$ENVIROO $MANAGER load_new
fi

RUN_PROJECT="$ENVIROO $MANAGER runserver 0.0.0.0:8000"
echo $RUN_PROJECT
$RUN_PROJECT