Title: Javascript Arguments
Date: 2007-09-15 03:27
Author: justinnhli
Slug: javascript-arguments

Why the `arguments` variable is not an Array in Javascript always
baffles me. The fact that it's an "Array-like Object" with the `length`
attribute makes it worse.

Coming from Lisp, I would like to pass all subsequent (optional)
arguments after a point to another function. For example:  

>     function foo(a, b) { ... bar(arguments.slice(2)); ...}

But of course `arguments` doesn't have the `slice` function. In Lisp, it
would be something like (forgive me if my Lisp is rusty):  

>     (defun foo (a b &rest others) ... (bar others) ...)

In the [code](http://ninghui48.googlepages.com/calendar.js) for my
[calendar](http://ninghui48.googlepages.com/calendar.html), I duplicate
the code I need, since it's only a short three lines. Otherwise, I would
have to use `Array.prototype.slice.call(...)` to turn it into an array
before `slice`-ing, like so:  

>     function foo(a, b) { ... bar.apply(this, Array.prototype.slice.call(arguments).slice(2)); ...}

Stupid. The other thing is that Javascript calls itself a functional
language, when some functions return useless values. But that's another
issue.

