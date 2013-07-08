MANAGE=./my_info/manage.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=my_info.settings $(MANAGE) test gen_info

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=my_info.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=my_info.settings $(MANAGE) syncdb --noinput

