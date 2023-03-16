title: Intermediate Programming Tips
category: resources

So you've learned the basics of programming - loops, functions, objects, and all that jazz. You're looking to tackle something bigger, a several hundred/thousand line program that does something cool. How do you do that?

Here are some tips on how to tackle bigger projects for the intermediate programmer.

* Aggressively focus on the hardest part of your code first. Don't know how to use that library that's central to the problem? Unsure how the machine learning classification algorithm works? If these are things that *must* work for the final product, and you don't know how to use/code them, then start there. If you're writing a course scheduler, and you're planning on using [OR Tools](https://developers.google.com/optimization/reference/python/index_python), then your first step is understanding that library's API. If you're doing an information retrieval project and want to use [Scrapy](https://scrapy.org/), start with the tutorials there.

* Create an end-to-end system as soon as possible. By "end-to-end", I mean a system that can take meaningful input and give meaningful output. Importantly, *this may not be the actual format of input and output for your project*. This means you should ignore any and all user interface issues. Ideally, the core of your project can be put into one or more top-level functions. For course scheduling, it's taking a list of class preferences and spitting out a schedule; for scraping, it's taking in keywords and spitting out a list of links. The fact that the keywords should come from a webapp, or that the schedule needs to be formatted into a table, is irrelevant here.

* Test your code incrementally. Don't write 300 lines of code before running everything and just expect it to work. Write 5-10 lines of code, then run that and check that it does what you want. Only after making sure it works should you write 5-10 more lines of code to repeat the process. In the ideal world, these 5-10 lines of code would be in functions, and you should have test cases that automatically check that your code is correct. The purist approach to this is to use test-driven development (TDD), which involves writing your test case before your code. It's rare for a project to apply TDD completely, but if you want to try, see [this introduction](https://medium.com/@bethqiang/the-absolute-beginners-guide-to-test-driven-development-with-a-practical-example-c39e73a11631).

* Review the organization of your code periodically. Even in a one-person project, you can quickly accumulate [technical debt](https://en.wikipedia.org/wiki/Technical_debt). Maybe you started with some names of people, so you put them in a list of strings. Then, you realized you need to separate first names and last names, so you have two lists of strings. Then every person needs an ID, and a birthday, and suddenly you have four lists just floating around. At this point, the better thing to do is to create a Person class and have a single list of those. The same thing can apply to functions, whether that's to [stop repeating yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) or to create better interfaces.

* Pursue other resources on how to improve your programming skills:

    * [*How To Plan a Coding Project - A Programming Outline*](https://medium.com/swlh/how-to-plan-a-coding-project-a-programming-outline-fc5917c60553), by Grant Darling.

    * [*The Mental Game of Python*](https://www.youtube.com/watch?v=Uwuv05aZ6ug), by Raymond Hettinger, about writing clean code. Despite the name, the ideas here apply to other programming languages as well.

    * [*Debugging*](<https://justinnhli.com/pages/a-debugging-guide.html>), by Justin Li. A guide to debugging.
