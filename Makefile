.PHONY: html

default: html

html:
	pelican -v -o html -s settings.py src

publish: html
	lftp sftp://justinnhli@rawhide.dreamhost.com -e "mirror -vvvR html justinnhli.com ; quit"

clean:
	rm -rf html/*
