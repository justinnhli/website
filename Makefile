PELICAN = $(shell which pelican)

.PHONY: html

default: html

html:
	$(PELICAN) -v -o html -s settings.py src

publish: html
	find html -name '.*.un~' -exec rm -f {} +
	find html -name '.*.swp' -exec rm -f {} +
	rsync --archive --progress --rsh=ssh html/ justinnhli.com:/home/justinnhli/justinnhli.com

clean:
	rm -rf html
