default:
	pelican -v -o html -s settings.py src

publish:
	lftp ftp://justinnhli@rawhide.dreamhost.com -e "mirror -R html justinnhli.com ; quit"

clean:
	rm -rf html/*
