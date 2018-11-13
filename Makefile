PELICAN = $(shell which pelican)

.PHONY: html

default: html

html: html/files/pygments.css
	$(PELICAN) --debug --verbose --settings settings.py --output html src

html/files/pygments.css:
	mkdir -p html/files
	pygmentize -S bw -f html -a .codehilite > $@

serve: html
	cd html && python3 -m http.server

publish: html
	find html -name '.*.un~' -exec rm -f {} +
	find html -name '.*.swp' -exec rm -f {} +
	rsync --archive --progress --rsh=ssh html/ justinnhli.com:/home/justinnhli/justinnhli.com

clean:
	rm -rf html
