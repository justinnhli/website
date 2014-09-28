.PHONY: html

default: html

html:
	pelican -v -o html -s settings.py src

publish: html
	lftp sftp://justinnhli@rawhide.dreamhost.com -e "mirror -vvvR --only-newer --ignore-time html justinnhli.com ; quit"

clean:
	rm -rf html/*
