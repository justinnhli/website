Title: Getting Past Free Hosting Ads
Date: 2007-09-17 15:02
Slug: getting-past-free-hosting-ads

My mom asked me to make a simple template of a website for her, so she
could do simple editing in the HTML to flesh out the site. She had
learned HTML years ago, when HTML 4 first came out, but is a little
rusty on the details. So I made a template with a left menu and right
content, with sample links and paragraphs of texts, using frames
(despite not liking frames, I have to sat that it's the easiest way to
make "floating" content, hands down).

The next problem was one of hosting. How do we get the page up? Googling
"free hosting" gives a lot of sites, and we randomly picked
www.00freehost.com. It was free, signup was not too bad, it had a
built-in Java FTP client. So I uploaded the template to see how it
works. The response was quick, no major issues.

One reason why the service is free is that they also offer paid
services, with more bandwidth, larger server space, etc. The other
reason is that they insert ads into your page. I really should have
expected that, but I guess I've been away from free hosting for so long
that I forgot. And since I was using frames with the left frame as the
menu (i.e. only has a list of text), the ads made it near impossible to
even locate the menu of links.

There had to be a way around this, I thought. Everything displayed in
the browser is HTML, and that can easily be changed with Javascript. My
theory is that I can somehow save what's on my page before, and use a
delayed Javascript call to replace the content of the document. It
seemed simple, but I had one problem: there was no way to save the
document before. I don't know how they load all the ads in, but it's
definitely between the tags, before my content. If I try to save the
original HTML with a script in the `head`, the browser wouldn't have
loaded the `body` yet, but anything in the body would be loaded after
their ads are inserted.

After wrestling with that for 30 minutes, I changed tactics. I wrapped
my actual content in a div, then had a script call after the div which
replaced the document. Like so:  

>         ...     document.body.innerHTML = \       document.getElementById('actual_content').innerHTML; 

That did the trick. When I visit the page, the ads would load first, so
for a few seconds there would be a moving smilie staring at me and no
content. Once the browser got to the script, BOOM, no ads, just my
content. Huzzah! Free hosting with no ads whatsoever.

Knowing that it worked, I pulled the Javscript into a separate .js file,
and included that in the head of each HTML file. Just to make it
cleaner. This means total ad-voidance with 4 extra lines of HTML.

It was only after I showed it to my mom that I was reminded it was
probably against the license agreement to do that. Oh well... It's not
like their ads didn't come up. It just didn't stay up.

:D

