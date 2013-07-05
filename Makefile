test: test1

test1: my_info/gen_info/tests.py
		python my_info/manage.py test gen_info

