VERSION = 0.3.0

MOCK_VERSION = 5.2.0
PYTEST_VERSION = 8.3.5
PYTEST-COV_VERSION = 4.1.0

TESTING_REQUIRES = \
	"mock" \
	"pytest" \
	"pytest-cov"

# If the first argument is "run"...
ifeq (run,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "run"
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(RUN_ARGS):;@:)
endif

.PHONY: run
run:
	python -m pickup_sticks $(RUN_ARGS)

test:
	python -tt -m pytest --cov=pickup_sticks --cov-report term-missing tests
