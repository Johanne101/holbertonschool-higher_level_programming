Requirements
---

*  All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
*  All your files should end with a new line
*  The first line of all your files should be exactly `#!/usr/bin/python3`
*  Your code should use the PEP 8 style (version 1.7)
*  All files must be executable
*  The length of your files will be tested using wc
*  All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*  Must use [`get`](https://docs.python.org/3.4/library/stdtypes.html#dict.get) to access to dictionary value by key
*  This code should not be executed when imported (`by using if __name__ == "__main__":`)

---

# General Objectives

## Python package `urllib`
<p>
**How to fetch** internet resources with the Python package `urllib`
The simplest way to use urllib.request is as follows:

```python3
import urllib.request
with urllib.request.urlopen(req) as response:
   the_page = response.read()
```

HTTP is based on requests and responses
  - the client makes requests and servers send responses.
urllib.request mirrors this with a Request object which represents the HTTP request you are making.
</p>

## |How to decode| `urllib` body response
## |How to use| the Python package `requests`
## |How to make| HTTP `GET` request
## |How to make| HTTP `POST`/`PUT`/etc. request
## |How to fetch| JSON resources
## |How to manipulate| data from an external service

# Resources
***Read or watch:***

* [Quickstart with Requests package: PYTHON3](https://docs.python.org/3/howto/urllib2.html)
  * [Error Codes](https://docs.python.org/3/howto/urllib2.html#error-codes)
* [Requests package]()
* [`get` python](https://docs.python.org/3.4/library/stdtypes.html#dict.get)
* [Learning Objectives](https://fs.blog/feynman-learning-technique/)

