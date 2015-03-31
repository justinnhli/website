PELICAN = $(shell which pelican)

.PHONY: html

default: html

html:
	$(PELICAN) -v -o html -s settings.py src

publish: html
	rm -f $(find . -name '.*.un~')
	rm -f $(find . -name '.*.swp')
	lftp sftp://justinnhli@rawhide.dreamhost.com -e "mirror -vvvR --only-newer --ignore-time html justinnhli.com ; quit"

clean:
	rm -rf html/*
