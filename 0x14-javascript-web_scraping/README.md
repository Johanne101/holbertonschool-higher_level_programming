JavaScript - Web scraping
===

More Info: **Getting Started for this project**

Install Node 10
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
```

Install `axios` module and use it
[Documentation](https://github.com/axios/axios)
```
$ sudo npm install axios --global
$ export NODE_PATH=/usr/lib/node_modules
```

# Resources
***Read or watch:***
* **Javascript:**
  * [Program to read text File](https://www.geeksforgeeks.org/javascript-program-to-read-text-file/)
  * [Program to write data in a text File](https://www.geeksforgeeks.org/javascript-program-to-write-data-in-a-text-file/)
* Working with JSON data
* The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco
* axios module
* Modern JS

General Objectives
---
- Why JavaScript programming is amazing
  0. Javascript: Program to read text File
- How to manipulate JSON data
- How to use `axios` and fetch API
- How to read and write a file using `fs` module


0. How to write a script that reads and prints the content of a file.
  + [Node.js fs.readFile() Method](https://www.geeksforgeeks.org/node-js-fs-readfile-method/)
  + [Node.js File System Module](https://www.w3schools.com/nodejs/nodejs_filesystem.asp)
  + [Web scraping with JavaScript and Node.js](https://towardsdev.com/web-scraping-with-javascript-and-node-js-2d024d665390)
<p>
**Used Function:** The `readFile()` functions is used for reading operation.

**Syntax:**
```
readFile( Path, Options, Callback)
```
**Parameters:** This method accepts three parameters as mentioned above and described below:

  * **path:** It takes in relative path from the program to the text File. If both file and program is in the same folder, the simply give the file name of the text file.
  * **Options:** It is an optional parameter which specify the data is to be read from the file. If nothing is passed, then default raw buffer is returned.
  * **Callback Function:** It is the callback function which has further two arguments (err, data). If the operation fails to extract the data, err shows what is the fault, else data argument will contain the data from the file.
</p>

1. How to write a script that writes a string to a file.
  + [Program to write data in a text File](https://www.geeksforgeeks.org/javascript-program-to-write-data-in-a-text-file/)
