title: Human Meaning
date: 2016-06-30

I had a [long Twitter conversation](https://twitter.com/jack_dot_bin/status/740420401596076032) the other day about including Twitter bots as an assignment in introductory computer science courses (CS1). The super-condensed version of that conversation is that bots include a lot of interesting CS1 concepts and can be a good cumulative project. There *are* are a lot of Twitter bots around, from [@big_ben_clock](https://twitter.com/big_ben_clock) to [@everyword](https://twitter.com/everyword), from [@GlitchLogos](https://twitter.com/GlitchLogos) to [@generativebot](https://twitter.com/generativebot). @big_ben_clock is hilarious in its Captain-Obvious-ness, and @generativebot has really cool pictures, but I can't help but feel they're all missing something.

For example, take a look at [@censusAmericans](https://twitter.com/censusAmericans). This is a bot that takes US census data, then interpolates backwards to create a 140 character story about a single American citizen. For example:

> I have trouble with my eyesight. Last time I got married was in 1998. I have been married twice. I have a high school diploma. - @censusAmericans ([2016-06-02 19:37](https://twitter.com/censusAmericans/status/738514821008723968))

I think we can all agree that there is something *human* about this bot. Not that the bot itself is human, but that the bot tells a plausible *story*. And if you look through the conversation I had, I pushed back against many of the suggestions because they seem... trivial. Writing a program that prints out the correct number of "BONG"s at the right time is not that hard. Writing an algorithm that generates random pictures is harder, but there's no narrative there. This is more obvious with something like [@one_small_bot](https://botwiki.org/bots/twitterbots/one_small_bot/) and [@MakingInvisible](https://twitter.com/MakingInvisible): the same linguistic template is used to generate endless variations, but we very quickly see the limits of what the bot can do. Sure, occasionally the random number generator hits on a great word with which to fill in the blank, but I can write a script that spills out all 100,000 combinations. To me, waiting for these moments is a sort of artificial suspense, no different from pulling the lever on a slot machine.

There is a different problem with these bots in that they do not take full advantage of Twitter. The vast majority of bots is using Twitter only as a publicity/broadcasting platform. These bots do not react to replies or likes, or do so in a way that is opaque, such as using the reply content as the seed for the next random image. But the allure of making a bot is precisely that there are other people out there, who may react to your bot in wildly different ways based on their own experience and prejudices. Think of [ELIZA](https://en.wikipedia.org/wiki/ELIZA), the first chatbot. It is no more sophisticated than many of the bots I've mentioned so far, but by asking question of the people it interacts with, it exposes something about those people which would not otherwise be seen. The bot is imbued with humanness by virtue of its users, and this is something that even @censusAmericans doesn't achieve.

In my Twitter conversation, I [proposed three bot ideas](http://twitter.com/justinnhli/status/740443407911419904):

* A bot that scrapes the internet for traffic accident reports in real time, then constructs a 140-character story about the victim, based on real information (eg. location, age, etc.).
* A bot that tweets every hour/day, but each time with a different personality. If people reply to the tweets of that bot, that same personality will respond - but only until the next hour/day, when a new personality takes over and all replies to older tweets will be ignored.
* A bot that searches for public tweets that mention Islam or terrorism, then replies with peaceful verses from the Quran. If the original tweeter replies, either thank/welcome them or placate them (still with Quran verses) depending on a sentiment analysis of the reply.

The first idea is clearly derivative of @censusAmericans, but I think the second and third ideas are really taking advantage of Twitter as a social medium. They are also the more technically challenging of the three, but that's beside the point, which is that Twitter is interesting precisely because there are so many people on it reacting to events in real time. If executed properly, I think these bots could raise real questions about identity and social interaction, and may even be considered *art* (in the crudest sense).

I've been thinking about this for the last 24 hours, and I've been wondering why so many technologists ignore the human aspects of technology. It seems obvious to me that @censusAmericans is more *meaningful* than @generativebot, and the last two bots in my ideas more meaningful than either - but so why hasn't anyone built them? The Quran bot - which I will refer to as @peaceful_quran from now on - is simpler to write than @generativebot, and arguably says more about the current state of the world.

This will seem off topic, but bear with me for a second. I recently binge watched all of [CGP Grey's videos](https://www.youtube.com/user/CGPGrey) (who, by the way, also is also [@cgpgrey](https://twitter.com/cgpgrey)), and stumbled upon his link to [this video on the future of education](https://www.youtube.com/watch?v=quYDkuD4dMU). Unlike most videos about education and the internet, however, this video emphasized that teachers are not replaced. To quote, 

> It's the teacher's job to point young minds towards the right kinds of question. The teacher doesn't need to give any answers - the answers are everywhere. We know now from years of measurements that learners who find the answers for themselves retain it better than if they're told the answers. [Sugata Mitra, Newcastle University Professor]
>
> People often ask us whether universities are a thing of the past, whether universities are going to die out. I definitely do not think so. There is something tremendous about getting people together in a place where serendipitous interactions can happen, where you can have face-to-face mentoring between an instructor and students; where students can talk to each other and create together and learn to debate ideas. This on-campus physical experience, at the moment, has no virtue substitute that is equally effective. [Daphne Koller, Coursera co-founder and co-CEO]
>
> What we need are teachers who will look people in the eye, and believe in them and push them forward. It's hard to do that on the internet; it really needs to be done in person. [Seth Godin, teacher & artist]

I can't be as critical about the obliviousness of the community, since this also took me a while to understand, but *of course* teachers are necessary. There are multiple psychological studies that show social interaction, and yes, [physical contact](https://en.wikipedia.org/wiki/Harry_Harlow#Partial_and_total_isolation_of_infant_monkeys), are necessary for normal development. We can do a lot on the internet, but we can't (yet) replace human connection.

And that's why I'm bringing this up. There is a lot of noise about technology being isolating - the most famous of this is perhaps [Sherry Turkle](https://en.wikipedia.org/wiki/Sherry_Turkle)'s book [Alone Together](https://www.goodreads.com/book/show/8694125-alone-together) - and in many ways I agree with that sentiment. But I don't think it has to be that way. Another way of saying this is that I don't think technology is *necessarily* isolating, but it is *often* isolating because technologists are ignoring the *meaning* that arises from interacting with other people. We can tell a story about this - how nerds grew up focused on the technology and never felt the need for friends - but we can also tell the opposite story that nerds have therefore spent much more time observing and understanding what people consider meaningful, and are in a position to instill that into the technology they make. This is not to say that there isn't a place for passive Twitter bots, but to reach for it as the first resort is ignoring a lot of potential for meaningful interaction.

The original Twitter conversation started with a discussion of whether bots would make a good CS1 assignment. I haven't decided if I will use it for my own class, but if I do, I will make sure that students work to include human meaning in their digital artifacts.