install:
	poetry install

test:
	poetry run pytest page_loader tests

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml tests

lint:
	poetry run flake8 page_loader tests

selfcheck:
	poetry check

check: selfcheck test-coverage lint

build:
	poetry build
	
package-install:
	pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build
