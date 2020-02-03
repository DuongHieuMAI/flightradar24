init:
	pip3 install --user -r requirements.txt

test:
	py.test --cov-report term --cov=flightradar24
