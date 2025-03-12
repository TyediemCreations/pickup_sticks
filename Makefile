VERSION=0.1.0

MOCK_VERSION = "5.2.0"
PYTEST_VERSION = "8.3.5"

TESTING_REQUIRES = \
	"mock" \
	"pytest"

run:
	python -m pickup_sticks

test:
	python -tt -m pytest tests
