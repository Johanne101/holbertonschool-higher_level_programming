JavaScript - Web jQuery
=========================

**General Overview:**

## Why JQuery make front-end programming so easy
## How to select HTML elements in JavaScript

#### Text Color
<p>
To change the text color of a given element,
first we need to access it inside the JavaScript
by using the `document.getElementId()` or `document.querySelector()`
methods and set its `style.color` property to your desired color.

Here is an example, that changes the text color to ``orange``:
</p>

```
const div = document.getElementById("container");

div.style.color = "orange";
```
## How to select HTML elements with JQuery
## What are differences between ID, class and tag name selectors
## How to modify an HTML element style
## How to get and update an HTML element content
## How to modify the DOM
## How to make a GET request with JQuery Ajax
## How to make a POST request with JQuery Ajax
## How to listen/bind to DOM events
## How to listen/bind to user events

----------------------
## More Info
### Import JQuery

```.js
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```
or query selector methods like:

```.js
document.querySelector("p"); # Get the first <p> element

document.querySelector(".example"); # Get the first element with class="example"
```

Resources
===========
**Read or watch:**

* [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
* [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
  - [Changing the text color](https://reactgo.com/change-text-color-javascript/#changing-the-text-color)
  - [JavaScript: jQuery selector()](https://www.w3schools.com/jsref/met_document_queryselector.asp)
* [Get and set content](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
* [Manipulate CSS classes](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
* [Manipulate DOM elements](https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)
* [API: jQuery](https://oscarotero.com/jquery/)
* [Introduction](https://jquery-tutorial.net/ajax/introduction/)
* [GET & POST request](https://jquery-tutorial.net/ajax/the-get-and-post-methods/)
* [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://www.youtube.com/watch?v=fEYx8dQr_cQ) *"YouTube"*
* [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
* [JQuery](https://jquery.com/)
* [JQuery API](https://api.jquery.com/)
* [JQuery Ajax](https://learn.jquery.com/ajax/)

