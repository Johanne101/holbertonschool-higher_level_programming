#Data Structures: Lists, Tuples

* Why Python programming is awesome
  * The python language is one of the most accessible programming languages
  available because it has simplified syntax and is not complicated,
  which gives more emphasis on natural language.
  Due to its ease of learning and usage, python codes can be easily
written and executed much faster than other programming languages.
* What are lists and how to use them
  * Lists are used to store multiple items in a single variable.
  Lists are one of 4 built-in data types in Python used to store
  collections of data,the other 3 are:
    * Tuple,
	* Set,
	* and Dictionary, all with different qualities and usage.
* What are the differences and similarities between strings and lists
  * Strings can only consist of characters,
  * while lists can contain any data type. 
  Because of the previous difference, we cannot easily make a list into a string
  but we can make a string into a list of characters,
  simply by using the `list()` function.
  * Strings are:
    * immutable, meaning that we cannot update them.
##However, strings are not interchangeable with lists because of some important differences
  * Strings can only consist of characters,
  * While lists can contain any data type.
* What are the most common methods of lists and how to use them
  * A **method** is the same as a function, except that it’s bound to an object.
  * A **list** is a collection of pieces of data.
  * A list is surrounded by square brackets [ ] with each item separated by a comma
    * ` , `
  * and can contain anywhere from zero to infinity items:
    * Strings,
	* numbers,
	* booleans,
	* even other lists can be items in a list
Lists are ordered and mutable (changeable), meaning each item is assigned
to a specific index and can be sorted, and has the ability to be altered.

###For example, to run the append() method on the list
  * `[‘pepperoni’, ‘sausage’, ‘mushroom’]`
you would just write:
  * `[‘pepperoni’, ‘sausage’, ‘mushroom’].append(‘onion’)`

Some methods accept what are known as ‘arguments,’ which go in the
parenthesis and further define what the method will do
**append()**  and **extend()**
**The append()** | method allows to add another item to the end of your list
The method takes one required argument,
which is the item you wish to add to your list.

**The extend()** | method similar to append() it allows to add onto your list

##Methods and Functions:
When we call a method, we tell what object it’s called on.
min
max
**len** | Gives us the number of items in a list.


###Below there are more examples of different methods:
Method | Description | Arguments
----------- | ------------- | -------------
**append()** | method allows you to add another item to the end of your list| 
The method takes one required argument,
which is the item you wish to add to your list.
**extend()** | it allows you to add onto your list;
however, the extend() method allows you to add all of the items from another
iterable
  * (list, tuple, set, etc.) to the end of your list as separate items instead
  of one item. | The method takes one required argument, the iterable.
**pop()** | method allows you to remove an element from your list
at a specified index value. | -.
**remove()** | method allows you to remove an item from your list.
Removes the first occurrence of a specified value in a list. | The method
takes one required argument, the item you wish to remove.


**sort()** | method sorts a list by certain criteria. | 
The method can take two optional arguments.
The first argument is setting either reverse=True or reverse=False.
**reverse()** | method reverses the order of the items in the list |
The method takes no arguments.
**count()** | method returns the number of occurrences
of a specified item in a list. This method can be useful
if you wish to find out what items appear more than once in a list. | 
The method takes one required argument,
which is the item you wish to find the count of `index()`
method returns the index of the first occurrence of the specified item.
If the item does not exist in the list, you will get an error.
insert()
method inserts a specified item into a list at a specified index. 
The method takes two required arguments — the integer index you wish to insert the value at and 
the item you’d like to insert.


copy()
method simply returns a copy of your list. 
The method takes no arguments.


clear()
method simply removes all items from a list, leaving an empty list. 
The method takes no arguments.

* How to use lists as stacks and queues
  * Stack:
    * A stack is a basic data structure that can be logically thought of as a
	linear structure represented by a real physical stack or pile, a structure
	where insertion and deletion of items takes place at one end called top of
	the stack according to the last-in first-out (LIFO) principle.
	`push` adds an item on top of the stack, `pop` removes the item from the top
  * Using Lists as Queues:
    * Queues:
	Queue is a linear data structure where the first element is inserted from
	one end called REAR and deleted from the other end called as FRONT.
	In a queue, one end is always used to insert data (enqueue) and the other
	is used to delete data (dequeue), because queue is open at both its ends.
	Queue follows First-In-First-Out methodology (FIFO)
	  * i.e., the data item stored first will be accessed first.


* What are list comprehensions and how to use them
  * List comprehensions are used for creating new lists from other iterables like:
    * tuples,
	* strings,
	* arrays,
	* lists, etc.
	A list comprehension consists of brackets containing
	the expression, which is executed for each element
	along with the for loop to iterate over each element.

* What are tuples and how to use them
Tuples are used to store multiple items in a single variable.
uple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. 
*A tuple is a collection which is ordered and unchangeable.*


* When to use tuples versus lists
Tuples are more memory efficient than the lists. When it comes to the time efficiency, again tuples have a slight advantage over the lists especially when lookup to a value is considered. If you have data which is not meant to be changed in the first place, you should choose tuple data type over lists.
The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable. This means that tuples cannot be changed while the lists can be modified.
Tuples are more memory efficient than the lists.
When it comes to the time efficiency, again tuples have a slight advantage over the lists especially when lookup to a value is considered.
If you have data which is not meant to be changed in the first place, you should choose tuple data type over lists.

* What is a sequence
Python Sequences
In Python programming, sequences are a generic term for an ordered set which means that the order in which we input the items will be the same when we access them.
Python supports six different types of sequences.
These are:
strings,
lists,
tuples,
byte sequences,
byte arrays, and 
range objects.


What is...
Description:
Sequences
A sequence is an ordered collection of items
If a sequence wasn't ordered, you couldn't refer to individual items by their index position.
*The word ordered is important*
When you iterate over a sequence
Using a for loop, for example - you’ll always get the items in the same order.
Iterables
*indexing must also start at zero.*
Is an object that contains either:
An _iter_ method
Or an _getitem_ method

All sequence types can be iterated over.
That means all sequence types - strings, lists, etc - are also iterable types.
Not all iterables are sequences

What is tuple packing
Tuple in Python
Python Tuples In python tuples are used to store immutable objects.In another way, it is called unpacking of a tuple of values into a variable.
Packing a Tuples
In packing, we put values into a new tuple
Unpacking a Tuple
While in “unpacking a tuple” we extract those values into a single variable. It is called unpacking of a tuple of values into a variable


What is sequence unpacking
Sequence unpacking in python allows you to take objects in a collection and store them in variables for later use. This is particularly useful when a function or method returns a sequence of objects
Python allows unpacking of any sequence(iterable) into variables using a simple assignment operation. Unpacking can be done by assigning sequence(iterable) to comma separated variables .



What is the del statement and how to use it
The del keyword is used to delete objects. In Python everything is an object, so the del keyword can also be used to delete objects like 
variables, 
lists, or
parts of a list etc.
The del statement works by unbinding the name, removing it from the set of names known to the Python interpreter. If this variable was the last remaining reference to an object, the object will be removed from memory. If, on the other hand, other variables still refer to this object, the object won’t be deleted.

Here, del is a Python keyword. And, obj_name can be variables, user-defined objects, lists, items within lists, dictionaries etc.

