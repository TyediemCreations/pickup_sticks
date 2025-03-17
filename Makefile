VERSION = 1.1.0

test:
	docker build --target test -t pickup_sticks-env .
	docker run -it pickup_sticks-env python -tt -m pytest --cov=pickup_sticks --cov-report term-missing tests
