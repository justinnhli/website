Title: Firefox Bookmark Keywords
Date: 2008-03-03 05:23
Author: justinnhli
Slug: firefox-bookmark-keywords

I had talked before about using Firefox's bookmark keywords, where you
can type a (few) letter(s) into the address bar and it will go to that
bookmark. This is even usable with arguments, so for example I can do:

`gm Chicago IL`

to get a Google Map of Chicago.

This usually works great, except when I want that page as it would be by
default. Because Firefox uses '`%s`' to signify where the arguments
would go, if I just type '`gm`' and hit enter, Google Maps will instead
look for a place called '`s`', which is usually in Mexico (strange).

The solution that I recently came up with was to put a space before the
'`%s`'. It made sense when I came up with it, but now I can't vocalize
why it would get rid of the %s if it is preceded by a space. But now, I
can get to Google Maps proper with just '`gm`'.

