JavaScript - Warm up
====================

Before getting started make sure you have the following installed...

## Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

## Install semi-standard
[Documentation](https://github.com/standard/semistandard)

```
$ sudo npm install semistandard --global
```

***Learning Objectives:***
1. Why JavaScript programming is amazing
2. How to run a JavaScript script
3. How to create variables and constants
4. What are differences between `var`, `const` and `let`
5. What are all the data types available in JavaScript
6. How to use the if, if ... else statements
7. How to use comments
8. How to affect values to variables
9. How to use while and for loops
10. How to use break and continue statements
11. What is a function and how do you use functions
12. What does a function that does not use any return statement return
13. Scope of variables
14. What are the arithmetic operators and how to use them
15. How to manipulate dictionary
16. How to import a file

* How to process.argv, reference [here](https://nodejs.org/api/process.html#process_process_argv)
<p>
The `process.argv` property returns an array containing the command-line arguments passed when the Node.js process was launched.

</p>

* What is scope and how to use it?


JavaScript basics
------------------
<p>
JavaScript is a programming language that adds interactivity to your website. This happens in games, in the behavior of responses when buttons are pressed or with data entry on forms; with dynamic styling; with animation, etc.
</p>

|Javascrip Data Types|
|:------------------:|
|`String`|
|`Array`|

> # Tips:
> Everything is `Object` and `Object` type in Javascript is powerful.

4. What are and what are the differences bettween `let`, `const`, & `var`?
------------------------------------------------------------------------------

|1 `let` |2 `const` |3 `var` |
|It’s the keyword to define a variable in the local scope|It’s the keyword to define a variable in the local scope|The scope of a var variable is functional scope.|
|It’s the keyword to define a variable with optionally initializing it to a value|It’s the keyword to define a constant variable|It can be updated and re-declared into the scope.|
|It’s the keyword to define a variable that can be re-assign during the execution|A user cannot update the const variable once it is declared.|It can be declared without initialization.|
|It cannot be accessed without initialization, as it returns an error.|It cannot be accessed without initialization, as it cannot be declared without initialization.| It can be accessed without initialization as its default value is “undefined”. |


|Can it be declared without ***initializing***???| `var` | `let` | `const` |
|:----------------|:----:|:----:|:----:|
|Yes or No(x)|- [YES] | - [x] | - [x] |

10. JS [Comments](https://www.w3schools.com/js/js_comments.asp)
-------------------------------------------------------

<p>
</p>

11. What are and How to use functions
-------------------------------------

|***Functions***| What it is? |
|:--------------|-------------|
|console.log()| is used to print any kind of variables defined before in it or to just print any message that needs to be displayed to the user.|

![picture alt](https://snook.ca/files/prototype_1.5.0_snookca.png)

12. What makes a function not return any statement
--------------------------------------------------

13. Scope Variables
-----------------

14. Aritmetic Operators
----------------------

15. Manipulating dictionaries
----------------------------

16. How to import a file?
----------------------------

Resources
===========
***Read or watch:***

* [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
* [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
  - [`Var`, `Let`, & `Const` - What are the differences?](https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/)
* [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics#operators)
* [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
* [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
* [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
  - [process.argv](https://nodejs.org/api/process.html#processargv)
* [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
  - [Object Basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
  - [Object-oriented](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS)
  - [Object Prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
* Intrinsic Objects
* [Module patterns](https://darrenderidder.github.io/talks/ModulePatterns/#/)
* [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
* [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)
* [Simple Intro to NodeJS Module Scope](https://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)
* [JavaScript Cheat Sheet](https://cheatography.com/davechild/cheat-sheets/javascript/)

RULES!!!
===========

|**GENERAL**|
|-----------|
|Allowed editors: `vi`, `vim`, `emacs`|
|All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)|
|All your files should end with a new line|
|The first line of all your files should be exactly `#!/usr/bin/node` |
|A `README.md` file, at the root of the folder of the project, is mandatory|
|Your code should be `semistandard` compliant (version 16.x.x). `Rules of Standard` **+** `semicolons on top`. Also as reference: [AirBnB style](https://github.com/airbnb/javascript)|
|All your files must be executable|
|The length of your files will be tested using `wc`|

