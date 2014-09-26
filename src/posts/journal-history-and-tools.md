Title: Journal History and Tools
Date: 2008-12-12 20:00
Author: justinnhli
Slug: journal-history-and-tools

When I first started writing in my personal journal (not to be confused
with this blog), it wasn't because I want to keep track of what I've
done or been through. It was because I wanted to write a journaling
program, and needed entries to test said program. I believe at the time
I hit a limitation where Java could only read 1024 characters at a time.
I'm pretty certain that's not true now, but as I wasn't as good a
programmer then, I gave up on the project.

My "test data" lived on, however, and came to be my journal.

In the 6.5 years I've written in my journal, it has gone through several
formats. I don't remember what it was when I first started, but around
2005 I turned my journal in HTML pages. I reasoned that I wanted to be
able to access this from anywhere, and as long as I have a browser
available I can read and search it.

In the next few years I became increasingly uncomfortable with putting P
and BR tags in front of my writing. So this past July, I finally broke
down, removed all the HTML code, and turned it to text, plain (pun
intended) and simple.

To help with my searching of the journal, I have written a bash script.
Here's the help:

`Usage: journal OPERATION [OPTIONS] [ARGS...]    -A archive to a datetimed tarball    -C count the number of entries    -D DATES ...        find entries by date    -F[cin]        term frequency        -c capitalized words only        -i ignore case        -n proper nouns only    -S[i][cd][r DATE DATE] TERMS ...        search entries for TERMS        -c only display number of results        -d only display date of results        -i ignore ignore case        -r YYYY[-MM[-DD]] YYYY[-MM[-DD]] resuls must be in given date range    -T generate tags file    -W wordcount of journal    -h show this help and quit`

As you can see, this script does a number of things. Let me explain each
operation.

-   -A: the archive operation. This puts everything in the directory
    into a tarball (that is, a compressed Tape ARchive file... go nerds)
-   -C: go 1, 2, 3, 4, and so on for every entry. Really, I don't think
    I need to explain more.
-   -D: find entries written on certain dates. So for example,
    2005-12-25 for Christmas of 2005, or 2005-12 for anything in
    December 2005, or just 2005 for the whole year.
-   -F: this is a new addition. It lets me see what words I use the
    most, by counting them and sorting by frequency. The further
    options, i and c, do exactly that. The proper noun option is
    interesting: it looks for capitalized words in the middle of a
    sentence. So it disregards, for example, the "so" at the beginning
    of this sentence, but would pick up "Tape ARchive" above.
-   -S: the main purpose of this script. It lets me to searching with
    some flexibility. You can put several words together, say "christmas
    easter" to find entries that mention both. Since beneath the hood it
    uses grep, I can also do disjunctive search, so "christmas|easter"
    would give entries that mention either "christmas" or "easter" or
    both. The r option, which lets you specify the dates of the entries
    you're looking for, is a new addition, I believe around this past
    summer.
-   -T: generates a vi tags file. This lets me do the same thing as HTML
    in-page anchor links, so I can jump from the reference to an older
    entry to the entry itself.
-   -W: self explantory.

I actually use this script a lot, whenever I'm looking up things I've
previously written.  There are a few things I want to try though:

-   turn the searching into full Google style, to support grouping (the
    use of parenthesis, so "(christmas and thanksgiving) or easter"
    would find entries with either the word "easter" or *both*
    "christmas" and "thanksgiving". It would also be nice to have the
    "-" operator, to specify entries *without* a word.
-   I recently tried to do some linguistics with this by reducing words
    to it's root/stem. So "reduce", "reduced", "reducing", "reduction"
    would all be converted to "reduce", and searching for "reduce" would
    find all these words. I succeed in writing a stemmer (based on the
    [Porter Stemming
    Algorithm](http://tartarus.org/%7Emartin/PorterStemmer/index.html)),
    but it turns out implementing it in Bash is way too slow. I have a
    stemmer though. I think I might email it to Porter for people's
    future reference.

