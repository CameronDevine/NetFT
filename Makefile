.PHONY: build upload clean doc

build:
	python setup.py sdist bdist_wheel --universal

upload:
	twine upload dist/*

clean:
	rm -rf *.egg-info build dist doc/build

doc:
	sphinx-build doc doc/build
