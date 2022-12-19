POETRY = poetry run
WORKDIR = yatube_api

style:
	$(POETRY) black -S -l 79 $(WORKDIR)
	$(POETRY) isort $(WORKDIR)

lint:
	$(POETRY) flake8
	$(POETRY) mypy $(WORKDIR)

test:
	$(POETRY) pytest -vv

