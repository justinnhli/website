title: Hiding Individual Code Cells in Jupyter
date: 2020-04-12
status: draft

One annoyance I have with [Jupyter Notebooks](https://jupyter.org/) is that there is built-in no way to hide the code. The way I use Jupyter, I tend to create headings and text in Markdown, but then I have to scroll past a bunch of code before I get to the plots. This is particularly annoying when I'm sharing a notebook with non-programmers, since they don't care about the code at all.

FIXME image

Most of the solutions for this problem insert code to [hide all code blocks in the entire notebook](https://stackoverflow.com/questions/27934885/how-to-hide-code-from-cells-in-ipython-notebook-visualized-with-nbviewer), but that's not what I want either. My ideal solution would be to be able to show and hide each individual code block, so I can edit the code for that cell if necessary.

Procrastinating over this weekend finally led to to code up a solution. The result looks like this:

FIXME image

The relevant code is in the first code block:

<!--? prettify linenums=true ?-->
```python
def create_hide_code():

    display(HTML('''
        <script>
            function code_toggle(button) {
                button = $(button);
                var input = button.parents(".cell").children(".input");
                input.toggle()
                if (input.css("display") === "none") {
                    button.html("Show Code");
                } else {
                    button.html("Hide Code");
                }
            }
        </script>
    '''))

    def hide_code():
        timestamp = str(monotonic_ns())
        display(HTML('''
            <button id="''' + timestamp + '''" onclick="javascript:code_toggle(this);">
                Hide Code
            </button>
            <script>
                setTimeout(function () {
                    var button = $("#''' + timestamp + '''");
                    button.html("Show Code");
                    button.parents(".cell").children(".input").hide()
                }, 500);
            </script>
        '''))
        
    return hide_code
```

This function consists of two parts. First, it loads into the notebook a JavaScript function that toggles whether the code is visible. Second, it defines and returns another function, which can be called to hide code. To use it, simply call `hide_code()` in the code blocks you want to hide:

FIXME image

When the cell is run, this will hide the code and display a "Show Code" button, which I can use to toggle the code for editing if necessary.
