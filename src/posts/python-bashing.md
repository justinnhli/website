Title: Python Bashing
Date: 2009-05-22 05:00
Slug: python-bashing

As a computer science major, it is not surprising that I write a lot of
small programs every day. From simple things like modifying some text
input in some way (a chain of sed's), to writing my alarm clock, a
twitter backup, and an ISBN converter. My journal search tool was
written by myself, and that goes back quite a ways.

All of the programs mentioned above, however, are Bash scripts.

I'm actually a little sheepish about this. After all, Bash is not a real
programming language, but just a way to automate a few administrative
operations. There is no type system, no support libraries, no object
oriented utilities.

I've thought about doing more things in python, but somehow there's a
barrier to entry to it. I reasoned that since what I do is mostly with
text, it's easier to read from files in Bash than in python (a single
cat as opposed to open().read()). But really that shouldn't be a
problem. The output might be an issue too, if I wanted things in nice
columns and what not. But then instead of column or paste I would just
be using printf or equivalent.

I was digging around Paul Graham's older essays, and I came across his
one titled "[Being Popular](http://www.paulgraham.com/popular.html)".
It's about what he things makes programming languages popular. Most of
the attributes in the essay don't describe the Bash script very well,
except for the section on Throwaway Programs. And that, I think, is
exactly why I use Bash scripts so often.

Because I'm using Linux, a lot of my operations are done on the command
line. I don't just mean the crazy programmer things like compiling or
system administration, but I mean every day things like moving files,
writing essays, even reading a book. My volume control, in fact, is also
a command line program (alsamixer; although now I have a keyboard
shortcut for that and I rarely actually open alsamixer). Given that I'm
in a terminal so often, Bash is practically always open for me.

It is precisely this always available attribute which makes me use Bash.
As Graham mentioned, I don't want to write something, then wait for it
to compile, then run it to see if it works. Bash works as an interactive
prompt, and I can type the whole program in "one line" and just run
that. More that that, I can test things a lot quicker in Bash than I can
in C or Java. Just open a new terminal (Ctrl-N) and I have a clean slate
to test if a certain line of my program does what it wants. Python, of
course, is also interactive, but it is unfortunately not as easily
accessible from the desktop. I have to type a full 7 keys
(P-Y-T-H-O-N-(enter)) to get to the interactive shell, and this slows
down the entire process.

So until someone manages to use python as their main shell, I'm sticking
with Bash.

