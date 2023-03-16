title: Bash Command Line Cheat Sheet
category: resources

Most commands looks like this: `ls -l code`

1. The first part (`ls`) is the *command*. Different commands do different things.
2. The second part (`-l`) is an *option*. They change how the commands work.
3. The third part (`code`) is an *argument*. They specify what the command acts on.

Options are always optional. Some commands (and some options) have required arguments. In this cheat sheet, `<argument>` means that the argument is required; `[argument]` means that the argument is optional.

## Getting Help

* <https://google.com/> - Google is your friend. Googling a command or a task will often give you multiple ways of doing what you need.
* `<command> --help` - Calling the command with the `--help` option will often print out a short help message.
* `man` *`<command>`* - Many commands have a <span style="text-decoration:underline;">man</span>ual you can read. It's on the verbose side and is not always easy to understand, but it's built into every system.
* <https://explainshell.com/> - If you see a command you want every option and argument explained, ExplainShell will match each part with its explanation from the `man` pages.

## Stopping

* `exit` - Log out of the command line.
* ctrl+c - Most commands can be stopped by pressing CTRL+C. Note that it's still Control, not &#8984; or Option or Alt, on a Mac.
* q - Some commands (notably `man`, `less`, and `top`) use the Q key to quit.

## File Navigation

* `pwd` - Print the <span style="text-decoration:underline;">p</span>resent <span style="text-decoration:underline;">w</span>orking <span style="text-decoration:underline;">d</span>irectory (ie. the current folder) you are in.
* `cd` *`[path]`* - <span style="text-decoration:underline;">C</span>hange <span style="text-decoration:underline;">d</span>irectory to the given path. If no path is given, changes to your home directory.
* `ls` *`[path]`* - <span style="text-decoration:underline;">L</span>i<span style="text-decoration:underline;">s</span>t the contents of the given path, or the current directory if none is given. Common options include `-a` to show <span style="text-decoration:underline;">a</span>ll files and `-l` to use the <span style="text-decoration:underline;">l</span>ong format (ie. more details).

## File Manipulation

* `mkdir` *`<path>`* - <span style="text-decoration:underline;">M</span>a<span style="text-decoration:underline;">k</span>e a <span style="text-decoration:underline;">dir</span>ectory (the given path). Use `-p` to also create intermediate (<span style="text-decoration:underline;">p</span>rerequiste) directories as needed.
* `mv` *`<file>`* *`<path>`* - <span style="text-decoration:underline;">M</span>o<span style="text-decoration:underline;">v</span>e a file to a directory.
* `cp` *`<file>`* *`<path>`* - <span style="text-decoration:underline;">C</span>o<span style="text-decoration:underline;">p</span>y a file to a directory.
* `rm` *`<file>`* - <span style="text-decoration:underline;">R</span>e<span style="text-decoration:underline;">m</span>ove a file. **This does not ask for confirmation and cannot be undone.**
* `rmdir` *`<path>`* - <span style="text-decoration:underline;">R</span>e<span style="text-decoration:underline;">m</span>ove a <span style="text-decoration:underline;">dir</span>ectory. Only works if the directory is already empty. **This does not ask for confirmation and cannot be undone.**
* `less` *`<file>`* - Display a file. Press `q` to quit.

## Text Manipulation

* `nano` *`<file>`* - Edit a file. The available commands are listed at the bottom, with the `^` meaning CTRL (eg. CTRL+X to exit).
* `head` *`<file>`* - Print the first 10 lines of a file. Use `-n 20` to print (for example) the first 20 lines.
* `tail` *`<file>`* - Print the last 10 lines of a file. Use `-n 20` to print (for example) the last 20 lines.
* `wc` *`<file>`* - Show a <span style="text-decoration:underline;">w</span>ord <span style="text-decoration:underline;">c</span>ount of a file.
* `sort` *`<file>`* - Sort a file by lines. Use `-i` to <span style="text-decoration:underline;">i</span>gnore case and `-n` to treat the lines as <span style="text-decoration:underline;">n</span>umbers.
* `grep` *`<text>`* *`<file>`* - Print the lines where *`<text>`* exists in *`<file>`*. Use `-i` to <span style="text-decoration:underline;">i</span>gnore case and **-r** to <span style="text-decoration:underline;">r</span>ecursively search through directories.
* `uniq` - Print the `uniq`ue lines of a file. Assumes the file to be sorted first. Use `-d` to show <span style="text-decoration:underline;">d</span>uplicates instead and `-c` to count each unique line.

## System Status

* `date` - Print the current date.
* `uptime` - Print how long the computer has been on.
* `top` - Show the most active programs. Press <span style="text-decoration:underline;">q</span> to quit.
* `df` - Show the amount of space available on the hard disk. Use `-h` to get <span style="text-decoration:underline;">h</span>uman-readable sizes.
* `du` *`<file>`* - Show the amount of space taken up by the file. The current directory is used if no file is given. Use `-h` to get <span style="text-decoration:underline;">h</span>uman-readable sizes, and `-s` to get <span style="text-decoration:underline;">s</span>eparate sizes for each file.
* `uname`- Print system information. Use `-a` to show <span style="text-decoration:underline;">a</span>ll information.

## Other Utilities

* `cal` *`[[month] year]`* - Print a <span style="text-decoration:underline;">cal</span>endar, optionally specifying year and month.
* `diff` *`<file1>`* *`<file2>`* - Find the <span style="text-decoration:underline;">diff</span>erence between two files. Use `-y` to show the files side-by-side.

## Advanced Topics

* Pipes - Many commands can be chained together with the pipe (`|`), so the output of one becomes the input of the other. For example, `head <file> | sort | uniq -c` will count the unique items in the first ten lines of a file.
* Command Substitution - In commands that have a text argument (eg. `grep`), the text could be the output of another command. For example, `grep "$(head -n 1 <file1>)" <file2>` will search `file2` for the first line of `file1`.
* Variables, Branches, Loops - Bash is a full programming language with variables, branches, and loops. Check the Advanced Bash Scripting Guide for more information.

## Other Resources

* [Linux Journey: Command Line](https://linuxjourney.com/lesson/the-shell)
* [Bash Guide for Beginners](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html)
* [Advanced Bash Scripting Guide](https://www.tldp.org/LDP/abs/html/abs-guide.html)
