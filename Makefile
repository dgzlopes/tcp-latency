.PHONY: install-hooks
install-hooks:
	tox -e pre-commit -- install -f --install-hooks

.PHONY: test
test:
	tox

.PHONY: clean
clean:
	find -name '*.pyc' -delete
	find -name '__pycache__' -delete

.PHONY: publish
publish:
	pip install wheel twine
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg tcp_latency.egg-info
.PHONY: super-clean
super-clean: clean
	rm -rf .tox
	rm -rf venv
	pyenv local --unset
