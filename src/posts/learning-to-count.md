Title: Learning to Count
Date: 2008-12-04 01:55
Author: justinnhli
Slug: learning-to-count

Over dinner tonight I over heard a girl ask another, jokingly, "If it's
twenty-one and thirty-one and so on, why isn't it tenty-one?"
Technically by the same logic it should be "ten-one", since twenty and
thirty are numbers by themselves. But she did raise a good question.

Most people know that the numbers we use most often, say, 42, are Arabic
numerals. Most specifically, they're in base ten; that, each position
represents that many powers of ten. Hence,

42 = 4 \* 10\^1 + 2 \* 10\^0 = 40 + 2 = 42

This applies to digits after the decimal point as well:

3.142 = 3 \* 10\^0 + 1 \* 10\^-1 + 4 \* 10\^-2 + 2 \* 10\^-3 = 3 + 0.1 +
0.04 + 0.002 = 3.142

I would hope that most people reading this blog know of other bases,
even if you don't use them. Binary is probably the most raised example

42~10~ = 101010~2~ = 1 \* 2\^32 + 1 \* 2\^3 + 1 \* 2\^1 = 42~10~

You can also use Hex (base 16):

42~10~ = 2A~16~

Where you use A=10, B=11, and so on. I once wrote a converter on my TI
that goes up to base 36. In any case, from here on, unless otherwise
noted, numbers will be in decimal.

On the other hand, there are less commonly used number systems.

42 = XLII

Yes, those are Roman numerals. Each letter has a certain value, and to
get the whole you just add them together... sort of. The special case is
when a letter of smaller value is to the immediate left of a larger one,
in which case you subtract that from the larger. Therefore,

LX = 60 but XL = 40

Most notably, Roman numerals are not positional - that is, the value of
each character/digit does not depend on where it is, except in the case
mentioned above. So in

III

the first I and the last I have the exact same value. This is in
contrast to

111

where the first 1 represents 100, the second 10, and so on. It is also
important to see the following:

What is 0 in Roman numeral?

The answer is that Roman numerals don't have a representation for zero.
Since their numbering system is not position, there is no need to
signify the lack of anything for a digit.

And now we have something like this:

twenty-one

Hm. That's a strange one. The proper way to look at this, I think, is to
treat "twenty" as one symbol, like how we treat "X" in Roman numerals.
It is interesting to look at this:

Decimal: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
18, 19, 20  
Binary: 0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100,
1101, 1111, 10000, 10001, 10010, 10011, 10100  
Hex: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 10, 11, 12, 13, 14  
Roman Numeral: I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII,
XIV, XV, XVI, XVII, XVIII, XIX, XX  
English: zero, one, two, three, four, five, six, seven, eight, nine,
ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen,
eighteen, nineteen, twenty.

Notice something strange? If we treat "twenty" as one symbol, then
counting in English does not reuse symbols until we reach "twenty-one",
which is "twenty" plus "one". All other systems here reuse certain
symbols, like the "1" in Arabic numerals and binary, or the "I" in Roman
numerals. Instead, in English there are 21 symbols from 0 to 20, then
there's a new symbol for 30: "thirty", and 40: "forty", and so on, up to
90 ("ninety") before going to 100 ("hundred").

There's no single symbol for 200 though; rather, "two hundred" is used.
This is *different* from "twenty-one", because we're not *adding* "two"
and "hundred", but *multiplying*. The next new symbol is "thousand", and
the next ones after that "million", "billion", "trillion" and so on.

I'm not sure if this can be counted (no pun intended... at first, at
least) as a number system, but it's interesting how different symbols
are used and combined to represent numbers.

Then there's the French:

French: zero, une, deux, trois, quartre, cinq, six, sept, huit, nerf,
dix, onze, douze, treize, quatorze, quinze, seize, dix-sept, dix-huit,
dix-neuf, vingt.

There is reuse of symbols at 17, then a new symbol for 20. 30 is
"trente", 40 is "quarante", 50 is "cinquante", and 60 is "soixante". But
note that 70 is "soixante-dix", that is, "60-10". It makes sense
therefore that 61 is "soixante -onze", or "70-11". Everything is nice up
to 80, which is not "soixante et vingt", but "quartre-vingts", literally
"four twenties" (also no pun intended).

It should be noted that regionally (in Belgium, for instance), people do
say "<span lang="fr" lang="fr">septante" for 70 and "nonante</span>" for
90. And in Switzerland, some people say "<span lang="fr"
lang="fr">huitante" for 80.</span>*<span lang="fr" lang="fr"></span>*  
*<span lang="fr" lang="fr">  
</span>*  
The Chinese system is, of these three languages, the closest to Arabic
numbers. Using pinyin:

Chinese: ling, yi, er, san, si, wu, liu, qi, ba, jiu, shi, shi-yi,
shi-er, shi-san, shi-si, shi-wu, shi-liu, shi-qi, shi-ba, shi-jiu,
er-shi

In Chinese, 0 to 10 have unique symbols, but starting from 11, these
symbols are repeated - added if decreasing, multiplied if increasing -
untill 100, which is "bai".

I knew all of this off the top of my head (except the French spelling
for a few numbers... meh), but those interested can go to Wikipdia's
[Numerals category](http://en.wikipedia.org/wiki/Category:Numerals) to
read more on different number systems.

