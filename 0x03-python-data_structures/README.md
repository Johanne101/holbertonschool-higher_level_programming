# Data Structures: Lists, Tuples

|**Why Python programming is awesome?!?!**|
|:---------------------------------------:|
| <p> The python language is one of the most accessible programming languages available because it has simplified syntax and is not complicated, which gives more emphasis on natural language. Due to its ease of learning and usage, python codes can be easily written and executed much faster than other programming languages.</p>|
|![altext](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.yjwQfbn9z1-5dSF7mdZvRgAAAA%26pid%3DApi&f=1)|

### 0. What are lists and how to use them
  * Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store
collections of data,the other 3 are:
    * Tuple,
	* Set,
	* and Dictionary

### 1. What are the differences and similarities between strings and lists?

* Strings can only consist of characters,

[String format() Method](https://www.w3schools.com/python/ref_string_format.asp)
#### The Placeholders

The placeholders can be identified using;
  * named indexes {price},
  * numbered indexes {0}, or even
  * empty placeholders {}
    * [Formating Types]()

* while lists can contain any data type.

Because of the previous difference, we cannot easily make a list into a string
but we can make a string into a list of characters,
simply by using the `list()` function.
  * Strings are:
    * immutable, meaning that we cannot update them.

#### However, strings are not interchangeable with lists because of some important differences

 * A **method** is the same as a function, except that it’s bound to an object.
 * A **list** is a collection of pieces of data.
 * A list is surrounded by square brackets `[ ]` with each item separated by a comma ` , ` E.g.:

***input:***

```
myroom = ["bed", "desk", "closet", "bathroom", "computer"]
print(myroom)
```

***output:***

```
['bed', 'desk', 'closet', 'bathroom', 'computer']
```

  * and can contain anywhere from zero to infinity items of:
    * Strings,
	* numbers,
	* booleans,
	* even other lists can be items in a list


|[List Methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)|
|----------------------|

#### 2. Most common methods of lists

Here are the most common methods of lists and how to use them:

|Method | Description | Arguments|Syntax|
|------ | ----------- | ---------|------|
|**.append()** | method allows you to **add another item to the end of your list**|The method takes one required argument, which is the item you wish to add to your list.|
|**.extend()** |adds the specified list elements (or any iterable) to the end of the current list.| The method takes one required argument, the iterable.|
|**.pop()** | method allows you to **remove an element from your list at a specified index value.** | -.|
|**.remove()** | method allows you to **remove an item from your list.** Removes **the first occurrence** **of** a **specified value in a list.**| The method takes one required argument, the item you wish to remove.|
|**.sort()** | method **sorts a list by certain criteria.** |can take two optional arguments. The first argument is setting either reverse=True or reverse=False.|
|**.reverse()** | method **reverses the order of the items in the list** |The method takes no arguments.|
|**.count()** | method **returns the number of occurrences** **of** a specified **item(s) in a list**. This method can be useful if you wish to find out what items appear more than once in a list. |<p>The method takes one required argument, which is the item you wish to find the count of.</p>|
|**.insert()**|method **inserts a specified item into a list** **at a specified index**.|The method takes two required arguments — the integer index you wish to insert the value at and the item you’d like to insert.|
|**.copy()**|method simply **returns a copy of your list**.| The method takes no arguments.|
|**.clear()**|method simply **removes all items from a list**, *leaving an empty list*. |The method takes no arguments.|
|**.index()**|**returns the index/position of** the first element with the **specified value**||````(x[, start[, end]])````|



Lists are ordered and mutable (changeable), meaning each item is assigned
to a specific index and can be sorted, and has the ability to be altered.

>>The `extend()` method allows you to **add onto your list** like `append()`...
>>however, `extend()` allows you to add all of the items from another iterable
* (list, tuple, set, etc.) >>to the end of your list as separate items instead of one item.


### 3. How to use lists as stacks and queues

* Stack:
    
	* A stack is a basic data structure that can be logically thought of as a
	linear structure represented by a real physical stack or pile, a structure
	where insertion and deletion of items takes place at one end called top of
	the stack according to the last-in first-out (LIFO) principle.
	
	`push` adds an item on top of the stack,
	`pop` removes the item from the top

* Using Lists as Queues:
    * Queues:
	Queue is a linear data structure where the first element is inserted from
	one end called REAR and deleted from the other end called as FRONT.
	In a queue, one end is always used to insert data (enqueue) and the other
	is used to delete data (dequeue), because queue is open at both its ends.
	Queue follows First-In-First-Out methodology (FIFO)
	  * i.e., the data item stored first will be accessed first.


### 4. What are list comprehensions and how to use them
* List comprehensions are used for creating new lists from other iterables like:
    * tuples,
	* strings,
	* arrays,
	* lists, etc.

A list comprehension consists of brackets containing
the expression, which is executed for each element
along with the for loop to iterate over each element.

[List conprehension](https://docs.python.org/3/glossary.html#term-iterable): ***Iterables***

### 5. What are tuples and how to use them

Tuples are used to store multiple items in a single variable.

>> *A tuple is a collection which is ordered and unchangeable.*

### 6. Tuples vs. Lists

**When to use tuples versus lists?**

Tuples are more memory efficient than the lists.

When it comes to the time efficiency, again tuples have a slight advantage over the lists especially when lookup to a value is considered.

>If you have data which is not meant to be changed in the first place,
>>you should choose tuple data type over lists.

The key difference between the tuples and lists is that while the tuples are immutable objects
the lists are mutable.

This means that tuples cannot be changed
*while the lists can be modified.*

|Data types|Description|Ordered or Unordered|Changeable or Unchangeable|Duplicates|syntax|
|:---------|-----------|:-------------------|--------------------------|:--------:|----------------------------|
|**List**|<p>Lists are used to store multiple items in a single variable. </p>|<p>**Ordered**: means the items have a defined order, and that order will not change. If you add new items to a list, the new items will be placed at the end of the list. </p>|**Changeable:** we can change, add, and remove items in a list after it has been created. |**Allows Duplicates:** Since lists are indexed, lists can have items with the same value|````thislist = ["item 1", "item 2", "item 3"]```` ````print(thislist)````|
|**Tuple**|<p>Tuples are used to store multiple items in a single variable.</p>|**Ordered**: It has a defined order and cannot be changed|**Unchangeable**|**Allows Duplicates**|````thistuple = ("apple", "banana", "cherry")```` ````print(thistuple)````|


### 7. What is a sequence

***Description:***

* [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
A sequence is an ordered collection of items

Sequences are a generic term for an ordered set which means that the order in which we input the items will be the same when we access them.

If a sequence wasn't ordered, you couldn't refer to individual items by their index position.
*The word ordered is important*

Python supports six different types of sequences;

* strings,
* lists,
* tuples,
* byte sequences,
* byte arrays and,
* range objects.

When you iterate over a sequence using a for loop, for example -


you’ll always get the items in the same order.

* Iterables
*indexing must also start at zero.*

Is an object that contains either:
  * An _iter_ method
  * Or an _getitem_ method

All sequence types can be iterated over.
That means all sequence types - strings, lists, etc - are also iterable types.

*Not all iterables are sequences*

### 8. What is tuple packing

Tuples: are used to store immutable objects.
In another way, it is called unpacking of a tuple of values into a variable.

**“packing a tuple”**, we put values into a new tuple

Unpacking a Tuple
While in **“unpacking a tuple”** we extract those values into a single variable. It is called unpacking of a tuple of values into a variable


### 9. What is sequence unpacking

Sequence unpacking in python allows you to take objects in a collection and store them in variables for later use. This is particularly useful when a function or method returns a sequence of objects
Python allows unpacking of any sequence(iterable) into variables using a simple assignment operation. Unpacking can be done by assigning sequence(iterable) to comma separated variables .

**Unpack a Collection**

If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.

Example
Unpack a list:

```
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```
```
apple
banana
cherry
```

### 10. What is the `del` statement and how to use it

The `del` keyword is used to delete objects. and since everything in Python is an object...

The `del` keyword can also be used to delete objects like;

* variables,
* lists, or
* parts of a list etc.

The del statement works by unbinding the name, removing it from the set of names known to the Python interpreter. If this variable was the last remaining reference to an object, the object will be removed from memory. If, on the other hand, other variables still refer to this object, the object won’t be deleted.

Here, `del` is a Python keyword, and, obj_name can be;

* variables,
* user-defined objects,
* lists,
* items within lists,
* dictionaries etc.


Resources
===========

**Read or watch:**

* Lists
  1. built-in methods: [List Methods](https://www.w3schools.com/python/python_lists_methods.asp)
    * [.index()](https://www.w3schools.com/python/ref_list_index.asp)
