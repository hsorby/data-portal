.PHONY: all serve

all: serve

serve:
		FLASK_DEBUG=1 FLASK_ENV=development flask run
