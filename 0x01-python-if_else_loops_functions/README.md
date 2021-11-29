## if/else, loops, functions
Control Flow
=============

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

* web development (server-side),
* software development,
* mathematics,
* system scripting.

## 0. Why indentation is so important in Python

The indentation level of your statements is significant
the exact amount of indentation doesn't matter at all, but only the relative indentation of nested blocks (relative to each other).

>>but it has to be at least one number of spaces.

without proper indenting the Python code, you will end up seeing IndentationError and the code will not get compiled.

Furthermore, the indentation level is ignored when you use explicit or implicit continuation lines. For example, you can split a list across multiple lines, and the indentation is completely insignificant. So, if you want, you can do things like this:

```
 foo = [
    'some string',
... 'another string',
... 'short string'
]
print(foo)

['some string', 'another string', 'short string']
```

* [Indentation Style](https://www.w3schools.com/python/gloss_python_indentation.asp):

you can write the inner block all on one line if you like, therefore not having to care about intendation at all.

***Input***:

```
if 5 > 2:
  print("Five is greater than two!")

if 1 + 1 == 2:
    print("foo")
    print("bar")
    x = 42

if 1 + 1 == 2:
    print("foo"); print("bar"); x = 42

if 1 + 1 == 2: print("foo"); print("bar"); x = 42
```

***Output:***
```
Five is greater than two!
foo
bar
foo
bar
foo
bar
```
***Input:***

```
if 5 > 2:
 print("Five is greater than two!")  
if 5 > 2:
        print("Five is greater than two!")
```

***Output:***

```
Five is greater than two!
Five is greater than two!
```
<p>
Sometimes you have a bunch of similar "if" statements which can be conveniently written on one line each.

If you decide to write the block on separate lines, then yes, Python forces you to obey its indentation rules, which simply means: The enclosed block (that's two "print" statements and one assignment in the above example) have to be indented more than the "if" statement itself. 
</p>
## 1. How to use the if, if ... else statements

## 2. How to use comments
<p>
Comments can be used to explain Python code, make the code more readable, or used to prevent execution when testing code.
</p>

***Example: Input***

```
#print("Hello, World! 1")
print("Cheers, Mate!")

print("1: Hello, World!") #This is a comment

#This is a comment
#written in
#more than just one line
print("2: Hello, World!")

"""
This is a comment
written in
more than just one line
"""
print("3: Hello, World!")
```

*Output*

```
Cheers, Mate!
1: Hello, World!
2: Hello, World!
3: Hello, World!
```

## 3. How to affect values to variables
Python has no command for declaring a variable. A variable is created the moment you first assign a value to it. Example.

```
x = 5 y = "John" print(x) print(y)
```

Variables are containers for storing data values.

#### [Assining Multiple Values](https://www.w3schools.com/python/python_variables_multiple.asp)


* How to use the while and for loops
* How is Python’s for different from C‘s?
* How to use the break and continues statements
* How to use else clauses on loops
* What does the pass statement do, and when to use it
* How to use range
* What is a function and how do you use functions
* What does return a function that does not use any return statement
* Scope of variables
* What’s a traceback
* What are the arithmetic operators and how to use them

Resources
=========

*Read or watch:*

- [Python Introduction](https://www.w3schools.com/python/python_intro.asp): (*What is Python, what can it do, why use python, syntax*)
  * [python syntax](https://www.w3schools.com/python/python_syntax.asp): (indentation, variables, comments)
    * [comments](https://www.w3schools.com/python/python_comments.asp)
    * [variables](https://www.w3schools.com/python/python_variables.asp): (creating, casting, get the type)
	* 
- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools): (Read until “4.6. Defining Functions” included)
- [Myths about Indentation](https://web.archive.org/web/20180218162410/http://www.secnetix.de/~olli/Python/block_indentation.hawk): (check the "waybackmachine")
IndentationError
How To Use String Formatters in Python 3
Learn to Program
Learn to Program 2 : Looping
