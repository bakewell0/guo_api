python manage.py runserver

pip:
pip install pip-save
pip-save install [<list of packages>]
pip-save install --upgrade [<list of packages>]
pip-save uninstall [<list of packages>]

pip install -r  requirement.txt
pip list
where python
pip freeze >requirements.txt
uwsgi uwsgiconfig.ini
uwsgi --http :9090 --wsgi-file server.py
ps aux | grep uwsgi
killall -9 uwsgi