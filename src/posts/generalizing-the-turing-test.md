Title: Generalizing the Turing Test
Date: 2013-11-18 19:02
Author: justinnhli
Slug: generalizing-the-turing-test

Are people familiar with the [Turing
test](http://en.wikipedia.org/wiki/Turing_test)? Named after [Alan
Turing](http://en.wikipedia.org/wiki/Alan_Turing), the WWII British
mathematician and code-breaker, it was proposed as a way of testing
whether computers are "intelligent". In addition to inventing this test
and helping break the
[Enigma](http://en.wikipedia.org/wiki/Enigma_machine), Turing is also
famous for the conception of a [Turing
machine](http://en.wikipedia.org/wiki/Turing_machine), a mathematical
construct that is useful for understanding computation in the abstract.
Unfortunately for Turing, he was also homosexual, and was prosecuted by
the state for it after the war; this eventually led to his suicide. In
2009 - 55 years after Turing's death - the British government [formally
apologized](http://en.wikipedia.org/wiki/Alan_Turing#Government_apology_and_pardon_support)
for its treatment of Turing, and only earlier this year, in 2013, was he
officially pardoned for his crimes.

Turing is also the subject of an upcoming biopic, [The Imitation
Game](http://en.wikipedia.org/wiki/The_Imitation_Game), starring
~~[Sherlock](http://en.wikipedia.org/wiki/Sherlock_%28TV_series%29)~~
[Benedict
Cumberbatch](http://en.wikipedia.org/wiki/Benedict_Cumberbatch). The
title of the film is, in fact, based on the Turing test (or rather, is
famous because of the test). In the Turing Test, a computer and a person
both try to convince a human judge that they are human. The judge can
only communicate with both parties through text, but they can ask
questions. A computer or a program is said to have passed to the Turing
test if, over multiple conversations, the judge cannot reliably and
correctly label which is the person and which is the computer. In some
sense, the computer needs to be *imitating* a person, whence the name of
the game.

(It can, of course, also go the other way, to have a [reversed Turing
test](http://en.wikipedia.org/wiki/Reverse_Turing_test): the goal could
be to convince the judge that both participants are computers. This
doesn't make sense as a test of intelligence, but the idea is the same.
You can also [try to convince the *judge*](http://xkcd.com/329/) that
they're a computer...)

Setting the question of whether the Turing test is a good test for
whether a computer is intelligent, the test is nonetheless elegant in
its design. There are several crucial elements of the design, that the
computer is not "the most intelligent" or "the most human like" compared
to other computers, and that the judge is not simply deciding whether
one conversant is a human or a computer; these features mean that the
computer must match the human in performance. Further more, because the
judge can ask the computer any question they want, the computer must be
able to talk about any subject the judge could think of. Thus, even
though no one has a good definition of "intelligence", the Turing test
at least allows us to apply a "[know it when I see
it](http://en.wikipedia.org/wiki/I_know_it_when_I_see_it)" criterion.

For the most part, familiarity of the Turing test has remained within
the academic fields of computer science, psychology, and philosophy. I
was recently surprised, however, that it came up in an [economics
article](http://econlog.econlib.org/archives/2011/06/the_ideological.html).
In this article, it is suggested that liberal economists can
successfully present conservative economic arguments, while the same
cannot be said of the opposite, for a conservative economist to present
liberal economic arguments. The author therefore proposes a variation of
a Turing test: put him (a conservative) in a room with five liberals,
and see if people can tell who's the fake; then put Paul Krugman (a
liberal) in a room with five conservatives, and again see if people can
tell who's the fake.

What, then, is the more general version of the Turing test? The Turing
test is really a special case of a [discrimination
test](http://en.wikipedia.org/wiki/Discrimination_testing). The key,
however, is that the Turing test is being used as a criterion: *if* the
computer cannot be distinguished from a human, *then* we shall consider
it as intelligent. This means that, crucially, we *do not need to define
the exact attribute* that we are judging by, only that it behaves
indistinguishably from the real thing. While we do not have a perfect
definition (or even a good one) of intelligence, the beauty of the
Turing test is that we don't need one to decide that a computer is
intelligent. This may be a very behavioral definition of intelligence -
it doesn't address the [Chinese
room](http://en.wikipedia.org/wiki/Chinese_room) problem, for example -
but it's better than endlessly debating the definition of intelligence.

Of course, the Turing test, clever as it is, is not the silver bullet
for all indefinable attributes. In fact, there are strong restrictions
on when the Turing test will be useful. For one, the judge must be
familiar with the attribute that is being judged; for example, I would
not be a good judge of liberal/conservative economists, since I myself
cannot tell the difference. More generally, the more discerning the
judge, the more "powerful" the Turing test becomes. Additionally, the
attribute being judged must be different from how the attribute is
generated. In the original Turing test, what we cared about was whether
the computer is intelligent, not how it came to be that way (that is,
whether it does so through neurons or silicon). This means that care
must be taken to remove elements that may give the distinction away,
which is why the original test uses text as the medium of communication,
as opposed to a face-to-face conversation, which would detract from the
task of judging intelligence.

It is curious to me that, despite spending some time on this post, I
cannot think of a single application of the Turing test. The closest
I've come is for [driverless
cars](http://en.wikipedia.org/wiki/Google_driverless_car), and using the
Turing test to see whether they drive safer than humans do. Such a test
would involve putting human and computer in simulated drives, and having
the judges simply watch a recording of the performance without knowing
which is which. While such a test would show that self-driving cars are
as safe - if not safer than - humans, it is also unnecessary: the
metrics for safety seems sufficiently well-defined that we don't need a
Turing test, and that any old comparison would suffice. This is nothing
more than an argumentation from [lack of
imagination](http://en.wikipedia.org/wiki/Argument_from_ignorance#Argument_from_incredulity.2FLack_of_imagination),
it may seem that we are simply not trained to think of tests in this
way. More often, when we think of an attribute we want to measure, we
define the attribute such that it is measurable, or else we give up
trying to get any accurate measurements. Maybe the Turing test is a good
way to attack some of these measurements we've given up on.

