Title: One Hand Keyboard
Date: 2007-11-15 02:16
Author: justinnhli
Slug: one-hand-keyboard

A while (a <span style="font-style:italic;">long</span> while) back I
was reading[xkcd's blog
post](http://blag.xkcd.com/2007/08/14/mirrorboard-a-one-handed-keyboard-layout-for-the-lazy/),
and while some of the comments were interesting, I had my own take to
it. My idea is to just use 9 keys, say, WERSDFXCV, as the keypad, and
type as you would on a cellphone.

There are several advantages to this over the mirrored keyboard. One is
that there is no new mapping to learn; everyone (well, everyone [with a
cell phone](http://ninghui48.blogspot.com/2007/10/voip.html)) would know
the configuration. The second advantage is that there would be less
finger movements for each word, which (like the last point) amounts to
the system being easier to learn. In the mirrored keyboard, each key
still only has one letter, so your fingers have to move over the
keyboard more. With the text messaging keyboard, each key represents 3
or 4 letters, so only a few fingers have to move, and only one row at a
time.

I forgot to mention that this system has to be used with a word list and
a regex search, as mentioned in the xkcd post. On normal phones you have
to press a key several times, which adds up to a lot more key presses
after a while. It would be much better if you press each key only once,
having each "number" stored in a buffer, and on word separating keys
(spaces, commas, periods, etc.) the system would flush the buffer by
matching each key with the possible letters, and extract out the word
you meant.

For those who are not comfortable at all with their left hands, this can
even be changed to a right hand dominant configuration. Instead of
turning certain keys into the num pad, you use the mouse instead. Your
left hand would simply be holding down a special combination of keys -
say, control-shift-alt - and you would move your mouse in the direction
of that number. 1 would be upper left, 2 straight up, 3 upper right, and
so on. 5 would be clicking the left mouse button. This is similar to
mouse gestures for Opera and Firefox, and could also use the same
configuration button of the right click as the special key, so the left
hand doesn't need to be on the keyboard at all.

The are two disadvantages I see in this system, ignoring the mouse
gesture variation for now. One: there is no way to get punctuation in.
This is a pain on cell phones, and I don't see a quick way for doing
that. Not even a regex search would help, since the computer will need
to know the context and meaning of what you're saying to determine which
punctuation to use. The second flaw is that the regex search for words
is inaccurate, and for small words will often require a choice. For
example, both "bake" and "cake" use the keys 2-2-5-3. Again, this cannot
be solved without the software knowing more about what you're writing
about.

Personally, I just move my right hand off my mouse and type normally.

