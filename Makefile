MANAGE=./my_info/manage.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=my_info.settings $(MANAGE) test gen_info
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=my_info.settings $(MANAGE) test http_request_storage
	
run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=my_info.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=my_info.settings $(MANAGE) syncdb --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=my_info.settings $(MANAGE) migrate
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=my_info.settings $(MANAGE) loaddata mydata.json

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=my_info.settings $(MANAGE) migrate

