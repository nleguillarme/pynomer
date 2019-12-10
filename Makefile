init:
		pip install -r requirements.txt
		python setup.py install

test:
		python -m pytest tests

.PHONY: init test
