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

# Performs database migrations
migrate:
	python manage.py makemigrations
	python manage.py migrate
