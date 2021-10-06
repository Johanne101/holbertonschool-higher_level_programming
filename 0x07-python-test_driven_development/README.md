------------------------------------
Python Test-driven development
====================================

  >" Trust but verify... with unit testing."
  >  >-Shakespeare

Python programming, is a powerful language for us computer nerds!
--------------------------------------------------------------------

### What is Interactive tests:

<p>
The doctest module searches for pieces of text that look like interactive Python sessions,
and then executes those sessions to verify that they work exactly as shown. ...
Depending on whether the examples or the expository text are emphasized,
this has the flavor of “literate testing” or “executable documentation”.
</p>

### Why tests are important?

you should always write the documentation (module(s) + function(s)) and tests first,
before you actually code anything.

### How to write Docstrings to create tests.

Here is an example of how to write functions with the Docstring...

```
# import StructuredText Docstring for testing the function.
from doctest import testmod

# define a function to test
def dnd_accept(self, source, event):
    """
    Decide what object will accept the drop.

    The returned object will become the new target for the drop operation.

    :param source: The object being dragged.
    :param event: The tk event that resulted in this call.
                  Usually a motion event.
    :return: The object that will accept a drop - this widget.
    """
    print("dnd_accept. Called on {}. source is {}, event type is {}".format(self, source, event.type))
    return self
```
```
# Google Docstring example.
def on_dnd_start(event):
    """
	Starts a drag and drop (dnd) operation.

    This is usually invoked by a mouse event binding on a
    widget that can be dragged.

    For example, `tile.bind('<ButtonPress>', on_dnd_start)`

    Args:
        event: The tk event that resulted in this call.
    Returns:
        The object to be dragged.  Here, it's the widget
        that was clicked to call this function.
    """
    tk.dnd.dnd_start(event.widget, event)
```


### How to write documentation for each module and function.


### What are the basic option flags to create tests.
### How to find edge cases.

Resources
------------------
### Read or watch:

1. [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html)(until “26.2.3.7. Warnings” included)
2. [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
3. [More on how to write doctests](https://www.digitalocean.com/community/tutorials/how-to-write-doctests-in-python)
4. [Interactive test - examples](https://www.tutorialspoint.com/test-interactive-python-examples-doctest)
5. [doctest - Testing through documentation here](https://pymotw.com/3/doctest/)
6. [Google Doctstring Example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
  * [More examples: Testing doctest module](https://www.geeksforgeeks.org/testing-in-python-using-doctest-module/)
  * [Test interactive example: doctest](https://docs.python.org/3/library/doctest.html)

Python Test Cases
------------------
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a *new line*
* All your test files should be inside a folder `tests`
* All your test files should be text files (extension: `.txt`)
* All your tests should be executed by using this command:

		python3 -m doctest ./tests/*


* All your **modules** should have a documentation:

		python3 -c 'print(__import__("my_module").__doc__)'


* All your **functions** should have a documentation:

		python3 -c 'print(__import__("my_module").my_function.__doc__)'


* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
