#--------------------------#
# Makefile                 #
# Provides run and clean   #
# commands for convenience #
#--------------------------#

# Gets rid of all temp files
clean:
	find -name '*~' -delete
	find -name '\#*\#' -delete
	find -name '*.swp' -delete

# Starts the server
run:
	python manage.py runserver

# Resets the database
reset:
	rm db.sqlite3
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser

# Performs database migrations
migrate:
	python manage.py makemigrations
	python manage.py migrate
