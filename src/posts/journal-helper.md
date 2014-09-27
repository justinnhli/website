Title: Journal Helper
Date: 2008-01-06 04:49
Slug: journal-helper

I thought I would say a few things about my other journal.

I've kept it for 6 years, my first entry on 2002-04-18. The funny thing
about that is I had started writing because I wanted to try programming
a database, and journaling software was the first thing I thought of; I
had written the first few entries as test data. The program I wrote then
has long been deleted, but the entries remain. Well, I actually lost the
first five or so when I deleted the directory containing the program,
but what could I do.

The original journals were written in one plain text file, one line for
the date and one line for the concatenated text. The test text didn't
need paragraphs, but now I just dump them all into one line. Since I've
given up my journaling program, I've instead put the entries into HTML
files, one year per file. The advantage there is that I can read my
journal in a web browser, and the text will word wrap automatically. I
still read my entries in a browser sometimes, especially when I need to
read chronologically.

Most of my reading, however, is done in a terminal. I wrote a script a
while back since I started using Linux heavily. Besides giving me
options for doing statistics on my entries (how many entries I've
written, how often I write, the most common words I use) and giving me a
single command to backup my journal, it does a pretty neat conjunctive
search. Because I have over 1000 entries with 700,000 words (see? the
script comes in useful), it's becoming increasingly hard to find
previous events to reference. Instead, I would do a simple search for
it. For example, I might remember going a school concert then watching a
movie. I could simply do

    ./tools -Sd concert movie

and that will give me all the dates in which the words 'concert' and
'movie' appears. Again, it's a neat little script that takes all the
search terms and uses them in grep, piping them one after the other.
Such is the power of Linux.

I haven't changed the basic layout of my journal for a few years now,
but lately I've been trying to think of a different format. Because grep
doesn't how I have one line for dates and one line for the text, it has
problem searching for a certain date. If I want entries which reference,
say, the entry for Christmas of 2005, the output will be all messed up,
since it actually matches the date of the entry, but gives the text of
the entry before that (since it's the line above, which is how it gets
the date). There's probably a really easy way of changing the script to
handle that, but I haven't found it yet.

