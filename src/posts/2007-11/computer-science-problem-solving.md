Title: Computer Science Problem Solving
Date: 2007-11-02 23:48
Slug: computer-science-problem-solving

Someone once asked me if studying computer science changes the way I
look at the world. I didn't think so at the time, but now I see that
maybe there are some influences. I can't say whether it's a good or bad
influence, but it definitely makes my thinking a lot more abstract.

Recently, my professor brought up an interesting viewpoint, that
programmers are actually using a lot of known solutions in solving
problems with the computer. The thought stuck in my mind, and the more I
think about it, the more true it seems. Here are a couple analogies that
map from computer science to the real world.

The example my professor gave was about traffic lights. Why do we have
traffic lights, and what purpose do they serve? After asking a number of
exploring questions, we arrive at that traffic lights are really there
to ensure a fair sharing of resources, that resource being the
intersection of two roads. Since the intersection technically belongs to
both roads, it's impossible to say which cars have precedence. The
traffic lights are to enforce which cars can go into the intersection at
what time.

During the discussion, I eventually realized that traffic lights are
actually mutual exclusion (mutex) locks, that prevent two different
users from doing something at the same time. If one road's is passing
through the intersection, the other road's can't. The whole idea of
mutual exclusion, of course, is from memory sharing between processes,
and how to prevent one program from overwriting another's work.

The professor then went on to other types of resource sharing, such as a
talking stick, which shares the right to talk. Everyone sits in a
circle, and who ever has the stick is allowed to talk. The computer
analogy to that was a token ring network, which I'm not familiar with.

Here's another fun analogy: sorting. This is a pretty prevalent
"problem" in computer science. By "problem" I mean it needs to be done
all the time, even though we already know the best way to do it:
quicksort. It is interesting to see a number of different types of
sorting in real life, however.

For example, if I hand you a deck of cards, how would you sort it? You
would probably go through and separate the diamonds from the clubs,
hearts and spades, and then sort each one individually. Note however
that when sorting each suit, you don't separate the cards into separate
piles (say, less than 4, 4 to 8, larger than 8), but might pick out
cards in ascending order. Another way to do the same within each suit is
to go through the stack and when you get to an out of order card, put it
in order in the part you've already gone through.

It turns out that there are algorithms that do all three of these
sorting techniques. When the items are put into categories before being
sorted, it's called a bucket sort. If you go through the items to pull
out the next one in line, it's a selection sort. The last one, because
the items are taken out and put into the correct position, is called
insertion sort.

I'm sure if I take the time I can think of more examples. My point here
though is that computer scientists use a lot of solutions to common
problems that we've already solved. We've sorted things before, and have
shared resources before, just not on computers. And if the base problem
is the same, then why not move the solution over to the domain as well?

Going back to the original question: does studying computer science
change the way one thinks? My answer is yes, but only in terms of
abstracting out these patterns in life. People don't become bound to
certain rules or boxed by their thinking in this way; it will only help
by making more connections.

