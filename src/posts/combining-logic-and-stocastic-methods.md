Title: Combining Logic and Stocastic Methods
Date: 2007-10-09 20:42
Author: justinnhli
Slug: combining-logic-and-stocastic-methods

This is a computer science heavy post, so if you don't have the stomach
for a lot of abstract, mathematical, theoretical ideas, you'd better
skip this one.

I hope you would read it though.

Right now you can say that there are two big camps in artificial
intelligence: those whose methods are based on logic, and those whose
methods are based on mathematics.

One logic based system would be Cyc, a knowledge base which can reason.
So if you put in "All men are mortals; Socrates is a man;" the program
can tell you that "Socrates is a mortal." Well, not in plain English
(although professor Chris Riesbeck and others are working on that), but
it has an understanding of what those words mean. It connects, say,
George Bush with USA, presidency, war on Iraq, and so on. Basically,
it's the "common sense" that a lot of people feel computers don't have.

On the other hand are stochastic or statistical systems, generally
labeled "machine learning" systems. They operate mostly on numbers,
although some use strings and other data structures as well. Most of the
cool-sounding AI techniques are in this category, including neural
networks and genetic algorithms. These programs are essentially giant
calculators, which take past events into account and try to
mathematically create the optimal solution. For example, a photograph
with a sun in it would have a much brighter spot somewhere on the
surface, and the program could analyze the distribution of light over
the surface to categorize whether a photo has the sun in it or not. It
doesn't really know what a sun is (a star that gives off heat and
light), but it does the job.

Obviously, both sides have their advantages and weaknesses, or there
wouldn't be two camps. The logicians require large amounts of data
beforehand - where the computer stores all that common knowledge - and
it could take a very long time to logically derive anything. Using the
Socrates example again, it also knows that men have two legs and dogs
don't have four legs, so it might conclude that Socrates is not a dog,
which is not very useful at all. The main problem here is how to sort
through all this junk. For stochastic methods, the problem is the
opposite. It is relatively faster than logic, but it doesn't really know
much about the thing it's doing. You can say that there is no creativity
involved, no way to do something unexpected. They are in a sense limited
to what they were programmed to do, within a very specific domain.

So the idea I had, and have held it for a while now, is to introduce
statistics into a knowledge base. This is how it will work. Cyc is
essentially built on connections between ideas, a hierarchy of different
relationships. Buying might be a subset of all possession transfers,
which in turn might be a subset of all human interactions.

The problem is that each idea, object, and relationship has so much
other stuff connected to it, you don't know where to begin. Example: a
story about animals making false cries of danger might induce thoughts
of Boy who Cried Wolf. There is however a lot of junk in both those
stories, when the central concept is very abstract, that of deceiving
others as entertainment and a trade off between humor and protection.
Humans can find connections without a problem, but machines have to
explore millions of concepts to hit on the right now.

So what you can do (or try do to; this is a theoretical discussion) is
put a weight on each relationship. Wolves might be more connected to
animals than to dogs, and birds more to doves than to penguins. Humans
have a tendency to use shortcuts, cognitive heuristics so we don't just
stand and think the whole day. Statistical information about the
strength of each link would be similar, allowing the machine to know
which links are more commonly encountered, and therefore should be
explored first.

Taking knowledge bases as relationships between objects, the entire KB
can be seen as a mathematical graph. And with statistical linkage
associated with each link/edge, guess what? We now have a undirected
weighted graph on our hands. The theorem proofer can now rely on the
large amount of graph algorithms (Dijkstra's algorithm, A\* search) to
either find the shortest path to proof a statement, or to generate new
statements. There is still the matter of the machine not knowing what
results are important, but that's a different problem.

One last thing about the statistics: one way to get the different
weights between different (but related) objects would to be search
another knowledge base: Wikipedia. Although Wikipedia is written in
English, the text is still somewhat machine readable. For example, the
machine will know to link to other pages if the user encloses something
in double brackets ([[ ]]). So one easy way to find the links is take
the inverse of the number of links it takes to link two wikipedia pages.
This is in fact another graph traversal problem, but much more easily
solved. So objects which are link directly to each other (say dog and
animal) would have a much higher chance of being evaluated than objects
far apart (say dog and black holes).

I think that's one way to take advantage of both worlds. I don't know if
this has been done before, and I'm not really in a mood to find out.

