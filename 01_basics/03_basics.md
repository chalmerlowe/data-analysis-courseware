---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region slideshow={"slide_type": "slide"} -->
# Welcome to the Dark Art of Coding:
## Introduction to Python
Basics

Operators, `str`, `int`, `float`, basic builtins, comments

<img src='../universal_images/logos.3.600.wide.png' height='250' width='300' style="float:right">
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# Today's main objectives

You will be able to:

* List several main operators and their order of precedence
* List several key data types
* List several builtin functions
* Find help for yourself on how to use those functions
<!-- #endregion -->

# Entering Python code in Jupyter cells
---


If you enter a line of code into a Jupyter cell and press:
**Shift + Enter**

* the cell will execute the code
* the cell will display the representation of that execution/evaluation **for the last line in the cell**
* the notebook focus will shift to the following cell


In this case, the 4 will be evaluated and the representation of that evaluation will be displayed, i.e. Jupyter will show you a 4.

```python slideshow={"slide_type": "slide"}
4
```

If you enter a line of code into a Jupyter cell and press: **Ctrl + Enter**

* the cell will execute the code
* the cell will display the representation of that execution/evaluation **for the last line in the cell**
* the notebook focus will stay in the same cell

Similarly, this simple addition will also be evaluated:

```python slideshow={"slide_type": "slide"}
5 + 6
```

# Operators
---

<!-- #region slideshow={"slide_type": "slide"} -->
Python operators allow for calculations between one or more operands. At face value, Python operators mirror exactly what you would expect from a mathematical operator (i.e. 2 + 2 equals 4). As we will soon see, Python provides additional capablities when using operators (via a principal called *overloading*) to enable some powerful data processing capabilities above and beyond just numerical calculations.

A sample of operators is below.

| Operator   | Operation     | Example   | Result   |
|:----------:|:--------------|----------:|---------:|
|**          |Exponent       | 2 ** 4    | 16       |
|*           |Multiplication | 3 * 4     | 12       |
|/           |Division       | 12 / 4    | 3        |
|+           |Addition       | 3 + 3     | 6        |
|-           |Subtraction    | 8 - 4     | 4        |

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
The order of operations matches the order used in mathematics.
Parentheticals can be used to override precedence.

You might remember from math class:

parentheticals -> exponents -> multiplication | division -> addition | subtraction 

Which is often taught using the mnemonic: **PEMDAS**

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
## Order of operations

The order of these operations matter:

Because of the order of operations, division occurs prior to the addition

This is the same as `1 + (2 / 3) => 1.66666...`
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
1 + 2 / 3
```

<!-- #region slideshow={"slide_type": "fragment"} -->
To force the addition to occur first, you can wrap it in parenthesis

`(1 + 2) / 3 => 1.0`
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
(1 + 2) / 3
```

<!-- #region slideshow={"slide_type": "slide"} -->
Below is a more sophisticated example of order of precedence:
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
((4 - 1) * (4 + 1)) / (7 - 2)  
```

<!-- #region slideshow={"slide_type": "fragment"} -->
To help clarify, see this step-by-step walk-through of order of precedence

```
((4 - 1) * (4 + 1)) / (7 - 2)
((4 - 1) * (4 + 1)) / 5
(3 * (4 + 1)) / 5
(3 * 5) / 5
15 / 5
3
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
NOTE: Failure to have two operands will result in an error.
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
42 -
```

# Experience Points
---

<!-- #region -->
## Complete the following exercises:

In **Jupyter** use each of the operators below to create calculations using the numbers provided. 


|Task|Operator| Operands |
|---|---|---|
|1.| \** | 3 and 5 |
|2.|\* | 2 and 3  | 
|3.| / |  6 and 3 |
|4.| \+ | 8 and 2 | 
|5.| \- | 9 and 4 |


**BONUS**: Try to combine operators and operands to create more complicated calculations, using parenthesis 
<!-- #endregion -->

When you complete this exercise, please put your green post-it on your monitor. 

If you want to continue on at your own-pace, please feel free to do so.

<img src='../universal_images/green_sticky.300px.png' width='200' style='float:left'>

```python
(8 + 2) / 3
```

<!-- #region slideshow={"slide_type": "slide"} -->
# Basic Data Types

Data Type | Examples | Name
----------|----------|-------
Integers  |  -10, 0, 1, 2, 3 | int
Floating point numbers | -10.0, 0.0, 1.1, 2.1, 3.7 | float
Strings   | 'x', 'aloha', 'world', 'PyHawaii', '42', '5.55' | str
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
It is possible to concatenate two strings (`str`) using the plus (`+`) operator

This use of the plus operator to "add" text strings together is an example of operator overloading (using an operator for multiple purposes).

<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
'Aloha' + 'World'
```

<!-- #region slideshow={"slide_type": "slide"} -->
Attempting to concatenate a `str` and an `int` will result in an error.

Overloading only goes so far.
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
'Py' + 7
```

<!-- #region slideshow={"slide_type": "slide"} -->
The multiplication operator (\*) is overloaded, similarly:
    
It is possible to 'multiply' OR repeat a `str` using the '*' operator
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
'-' * 60
```

<!-- #region slideshow={"slide_type": "fragment"} -->
Attempting to multiply two strings (str) will result in an error
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
'Py' * 'Hawaii'
```

# Experience Points
---

<!-- #region -->
## Complete the following exercises:

In **Jupyter** create the following data types (for the numbers, use various operators to do **math**).

Data type | Values
----|----
integers | `-10, 0, and 42`
floating point numbers | `-10.0, 0.1, 42.0, and 3.7`
strings | `'x', 'aloha', and 'Dark art of coding'`


## Complete the following exercises:

In **Jupyter** complete the following exercises to explore operator overloading (feel free to swap out alternate values as you desire):

Task | Operator | Operands 
----------|:----------:|-----
concatenate  | + | 'diana' and 'prince'
multiply | * | 'kara' and 10
<!-- #endregion -->

<img src='../universal_images/green_sticky.300px.png' width='200' style='float:left'>


# Variables
---

```python slideshow={"slide_type": "slide"}
ip_addresses = 101
ip_addresses
```

```python slideshow={"slide_type": "fragment"}
ip_addresses + 10
```

```python
ip_addresses
```

```python slideshow={"slide_type": "fragment"}
hosts = 5
ip_addresses + hosts
```

```python

```

```python slideshow={"slide_type": "slide"}
hostname = 'bruces_laptop'
vehicle = 'batmobile'
```

```python

```

<!-- #region slideshow={"slide_type": "fragment"} -->
## Valid variable names

There are several options available in terms of how you craft Python variable names... any of the following are allowed.

```
name              # lower case
className         # camelCase
class_name        # snake_case
_name             # leading underscore
NAME              # ALL CAPS
nam3              # letters and numbers (NOTE: can't start with a number)
```

The following is NOT allowed:
```
3kans             # No leading numbers
```

<!-- #endregion -->

# Experience Points
---

<!-- #region -->
## Complete the following exercises:

In **Jupyter** create a series of variables as listed below (feel free to swap out alternate values as you desire):


Variable label | Variable value
----------|----------
age  | 42 
tool | 'nikto' 
name | 'bruce wayne'
alias | 'batman'
os | 'OS X'
pi | 3.14
<!-- #endregion -->

<img src='../universal_images/green_sticky.300px.png' width='200' style='float:left'>

<!-- #region slideshow={"slide_type": "slide"} -->
# Builtin Functions
---
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Python comes with a collection of functions to help you handle common tasks

### So, what are functions?

Functions are common in Python, as we will learn. This introduction is gonna be very limited, as we will dive much more deeply into functions at a later time.

For now, functions are:

* short self-contained snippets of code
* typically designed to solve a single problem or related set of problems
* often accept inputs and produce outputs (but aren't required to do so)
* referred to by name
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
print('Aloha Hawaii')
print()
print('How old are you?')                        
```

```python slideshow={"slide_type": "slide"}
help(print)
```

```python
print('hello my number is ', 42, 63, end='****\n')
print('hello my number is ', end='!')
```

```python
3 + 4
12 + 5
4 + 5
```

<!-- #region slideshow={"slide_type": "slide"} -->
Based on the help documentation, let's make note of some **semi-standard conventions**. You will find:

1. **Basic usage** is outlined near the top
1. All the **possible arguments** are listed with any **default values**
1. Ellipsis, in this case means you can have as many values as you like
1. Items with default values are **essentially optional**


    Help on built-in function print in module builtins:

    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.

<!-- #endregion -->

NOTE: When using Jupyter (or IPython), there is an easier syntax to get help: 

You can type the name of a function, followed by a question mark and execute the cell. This will show an augmented help display similar to the one produced by the `dir()` function.

`print?`

```python
import pandas as pd
pd.read_csv
```

<!-- #region slideshow={"slide_type": "slide"} -->
## input()

The `input()` function allows you to accept inputs from your user.

If can be used with OR without a string argument as a prompt, as shown below:

<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
food = input()
```

```python
food
```

```python slideshow={"slide_type": "slide"}
my_favorite_food = input('What is your favorite food?')
```

```python
my_favorite_food
```

<!-- #region slideshow={"slide_type": "slide"} -->
## print()
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
The `print()` function, as we have seen, can display a string representation of an object or the value of a variable.

The `print()` function can display the results of operations, as well as simple strings or string representations of variables OR objects.

Here, the string within the `print()` function is a concatenation of the literal string and the variable output by the `input()` function we used above.
<!-- #endregion -->

```python
'I also love: ' + 'lobster'
```

<!-- #region slideshow={"slide_type": "slide"} -->
## len()

The `len()` function displays the length of a Python object (if that object has a length characteristic OR if one can be calculated). Examples include:

* the number of characters in a string
* the number of items in a list
* the number of key/value pairs in a dictionary
* many, many more...

(I know we haven't talked about lists OR dictionaries yet. We will! The principal here is that `len()` enables us to determine the length of many Python objects.
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
len('ab')
```

```python slideshow={"slide_type": "fragment"}
len(my_favorite_food)
```

<!-- #region slideshow={"slide_type": "slide"} -->
## str()

Strings (often called `str` based on the factory function that can be used to create them) are sequences of characters. If you have an object that is not a `str` but you want to convert it OR cast it to become a `str`, you can do so with the `str()` function. A common example is to convert an integer into a `str`.
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
str(5)
```

```python slideshow={"slide_type": "fragment"}
str(-2 * 4)
```

<!-- #region slideshow={"slide_type": "slide"} -->
## int()

Integers can be created using the `int()` function. If you have a value, such as a `str` that you want to convert OR cast to an integer, the `int()` function can do it.
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
int('-42') * 2
```

<!-- #region slideshow={"slide_type": "slide"} -->
Let's look at another help documentation:

* **Basic usage** outlined near the top
* Slightly different way to show usage and **optional elements**
* x is **optional** in the first usage pattern
* x is **required** in the second usage pattern
* **'->'** indicates that the function returns a value, which can be saved for later


    class int(object)
     |  int(x=0) -> integer
     |  int(x, base=10) -> integer
     |
     |  Convert a number or string to an integer, or return 0 if no arguments
     |  are given.  If x is a number, return x.__int__().  For floating point
     |  numbers, this truncates towards zero.
     |
     |  If x is not a number or if base is given, then x must be a string,
     |  bytes, or bytearray instance representing an integer literal in the
     |  given base.  The literal can be preceded by '+' or '-' and be surrounded
     |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
     |  Base 0 means to interpret the base from the string as an integer literal.
     |  int('0b100', base=0)
     |  4
<!-- #endregion -->

```python
a = '42'

int(a)
```

<!-- #region slideshow={"slide_type": "fragment"} -->
The `int()` function will truncate decimal numbers towards zero (down for positive numbers, but up for negative numbers).
<!-- #endregion -->

```python slideshow={"slide_type": "fragment"}
int(42.11)
```

```python slideshow={"slide_type": "fragment"}
int(41.95)
```

```python slideshow={"slide_type": "fragment"}
int(-41.95)
```

<!-- #region slideshow={"slide_type": "slide"} -->
## float()

The `float()` function will convert values into floats (i.e. decimal numbers).
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
float('42.11')
```

```python slideshow={"slide_type": "fragment"}
float('41.0')
```

## How do you get a list of all builtin functions:

You can use the `dir(__builtins__)` function to lookup the following:

* all the builtin functions
* all the builtin errors (more on this later)
* datatypes such as `False`, `True` and `None` (more on these later)
* several other items that we won't cover here...

The output of this function will show you all of these values in **lexigraphical order** ... meaning terms that start with an uppercase letter will be first and alphabetized and any terms that start with a lowercase letter will come last and will be alphabetized.

For our purposes, we will focus on just the lowercase items at the end of the list.

```python
dir(__builtins__)
```

As a reminder, you can learn more about any builtin function using Jupyter's question mark based help functionality.

```python
len?
```

```python

```

<!-- #region slideshow={"slide_type": "slide"} -->
## Nuances about comparing datatypes...

Python allows you to compare elements of the same datatype (i.e. compare integers to integers OR float to float). It generally doesn't let you compare different datatypes, unless that comparison makes sense...

Comparing an `int` to a `str` doesn't work...
<!-- #endregion -->

```python slideshow={"slide_type": "slide"}
13 == '13'
```

But comparing a `float` to an `int` does work...

```python slideshow={"slide_type": "fragment"}
13.0 == 13
```

# Comments
---

<!-- #region -->
There are three commonly accepted ways to create comments in Python.

NOTE: Python **ignores ALL comments**.

### Line starting with a hashtag    
    
```python    
# comment: blah, blah, blah
```

### Text on any line, following a hashtag

```python
print('hello')      # comment: generally focused on the content of that line
```

### Text contained in triple quotes.

```python
'''
multiline
comment
blah
blah
blah
'''
```
<!-- #endregion -->

# Experience Points
---


## Complete the following exercises:


In your **text editor** create a simple script called `my_basics.py` to do each of the following steps.

Execute your script in **Jupyter** using the command `run my_basics.py`.

I suggest that as you add each feature to your script that you run it right away to test it incrementally. 

1. Include a **comment** indicating your name and date.

1. `print()` your **name** 

1. `print()` a **blank line**

1. Convert a numeric string (i.e. '13') to an integer AND assign the label: `myinteger`.

1. `print()` the variable `myinteger`.

1. Use `input()` to prompt for your first name AND assign the label: `fname`.

1. Calculate the length of `fname` AND assign the label: `length`.

1. `print()` the variable `length`.

1. Convert a negative number to a str AND assign the label: `neg_number`.

1. Convert a float to an integer AND assign the label: `flt_number`.

1. `print()` the variable `neg_number`

1. `print()` the variable `flt_number` 

1. Test two strings, `selina kyle` and `harleen quinzel`, for equality AND assign the result the label: `comparison`.

1. `print()` the variable `comparison`.

**SOLUTION**: a script with the solution to this exercise is included with this notebook, called: `soln_my_basics.py`


<img src='../universal_images/green_sticky.300px.png' width='200' style='float:left'>
