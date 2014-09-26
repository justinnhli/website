Title: Outliner
Date: 2007-12-11 04:33
Author: justinnhli
Slug: outliner

Since I'm basically done with my natural language processing project
this quarter, I thought I would write down an idea I have for my project
next quarter for practicum.

Either I would do the [ToA
Constructor](http://ninghui48.blogspot.com/2007/11/toa-constructor.html),
or I would write something which can extract the structure of a
document.

As it appears it me is should be simple. The first thing to try is to
grab the HTML header tags, which would of course indicate a title. I
don't think that will work on too many pages though, since not a lot of
people like them. The next thing would be grabbing everything under a
certain word length that's on a line by its own. I can think of them
being either headings, or one liners made for effect. That's basically
it. If these two don't work, I suppose we could also try scanning for a
larger font size, but that takes in account CSS and all the other SGML
junk, and is a lot harder to do.

Although, somehow I don't think I'll be working on this next quarter.
But it's an idea.

