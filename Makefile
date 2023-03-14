PELICAN = $(shell which pelican)

.PHONY: html

default: html

html:
	$(PELICAN) --settings settings.py --output html src

serve: html
	cd html && python3 -m http.server

publish: html
	find html -name '.*.un~' -exec rm -f {} +
	find html -name '.*.swp' -exec rm -f {} +
	rsync --archive --progress --rsh=ssh html/ justinnhli.com:/home/justinnhli/justinnhli.com

clean:
	rm -rf html
