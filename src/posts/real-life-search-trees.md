Title: Real Life Search Trees
Date: 2007-10-21 22:17
Author: justinnhli
Slug: real-life-search-trees

I've known this for a while, but was reminded of it when I visited the
library today and thought I should share.

The main Northwestern University library has a very strange structure.
Inside each level in each tower, the book shelves are arranged in a
circle, so that each shelve is on a diameter. Books are arranged by call
number along the radius. That is, if you call the direction of the door
0 degrees, the further you go clockwise, the higher the call number.

To make the NU library configuration clearer, [here's a
map](http://www.library.northwestern.edu/facilities/main_level_3_4.html)
of a standard floor. The lines arranged in a circle are shelves.

Compared to normal libraries, where the shelves are arranged by call
number in rows, this makes no sense at all. But get this: finding a call
number is quicker in the circular system than the traditional system.

Here's the reason. Because the shelves at NU are not all along the
circumference, but have a distance from the center, the shelves
essentially form a [search
tree](http://en.wikipedia.org/wiki/Binary_search_tree). Instead of
starting from where you enter, you walk to the center first. Then just
follow down the aisle which has a call number closest to the book you
want. In mathematical terms, the shelves have a depth of roughly 3 and a
branching factor of 2, which makes the books really easy to find. Of
course, once you get to the correct shelf you have to find the book the
normal way.

In contrast to the tree structure of NU library, traditional libraries
is a linked list. You have to walk through shelves with a lower number
before you get to the shelf you want. There's no short cut for this
process. Therefore, the NU library search time is logarithmic (log base
2), while traditional libraries have a linear search time.

I don't think too many people know this. Today was the first time I saw
someone (besides myself) going to the center first and finding books
that way. Shame.

