Object Oriented Programming (**OOP**)
=======================================

### Why Python programming is awesome

So there's several different programming paradigms and unitl now
When we say everything in Python is an object...

> I seriously mean it!
>> EVERYTHING IN PYTHON ARE OBJECTS!!!!

**Everything.** Even types are implemented as clases.

### What is OOP

<p>

**Object Oriented Programming** uses classes and methods to provide objects
that encapsulates both data and the functions that operate on that Data.
*Method* is just another word for function.

When a function is part of a class in Python we call it a method.
Now, there is a slight difference between a function and a method
but writing a method is the same as writing a function.
**Example:**
</p>

```
class Kettle(object):
	def __init__(self, make, price):
		self.make = make
		self.price = price
		self.on = False
```
<p>

Looking at the code above, you can think of a class as a template from which
objects can be created. So when we create objects of this kettle class, they all
have a name and a price.
  >>>*Now they wont have the same name nor the same price*<<<
Each instance of the class will have it's own values for name and price.
So as it was mentioned before, classes is like a template from which objects can be
created and all the objects created from the same class will share the same characteristics.

Now an **instance** is just another name for an object created from a class definition.

</p>

### “first-class everything”
### What is a class
### What is an object and an instance
### What is the difference between a class and an object or instance
### What is an attribute
### What are and how to use public, protected and private attributes
### What is self
### What is a method
### What is the special `__init__` method and how to use it
### What is Data Abstraction, Data Encapsulation, and Information Hiding
### What is a property
### What is the difference between an attribute and a property in Python
### What is the Pythonic way to write getters and setters in Python
### What are the special `__str__` and `__repr__` methods and how to use them
### What is the difference between `__str__` and `__repr__`
### What is a class attribute
### What is the difference between a object attribute and a class attribute
### What is a class method
### What is a static method
### How to dynamically create arbitrary new attributes for existing instances of a class
### How to bind attributes to object and classes
### What is and what does contain `__dict__` of a class and of an instance of a class
### How does Python find the attributes of an object or class
### How to use the getattr function

Resources
-------------
- [Encapsulation](https://www.geeksforgeeks.org/encapsulation-in-python/ )
