# Python Hiccup

Python Hiccup is a library for representing HTML using plain Python data structures.

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/DavidVujic/python-hiccup/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/DavidVujic/python-hiccup/tree/main)

[![CodeScene Average Code Health](https://codescene.io/projects/59968/status-badges/average-code-health)](https://codescene.io/projects/59968)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DavidVujic_python-hiccup&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=DavidVujic_python-hiccup)

[![Download Stats](https://img.shields.io/pypi/dm/python-hiccup?label=Downloads)](https://pypistats.org/packages/python-hiccup)

## What is Python Hiccup?
This is a Python implementation of the Hiccup syntax. Python Hiccup is a library for representing HTML in Python.
Using `list` or `tuple` to represent HTML elements, and `dict` to represent the element attributes.

_This project started out as a fun coding challenge, and now evolving into something useful for Python Dev teams._

## Usage
Create server side HTML using plain Python data structures.
You can also use it with __PyScript__.

## Example

Python:
``` python
from python_hiccup.html import render

render(["div", "Hello world!"])
```

The output will be a string: `<div>Hello world!</div>`


With Hiccup, you can create HTML in a programmatic style.
To render HTML like:
``` html
<ul>
    <li>one</li>
    <li>two</li>
    <li>three</li>
</ul>
```

with Python:
``` python
def todo(data: list) -> list:
    return [["li", i] for i in data]

data = todo(["one", "two", "three"])

render(["ul", data])
```

## Basic syntax

Python:
``` python
["div", "Hello world!"]
```

The HTML equivalent is:
``` html
<div>Hello world!</div>
```

Writing a nested HTML structure, using Python Hiccup:

``` python
["div", ["span", ["strong", "Hello world!"]]]
```

The HTML equivalent is:
``` html
<div>
    <span>
        <strong>Hello world!</strong>
    </span>
</div>
```


Adding attributes to an element, such as CSS id and classes, using Python Hiccup:

``` python
["div", {"id": "foo", "class": "bar"}, "Hello world!"]
```

or, using a more concise syntax:
``` python
["div#foo.bar", "Hello world!"]
```

The HTML equivalent is:
``` html
<div id="foo" class="bar">Hello world!</div>
```

Adding valueless attributes to elements, such as the `async` or `defer`, by using Python `set`:
``` python
["!DOCTYPE", {"html"}]
["script", {"async"}, {"src": "js/script.js"}]
```

The HTML equivalent is:
``` html
<!DOCTYPE html>
<script async src="js/script.js"></script>
```

### Adding unescaped content
This is useful when rendering HTML entities like `&copy;`.

``` python
from python_hiccup.html import raw

data = ["div", raw("&copy; this should <strong>not</strong> be escaped!")]
```

The HTML output:

``` html
<div>&copy; this should <strong>not</strong> be escaped!</div>
```

## Resources
- [PyScript and python-hiccup example](https://pyscript.com/@davidvujic/pyscript-jokes-with-a-hiccup/latest?files=main.py) - PyScript Jokes with a Hiccup
- [Hiccup](https://github.com/weavejester/hiccup) - the original implementation, for Clojure.

## Existing python alternatives
- [pyhiccup](https://github.com/nbessi/pyhiccup)
- [piccup](https://github.com/alexjuda/piccup)

## Development
Running lint:

``` shell
uv run ruff check
```

Running type checks:

``` shell
uv run ty check
```

Running tests:

``` shell
uv run pytest
```
