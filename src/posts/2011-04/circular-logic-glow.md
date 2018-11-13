Title: Circular Logic - "glow"
Date: 2011-04-04 21:33
Slug: circular-logic-glow

The NYTimes [has a regular column on math puzzles](http://wordplay.blogs.nytimes.com/category/Numberplay/). I don't usually look at them, but when I do [I prefer Dos Equis](http://www.youtube.com/watch?v=8Bc0WjTT0Ps)... what? Oh yes, Numberplay. Most of the time I can't be bothered to figure out the answer, but [one of the questions this week](http://wordplay.blogs.nytimes.com/2011/04/04/numberplay-circular-logi/) happens to be computationally easy. The question is:

> Consider the word "glow." If you replace each letter with its counterpart in a mirror alphabet you will get the legitimate word "told." What other words exhibit this same property?

So I started wrote a little script in Python:

```python3
#!/usr/bin/env python3

import re

words = set()
with open('/usr/share/dict/cracklib-small') as fd:
    for word in fd.readlines():
        word = word.strip()
        if len(word) == 1 or re.match('[^a-z]', word):
            continue
        words.add(word)

for word in words:
    mirror = ''.join(chr(219 - ord(c)) for c in word)
    if mirror in words:
        print(word, mirror)
```

This script uses the computer's dictionary file (which I've used [before](http://justinnhli.com/posts/2011/03/herstory.html)), mutates the letters, then checks if the result is in the dictionary. The script outputs:

    all   zoo
    ark   zip
    art   zig
    blip  york
    de    wv
    dr    wi
    drib  wiry
    elm   von
    era   viz
    err   vii
    fir   uri
    fm    un
    ge    tv
    girl  trio
    girt  trig
    glib  tory
    glow  told
    gm    tn
    gs    th
    hob   sly
    hold  slow
    holt  slog
    holy  slob
    horn  slim
    ir    ri
    irk   rip
    iv    re
    ivy   reb
    levi  over
    low   old
    lug   oft
    md    nw
    me    nv
    mix   nrc
    mn    nm
    mrs   nih
    ms    nh

As a sanity check, notice that "glow" does indeed turn into "told" (and vice versa).

Problem solved in 10 minutes.

PS. I would have commented on the post, but I have no clue what my NYTimes password is.
