Title: Some Trends
Date: 2011-02-13 01:53
Slug: some-trends

I've been playing with graph creators lately. No, not the [mathematical
graphs](http://justinnhli.com/posts/2010/12/sooner-apparently-means-later.html)...
well, I mean... the *other* type of mathematical graphs (aka. *plots*).
In particular, I was trying my hands at
[gnuplot](http://en.wikipedia.org/wiki/Gnuplot), and of course I needed
data. Where better than to plot trends from my own journal?

The x-axis shows time; each point represents the average over 6 months,
taking the first/later half of the year. The y-value is the percentage
of entries over this period which contains this word (or variants
thereof; for example, the Twitter plot also includes the word "tweet").
This is all generated programmatically - I extended my journal script to
calculate the percentage of entries containing given terms and output it
in table (space-separated value) form, which gnuplot then reads. Since
the data is highly specific, my gnuplot is also particular to this
application. I abused gnuplot's ability to ignore non-existent columns
and left it using 5 columns. The source is below:

    #!/usr/bin/env gnuplotresetset terminal pngset title "Prevalence of Term over Time" font "Arial,16"set border 3set xdata timeset timefmt "%Y-%m"set format x "%Y"set xlabel "Date" font "Arial,12"set xtics nomirror rotate by -45set mxtics 0set ylabel "Percent Entries with Term" font "Arial,12"set yrange [0:100] set ytics 10 nomirror                   set key autotitles columnheader enhanced reverse outside font "Arial,12"set style data lines # linewidth 2 ?set grid# plot [raw_data] using [x-col]:[y-col] [attributes]...plot "data.csv" using 1:2 linewidth 2, \             "" using 1:3 linewidth 2, \             "" using 1:4 linewidth 2, \             "" using 1:5 linewidth 2, \             "" using 1:6 linewidth 2, \             "" using 1:7 linewidth 2, \             "" using 1:8 linewidth 2

In the future I'm considering writing a script that generates gnuplot
scripts. It'll be easier than remember all these ugly commands.

And here are the resulting plots. The first one is on my use of online
services. You can clearly tell when I started using Reddit and how
quickly it dominated my life. The growth of Twitter is much slower
comparatively. Facebook is huge mostly because it's my main source of
how other people are doing.

<div class="separator" style="clear:both;text-align:center;">

[![](http://justinnhli.files.wordpress.com/2011/02/eb548-online-services.png?w=300)](http://justinnhli.files.wordpress.com/2011/02/eb548-online-services.png)

</div>

<div class="separator" style="clear:both;text-align:center;">

</div>

Next are some hobbies of mine, at least those I can think of off the top
of my head. It's obvious when I started climbing more often (and
therefore better); it's also clear that when I teach at CTY, it becomes
a big part of my life. As a computer science major and now a grad
student, I clearly code more than the chart shows; one could consider
that as habituation, I guess.

<div class="separator" style="clear:both;text-align:center;">

</div>

<div class="separator" style="clear:both;text-align:center;">

[![](http://justinnhli.files.wordpress.com/2011/02/74af8-hobbies.png?w=300)](http://justinnhli.files.wordpress.com/2011/02/74af8-hobbies.png)

</div>

Here's another one, on academic topics. These were all topics I
considered studying in college. I eventually majored in computer science
and got a certificate in engineering design, but took extra classes in
all these subjects. I think it's neat that these topics has all been
mentioned more often over time - that I'm still into the same subjects I
was in high school and college... except design, which I haven't done
any of since junior year.

<div class="separator" style="clear:both;text-align:center;">

</div>

<div class="separator" style="clear:both;text-align:center;">

[![](http://justinnhli.files.wordpress.com/2011/02/d7d75-subjects.png?w=300)](http://justinnhli.files.wordpress.com/2011/02/d7d75-subjects.png)

</div>

I would love to do more of these, but I can't think of anymore sets of
terms to compare. Comment if you can.

