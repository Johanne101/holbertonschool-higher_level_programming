Object Oriented Programming (**OOP**)
=======================================

### Why Python programming is awesome

So there's several different programming paradigms and unitl now
When we say everything in Python is an object...
I seriously mean it!

>> EVERYTHING IN PYTHON ARE OBJECTS!!!!

**Everything...** Even types are implemented as clases.

### What is OOP?

<p>

**Object Oriented Programming** uses classes and methods to provide objects
that encapsulates both data and the functions that operate on that Data.
*Method* is just another word for function.

When a function is part of a class in Python we call it a method.
Now, there is a slight difference between a function and a method
but writing a method is the same as writing a function.
**Example #1:**
</p>

```
# Here Kettle has been defined as a class
class Kettle(object):
	def __init__(self, make, price):
		self.make = make
		self.price = price
		self.on = False
```
<p>

Looking at the code above, you can think of a class as a template from which
objects can be created.
So when we create objects of this kettle class, they all have a name and a price.

  >>>*Now they wont have the same name nor the same price*<<<

Each instance of the class will have it's own values for name and price.
So as it was mentioned before, classes is like a template from which objects can be
created and all the objects created from the same class will share the same characteristics.

Now an **instance** is just another name for an object created from a class definition.
- So *if we create a kettle called* **Kenwood**;
  * Then Kenwood will be an **instance** of the kettle class.
- You can also say that **Kenwood**
  * is an object of type kettle.
**Example #2.a:**
</p>

```
# Example of creating an instance of the kettle class
# And I gave it the name 'Kenwood'
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)


# we can adjust the price can be $12.75
kenwood.price = 12.75
print(kenwood.price)
```


**Example #2.b: Another instance is created in the code below and this time it's called Hamilton**

```
hamilton = ("Hamilton", 14.55)
```

<p>
* Each *instance* has its own values for name and price.
* And their accessed byt using `.` annotations
  * So we type in;
    * `Kenwood.price` or
	* `Hamilton.make`
	to access that information.

</p>

### “first-class everything”
### What is a class

<p>
A good analogy here is plans for building a house...
The plan itself just describes what the house will look like.
It's size, how many rooms it will have, etc. This is similar the *plan* to the *class*.
Which is just a template for creating objects.

* Once you have a plan, you can then create as many houses as you want based on that plan.
* And the same is true of classes once a class has been defined...

>> "like how kettle class that we defined on example #1 above"

* We can then create as many instances of that classes as we want

**Be AWARE...**
Just as you can't do anything with the house plan other than build houses based on it.
You can't relly do anything with the class, other than create instances of it.
Once the instances have been created you can then call their methods, and access their variables.
</p>

**Input:**
```
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
```

**Output**
```
Kenwood
8.99
12.75
Models: Kenwood = 12.75, Hamilton = 14.55
```
so the code above has retrieved the values out of each instance of the 2 kettle objects
that we have created.
The parameters in the format method above are the make, and price **data attributes** of the;
  * Kenwood, and
  * Hamilton objects.

> Before we have been used to talking about variables, but...
> when a variable is bound to an instance of a class it's refered to as a
>> **data attribute**

## Learn your OOP Terms:

|Term        |What is it? |
|:-----------|-----------:|
|Class       |template for creating objects. All objects created using the same class will have the same characteristics. |
|Object      |an instance of a class. |
|Instantiate |create an instance of a class. |
|Method      |a function defined in a class. |
|Attribute   |a variable bound to an instance of a class. |


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
- [Encapsulation](https://www.geeksforgeeks.org/encapsulation-in-python/)
- [Creat an empty Class](https://www.foxinfotech.in/2018/09/how-to-create-empty-class-in-python.html#:~:text=In%20Python%2C%20you%20can%20create,it%20does%20nothing%20when%20executes.)
- [Define a class](http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html)
- 
