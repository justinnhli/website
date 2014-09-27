Title: Sooner apparently means later
Date: 2010-12-21 02:49
Slug: sooner-apparently-means-later

In the mean time, here's a [fun charge on spring
simulator](https://dl.dropbox.com/u/316654/feynman/index.html). It uses
a naive [force-based
algorithm](http://en.wikipedia.org/wiki/Force-based_algorithms_%28graph_drawing%29)
to do the drawing. Those among you with a sharp eye will have noticed I
named this simulation "Feynman", named after of course the famous
physicist [Richard
Feynman](http://en.wikipedia.org/wiki/Richard_Feynman). In his
[biography](http://books.google.com/books?id=IWQ_y90P2uIC&dq=isbn:0679747044&source=gbs_navlinks_s) -
James Gleick's Genius - the author describes how Feynman perceives
equations (he has grapheme-color
[synesthesia](http://en.wikipedia.org/wiki/Synesthesia) specific to
mathematical equations. I have written about the general form
[before](http://justinnhli.com/posts/2009/05/synesthesia.html)). I
quote from the book:

> In high school he had not solved Euclidean geometry problems by
> tracking proofs through a logical sequence, step by step. He had
> manipulated the diagrams in his mind: he anchored some points and let
> others float, imagined some lines as stiff rods and others as
> stretchable bands, and let the shapes slide until he could see what
> the result must be. These mental constructs flowed more freely than
> any real apparatus could. now, having assimilated a corpus of physical
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
> he understood so intimately. "As I'm talking," he once said, " I see
> vague pictures of Bessel functions from Janke and Emde's book, with
> light tan j's, slightly violet-bluish n's, and dark brown x's flying
> around. And I wonder what the hell it must look like to the students.

The idea behind this project was to make an interactive mind mapping
application, where no hierarchy is enforced or even implied - unlike
most mind mapping software such as [XMind](http://www.xmind.net/). This
means a free-form graph layout application. To get the recursive depth,
however, each node will also be a summary representation of another mind
map/graph, so the user can drill down indefinitely to find more and more
detail. What I've coded so far is only a test of the graph layout; I
will eventually put in the functionality to create nodes and label and
expand them.

In the mean time, a fun emergent game is to try and drag the nodes such
that the graph is [planar](http://en.wikipedia.org/wiki/Planar_graph).
Just refresh the page to get a new randomly generated graph.

