Title: How to Backup Your Data
Date: 2007-12-18 17:04
Slug: how-to-backup-your-data

Remember how I managed to [fry my USB
port](http://justinnhli.com/posts/2007/11/i-was-shocked.html) with a
little ESD? The most immediate problem is that I could not use my USB
mouse, and had to stay with my trackpad for a few weeks. I also knew at
the time, however, that I would have a hard time backing up my data to a
USB connected external disk.

I bought a PCMCIA-USB card yesterday, which worked fine for the mouse.
When I tried to plug in my external disk though, none of my three OSes
(Windows, Ubuntu, and Arch) detected the device at all, even though the
light on the drive lit up. I had already anticipated that the PCMCIA
card won't have enough power for the disk. Luckily, the disk came with
an second power only USB cable, which I then also plugged in but to no
avail.

After trying the drive on my desktop, and moving it back and forth for a
while, I figured out that the power cable does not by itself provide
enough power. If it needs the power cable, then both that and the
power+data cable needs to give it juice for it to run. It seems that the
PCMCIA card just doesn't give enough juice.

I was then at a dilemma. I want to backup my files (so I could reinstall
my OSes, something I do once or twice a year). There doesn't seem to be
a way to connect my laptop to my disk though.

What I eventually did was a really convoluted way of doing backups, but
it works. I took my new Ubuntu 7.10 boot disk and ran it on my desktop.
Now I have two Linux boxes running. I connect my external disk to my
desktop, which detects it and reads it correctly. Finally, I use SFTP to
connect my desktop to my laptop, and do a backup "remotely" that way.

The result: I'm typing this post on a newly installed Ubuntu 7.10.

