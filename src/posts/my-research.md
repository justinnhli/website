Title: My Research
Date: 2010-05-21 04:40
Author: justinnhli
Slug: my-research

I've wanted to write this post for a while, but have never found the
motivation to do so. There's a workshop this coming week, however, and I
am scheduled to present this stuff on Thursday (today... I did okay, I
think). So, I decided this is the perfect time to given a non-technical
(that is, non-mathematical) introduction to what I do... there truly is
no greater motivator than procrastination.

For those of you who don't know, I'm a grad student in computer science
at the University of Michigan, specializing in artificial intelligence.
Within this field, which is wider and deeper than most people realize, I
am looking at the problem of *reinforcement learning* (RL). The
formulation of the problem is simple. An *agent* interacts with some
*environment* by performing *actions*. The environment reacts, and may
occasionally reward or punish the agent. The goal of the agent is to
maximize the amount of *reward* (or equivalently, minimize the amount of
punishment) it gets. Hence the name reinforcement learning: the reward
and punishment terminology is borrowed from the theory of *operant
conditioning* in psychology.

Does this problem sound easy? It's not. Let's use a computer game as an
example... say, Pong. A Pong agent has two actions available to it: move
up and move down. The environment includes the ball and the opposite
agent. A simple *reward function* gives the agent 1 point for winning a
game and -1 point for losing the game. Now, put yourself in the role of
the agent. You might think, "Oh, just follow the ball by moving up and
down, and don't let the ball get past me." Well, you know that, but how
does the agent know that? Remember, the agent doesn't know it is in a
Pong game - all it observes are a bunch of numbers. The agent doesn't
know it will be rewarded for getting the ball past its opponent, nor
that it will be punished for letting the ball past it. It doesn't know
that the ball will "bounce" when it touches anything - or even what
constitutes "touching", "opponent", and "past".

Without any knowledge, the agent will have to act randomly, at least at
first. It might get lucky and defend its goal once or twice, but more
likely it will let its opponent score and be punished. There comes the
first hurdle of reinforcement learning: how does the agent know what it
did wrong? The converse is also true if the agent scored - what did it
do right? This is called the *credit assignment problem*, because the
agent is trying to figure out what gets the credit (or blame) for the
reward (or punishment) it received. Again, remember what while you
intuitively know that the agent missed the ball, the agent doesn't have
any model of cause and effect to realize this.

To understand the basic solution to reinforcement learning, I must say
more about those numbers that the agent observes. For Pong, there might
be four numbers: the agent's vertical position, its opponent's vertical
position, and the vertical and horizontal position of the ball. Each of
these numbers are a *state variable*, and the different values these
numbers can take in conjunction is called the *state space* - as in "the
state of the union", not "the state of Michigan" - because they can
describe every situation in the environment. To make reinforcement
learning somewhat easier, researchers tend to view tasks as a *Markov
decision process* (MDP). The distinguishing property of an MDP is that
the next state of the environment depends only on the current state. For
the Pong example, the state space described by the four numbers listed
above does not make the game an MDP, since the ball can be moving
arbitrarily fast or slow. If instead six numbers are used - the
represent the horizontal and vertical velocity of the ball - then the
task would become an MDP.

To be concrete, every action the agent takes changes the state of the
environment. At each new state, the agent may receive a reward or a
punishment, and then it has to take another action, and so on.

Now that the agent has some idea of how to relate one set of numbers to
another, it can start learning. In place of human level reasoning, the
agent simply plans backwards. Intuitively, if you get punished for being
in this state, you know you shouldn't have taken that last action from
the previous state. For Pong, this partially corresponds to not moving
up if the ball is below you and just about to pass you. This picture is
not complete though, because if you are at the top of the screen and the
ball is at the bottom, you would not have gotten to the ball in time to
deflect it anyway. This means that the faulty action lies further back
in time.

Here's what the agent does. The agent remembers the *state* in which it
got a reward or a punishment. Knowing whether this state is good or bad,
it knows that the previous action from the previous state is also good
or bad. Now knowing about this previous state, and can know about the
state two steps back, and three steps back, and so on. That is, the
agent learns by propagating the rewards back through the states, so the
next time it finds itself in the same situation, it will either avoid
that action (because it was eventually punished for it) or do the same
thing (because it was eventually rewarded for it).

This was the state of the art 25 years ago.

Before I talk about more recent developments in the field, I want to
raise a few problems in the solution above. The shallowest, but also
most thought provocative, is this: how does the agent know it's doing
its best? Imagine the task is to go from the bedroom to the bathroom to
pick up an object. Through pure chance, the agent does this by going
through the living room, the kitchen, and the broom closet, despite
there being a door directly between the two rooms. Further imagine that
the agent is rewarded based on how quickly it gets to its destination
(I'm sure you can think of a reasonable, real life scenario for this).
How would the agent know that the path it found is the shortest one?
This problem is known as the *exploration-exploitation problem*. It is
thus named because the agent needs to explore to know more about the
environment, but this often means not exploiting the best action for the
agent. In practice, researchers simply make the agent act randomly some
small percentage of the time, so it will do its best for the most part
but be constantly exploring. For the jargon-philiac, this is called an
*epsilon-greedy* exploration strategy, where epsilon is the small
percentage mentioned above.

There are other variations to this general framework which researchers
are working on, such as partial observability (what if the agent doesn't
know the value of some state variables?) and stochastic actions (what if
actions only succeed some of the time?). I will skip the details on
these topics and instead focus on what I'm looking into.

Pong, while an illustrative example, is not the most complicated
environment for an agent to learn in. For one, there are only a limited
number of situations for the agent to be in: in the original pixelated
arcade game, there might only be a thousand or so different states. A
modern computer running the algorithm I described above would find the
optimal strategy (or *policy*) in less than a minute. Consider instead
the rooms example I just gave, where the agent must move from one room
to another. There can be an arbitrary number of rooms, and each room
itself can be arbitrarily large. Even if the starting and ending
positions are unchanged every time the agent must complete the task, it
might still take the agent a long time simply due to how much exploring
it has to do.

Yet, unlike Pong, this more complicated problem also presents more
information for the agent to use. For example, completely exploring one
room is useless when the goal is in another room. If you were to give
directions to a human, you might tell them to go out of the room, walk
down the hallway, and take the last right. Alternately, you might tell
them that the thing they're looking for is not in the living room, but
in the kitchen. The other person, on hearing these instructions, could
then ignore everything in their current room.

What these two instructions have in common is *abstraction*. The first
instruction abstracts over actions (it doesn't say "take 10 steps
forward, then 2 steps left,..."), while the second instruction abstracts
over states (it's saying that everything outside the kitchen is one room
which doesn't matter). Despite this distinction, the two types of
abstractions are related: the first instruction is implicitly saying
that the current room and the hallway are not worth exploring, and the
second instruction can be thought of as the action "go to the kitchen".

My research is related to this idea, although it's a little more
specific. Expanding the example beyond rooms, if I'm giving instructions
for someone to get to the Eiffel Tower in Paris, I would tell them to
get to the airport, take a plane, etc. Each of these "actions" can be
further broken down: order a cab, get out of the house, get in the
cab,... And even further: walk to the phone, call the cab company,...
This is called an *action hierarchy*, as the first actions "contain" the
second ones, which "contain" the third, and so on, until at the lowest
level the actions are simply "move this muscle". How do humans break
down such a complex task, and can a computer do the same thing?

So far, the state of the art (which is about 5 years old) is "sort of".
Given just the MDP assumption, there are proposals for what *subgoals*
should be. The most general ones are different ways of identifying
bottlenecks - that is, states which an agent must go through to reach a
goal. Think of the door to a room, and in order to get anywhere else you
must first go through that door. Other ideas include things like looking
at what states you have commonly visited in your experience, or perhaps
looking at what you're rewarded handsomely for.

Even knowing what appropriate subgoals are, the agent is not done.
Imagine that both the door to your room and the door to the apartment
are given as subgoals. How will you know that the door to your room is
the first thing to go for, before trying to read the door to your
apartment? Depending on the viewpoint, this could either be a problem of
restricting the *proposal* of actions, or it could be one of inducing a
*preference* on different possible actions. This appears to be a
slightly easier problem to solve, and I was surprised to find that there
is almost no prior work in this area. I intend to look into this
question further, and hopefully by the end of the summer I will have
some intuition as to what might work and what won't.

Post script: to people not in computer science or perhaps in but not in
AI, the problem of action hierarchies might sound insignificant. Despite
[my previous
misgivings](http://justinnhli.blogspot.com/2009/03/academic-typecasting.html)
about being limited to too specific a field, I find this problem
genuinely interesting. Although it may not change the world (yet), I do
think its solution will contribute to an understanding of humans and
intelligence.

