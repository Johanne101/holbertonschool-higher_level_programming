Import & modules
================

## Learning Objectives

### General:
- Why Python programming is awesome
  * Despite it's easy use, It's also a very powerful language
  * I'ts one of the 3 "official" languages at Google as an example.

- How to import functions from another file
<p>
A function can be called and run in a different file than the file where the function is defined.

If a new file called `myfunctions.py` is created and contains two function definitions, 
  * `plustwo()` and 
  * `falldist()`

The functions `plustwo()` and `falldist()` can be used by a separate script,
as long as the file and function names are imported in the separate script first.
***It is essential that the file which contains the function definitions ends in the `.py` extension.***
Without a `.py` extension, the file where the functions are defined can not be imported

```
# myfunctions.py

def plustwo(n):
    out = n + 2
    return out


def falldist(t,g=9.81):
    d = 0.5 * g * t**2
    return d
```
This file, `myfunctions.py` can be imported into another script (another .py file)

### Steps in how to use imported functions:

To use the functions written in one file inside another file
1. include the import line
  - `from filename import function_name`

Note that although the file name must contain a `.py` extension,
*.py* is not used as part of the filename during import.

**SYNTAX:**
```
from function_file import function_name

function_name(arguments)

# Example 1:
from myfunctions import plustwo

plustwo(3)

# Example 2:
import function_file

function_file.function_name()
```

2. including multiple functions from the same file by seperating the with commas.

**SYNTAX:**
```
# Example 1
from myfunctions import falldist, plustwo

out1 = falldist(3)
out2 = plustwo(3)


print(out1, out2)
```
</p>
### Modules:
**First, what is a Module?**
<p>

Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

1. Creating a Module:

To create a module just save the code you want in a file with the file extension `.py`:
**Example:**
```
# Save this code in a file named my-first_module.py

def greeting(name):
  print("Hello, " + name)
```

2. Use the Module:

Now we can use the module we just created, by using the import statement:

```
import mymodule

mymodule.greeting("Alex")
```
</p>

### Built-in Functions:

- How to use the built-in function `dir()`?

`dir()` is a powerful inbuilt function in Python3,
which returns a list of the attributes and methods of any object
(say functions , modules, strings, lists, dictionaries etc.)

**Syntax:**
```
dir({object})
```

**Parameters:**
```
object [optional] : Takes object name
```

**Returns:**

`dir()` tries to return a valid list of attributes of the object it is called upon.
Also, dir() function behaves rather differently with different type of objects,
as it aims to produce the most relevant one, rather than the complete information.

  * For **Class Objects**, it returns a list of names of all the valid attributes and base attributes as well.
  * For **Modules/Library** objects, it tries to return a list of names of all the attributes contained in that module. 
  * If no parameters are passed it returns a list of names in the current local scope

- How to prevent code in your script from being executed when imported
<p>
To stop code execution in Python you first need to import the sys object.
After this you can then call the exit() method to stop the program running.
It is the most reliable, cross-platform way of stopping code execution.
**SYNTAX EXAMPLE:**
```
import sys
sys.exit()

```
</p>

#### Command Line Arguments:
<p>
- How to use command line arguments with your Python programs
Python provides a getopt module that helps you parse command-line options and arguments.

```$ python test.py arg1 arg2 arg3```

The Python sys module provides access to any command-line arguments via the `sys.argv`.
This serves two purposes:

  * sys.argv is the list of command-line arguments.
  * len(sys.argv) is the number of command-line arguments.

Here is `sys.argv[0]` is the program as an example:
```
#!/usr/bin/python

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

```
</p>

Requirements
-------------
### General:
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.\*)
* All your files must be executable
* The length of your files will be tested using `wc`

Resources
-----------
#### Read or watch:

- [Modules](https://docs.python.org/3/tutorial/modules.html#modules)
- [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
- [Pycodestyle](https://pypi.org/project/pycodestyle/): Style Guide for Python Code
- [Imports](https://problemsolvingwithpython.com/07-Functions-and-Modules/07.05-Calling-Functions-from-Other-Files/)
- [Command Line Arguments](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)

**man or help:**
- `python3`

