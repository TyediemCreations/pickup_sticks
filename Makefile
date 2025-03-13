VERSION=0.1.0

MOCK_VERSION = 5.2.0
PYTEST_VERSION = 8.3.5
PYTEST-COV_VERSION = 4.1.0

TESTING_REQUIRES = \
	"mock" \
	"pytest" \
	"pytest-cov"

run:
	python -m pickup_sticks

test:
	python -tt -m pytest --cov=pickup_sticks tests
