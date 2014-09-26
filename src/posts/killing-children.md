Title: Killing Children
Date: 2009-05-20 05:00
Author: justinnhli
Slug: killing-children

It is commonly known that a lot of computer jargon are tongue in cheek,
especially when they were first developed. For examples, processes are
compared to people, so when they *spawn* other processes, the original
one is called the *parent* and the other one the *child*. When you stop
a process, it's called *killing* it. There are also times when the
process is *dead* but still taking up resources, and very naturally we
call them *zombies*...

Recently I ran into the problem of killing child processes. I want the
output of a command in a variable, so something like this:

`output="$(command...)"`

The problem is two fold: the command itself spawns new children, and the
command I'm running may not terminate. What I want to do is set a timer,
then when the time is up I would kill the process. To kill it though, I
would have to kill the youngest (inner most) child. I couldn't find a
simple way to do this, so this is what I came up with:

    output="$(command...)" &t=1d=0while (( "$t" < 120 && "$d" == 0 )); do    sleep 1    if jobs | grep -v 'Done' | grep -v 'Exit 1' | grep 'parse' > /dev/null; then        t="$(( $t + 1 ))"    else        d=1    fidoneif (( "$d" == 0 )); then    ps -AH | grep -A 10 "^ *$(jobs -l | awk '{print $2}')" | grep -B 10 ps | grep -v ps | awk '{print $1}' | while read pid; do        kill -9 "$pid"    done    output=''else    output="$(command..)"fi 

     

My question is, is there a simpler way?

