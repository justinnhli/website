Title: Musings on Human-Level Artificial Intelligence
Date: 2009-01-23 06:00
Author: justinnhli
Slug: musings-on-human-level-artificial-intelligence

I've been thinking a lot about human-level artificial intelligence (for
convenience and humor, let's just call it HAI) lately. I suppose it
started in November, when I was looking at Carnegie Mellon for grad
school and I stumbled across Professor Scott Fahlman's blog, "Knowledge
Nuggets". Although his research is in knowledge representation, he
writes about HAI as well. In several posts, he outlined what we are
missing in current AI research, and what he thinks a knowledge base (KB)
for HAI would be like. Although I've never communicated with him, he was
the main reason I chose to take Knowledge Representation this quarter
instead of Introduction to Computational Linguistics. It reminded me
that my real interest is in the artificial creation of a psychology. For
a while I was distracted by other, perhaps much easier and more
practical fields of AI like textual analysis, but reading Fahlman's blog
brought back my interest in strong AI (an AI which can actually think,
as opposed weak AI, which only gives the appearance of thinking).

Since then I have thought more about this problem, and I would like to
use this post to organize my thoughts. Reading first Alan Turing's
essays from the beginning of the digital computer and his visions of
what computers can do, then Douglas Hofstader's Godel, Escher, Bach on
symbols manipulating symbols, resulted in a large number of ideas.
Comparing those ideas with the current state of AI, I also see some
difficult problems to solve. I would love to tackle some of them, and
while I don't think having HAI is impossible within my lifetime, it will
definitely take a lot of smart people and clever innovations.

Let me start, then, with a quote from Turing, from his paper "Computer
Machinery and Intelligence":  

> Instead of trying to produce a programme to simulate the adult mind,
> why not rather try to produce one which simulates the child's?
> </p>

It occurred to me that a lot of AI research is done in replicating what
we see in adults. This not only applies to early AI research, when
theorem provers and chess masters were written. Planning, problem
solving, knowledge representation, reading and understanding language...
these are all behaviors which humans learn relatively late in life.
While I don't doubt there are many practical applications of results
from these areas - that may perhaps even be the reason *why* there is so
much research - it seems difficult if not impossible to arrive at a
general HAI from this direction. Intelligence itself is a complex enough
creature; studying it after it has matured and grown is like trying to
reconstruct a tree. Although recreating the tree may be the ultimate
goal, studying the structure of the seed is the better path for
research. A successful replication of the seed necessarily leads to the
replication of the tree, and yet the seed is infinitely simpler than the
tree with its myriad of branches and leaves and flowers.

Similarly, understanding the cognition of a child - or perhaps even an
infant - might be a more worthwhile direction of research. Continuing
from Turing's previous quotation:  

> If this [the child brain] were then subjected to an appropriate course
> of education one would obtain the adult brain. Presumably the child
> brain is something like a notebook as one buys it from the
> stationer's. Rather little mechanism, and lots of blank sheets.
> (Mechanism and writing are from our point of view almost synonymous.)
> Our hope is that there is so little mechanism in the child brain that
> something like it can be easily programmed.
> </p>

Of course, I understand that while there may be little in the brain,
that doesn't mean that it's not *complex*. It's simply because it's
*less* than an adult brain that it's our object of study. A similar
argument can be made for studying the brains and intelligence of other
animals, and there would probably be contributions to be made there, but
the gap between human intelligence and animal intelligence is too wide
to only study animals.

Here, I would like to point out that studying the intelligence of humans
or animals is not the equivalent of studying the brains of humans or
animals. Studying the neurological processes in the brain to arrive at
intelligence would be like building a car from quarks and electrons.
Hofstadter writes:  

> ... we hope that thought processes can be thought of as being sealed
> off from neural events in the same way that the behavior of a clock is
> sealed off from the laws of quantum mechanics, or the biology of cells
> is sealed off from the laws of quarks.
> </p>

Studying neurons again makes the problem too complex. That is not to say
the neurological study of the brain is useless. We can learn much about
human intelligence if we could  

> ... step back... towards a higher, more chunked view. From this
> vantage point, we hope we will be able to perceive chunks of program
> [or groups of neurons] which make each program [or group] seem
> rationally planned out on a global, rather than a local, scale - that
> is, chunks which fit together in a way that allows one to perceive the
> goals of the programmer [or the brain]... There is some sort of
> abstract "conceptual skeleton" which must be lifted out of low levels
> before you can carry out a meaningful comparison of... two animals [or
> intelligences].
> </p>

That was Hofstadter again. The assumption is that intelligence can be
abstracted out from the neural structure and implemented on a computer.
There is of course a chance that this assumption is unjustified, in
which case strong HAI is impossible.

But taking the assumption for now, what "mechanism" does a child brain
(from here I will use the words "brain" and "mind" interchangeably, to
match Turing's wording) consist of? In a letter from Christopher
Strachey to Turing, he wrote:  

> I am convinced that the crux of the problem of learning is recognizing
> relationships and being able to use them... there are, I think, three
> main stages in learning from a teacher. The first is the exhibition of
> a few special cases of the rule to be learned. The second is the
> process of generalization - ie. the underlining of the important
> features that these cases have in common. The third is that of
> verifying the rule in further special cases and asking questions about
> it.
> </p>

I think what Strachey said has credit, and I will return to it
momentarily. There are, I think, other considerations. Without saying, a
child brain in the form of a computer and a child brain in the form of a
human has significant differences. The biggest one is the lack of
physical environment, or to give it another name, reality. A lot of what
the child first learns relates to the external environment. Infants at
around 10 months of age learn that objects still exist when out of
sight; before that, however, when infants see a toy hidden under a
blanket, they wouldn't know to look under the blanket for it. This is
called object permanence, and is a perfect example of how the
environment helps children's cognitive development. Presumably they
notice that objects keep reappearing when they disappear, and eventually
realized that objects do not in fact "disappear".

How can a HAI learn such a concept without the environment around it? It
may turn out that getting an abstract intelligence doesn't require
learning object permanence. This would be a great test of the abilities
of a developing HAI though. There is another, more serious, potential
consequence of existing in digital space: the HAI may never learn
language. Language is partially a mapping, through the phonetic sounds
we produce, between our thoughts and objects in the real world. If a
computer never "encounters" a chair, it wouldn't know what a chair is.
More disturbingly, a computer never encounters the three dimensional
space we live in. A number of other concepts familiar to us as humans
become meaningless for a disembodied HAI. As Hofstadter wrote, "thoughts
must depend on *representing reality in the hardware of the brain*." For
a HAI to have thoughts, then, there must be some reality in which it
exists whether real (such that the HAI is embodied in a robot) or
virtual (a digital, artificial reality which we have control over). In
either case, the environment should not only be passive, but created
such that the HAI could react to it. A particularly interesting idea I
had was to give the HAI a lower dimension reality - so it lives on a
plane, and its "vision" consists of a colored line. This simplification
serves both the purpose of giving the HAI an environment, while keeping
it simple enough for it to understand and for us to understand its
understanding.

Assuming these external (to the HAI) issues are solved, we now turn back
to the problem of what internal mechanisms a child brain must have to
being the learning process. What is the starting state, the tabula rasa
from which knowledge will be written? It seems to me that the ability to
recognize patterns is of utmost importance. Without it we wouldn't learn
object permanence, or recognize that an armchair and a stool both belong
in the category of chairs. The whole idea of creating ontologies, which
is what KBs are, is based on the ability to recognize patterns and
classify objects. The way we learn, too, is from recognizing patterns:
we classify both hand written and printed letters as part of the
alphabet, and we look at past experiences for insight on how to solve
unfamiliar problems.

The last point on solving unfamiliar problems actually pushes the
ability behind simple recognition of patterns to *using* these patterns,
what Strachey called "the process of generalization". I will give it
another name: induction. Note that this is not the mathematical meaning
of induction - the reduction of an infinite number of cases to finite
base cases - but the reasoning meaning of induction. We may burn our
fingers once, twice on a hot stove, and we learn to stop putting our
fingers on stoves or other hot objects. There are more abstract
generalizations, too. We learn the quadratic formula by applying it on
many different equations, but we know that the formula doesn't only
apply for these exact numbers: it applies for any equation of the same
form. This is due to our generalization of the pattern we have
recognized in the equations which the formula solves.

There are admirable advances in pattern recognition. Within a KB, a
Structure Mapping Engine (SME) can make analogies between two domains.
This is how it works. The KB contains statements about how different
components of a domain relate. SME first finds a relationship which
exists in both domains; the things related by this relationship are then
mapped onto one another. Each of these mappings be generate deeper
mappings - that is, there are more relationships that are similar in
these components. These nested relationships give each domain a
*structure* - hence the name of the engine. By comparing not the actual
objects but the relationships between objects in the two domains, a
"deeper" analogy is drawn.

While this is a highly successful way of recognizing patterns and a
solid step towards HAI, I can see at least one extension to the KB-SME:
the pattern found should be added back into the KB as an object of its
own. This stems from the fact that humans do not only reason on one
level, but finds patterns made up of patterns, and patterns made up of
those, and so on. Induction is the step for the HAI to create an
ontological KB for itself, and is necessary for it to learn anything of
significance. This is of course, easier said than done: how should the
pattern be represented?

This, in fact, leads to a broader question: how should anything be
represented in the first place? The idea of creating a child HAI is not
complicated, but it brings into question many processes which we do not
yet understand about our brains. If the child brain is to be "lots of
blank sheets", how are the perceptions of the HAI written on the blank
sheets? The knowledge in the knowledge bases currently in use all came
from humans; some programmer/knowledge worker devised an organizational
scheme, and the objects are related correct to each other. For humans
there is some hard-wired method of translating our sensations into
objects of thought. Children don't know what any "thing" is when they
are born, but eventually they have the concept of a generic "object".
Not only do they have the concept, but they can reason with such a
generic object without ever having seen one. Without the abstract
representation of the world, an induction engine - no matter how good -
will be useless.

Not that our unbuilt HAI has a good induction engine. There is a large
obstacle in this area as well: how should the actions of the HAI be
represented such that the HAI can change them? To take a simple case, I
am capable of using deductive logic. When I first learned it, I probably
made lots of mistakes, for example, affirming the antecedent. But as I
learned about logical fallacies, my thinking changed as well. I not only
stopped myself from making these errors, but I am able to catch myself
when I do make them. The same kind of introspection is need when we try
and fail to remember a salient event (say, ate breakfast with the
president), and therefore know it did not happen. The method of thinking
suddenly became the object of thinking. It is perhaps not co-incidental
that this forms the kind of "strange loop" which lies at the heart of
Hofstadter's book. Without the ability to modify its own behavior, any
HAI will still only be following algorithms and incapable of truly
surprising us - not to mention not really a HAI.

The opposite end of the same problem is, what set of algorithms should a
HAI not be able to change? There are processes which I cannot stop
myself from doing - the best example being the recognition of faces in
inanimate objects. I could not change how I look at faces any more than
herring gull chicks can stop pecking at yellow sticks with red spots.
Similarly, the will be aspects of a HAI which is hard coded; the
perception of causality being a highly possibly example. More over, it
is impossible for every line of code to be modifiable by the HAI itself.
The answer to this question would not only be what needs to be hard
coded for the HAI to learn, but also how little can be hard coded to
have the same affect.

An additional difficulty of modifiable processes is that current KBs are
ill suited to hold procedural knowledge. This runs against the current
consensus that procedural knowledge and declarative knowledge is kept
separately. Episodic memory should be included in the knowledge base as
well, since this forms the basis of induction as well as the subjects of
thought. Both these types of knowledge requires that the causal and
temporal relationships in current KBs be greatly expanded and specified.
It would be interesting to build a microtheory on action and its
possible consequences.

I have presented a few ideas here, but also raised a lot of obstacles
which the path to HAIs must conquer. I would just like to close by
saying that, creating a HAI may not in fact by very illuminating for
human cognition. When a HAI does start learning, all the symbols it
creates will be radically different from the symbols we use; we may not
be able to assign meaning to those symbols at all. Of course, that
doesn't diminish the allure of creating a human-level artificial
intelligence at all.

