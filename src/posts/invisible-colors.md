Title: Invisible Colors
Date: 2013-11-05 14:51
Slug: invisible-colors

Often, when I have conversations with non-computer-science people, these
"conversations" often resemble "arguments". One recurring argument is
how we decide whether something has a particular property. To give a
concrete example, we might try to figure out whether a [critical
review](http://en.wikipedia.org/wiki/Literary_criticism) (of a book,
say) is *authentic*, that is, that it was derived from the true beliefs
of the literary critic. It turns out that the disagreement runs deeper
than literary criticism, and I want to address that in this post.

Sidenote: the core ideas in this post were inspired by [another
article](http://ansuz.sooke.bc.ca/entry/23). I think I push the idea a
little further here, and also give better examples, so feel free to read
the article and come back. At the very least, it’ll plug any explanation
pitfalls in this post.

The big takeaway of this post is that sometimes we care about properties
of objects that cannot be found in the make up of that object. To use a
simple examine, my name is “Justin”, but if you take me apart atom by
atom, there is no “Justin-ness” property to be found anywhere. Note that
this is not simply the distinction between a system of components versus
individual components; the “circulatory system” may not reside in any
individual atom, but we can point to some group of atoms (ie. the heart,
blood vessels, etc.) and say that they make up the “circulatory system”.
In this case, the circulatory system is the result of the interactions
of atoms; the same cannot be said of the name “Justin”.

Maybe a real-world example would make the point clearer. In business,
when you receive funding from some source, sometimes there will be
stipulations for how you may use that money; this is the case for the
[US
government](http://en.wikipedia.org/wiki/Government_procurement_in_the_United_States).
Closer to home, the [Computer Science and Engineering Graduates
(CSEG)](http://www.eecs.umich.edu/CSEG/) student group gets money from
the University of Michigan, but they can’t use that money to buy
alcohol. At the same time, CSEG also collects money from graduate
students; this money *can* be used to buy alcohol. To keep these funds
separate, CSEG actually has two bank accounts, and is not allowed to
arbitrarily move money from one to the other (for some definition of
arbitrary). There is no difference between the money in these two
accounts, of course; money is
[fungible](http://en.wikipedia.org/wiki/Fungibility), and merchants
would happily accept money from either. But to abide by university
regulations, CSEG must distinguish between the two, and only use one of
them to buy booze. In finance, this distinction is called the Color of
money, a term I will adopt here (and also used in the source article
above, although for a different reason).

If we want to get technical, Color-like properties are ones that do not
exist in the object itself. We can take apart CSEG’s two bank accounts
(they won’t be happy about this), and nothing in the account will say
that one can be used to buy beer. Nothing in the external world can tell
us the Color of the accounts; instead, Color is something that we need
to keep track of ourselves. In memory research, properties like Color
are called
[“non-projectable”](http://journals.cambridge.org/action/displayAbstract?fromPage=online&aid=29215),
because the outside world cannot give us this information (if you want
to be poetic, it cannot “project” the information into our heads). What
this usually means is that Color is not about the object itself, but
about the *history* of the object. When we say that this account has a
Color of “cannot buy booze”, what we mean is that the money in this
account came from the university and not from students. It’s how the
money got there, not what the money is, that defines this distinction.

Since Color is not an intrinsic part of an object, we can do strange
things with it. For example, CSEG can do tricks to change the Color of
money, by paying for some social event (for example, rock climbing),
then charging grad students to attend. The money with the “no booze”
Color is now spent (notably, not on booze); the money that CSEG now has
came from students, and so has the “yes booze” Color, even though these
two may be the exact same amount. We have now changed the Color of
money, and can do different things with it (eg. a bar crawl). This is,
of course, a form of [money
laundering](http://en.wikipedia.org/wiki/Money_laundering), but no one
seems to mind.

I want to return to computer science now, and give another example of
Color: whether a file is subject to copyright (this was the example in
the source article). Let’s say I have three copies of a song (say, [this
one](http://www.youtube.com/watch?v=dQw4w9WgXcQ)), which I got from
different places: one I got from the artist as a gift, one I got as a
digital download from iTunes, and one that I got from a BitTorrent
file-share. From the computer’s perspective, these three files are
*exactly the same*, down to every 1 and 0 at the binary level. (This is
not strictly true, but we’ll run with it for now.) The computer can’t
stop me from making a copy of my iTunes version for a friend – not
because it doesn’t have the power to, but because it doesn’t know which
one came from iTunes. There’s nothing in the bits that say whether I’m
legally allowed to copy a file; the legality of that operation is a
Color.

For obvious reasons, this is a big problem for lawyers. To make sure
everyone is paying for their music, they want to impose restrictions on
what people can do with their files, so they come up with [digital
rights management
(DRM)](http://en.wikipedia.org/wiki/Digital_rights_management). They
require iTunes to add extra 1’s and 0’s to their files, so that my
computer knows it’s from iTunes, and can stop me from making copies; in
computer science jargon, this is called *metadata*, since it’s data
about the data itself. The problem is that metadata doesn’t change the
file in any intrinsic way; it merely adds some numbers to the end. If I
want, I can decide to add this metadata myself – or more likely, remove
this metadata – and all of a sudden my computer can again copy files
from iTunes.

(In reality, there’s the issue of encryption – changing the file in some
way that requires special knowledge to read. This is a bigger problem,
since encryption is designed to make its reversal – “removing the
metadata” – difficult. But none the less, if the encryption can be
reversed (ie. if the file can be decrypted), the file can again be read
and copied.)

If all this computer science stuff seems complicated, it turns out that
the same problem exists in [meat
space](http://www.urbandictionary.com/define.php?term=meat%20space).
Copyright, ultimately, is about the *ownership* of an idea, and
ownership applies equally well to real objects. Let’s say you and I both
own the same coffee mug, which are identical in every way. I can take
both, move them around behind my back, then bring them back out and ask
you which one is yours. You can’t tell, of course, because the mugs are
identical; you are now in the same position as the computer with the
three files.

“But wait!” you say, “I can just stencil my name onto my cup, and now my
cup is different! What do you think of that?” You’re right, of course,
but that’s the point: your name on your cup doesn’t really mean that you
own the cup. I can, for example, *also* stencil *your* name on *my* cup;
nothing stops me from doing this, and the cup is still *mine*, even
though it has *your* name on it. The ownership survives regardless of
what changes you make to your cup and what changes I make to mine; it
does not depend on the physicality of the cup, and is therefore a Color.

(Encryption in this case, I suppose, is equivalent to locking up your
mug. Even then, nothing stops me from picking the lock and claiming the
cup is mine.)

As the source article pointed out, it’s not that computer scientists
don’t care at all about Color. When we need a random number (excuse me,
a randomly-generated number), we are a lot that the numbers are actually
random. Theoretically, rolling a die and getting five 6’s consecutively
(6, 6, 6, 6, 6) is just as likely as getting any other sequence (say, 4,
6, 5, 1, 6); they both have (16)5=17776=0.000129 probability of
happening. But, like any Color, randomness is not in the sequence
itself, but in how the sequence is generated. Which is why we care about
how a [random number
generator](http://en.wikipedia.org/wiki/Random_number_generation) works,
precisely because we can’t tell just by looking at the numbers. In the
ideal case, we’ll have the [source
code](http://en.wikipedia.org/wiki/Source_code), so we can
mathematically prove that the generated numbers are random; in practice,
we leave this job to a small subset of people, and trust that whatever
random number generator we use is good enough.

I am finally ready to go back to my opening example about authenticity
in literary criticism. In real life, the discussion came about because
my friend mentioned that in the school of [New
Historicism](http://en.wikipedia.org/wiki/New_Historicism), critics
frame the piece of literature in its historical context; they might, for
example, comment on how colonialist ideas show up in Shakespeare’s
works. This is notable because the idea of colonialism wasn’t around
during Shakespeare’s time; it is only in hindsight that we can point out
these influences. I then asked the question of whether a critic can
*pretend* to be from a different time period, and review a work from
that perspective; an example might be to review Shakespeare as someone
from a inter-stellar civilization. My friend was rather horrified, and
said that such a review would be science fiction and not literary
criticism, that it would not be *authentic*. I then modified my example:
what if a critic is familiar with modern psychology, but *pretended* not
to be, and wrote a review using psychoanalytic theories? Would such a
review be accepted into literary journals? My interest at the time was
more about the need for scientifically-accurate literary criticism, but
it also touched on the issue of authenticity. Given my friend’s previous
vehement reaction, I was surprised to hear that such a review would be
publishable, despite, of course, it also being inauthentic.

As might be obvious by now, the problem is that the authenticity of a
review is not a property of the review itself, but a Color. Two critics
can have completely difference view points but write the exact same
sequence of words in a review; nothing in the words would distinguish
which one is authentic and which isn’t. To be fair, this is not just a
problem for literary criticism, but for academia as a whole: any
manuscript to be reviewed for publication should be true, but that truth
is not a property of the manuscript, and therefore cannot be determined
100% accurately every single time. The difference between literary
criticism and (say) computer science is that in computer science, the
manuscript contains experimental results; this allows the experiment to
be replicated and the results reproduced, thus checking the correctness
of the manuscript (albeit after it has already been accepted or rejected
for publication). This path to determine correctness (or the criticism
equivalent, authenticity) is not open to literary criticism: there is
nothing to compare a review against, since a review is by nature
subjective, and a different critic cannot “reproduce” the views of the
original author. Of course, we’ve actually already encountered this
problem before. Correctness in the sciences is like having the random
number generator available; if we don’t believe the sequence is random,
we can look at the random number generator itself and “reproduce” the
results. Authenticity, on the other hand, is like being given a
[black-box](http://en.wikipedia.org/wiki/Black_box) random number
generator; we might be able to say something is not authentic if it is
painfully obvious (like if the generator always produces 6’s, or if a
critic claims to be part of an inter-stellar civilization), but for less
egregious violations, there’s simply no way to tell.

I didn’t mean this post to be an attack on literary criticism; it was
merely a convenient example (and a true and authentic one; you’ll just
have to trust me on this…). The issue of Color comes up in many other
places, including within computer science itself, and I’m sure has
sparked many debates similar to the one between me and my friend. Color
is therefore a useful thing to keep in mind, especially since it makes
an appearance in both the sciences and the humanities. Instead of
arguing over why it is unrealistic to care about some property, we might
invoke the concept of Color and move on to whether and how accurately we
can determine that Color instead.

PS. I do want note the irony in how literary criticism as a field cares
so much about authenticity, given that they spend a lot of effort
separating the creator and the work created; this is the (famous?)
[“death of the
author”](http://en.wikipedia.org/wiki/Death_of_the_Author) view of
literature. Somehow, this philosophy does not extend to criticism
itself.
