#
#	Here we put some useful bash functions
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
	python manage.py makemigrations main
	python manage.py migrate
}