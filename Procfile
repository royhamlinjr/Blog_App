<<<<<<< HEAD
web: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py shell -c "from django.contrib.auth.models import User; print(list(User.objects.values_list('username', flat=True)))" && gunicorn myapp.wsgi --bind 0.0.0.0:$PORT
=======
web: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py shell -c "from django.contrib.auth.models import User; u = User.objects.filter(username='admin123').first(); u.set_password('admin123'); u.save() if u else None" && gunicorn myapp.wsgi --bind 0.0.0.0:$PORT
>>>>>>> 228e9064915ae955fb9da3d7855b9b4521965cfa
