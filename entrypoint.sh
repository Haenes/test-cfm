#!/bin/sh

cd src


echo "----------- Apply migrations -----------"
python manage.py makemigrations && python manage.py migrate --no-input


echo "----------- Create superuser -----------"
script="
from django.contrib.auth.models import User;

username = 'test';
password = 'Test123#';
email = 'test@test.test';

if not User.objects.filter(username=username):
    User.objects.create_superuser(username, email, password);
    print('Superuser created.');
else:
    print('Superuser already exists.');
"
printf "$script" | python manage.py shell


echo "----------- Run -----------"
python manage.py runserver 0.0.0.0:8000
