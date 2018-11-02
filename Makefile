.PHONY: all build upload clean

all: build upload clean

build:
	python setup.py sdist bdist_wheel --universal

upload:
	twine upload dist/*

clean:
	rm -rf *.egg-info build dist
