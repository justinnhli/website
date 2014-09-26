Title: Trains and Skip Lists
Date: 2009-03-20 05:00
Author: justinnhli
Slug: trains-and-skip-lists

I was on the El to the airport the other day (for my Michigan visit,
actually), and I was wondering how the train system could be improved.
Someone once suggested that the network should be built like a spider
web centered around down town Chicago. There would be trains which take
you down town, but also other lines which circle the city. A line like
that would certainly make the trip from Evanston to O'Hare a lot
shorter, but it's a costly way to make the train system efficient.

Instead, as a <span style="text-decoration:line-through;">nerd</span>
computer scientist, I thought about how trains are kind of like [linked
lists](http://en.wikipedia.org/wiki/Linked_list). You start at some
node, but to get to another node you have to go through everything
that's in between. This is, of course, as opposed to
[arrays](http://en.wikipedia.org/wiki/Array), where you can just jump to
the node you need.

And then I realized, people have solved this problem in computer science
before. The solution: [skip
lists](http://en.wikipedia.org/wiki/Skip_list). These are not data
structures normally taught in courses (although I heard that has changed
since I took it... sigh), but the principle it functions on is simple.
Going with the train analogy (and only going one way for the moment),
instead of having one train stop at every station, you have several
trains/tracks. One would stop at every station, another would stop at
every other station, then every fourth, eighth, and so on. Getting to
your destination would then involve transferring to trains that skip
more and more stations, stay on that train until its next stop is past
yours, then transfer to slower and slower trains.

Of course, this idea is not new to transportation companies either.
Usually it's given the name "express". The only difference is that the
express tends only to run during rush hours, and not otherwise. That is
understandable - if there aren't that many passengers, profit will be
low or even non-existent if there are several trains going around rather
than just one.

And yet, the tracks are already there. Between Howard and Fullerton the
Red and Purple Lines run on separate tracks. They don't stop at the same
stations (except Belmont), but the tracks are there for this to happen.

So here's what I suggest. Instead of doing the whole skip-2, skip-4,
skip-8 system, which would require a separate track for each train, just
use two tracks. Have the express do a skip-4 or something otherwise in
the middle. The express will then travel roughly 4 times faster than the
normal train, greatly speeding up travel. At the end of each track, just
do a merge to change sides, and the trains are ready to go back.

Unfortunately, in the current economic climate no one will do this. It's
probably prohibitively expensive, and will never get enough passengers.
And the space to get 4 tracks (2 there and 2 back) is also pricey. But
it looks good on paper!

And that is how computer science (tries to) impact real life.

