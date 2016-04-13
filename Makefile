PELICAN = $(shell which pelican)

.PHONY: html

default: html

html:
	$(PELICAN) -v -o html -s settings.py src

publish: html
	find html -name '.*.un~' -exec rm -f {} +
	find html -name '.*.swp' -exec rm -f {} +
	lftp sftp://justinnhli@justinnhli.com -e "mirror -vvvR --only-newer --ignore-time html justinnhli.com ; quit"

clean:
	rm -rf html
