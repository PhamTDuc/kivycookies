.PHONY: help, hello.world

help:
	@echo test - run the test py.test suite
	@echo coverage - generate a coverage report and open it
	@echo docs - generate Sphinx HTML documentation and open it

hello.world:
	@python -m helloworld