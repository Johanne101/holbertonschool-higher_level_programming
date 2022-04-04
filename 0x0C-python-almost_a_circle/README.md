Background Context
=======================

The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

**In this project, you will review everything about Python:**


|Concept                  | Descriptions                   |
|-------------------------|--------------------------------|
|Import |                                                  |
|Exceptions |                                              |
|Class |                                                   |
|Private attribute |                                       |
|Getter/Setter |                                           |
|Class method |                                            |
|Static method |                                           |
|Inheritance |                                             |
|Unittest |                                                |
|Read/Write file |                                         |
|You will also learn about: | `args` and `kwargs`, Serialization/Deserialization, JSON|

<p>
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class.
With a setter, you are able to validate what a developer is trying to assign to a variable.
So after, in your class you can “trust” these attributes.
</p>


General
------------
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is \*args and how to use it
* What is \*\*kwargs and how to use it
* How to handle named arguments in a function

**Index:**
----------

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is \*args and how to use it
* What is \*\*kwargs and how to use it
* How to handle named arguments in a function


***Python Unit Tests: guideline***
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line.
* All your test files should be inside a folder `tests`
* You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* All your test files should be python files (extension: `.py`)
* All your test files and folders should start with `test_`
* Your file organization in the tests folder should be the same as your project: ex: for `models/base.py`, unit tests must be in: `tests/test_models/test_base.py`
* All your tests should be executed by using this command: `python3 -m unittest discover tests`
* You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py`
* We strongly encourage you to work together wit other on test cases so that you don’t miss any edge case
