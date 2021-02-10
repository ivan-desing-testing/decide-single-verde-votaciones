%prueba
release: sh -c 'cd decide && cp travis_local_settings.py local_settings.py'
% prepara el repositorio para su despliegue. 
release: sh -c 'cd decide && python manage.py createsuperuser && python manage.py migrate'
% especifica el comando para lanzar Decide
web: sh -c 'cd decide && gunicorn decide.wsgi --log-file -'