# Quick and dirty Makefile deployment
#
# SPDX-FileCopyrightText: Copyright (c) 2022 Tammy Cravit
#
# SPDX-License-Identifier: MIT


PROJECT_NAME     ?= tmt_carddeck
CIRCUP           ?= $(HOME)/.pyenv/shims/circup
CPY_VOLUME_NAME  ?= CIRCUITPY
CPY_DRIVE        ?= /Volumes/$(CPY_VOLUME_NAME)
CODE_PY_FILENAME ?= $(PROJECT_NAME)_test.py
SECRETS_PY_FILE  ?= $(HOME)/projects/circuitpython_secrets.py
LIBRARIES_LIST   ?= adafruit_adt7410 adafruit_bitmap_font adafruit_bus_device \
					adafruit_display_notification adafruit_display_shapes \
					adafruit_display_text adafruit_displayio_layout \
					adafruit_esp32spi adafruit_fakerequests adafruit_imageload \
					adafruit_io adafruit_itertools adafruit_minimqtt \
					adafruit_miniqr adafruit_pixelbuf adafruit_portalbase \
					adafruit_progressbar adafruit_pyportal adafruit_requests \
					adafruit_sdcard adafruit_slideshow adafruit_ticks \
					adafruit_touchscreen asyncio neopixel simpleio

help: ## Show this help
	@echo "\033[34m******************************************************************************\033[0m"
	@echo "\033[34m***                Simple CircuitPython Deployment Makefile                ***\033[0m"
	@echo "\033[34m***        Tammy Cravit || tammy@tammymakesthings.com || 2022-05-07        ***\033[0m"
	@echo "\033[34m******************************************************************************\033[0m"
	@echo ""
	@echo "\033[33m==========================> Configuration Variables <=========================\033[0m"
	@echo "\033[36mPROJECT_NAME\033[0m         $(PROJECT_NAME)"
	@echo "\033[36mCIRCUP\033[0m               $(CIRCUP)"
	@echo "\033[36mCPY_DRIVE\033[0m            $(CPY_DRIVE)"
	@echo "\033[36mCODE_PY_FILENAME\033[0m     $(CODE_PY_FILENAME)"
	@echo "\033[36mSECRETS_PY_FILE\033[0m      $(SECRETS_PY_FILE)"
	@echo ""
	@echo "\033[33m=============================> Makefile Targets <=============================\033[0m"
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""


libinstall: ## install needed libraries (with circup)
	$(CIRCUP) install $(LIBRARIES_LIST)

libupdate: ## update all libraries (with circup)
	$(CIRCUP) update --all

deploy: ## deploy the project to the CircuitPython device
	cp $(SECRETS_PY_FILE) $(CPY_DRIVE)/secrets.py
	cp examples/$(CODE_PY_FILENAME) $(CPY_DRIVE)/code.py
	cp -R assets $(CPY_DRIVE)
	cp -R $(PROJECT_NAME) $(CPY_DRIVE)/lib
	rm -fr $(CPY_DRIVE)/lib/$(PROJECT_NAME)/__pycache__

.PHONY: deploy help libinstall libupdate

.DEFAULT: help
