Title: Linux Monitor Power Save
Date: 2007-09-28 23:11
Slug: linux-monitor-power-save

Ever since I've been playing with Linux, I have tried to get it go turn
off the monitor. There is a widely distributed way of doing that, but
for some reason it never worked for me. So last weekend, when I had some
time on my hands, I hunted around and found another way.

Usually, if you use the X window system, you can just do  

>     xset dpms force off

and that will turn off the monitor. Alternatively, you can install
xscreensaver and do that from the control panel too, started by  

>     xscreensaver-demo

This method actually allows the screen to go blank after an idle period.

As I said, neither of these methods worked for me. The command runs
without trouble, but there's no output, nothing. For the graphical way
of setting a timer and turning it off, it just doesn't work. Instead, I
found that I could use something called vbetool. It's a video bios tool,
which means it sort of goes under the OS and directly turns off the
screen.

I've made it into a keyboard shortcut, but from the command line/virtual
terminal (while running X), do  

>     vbetool dpms off

and it will turn off. It won't turn on again even if you move the mouse
or press a button though, so instead my shortcut is mapped to  

>     vbetool dpms off && read && vbetool dpms on

so when you press enter after it goes off, it turns back on. Otherwise,
you could switch to a virtual console (Ctrl + Alt + F[1-6] in X) and
switch back (Alt + F7) to activate it.

There are obviously problems with this, but it does work to turn off the
monitor when I sleep and use the laptop as an alarm. The problems
include:

-   not synced with xscreensaver lock screen - turning the monitor off
    doesn't lock the screen, and if the screensaver comes up you have to
    type the password blind.
-   doesn't turn on if a new window pops up - the "read" command to
    detect the enter requires the terminal to have focus. If a new
    window pops up (say, someone's IM), it loses focus and so I can't
    turn it off. I have to do it the old way, or Alt+Tab blindly around
    till I get the terminal back

