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

```.js
const div = document.getElementById("container");

div.style.color = "orange";
```

or query selector methods like:

```.js
document.querySelector("p"); // Get the first <p> element

document.querySelector(".example"); // Get the first element with class="example"
```

## How to select HTML elements with JQuery

#### Definition and Usage
<p>
The `css()` method sets or returns one or more style properties for
the selected elements.
</p>

**When used to return properties:**
<p>
This method returns the specified CSS property value of the FIRST matched element. However, shorthand CSS properties (like "background" and "border") are not fully supported and may give different results in different browsers.
</p>

**When used to set properties:**
<p>
This method sets the specified CSS property for ALL matched elements.
</p>

#### Using elements, ID's and classes

**Using a jQuery Selector for HTML using jQuery**:
<p>
A selector of jQuery starts from the dollar($) sign with a parenthesis – `$()` after it. Below are the various selectors you can use to select and manipulate an HTML element.
</p>

**The #id selector**
<p>
A very common selector type is the ID based. It uses the ID attribute of a HTML tag to locate the desired element. An ID should be unique, so you should only use this selector when you wish to locate a single, unique element. To locate an element with a specific ID, write a hash character, followed by the ID of the element you wish to locate.
</p>

##### Syntax
Return the CSS property value:

```.js
$(selector).css(property)

$(selector).css(property,value) // Set the CSS property and value

$(selector).css(property,function(index,currentvalue)) // Set CSS property and value using a function

$(selector).css({property:value, property:value, ...}) // Set multiple properties and values
```

## What are differences between ID, class and tag name selectors
## How to modify an HTML element style
### Event Handling

<p>
Show the #banner-message element that is hidden with display:none in its CSS when any button in #button-container is clicked.

```.js
var hiddenBox = $( "#banner-message" );
$( "#button-container button" ).on( "click", function( event ) {
  hiddenBox.show();
});
```
</p>

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

Resources
===========
**Read or watch:**

* [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
* [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
  - [Changing the text color](https://reactgo.com/change-text-color-javascript/#changing-the-text-color)
  - [JavaScript: jQuery selector()](https://www.w3schools.com/jsref/met_document_queryselector.asp)
  - [ Using jQuery HTML/CSS Methods](https://www.w3schools.com/jquery/jquery_ref_html.asp)
  - [jQuery css() method](https://www.w3schools.com/jquery/css_css.asp)
  - [Methods](https://api.jquery.com/click/#click-handler)
  -[JQuery | Change the text of a span element](https://www.geeksforgeeks.org/jquery-change-the-text-of-a-span-element/)
  - [How to use jQuery selector](https://tutorialdeep.com/jquery/jquery-selector/)
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
* **Installs**:
  * [jQuery npm Install and more](https://jquery.com/download/)
  * [jQuery Downloads](https://jquery.com/download/)
  * [jQuery-migrations Plugin](https://api.jquery.com/category/ajax/)
  * [jQuery: Ajax](https://api.jquery.com/category/ajax/)
