Title: Gooey Pipes
Date: 2008-02-16 01:54
Author: justinnhli
Slug: gooey-pipes

It's a stroke of fate that I first found this topic in an
[article](http://www.freesoftwaremagazine.com/columns/why_cant_free_software_guis_be_empowering_instead_limiting)
from my RSS reader, and now it seems I'll be working on a prototype of
such a system for HCI. It's a really cool idea, actually.

First, I should probably explain what pipes are, and how they can be
gooey. Pipes, in computer science, are means of transforming the output
of one program into another program's input. For example, I could have a
program that does searching (<span
style="font-family:courier new;">grep</span>), and I want to sort the
search results (<span style="font-family:courier new;">sort</span>), and
finally display only the unique ones (<span
style="font-family:courier new;">uniq</span>). In a terminal, this would
be:  

> grep | sort | uniq
> </p>

Note the "pipe" symbol, also known as the "vertical bar" or "OR" in most
computer programming languages. This is why it's known as a pipe; it
also makes sense that information is put in a pipe and literally
redirected to another program.

The power of pipes is fairly obvious, but notice that all the pipes
above are in text. There is currently no way to provide the same power
and flexibility graphically. That is, it would be cool if we could make
some GUI gooey pipes.

There are some existing programs which replicates this process in
various ways. One is Apple's Automator, which not only allows piping,
but also primitive looping. The other is Yahoo!'s Pipes, which only
works with online data sources. It would, indeed, be interesting to see
such tools being used on the desktop. The article also has a point about
putting multiple streams of data together, which is not really possible
(unless you write to variables or files) in a terminal.

Let's see what we come up with.

