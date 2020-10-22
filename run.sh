# written by Alex Jabbour oct 21
#!/bin/bash
if [ "$#" -eq 1 ]
then
	export FLASK_ENV=development
fi
export FLASK_APP=main.py
python3 -m flask run
