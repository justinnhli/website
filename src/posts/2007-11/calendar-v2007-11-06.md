Title: Calendar v2007.11.06
Date: 2007-11-07 04:47
Slug: calendar-v2007-11-06

I finished [revamping my
calendar](http://ninghui48.googlepages.com/calendar.html) today. The
idea has been out [for a
while](http://justinnhli.com/posts/2007/10/calendars-and-to-do-lists.html),
but I only recently got around to designing and coding the interface. I
think the code is actually cleaner than what I started out with, despite
having multiple extra rows that I didn't have before. The reason for
that is I switched almost completely to ID based element selection, as
opposed to my previous method of using long chains of
firstChild.lastChild's. If you use Firefox's DOM Inspector (installed by
default on Mac and Linux, optional on Windows; if you don't have it you
have to completely reinstall Firefox), you can see that most of the high
up elements have IDs and at least one class. This made both the CSS and
the code a lot cleaner.

Functionally, the big difference is where all the tasks are shown.
Before, the tasks for a day are simply listed in the mouse over pop up
for the date. Then all the to-do items for the coming week are also
shown in the Agenda pop up, found in the lower left corner of the page.
Any over due items are listed there as well.

This normally works great, except when I have to combine normal events
with the tasks. For example, if you go to 2007-11-05 through the Date
Selector (top left corner), you can see that I had a midterm on that
day. What would have taken a while to notice (if at all) in the old
calendar is that I have four things due the next day. So, I could either
go hiking and study over the weekend, or I could study and do homework.
If I just saw the calendar, and didn't realize I have homework due the
next day, I would probably have gone hiking. But knowing that I have
work to do, and four pieces of them no less, I would probably have opted
to finish (at least some of) it over the weekend.

That's the main advantage of showing to-do tasks visually. A side
benefit is that the date column is now very clean, only being a
different color if there really is a special event, or a conflict, or if
I deleted something on that date (look at Thanksgiving).

I'm not too happy with the color of the near-black to-do reminders, but
I could not find another color for it to work. By that, I mean I can't
find another color as defined by [the Tango
project](http://tango.freedesktop.org/Tango_Icon_Theme_Guidelines);
that's the only reason these colors go together so well in the first
place.

