Title: Text Based Mind Map
Date: 2007-10-21 17:59
Slug: text-based-mind-map

Last year for my learning and organizational change class I visited
Willard for a meeting. Willard has a "library" of sorts, which is really
just a bookshelf with some old books people never read. One of books on
that shelf was James Gleick's *Genius: The Life and Science of Richard
Feynman*. I was more attracted to the word "genius" than to Feynman,
having no idea who he was at the time. It was a great read, really gets
you into admiring Feynman's intelligence. The passage that gave me this
idea, however, does little to show how smart Feynman is.  

> "In high school he had not solved Euclidean geometry problems by
> tracking proofs through a logical sequence, step by step. He had
> manipulated the diagrams in his mind: he anchored some points and let
> others float, imagined some lines as stiff rodes and others as
> stretchable bands, and let the shapes slide until he could see what
> the result must be. These mental constructs flowed more freely than
> any real apparatus could. Now, having assimilated a corpus of physical
> knowledge and mathematical technique, Feynman worked the same way. The
> lines and vertices floating in the space of his mind now stood for
> complex symbols and operators. They had a recursive depth; he could
> focus on them and expand them in more complex expressions, made up of
> more complex expressions still. He could slide them and rearrange
> them, anchor fixed points and stretch the space in which they were
> embedded. Some mental operations required shifts in the frame of
> reference, reorientation in space and time. The perspective would
> change form motionlessness to steady motion to acceleration. It was
> said of Feynman that he had an extraordinary physical intuition, but
> that alone did not account for his analytic power. He melded together
> a sense of forces with his knowledge of the algebraic operations that
> represented them. The calculus, the symbols, the operators had for him
> almost as tangible a reality as the physical quantities on which they
> worked. Just as some people see numerals in color in their mind's eye,
> Feynman associated colors with the abstract variables of the formulas
> he understood so intimately. 'As I'm talking,' he once said, 'I see
> vague pictures of Bessel functions from Janke and Emde's book, with
> light tan j's, slightly violet-bluish n's, and dark brown x's flying
> around. And I wonder what the hell it must look like to the
> students.'"
> </p>

At first my thought was to write a program that could do physics,
allowing for as much abstraction as the user wanted. For example, one
could model a roller coaster as one train, or as several cars, or as
several cars with people in it, and so on. It has the same "recursive
depth" that Gleick described, except it was for actual objects and not
for equations. And if you think about it, we do this all the time:
understand the whole, and only go into the details if necessary.

I only wrote a sparse amount of documentation then, and never wrote a
single line of code for it. The idea slowly turned from physical
modeling to mind mapping. My problem with mind maps is that, one you
can't search them with computers, and two it gets really messy when you
have lots of stuff on it. The latter is especially true if the lower
branches have a lot of connections, so you have lines flying from this
side to that side. And yet, mind maps are really all about these
connections; without them the mind map would just be a spread out
hierarchy tree.

One way to solve this ugly mess is to visualize the tree in 3D. You
would only see a small part of the tree at a time, a cluster of branches
at the same level. Links to other parts of the tree would be, well,
links, and clicking on them would take you to another cluster of ideas,
with the link highlight somehow. Each individual idea would perhaps be
identified with a URI based on its location in the hierarchy. This way,
any idea can be placed into the map, and be easily linked without making
the map complicated. This would also embed the idea of recursive depth;
one could keep pushing ideas down the tree, and again keep them linked
without uglifying the map.

The only downside I see to this is the lack of complete picture, being
unable to see everything at once. Perhaps on each level the size of the
words would indicate how many nodes and links that branch has underneath
it, giving the map the appearance of a [tag
cloud](http://en.wikipedia.org/wiki/Tag_cloud)?

