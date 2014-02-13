default:
	pelican -v -o html -s settings.py src

clean:
	rm -rf html/*
