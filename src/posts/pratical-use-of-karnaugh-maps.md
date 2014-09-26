Title: Pratical Use of Karnaugh Maps
Date: 2007-09-15 19:24
Author: justinnhli
Slug: pratical-use-of-karnaugh-maps

I can't believe I just used a truth table and a Karnaugh Map to help
write my calendar!

My 4 variables were:

-   whether an event begins repeating after the first displayed date (A)
-   whether the first occurrence of an event ends after the first
    displayed date (B)
-   whether the first occurrence of an event ends before the last
    displayed date (C)
-   whether an event stops repeating before the last displayed date (D)

This sounds confusing, doesn't it. Let's say I have an event like dorm
munchies, which is from 23:30 to 00:30 every Friday night of Fall
quarter (from 09-28 to 12-07). Before I start spewing out the dates when
this would happen, I need to know whether I should bother at all. Not
calculating the dates, of course, means the calendar will load faster.
Imagine not doing this for just dorm munchies, but also all your
classes, group meetings, and TA sessions! Knowing what to calculate and
what not to will save loads of time (which just happen to be counted in
milliseconds, but that's eons for a CPU).

So, let's play with logic. For the above scenario, we have

-   Start Date: 09-28
-   End Date: 12-07
-   Start Time: 23:30
-   End Time: 00:30

So, the event repeats from 09-28 to 12-07. The first time it will happen
is 09-28 23:30, which I call the Start Date Time, or SDT. The first time
it ends is on 09-29 00:30, which I call the End Time, or ET. The date it
will last occur is 12-07, so I call 12-08 00:00 the End Date, or ED.
Note that ED marks the time after which the event will no longer <span
style="font-weight:bold;">start</span>; the last munchy will not end
until 12-08 00:30.

I'll show you the solution first, and explain how I got there. In
addition to the shorthands about, I also use CSD and ESD for Calendar
Start Date and Calendar End Date respectively.

  ------------ ----------- ----------- ----------- ------------------
  SDT \< CED   ET \> CSD   ET \< CED   ED \> CSD   Should Calculate
  T            T           T           T           T
  T            T           T           F           T
  T            T           F           T           T
  T            T           F           F           T
  T            F           T           T           T
  T            F           T           F           T
  T            F           F           T           X
  T            F           F           F           X
  ------------ ----------- ----------- ----------- ------------------

The goal of this exercise is to find when the event might possibly
appear on the calendar, whether it's only once or for every week in that
span.

First, you will note that I didn't extend the table for when SD \> CED.
If the event starts after the calendar stops, under no circumstance will
it appear on the calendar. That's 8 out of 16 possible permutations.

Second, since CSD is before CED, ET has to either be before CED or after
CSD. That is  

> (CSD (ET CSD)
> </p>

This makes the last two roles of the table Don't Cares, to make it
whatever we want to simplify the final equation. 10 down, 6 to go.

A simple example will show that when SDT CSD are both true, it will be
on the calendar. Because CSD \< CED, the first repetition of the event
is bound to appear on the calendar, no matter when the repeating stops.
That gets rid of 4 more; 14 down, 2 to go.

A similar argument can be used when ET CSD, but it's a little trickier.
If the first event ends before CED, that means it will repeat after
that - unless it stops before the calendar starts at CSD. However, since
ED \> CSD, we know that at least some repetition of the event is in
calendar range.

Last permutation. If the first repeat both starts and ends before the
calendar ends (CDT \< CED, ET \< CED), again the event would repeat
after that. But now, ED is before CSD. So the event has no way of being
on the calendar, right? <span style="font-weight:bold;">Wrong</span>.
Remember how ED is the last date the event will <span
style="font-style:italic;">start</span>? Well, the event doesn't <span
style="font-style:italic;">end</span> on that day. So if CSD = 12-08,
although ED \< CSD, <span style="font-style:italic;">there is still 30
minutes of munchies at the beginning of 12-08!</span> So the event could
still appear on the calendar in this case. All permutations done!

Now for the Karnaugh Map. To simply things, lets label the inequalities
A, B, C, and D.

<table>
<tr>
<td colspan="2" rowspan="2">
</td>
<td colspan="4">
AB

</td>
</tr>
<tr>
<td>
11

</td>
<td>
10

</td>
<td>
00

</td>
<td>
01

</td>
</tr>
<tr>
<td rowspan="4">
CD

</td>
<td>
11

</td>
<td>
T

</td>
<td>
T

</td>
<td>
F

</td>
<td>
F

</td>
</tr>
<tr>
<td>
10

</td>
<td>
T

</td>
<td>
T

</td>
<td>
F

</td>
<td>
F

</td>
</tr>
<tr>
<td>
00

</td>
<td>
T

</td>
<td>
X

</td>
<td>
F

</td>
<td>
F

</td>
</tr>
<tr>
<td>
01

</td>
<td>
T

</td>
<td>
X

</td>
<td>
F

</td>
<td>
F

</td>
</tr>
</table>
The solution to such a torturous problem is surprising simple: the event
might be on the calendar if A is true, or if the event first starts
before the calendar begins.

And you thought all that stuff learned in Intro to CE was useless...

