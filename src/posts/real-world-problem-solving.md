Title: Real World Problem Solving
Date: 2007-11-25 01:45
Author: justinnhli
Slug: real-world-problem-solving

I had written before about how programmers often [use existing solutions
and implement it
digitally](http://ninghui48.blogspot.com/2007/11/computer-science-problem-solving.html)
for some cause. A few weeks ago in my design class we had a guest
lecture on designing for the environment. One of the things the lecturer
said (one of the two things I wrote down) was that the current model of
production uses the cost of extraction in calculating the price of the
product. For example, paper is priced by the cost it takes to cut down
the trees, transport it to the factory, and turn it into paper.
Similarly, oil is priced by how hard it was to take it out of the
ground.

The lecturer suggested instead that products should be priced by the
cost of replacement. The cost of extraction would count, yes, but we
should also be paying for what happens to the product after we are done,
when we throw it out. Also included in the cost of replacement is what
we are going to do with the now bare extraction area. The cost of office
paper, therefore, would include not only those things mentioned above,
but also the cost of recycling (either into paper again or into
cardboard, which is technically "down-cycling"), the cost of it being
transported to the landfill, and the cost of raising a tree to replace
the tree which was cut, all the way to the point where we can use that
tree to make paper again.

Obviously, this would make the price of paper exorbitant, but then again
we've been getting away cheap for using all of earth's resources for the
past... 4000 years, probably. I don't think the problem is with
humanity's need to exploit, but as the lecturer pointed out, it has to
do with how far we're looking when we exploit. All animals exploit,
although of course not on the same scale, but humans have the ability to
look ahead and predict what will happen. The problem is that the
companies doing the extraction, the production, are not looking far
enough ahead. When we exploit, we want to keep exploiting. Companies may
look 10, maybe at most 50 years in the future, but that is not long at
all on the time scale of, say, oil production. For paper and trees it is
barely enough. Which is why I think there will be a huge crisis in the
next century or so, in terms of how we get our energy, and how we think
about the environment.

Interestingly, I found a current case where the cost of production is
the same as the cost of replacement: programming. Computer programmers
often have to worry about memory, not just how much of it we're using,
but also whether we're "wasting" it by asking for it and not using it.
In C and C++, if we use memory and don't return it, we call it a "memory
leak". This doesn't happen with more recent languages, which have
automatic "garbage collectors". However, we still have to worry about
using too much memory, because garbage collection is a slow process, and
will take up CPU cycles. To prevent this, people try to do what we call
"garbage avoidance".

See the parallel? Although the waste in computer science is not
physical, it is considered in the stages of "production" (creating some
internal structure in the program) so that after the "lifetime" of the
product is over (that structure is not needed anymore) the "resource" is
cheaply replaced, or is used to create another "product". Upon
reflection it makes sense: computer memory and programs which use that
memory form a closed system, and therefore the user must be careful not
to over-exploit memory or other types of "resource". Similarly, oil,
trees, etc. are all resources in a closed system (earth), and we as
users of these resources need to start worrying about replenishing it,
so that we won't find we have none left when it is most needed.

