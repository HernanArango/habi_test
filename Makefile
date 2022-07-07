.PHONY: dev
install:
	pip install -r requirements.txt
test:
	pytest
run:
	python server.py