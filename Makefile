default:
	pelican src -o html -s settings.py

clean:
	rm -rf html/*
