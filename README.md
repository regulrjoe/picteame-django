# Activate virtual environment
`$ source django_env/bin/activate`

# Run server
./runserver.sh

# Make migrations
python3 manage.py makemigrations

# Migrate
python3 manage.py migrate

# Open database
psql -U postgres -d picteame
or
python3 manage.py dbshell

# Create super user
python3 manage.py createsuperuser
