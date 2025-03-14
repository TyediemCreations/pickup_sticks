VERSION = 1.0.0

MOCK_VERSION = 5.2.0
PYTEST_VERSION = 8.3.5
PYTEST-COV_VERSION = 4.1.0

TESTING_REQUIRES = \
	"mock" \
	"pytest" \
	"pytest-cov"

test:
	python -tt -m pytest --cov=pickup_sticks --cov-report term-missing tests
