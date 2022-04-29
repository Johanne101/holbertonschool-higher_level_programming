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
The simplest way to use `urllib.request` is as follows:

```python3
import urllib.request
with urllib.request.urlopen(req) as response:
   the_page = response.read()
```

HTTP is based on requests and responses
  - the client makes requests and servers send responses.
urllib.request mirrors this with a Request object which represents the HTTP request you are making.
</p>

## How to decode `urllib` body response

```python3
#!/usr/bin/python3
""" Fetch's internet resources w/ the Python package urllib """
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
   html = response.read()
   print('Body response:')
```

### Response Headers


## How to use the Python package `requests`
| How to make HTTP| Requests |
|`GET` | ... |
|`POST`/`PUT`/etc | ...|



<p>

Now, to make HTTP requests in python, we can use several HTTP libraries like:

httplib
urllib
requests

### Higher-level interface

```python3
urllib.urlopen(url[, data[, proxies[, context]]])
```

</p>

<p>
Now, we have a Response object called r. We can get all the information we need from this object.

Requests’ simple API means that all forms of HTTP request are as obvious. For example, this is how you make an HTTP POST request:
```
>>> r = requests.post('https://httpbin.org/post', data = {'key':'value'})
```
Nice, right? What about the other HTTP request types: **PUT, DELETE, HEAD and OPTIONS**? These are all just as simple:

```
>>> r = requests.put('https://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('https://httpbin.org/delete')
>>> r = requests.head('https://httpbin.org/get')
>>> r = requests.options('https://httpbin.org/get')
```
</p>

## How to fetch JSON resources
## How to manipulate data from an external service
## Requesting GitHub credentials (username and password) Using GitHub API
<p>
* You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
* The first argument will be your username
* The second argument will be your password (in your case, a personal access token as password)
* You must use the package requests and sys
</p>

# Resources
***Read or watch:***

* [Quickstart with Requests package: PYTHON3](https://docs.python.org/3/howto/urllib2.html)
  * [Error Codes](https://docs.python.org/3/howto/urllib2.html#error-codes)
* [Requests package]()
* [Higher-level interface: `urllib`](https://docs.python.org/2/library/urllib.html#high-level-interface)
* [`get` python](https://docs.python.org/3.4/library/stdtypes.html#dict.get)
* [Get & Post requests: Geek for geeks](https://www.geeksforgeeks.org/get-post-requests-using-python/)
* **URLLIB**;
  * [`urllib.error.HTTPError`: examples](https://www.programcreek.com/python/example/68438/urllib.error.HTTPError)

* [Learning Objectives](https://fs.blog/feynman-learning-technique/)
* [Basic Authentication](https://docs.github.com/en/rest/overview/other-authentication-methods)
  * [personal access token as password](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
  * [GitHub API: Taking GitHub Credentials](https://docs.github.com/en/rest/users)
