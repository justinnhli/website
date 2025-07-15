title: A Debugging Guide
category: resources

## Table of Contents

* [Introduction](#introduction)
* [Terminology](#terminology)
* [The Mental Game of Debugging](#mental-game)
* [A Debugging Guide](#guide)
    1. [Verify that the symptom exists, and determine the correct behavior](#guide-1)
    2. [(Optional) Create a minimal test case](#guide-2)
    3. [Add some diagnostic code immediately before the symptom](#guide-3)
    4. [Make sure your diagnostic code is correct and that its output is easy to understand](#guide-4)
    5. [Identify which variable(s) are incorrect, and what its correct value(s) should be](#guide-5)
    6. [Add the diagnostic code earlier in your program execution when you are sure your code is correct](#guide-6)
    7. [Keep adding diagnostic code until you have identified where the bug is](#guide-7)
    8. [Fix your code](#guide-8)
    9. [(Optional) Create a test for this bug](#guide-9)
* [Conclusion](#conclusion)
* [Other Resources](#resources)

## Introduction <a id="introduction"></a>

> "Debugging is twice as hard as writing a program in the first place."
>
> \- Brian Kernighan, The Elements of Programming Style

More than programming, debugging requires the mindset of a problem solver. Code *can* be written sloppily and in an ad-hoc way; debugging *must* be done methodically and with attention to detail. This guide is about the concrete steps of debugging, but I highly recommend first reading [Ryan Chadwick's problem solving tutorial](https://ryanstutorials.net/problem-solving-skills/) for an introduction to the appropriate attitude and mindset. This guide is heavily inspired by [a similar guide by John Regehr](https://blog.regehr.org/archives/199).

## Terminology <a id="terminology"></a>

To make things clearer, I will use the following terms for the rest of this guide:

* *Symptom* - The behavior of the program that is incorrect. This could be a null pointer exception, or a ValueError, or simply some output or return value that is incorrect.
* *Bug* - The underlying code that is incorrect, which made lead to zero or more symptoms.
* *Diagnostic Code* - Code that is written not as part of the program, but to help with debugging.
* *Input* - The data that your program operates on. This could be actual typed input from the user, arguments to a function, numbers from a spreadsheet, or even mouse movements on a webpage.
* *Test Case* - Although this usually means some input that we know the correct behavior for and can check against, here I use this term to mean the input that causes the program to exhibit symptoms.
* *Minimal Test Case* - The smallest test case that will cause the same symptom. Alternately, the smallest test case that will expose the same bug (even if the symptoms are different).

It is important to remember here *symptoms are not the same as bugs*. Your program may be buggy, but could run fine without symptoms on the input you are using. Sometimes, different symptoms under different inputs may ultimately be caused by the same bug. Other times, a symptom may be due to multiple bugs in your code, all of which must be fixed before your program is correct. On occasion, the symptom may lead to the realization that your current approach is completely infeasible, forcing you to rewrite your code from scratch; in that case, there is no single "bug" that's causing your program to fail.

Debugging is process where, given one or more symptoms, you determine the bug(s) that led to it, and (ideally) removing those bugs from the code. In this sense, debugging is like being a detective trying to figure out what happened from evidence left behind, or like a scientist trying to understand some puzzling phenomenon. Lucky for us as programmers, we have the ability to replay what happened by running the program again, and to ask the computer to tell us more about what is happening by adding diagnostic code.

<!--
TODO talk about the relationship between testing
-->

## The Mental Game of Debugging <a id="mental-game"></a>

> "Would you tell me, please, which way I ought to go from here?"
> 
> "That depends a good deal on where you want to get to," said the Cat.
> 
> "I don't much care where -" said Alice.
>
> "Then it doesn't matter which way you go," said the Cat. 
>
> \- Lewis Carroll, Alice in Wonderland

This guide is written for what's known as "print debugging" - that is, I'm assuming that the only thing you have is the source code and the ability to add print statements. Many languages and IDEs have debuggers, which will do the printing for you or offer other ways of understanding what your program is doing. These are highly useful, and I recommend learning to use them in your programming language/environment of choice. Debuggers may not always be available, however, and even with debuggers, the *thinking process* of debugging is the same, which is why this guide uses print debugging.

A lot of programmers, when they first start writing code, engage in what I call "trial-and-error debugging". That is, when they see that their program doesn't work, they randomly change their code, then run it to see if that fixed the problem. *This habit is counter-productive, and the sooner you get rid of it the better.* While this strategy might get you through your first (or even second) programming class, it will *not* work as your program gets more complicated. There are simply too many possible things to change, and without knowing what you're doing, proceeding with guess-and-check will never fix your program - or worse, introduce additional bugs.

Instead, debugging requires having a clear understanding of *what your code should be doing* and *what your code is actually doing*. After all, what is a bug if not a mismatch between expectation and reality? As per the *Alice in Wonderland* quotation, if you don't know what your code is supposed to do, then it doesn't matter what changes you make. The *mental game* of the debugging process starts here, and the rest of this guide is about the *mechanics* of figuring out where this mismatch occurred.

## A Debugging Guide <a id="guide"></a>

Now that you've discovered a symptom of a bug in your program, what do you do next? Here's a brief guide:

1. <a id="guide-1"></a> Verify that the symptom exists, and determine the correct behavior. As I said, that second part is probably *the* most important step of debugging: *you can't debug your code if you don't know what your code is supposed to do*. And I don't mean what your code is supposed to do overall; I mean what your code is supposed to do *at every single line*, why that line is necessary, and what value each variable is supposed to have at that point. If you can't answer that question, this is the time to pause and review the step-by-step outline for your code - you do have a step-by-step outline, right?

2. <a id="guide-2"></a> (Optional) Create a minimal test case. When you first discover a bug, the inputs required to trigger the symptom are often complicated, which makes the debugging process itself complicated. The goal of this step is to see if you can simplify the input so it's easier to understand what is going on and, ideally, create the smallest possible input that would still trigger the bug. How to create a minimal test case is highly dependent on the program, and may only be possible after some of the later steps, which is why this step is optional.

3. <a id="guide-3"></a> Add some diagnostic code immediately before the symptom. Since we are using print debugging, this means printing out relevant variables so that you can peek inside your program as it runs. You can think of this as trying to create a new "symptom" - you know what the diagnostic code should print, and you can now check that it is (or isn't) printing that. What variables to print depends on your program; you want to balance having useful information with not being overwhelmed with data. You can always add more diagnostics, however, so start with what you think might be wrong and go from there.

    Note that this step may involve more than just adding a single `print()` statement. If your code is dealing with nested lists and classes that contain each other, you might have to write loops or even recursive functions to print them all out. One piece of advice here is try to minimize how much of this support code is in your main program. Instead of writing your loops directly above where the symptoms show up, put that loop in a function, and call that function before your symptom. This helps keep your actual code clean, and will also let you reuse that diagnostic function in other places.

4. <a id="guide-4"></a> Make sure your diagnostic code is correct and that its output is easy to understand. Never forget that *your diagnostic code is still code, and it can have bugs of its own*. You will never fix your bug(s) if your diagnostics is feeding you bad information. Similarly, if your program now crashes in your diagnostic code, you're not learning anything about where your code might be incorrect.

    Slightly related to making sure your diagnostic output is correct is making sure your diagnostic output is understandable. Don't just print out a variable; print out the variable and some text that tells you what variable it is and where it's printing from. There is nothing more draining than having to count the lines to figure out which value corresponds to which variable.

5. <a id="guide-5"></a> Identify which variable(s) are incorrect, and what its correct value(s) should be. If you don't know which variables are incorrect, see the note in Step 1.

6. <a id="guide-6"></a> Add the diagnostic code earlier in your program execution when you are sure your code is correct. Double-check that the diagnostic output is indeed what it should be. This step is not strictly necessary, but it's good practice regardless, for reasons you will see in the next step.

7. <a id="guide-7"></a> Keep adding diagnostic code until you have identified where the bug is. If the diagnostic output is correct for some part of your program, add diagnostic code to a later line. If the diagnostic output is *incorrect* for some part of your program, add diagnostic code to an earlier line. The goal here is to isolate a single line of code where your bug might be, before which your diagnostic code shows no symptoms, after which the diagnostic output is incorrect. If this line of code calls a function, you may have to continue debugging inside that function.

    To beat on a dead horse, doing this step effectively requires you to know exactly what your program should do. For example, let's say your diagnistic code showed that a variable is zero. Is it *correctly* zero, so you need to add a special case to handle that? Or is it *incorrectly* zero, so you need to track down where it's being calculated? Just knowing what value each variable has is insufficient; you must also be able to identify which of those values are correct and incorrect, in order to trace down the bug.

    It is important to remember here that you might have to chase through multiple layers of apparent symptoms and bugs. For example, the original symptom might be caused by a variable being zero, but that variable is being set to the return value of a (correct) function, so now you have to chase down where the arguments of that function is set. Also keep in mind that a symptom may be hiding multiple bugs, as might be the case if *two* of the arguments to that function are wrong. In that case, you will have to focus on one symptom/bug first before the other, but the process of debugging is the same.

    Assuming there is only one bug, there are two main ways this step can go wrong:

    * There is more than one line of code between where your diagnostics are correct and where they are incorrect, and you are not sure where to add diagnostic code next. Often, the code here is complicated with loops and function calls and all sorts of other things. There are two common causes of this blockage:

        * It might be because *your diagnostics are not detailed enough* to further narrow down where the bug could be. Maybe you have only been printing the ID of an object and not all of its other member variables, and it is the member variables that are being checked. Maybe you have only been printing some variables but not others, and those other variables are being changed. In this case, the next step is obvious: add more diagnostic code until all the relevant variables are printed out, then go back to Step 5.

        * It might be because *you do not fully understand what your code should be doing*. In this case, the next step is *also* obvious, but much harder: think through what the correct behavior of your code should be. Again, see the note in Step 1.

        Note that these causes are not mutually exclusive - you might not be printing some variable, *and* you are also unsure how that variable should change in the code.

    * The line of code you identified was written by someone else. For example, it might be a call to a function given to you by your professor, a function from a library/framework, or a function that is part of the standard library of the programming language itself. In this case, you should:

        1. Re-read the documentation for that function to make sure you understand what its parameters and return values are, and that it does what you think it should do.

        2. Double-check that you are calling the function with the correct arguments, in the correct order.

        3. To be *absolutely* sure that you are calling the function correctly, try writing a small program that only calls that function, making sure to recreate your arguments from scratch. This may or may not be possible depending on your program and how complicated your arguments are.

        4. If you are absolutely sure that you are using the function correctly, it's not impossible that the function has a bug! If the function comes from a library or framework, this is the time to start Googling to see if other people have run into this issue.

        5. If searching online doesn't give any answers, this is the time to contact the author of the code, either by filing a bug report on Github (if the code is open source), or by emailing your professor. Since you may not get an answer for a while (or ever), it is time to start thinking about how you can write your code *without* using the buggy function.

8. <a id="guide-8"></a> Fix your code. This is the step that most people imagine when they think about debugging, but as you can see, this step is only possible after a lot of thought and work. If you got to this step, then you have identified the line where the bug lives. Even then, however, fixing the bug may not be trivial. In the best case scenario - which most bugs fall into - you made a typo or forgot to do some basic operation, in which case you can fix that and be on your way. In the worst case scenario, the bug has exposed a gaping hole in how your program works. Maybe there's an edge case you didn't think of; maybe the input that triggers the bug violates some fundamental assumption you had. It's entirely possible that your program is unfixable, and you will have to start from scratch without that assumption.

9. <a id="guide-9"></a> (Optional) Create a test for this bug. In the ideal case, you already have a suite of tests to automatically check that your code is correct. Now that you've fixed the bug, you want to make sure that it never shows up again. If you created a minimal test case in Step 2, then add that test case into your test suite. If you don't have a minimal test case, you can create one now (much more easily, now you know what the bug is), then add that to your suite.

<!-- TODO 

## A Simple Example

(FIXME add back comment directive for prettify)
```python
def quadratic(a, b, c):
    """Solve the quadratic formula and return the first (positive) root."""
    root = sqrt((b * b) - (4 * a * c))
    numerator = -b + root
    x = numerator / 2 * a
    return x
```

## A More Complicated Example

FIXME how I overwrote my AVLTree in MemArch?

-->

## Conclusion <a id="conclusion"></a>

To summarize: debugging is about finding the mismatch between *what your code is doing* and *what you expect your code to do*. You can't debug without knowing both. Figuring out former is "easy": you add diagnostic code. It's not knowing the latter where most people get stuck with debugging.

Good luck, and happy bug hunting!

## Other Resources <a id="resources"></a>

* [Problem Solving Skills and Techniques](https://ryanstutorials.net/problem-solving-skills/) - Ryan Chadwick
* [How to Debug](https://blog.regehr.org/archives/199) - John Regehr
* [What does debugging a program look like?](https://jvns.ca/blog/2019/06/23/a-few-debugging-resources/) - Julia Evans
* [The Pocket Guide to Debugging (paid zine)](https://jvns.ca/blog/2022/12/21/new-zine--the-pocket-guide-to-debugging/) - Julie Evans
* [UChicago's debugging guide](https://uchicago-cs.github.io/debugging-guide/)
