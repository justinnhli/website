Title: Batch Quick Adding in Google Calendar
Date: 2008-09-13 18:15
Slug: batch-quick-adding-in-google-calendar

I decided to switch to Google Calendar recently, despite my painfully written HTML/JavaScript calendar I had before. One thing that was a pain for me to do was to import the birthdays I have saved into Google Calendar. Since my previous calendar is home-brewed, I didn't use anything like the iCal format, or even CSV. Instead, the format looks something like this:

> <li>
> N|198712200000|2400|-|1|A|Justin Li's Birthday
> </li>

The scheme is actually rather ingenious, if I may say so myself. The first letter declares what it is (either an event, a note, or a task).  The following string of numbers is the date and time when the event starts. Following that is the ending date and time, the date it stops repeating (if it repeats), and then a code for how it repeats. The 'A' is a color tag, and finally we have what the event is. If I want to, I could also put down the venue as well as a longer description, but here it's not necessary.

It would seem that this format is close to the CSV format needed by Google, except for one thing: I'm not sure how to specify recurrence.  For a birthday it would clearly repeat every year on the same day, which I specified in my calendar with the dash (for a never ending repetition) and the '1' (for repeating every single year). I have no idea what Google's CSV format requires for recurrance.

Instead, I was rather taken by the Quick Add feature. It definitely understands commands like this:

> Justin Li's Birthday on 1987-12-20 every year

For humans there is the slight problem of how it could be 1987 <span
style="font-style:italic;">every</span> year, but the meaning is
nonetheless clear. I could easily change the text entries to Quick Add
format:  

> `cat entries | sed 's/^[^0-9]*\([0-9]\{4\}\)\([0-9]\{2\}\)\([0-9]\{2\}\).*|\([^|]*\)$/\4 on \1-\2-\3 every year/'`

That should do it. For those interested in Bash scripting, I'm using `sed` to do a regular expression (regex) substitution. I picked out the year, month, date, and the event name, and reorganized them into the format above.

That was the easy part. The hard part was looking for a way to use quick add multiple times (almost) simultaneously, so I could enter all the birthdays at the same time. A quick Google search returned this [onfocus article](http://www.onfocus.com/2006/04/3799). At first it looks promising, but then I realized it's simply converting to CSV, which doesn't help me much.

Digging further I found Elias Torres's [Google Calendar Quick Add Firefox extension](https://addons.mozilla.org/en-US/firefox/addon/2405).  Sounds great! I would still have to copy each line into the textbox, but that's a start... if the extension was for Firefox 3, that is. I have unfortunately not yet learned to write Firefox extensions, and therefore gave this up and kept looking.

Then I remembered [Ubiquity](https://wiki.mozilla.org/Labs/Ubiquity), the snazzy Firefox extesion that aims to "[connect] the Web with language in an attempt to find new user interfaces that could make it possible for everyone to do common Web tasks more quickly and easily." Interested readers can go to the [Mozilla Labs blog post](http://labs.mozilla.com/2008/08/introducing-ubiquity/) for a detailed description, a video demo, and more.

The feature I was most interested in was the add-to-calendar function in Ubiquity, which, well, adds an event to Google Calendar. It does take advantage of the Quick Add function, but a quick look at the source code for that function, and testing it out, reveals that it dumps the recurrence information, which is what I wanted most. The script adds events in two parts: first, it lets Google parse what you wrote, then it tells Google to add it. The URL for the parser for the above command is:

> http://www.google.com/calendar/compose?qa-src=QUICK\_ADD\_BOX&ctext=Justin%20Li%27s%20Birthday%20on%201980-12-20%20every%20year

As you can see, the plain English event description is just tagged on the back. Google will spit something like this back out:

> while(1); [['\_SpawnQuickAddEvent', 'Justin Li's Birthday', '', '',
> '19801220', '19801221', [], '', null, null, [],
> 'RRULE:FREQ=YEARLY;INTERVAL=1']]

A quick glances reveals it to be JavaScript code. Ubiquity than takes this and forms anther query, which I won't go into. Suffice to say it doesn't use the RRULE part of the data, which means it disregards the recurrence. It does however use the following URL:

> http://www.google.com/calendar/event?

What I need to do now is to figure out what the parameter name is for the recurrence rule. After looking online with no results (which surprises me; usually things like this, especially for a Google service, are well discussed and documented), I added a few fake events through the actual Google Calendar site, and watched the Net traffic through [Firebug](http://getfirebug.com/). That quickly revealed the parameter to be `recur`, which lead to the final URL for batch Quick Adding:

> http://www.google.com/calendar/event?action=CREATE&secid=...&output=js&recur=RRULE:FREQ=YEARLY;INTERVAL=1&dates=19871220/19871221&text=Justin Li's Birthday

Breaking it down:

* `action=CREATE` tells Google to add the event to its database
* `secid=...` is the session security id, which can be found in the browser's cookies
* `output=js` tells Google what to show after it's done. You can also use output=xml to get a webpage back
* `recur=RRULE...` is how the event will repeat, which the Google parser gave us
* `dates=.../...` gives the beginning and end dates for your event
* `text=Justin...` is the title of the event.

And that's it! I added close to 200 birthdays to my calendar in no time (using some more regex trickery and heavily abusing "Open Link in New Tab"). I have no doubt this will come in useful again sometime.

Of course, I spent over 2 hours figuring all this out. But that's part of the fun.
