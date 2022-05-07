# Quick and dirty Makefile deployment

CPY_VOLUME_NAME  ?= CIRCUITPY
CPY_DRIVE        ?= /Volumes/$(CPY_VOLUME_NAME)
CODE_PY_FILENAME ?= tmt_carddeck_test.py
SECRETS_PY_FILE  ?= $(HOME)/projects/circuitpython_secrets.py

deploy:
	cp $(SECRETS_PY_FILE) $(CPY_DRIVE)/secrets.py
	cp examples/$(CODE_PY_FILENAME) $(CPY_DRIVE)/code.py
	cp -R assets $(CPY_DRIVE)
	rm -fr tmt_carddeck/__pycache__
	cp -R tmt_carddeck $(CPY_DRIVE)/lib

.PHONY: deploy

.DEFAULT: deploy

