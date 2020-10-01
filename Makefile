.PHONY: help, hello.world

help:
	@echo "test - run the test py.test suite"
	@echo "coverage - generate a coverage report and open it"
	@echo "docs - generate Sphinx HTML documentation and open it"
	@echo "apk - build an android apk with buildozer"
	@echo "deploy - deploy the app to your android device"
	@echo "po - create i18n message file"
	@echo "mo - create i18n locales files"

hello.world:
	@python -m helloworld