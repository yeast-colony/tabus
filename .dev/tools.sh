#
#	Here we put some useful bash functions
#	Call that function only from root directory
#

function test {
	echo $k
}

function tabus__reload {
	source .dev/tools.sh	
}

function tabus__shell {
	python3 manage.py shell
}

function tabus__migrate {
	python3 manage.py makemigrations main
	python3 manage.py migrate
}

function tabus__cleanMigrationsAndDB {
	rm -r main/migrations/*
	rm db.sqlite3
}

function tabus__testsrun {
	python3 manage.py test --pattern *__test.py -v 3
}