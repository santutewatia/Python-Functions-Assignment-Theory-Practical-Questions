#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Python Functions Assignment Theory & Practical Questions

                 Theory Questions 
   
Ques 1  #What is the difference between a function and a method in Python?

Ques 2  #Explain the concept of function arguments and parameters in Python.

Ques 3  #What are the different ways to define and call a function in Python?

Ques 4  #What is the purpose of the `return` statement in a Python function?

Ques 5  #What are iterators in Python and how do they differ from iterables?

Ques 6  #Explain the concept of generators in Python and how they are defined.

Ques 7  #What are the advantages of using generators over regular functions?

Ques 8  #What is a lambda function in Python and when is it typically used?

Ques 9  #Explain the purpose and usage of the `map()` function in Python.

Ques 10 #What is the difference between `map()`, `reduce()`, and `filter()` functions in Python?

Ques 11 #Using pen & Paper write the internal mechanism for sum operation using  reduce function on this given
       list:[47,11,42,13]; 


# In[ ]:


# Theory Questions


# In[ ]:


# Ques 1

# What is the difference between a function and a method in Python?

In Python, functions and methods are both blocks of reusable code, but they differ in how they are
used and where they are defined. Here’s a breakdown of the differences:

1. Function:
    
Definition: A function is a block of code that is defined using the def keyword and can be called 
independently from any object. It can take inputs (parameters) and return a value.

Scope: Functions are generally defined at the global or module level.
    
Calling: You can call a function by its name and pass the required arguments.


# In[1]:


# Example:
# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))  # Output: "Hello, Alice!"


# In[ ]:


2. Method:
    
Definition: A method is a function that is associated with an object. It is defined inside a class 
and is called on an instance of that class (i.e., an object).

Scope: Methods are defined within a class and operate on the data contained in the instance of the 
class.
Calling: You call a method using the object (or class) it belongs to, and it often takes the 
object’s data (the instance itself) as an implicit parameter (self).


# In[2]:


# Defining a class with a method
class Person:
    def __init__(self, name):
        self.name = name
    
    # Defining a method
    def greet(self):
        return f"Hello, {self.name}!"

# Creating an instance of the class
person = Person("Alice")

# Calling the method on the instance
print(person.greet())  # Output: "Hello, Alice!"


# In[ ]:


Summary

A function is a standalone block of code that performs a specific task, while a method is a 
function that is associated with an object and operates on its data.

Functions are called independently, whereas methods are called on objects or instances of a class.
Methods automatically receive the object (instance) they belong to as an argument via self.


# In[ ]:


# Ques 2

#Explain the concept of function arguments and parameters in Python.

1. Parameters:
    
What are they?: Parameters are like placeholders or labels inside a function definition. 
They tell the function what kind of input it can expect.

When are they used?: When you define a function, you use parameters to show what values the 
function will need.


# In[6]:


# Example
# In this example, name is the parameter. 
# It's just a placeholder for whatever name you give the function when you call it.

def greet(name):  # 'name' is a parameter
    return f"Hello, {name}!"


# In[ ]:


2. Arguments:
    
What are they?: Arguments are the actual values you pass to the function when you call it.

When are they used?: When you run (or call) the function, you give it arguments. 
These arguments are matched with the function’s parameters.


# In[5]:


# Example:
# Here, "Alice" is the argument you pass to the function. This value replaces the parameter 
# name in the function.
greet("Alice")  # "Alice" is an argument


# In[ ]:


Summary

Parameters are placeholders in the function definition.

Arguments are the actual values you pass to the function.

Python allows different ways to pass arguments, like positional, 
keyword, default, and even a variable number of arguments with *args and **kwargs.
This makes functions very flexible


# In[ ]:


# Ques 3

#What are the different ways to define and call a function in Python?

In Python, there are several ways to define and call a function, providing flexibility for different
programming needs. Let's look at these different methods:

1. Regular Function Definition and Calling

A basic function is defined using the def keyword followed by the function name and parameters 
inside parentheses. You call it by its name, passing in arguments if needed


# In[7]:


#  Example

# Defining a regular function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))  # Output: Hello, Alice!


# In[ ]:


Summary:
    
1 Regular function: Defined with def, called by name.
    
2 Functions with default arguments: Assign default values to parameters.
    
3 Keyword arguments: Specify arguments by name when calling.
    
4 Arbitrary arguments (*args): Handle variable numbers of arguments.
    
5 Arbitrary keyword arguments (**kwargs): Handle variable numbers of keyword arguments.
    
6 Lambda functions: Small, anonymous functions for simple tasks.
    
7 Nested functions: Functions within other functions.
    
8 Recursive functions: Functions that call themselves.
    
9 Higher-order functions: Functions that accept other functions as arguments or return functions.

These different ways of defining and calling functions allow flexibility in how you write Python code for various use cases.


# In[ ]:


# Ques 4

#What is the purpose of the `return` statement in a Python function?


The return statement in a Python function is used to send a result back to the caller of the function.
It allows a function to output a value or result after performing its operations. Here’s a simple 
breakdown of its purpose and how it works:

Purpose of the return Statement:

1 Sending Results Back:

The return statement allows a function to send a value back to where it was called, making 
it possible for the function to provide a result to the rest of your program.

This result can be used in expressions, assigned to variables, or passed to other functions.

2 Ending Function Execution:

When the return statement is executed, it immediately stops the function’s execution.
No code after the return statement is executed.

3 Returning Values:

You can return any type of value, including numbers, strings, lists, dictionaries, or even other functions.

4 Returning Multiple Values:

You can return multiple values from a function by separating them with commas.
These values are returned as a tuple.


# In[8]:


# Examples:
# Returning a Single Value:
# Here, return a + b sends the sum of a and b back to the caller, and result holds the value 8.
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8



# In[ ]:


Summary:
    
The return statement is used to send a result from a function back to the caller.

It can return any value, and if no value is provided, it returns None.

It ends the function execution, so no code after the return statement is executed.

Multiple values can be returned as a tuple.

The return statement is crucial for creating functions that perform computations or data processing
and need to provide results to other parts of the program.


# In[ ]:


# Ques 5

#What are iterators in Python and how do they differ from iterables?


In Python, iterators and iterables are related concepts used for looping over sequences of items.
Here’s a simple explanation of each and how they differ:

Iterable

What is it?: An iterable is any Python object that can return an iterator. It means the object
can be looped over (iterated) using a for loop or other iteration methods.

Examples: Lists, tuples, strings, and dictionaries are all iterables.

How to Check: You can check if an object is iterable by using the iter() function. If iter() can 
be called on it, it’s iterable.


# In[9]:


my_list = [1, 2, 3]
print(iter(my_list))  # This works, so my_list is iterable


# In[ ]:


Iterator

What is it?: An iterator is an object that represents a stream of data. 
    
It provides a way to access elements one at a time. An iterator keeps track of its current position and knows how to get the next item.

How It Works: An iterator has two main methods:

__iter__(): Returns the iterator object itself.
__next__(): Returns the next item in the sequence. When there are no more items, it raises a 
StopIteration exception.
    
Examples: Iterators are often created from iterables. For example, calling iter() on a list 
returns an iterator.



# In[10]:


my_list = [1, 2, 3]
my_iterator = iter(my_list)  # Create an iterator from the list

print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3


# In[ ]:


Key Differences

Definition:

Iterable: An object that can return an iterator (e.g., lists, tuples).

Iterator: An object that represents a sequence of items and can be used to iterate through them.
    
    
Summary:
    
Iterable: An object that can be looped over, like a list or string. It provides an iterator.
Iterator: An object that keeps track of where it is in a sequence and knows how to get the next item.
    
Iterators and iterables are foundational for looping and handling sequences in Python.


# In[ ]:


# Ques 6

#Explain the concept of generators in Python and how they are defined.

Generators in Python are a type of iterable, like lists or tuples, but they are more memory-efficient.
Instead of storing all items in memory at once, generators produce items one at a time and only when
needed. This makes them suitable for handling large datasets or streams of data.

Concept of Generators

1 Definition:

Generators are functions that use the yield keyword to return values one at a time. 
Each time a generator function is called, it resumes where it left off, continuing from 
the last yield statement.

2 How They Work:

When a generator function is called, it returns a generator object, not the result. 
This generator object can be iterated over to obtain the values yielded by the generator function.

3 Benefits:

Memory Efficiency: Generators do not store all items in memory, which is useful for processing
large data sets.
Lazy Evaluation: They generate items only when needed, which can be more efficient than
generating all items upfront.


# In[11]:


# Defining Generators
# Generators are defined like regular functions but use the yield statement instead of return:

# Basic Generator:

# A generator function uses yield to produce values. Each call to next() on the generator object
# resumes the function from the last yield.

# Example:
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()  # Create a generator object
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# Calling next(gen) again would raise StopIteration


# In[ ]:


Summary

Generators are special types of iterators that use the yield keyword to produce values one at a time.

Memory Efficient: They handle large data sets without storing everything in memory.
    
Lazy Evaluation: Values are generated only when needed.
    
Defined: Using functions with yield or generator expressions.
    
Generators provide a powerful way to work with sequences of data efficiently and can be used anywhere you would use an iterable.


# In[13]:


# Ques 7

#What are the advantages of using generators over regular functions?


Generators offer several advantages over regular functions, especially when dealing with large
datasets or situations where you don't need all the values at once. Here's a breakdown of the
advantages of using generators over regular functions:


# In[ ]:


Memory Efficiency

Regular functions: When a regular function returns a large collection (like a list), it generates
all the values at once and stores them in memory. This can be a problem if the collection is very 
large, as it consumes a lot of memory.

Generators: With generators, values are produced one at a time, as needed. This means they don’t 
store the entire sequence in memory, making them much more memory-efficient.
    


# In[1]:


def generate_numbers(n):
    for i in range(n):
        yield i  # Produces one value at a time

gen = generate_numbers(1000000)  # Uses very little memory

# In contrast, returning a list of 1 million numbers from a regular function would
# require storing all the numbers in memory at once.




# In[ ]:


Advantages:
    
Memory Efficiency: Only produces values when needed, saving memory.
    
Lazy Evaluation: Values are generated on-the-fly, reducing computation time.
    
Improved Performance: Especially for large datasets or streams, as they don’t need to store all values 
in memory.

Simpler Iteration: Cleaner and more concise code for iterative processes.
    
Handling Infinite Sequences: Can handle infinite sequences without consuming large amounts of memory.
    
Pipelines: Ideal for streaming and pipeline processing, where data is processed step-by-step.
    
State Preservation: Generators can remember their state between next() calls.
    
Generators provide a more efficient and scalable way to handle sequences and streams of data, especially when dealing with large or potentially infinite data sets.


# In[ ]:


# Ques 8

#What is a lambda function in Python and when is it typically used?

A lambda function in Python is a small, anonymous function defined using the lambda keyword instead 
of def. These functions can have any number of arguments but only one expression, which is evaluated 
and returned. They are typically used for short, simple operations that don’t require a full function
definition.


# In[4]:


#Syntax of Lambda Function

lambda arguments: expression

# Arguments: The inputs to the function (can be multiple).
    
# Expression: The operation performed by the function, and it must return a value.


# In[5]:


# Example of a Lambda Function
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# In this example, lambda x, y: x + y defines a function that takes two arguments (x and y) and
# returns their sum. It is assigned to the variable add, which can be called like a regular function.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'Function')

When you need a small, one-time-use function, especially as an argument to another function.

When the function logic is simple enough to be expressed in a single line.

When defining a full function using def would add unnecessary complexity.

Summary

Lambda functions: Small, anonymous functions that are defined with the lambda keyword.
    
Typically used: In places where a short, throwaway function is needed, like with map(), filter(), 
or sorted().

Advantages: Concise and useful for simple operations.
    
Limitations: Can only contain a single expression and may reduce readability for complex tasks


# In[ ]:


# Ques 9

#Explain the purpose and usage of the `map()` function in Python.

The map() function in Python is used to apply a given function to all items in an iterable
(like a list, tuple, or set) and returns a map object (an iterator) with the results.

Purpose of map()

The primary purpose of the map() function is to apply a function to each item in an iterable 
(such as a list) without the need for an explicit loop. This can make the code more concise and
readable, especially when working with simple transformations.


# In[8]:


Syntax

map(function, iterable)

function: The function that you want to apply to each element of the iterable. This can be a 
built-in function, a lambda function, or a user-defined function.

iterable: The data structure (like a list, tuple, etc.) whose elements you want to transform.


# In[10]:


# Usage of map()

# Basic Example: Applying a built-in function like str() or len()
numbers = [1, 2, 3, 4]
result = map(str, numbers)  # Converts each number to a string
print(list(result))  # Output: ['1', '2', '3', '4']


# In[ ]:


Advantages of map()

Conciseness: It eliminates the need for an explicit loop to apply a function to elements.
    
Efficiency: As it returns an iterator, map() is more memory-efficient when working with large datasets.
    
Readability: Can make code cleaner and more readable, especially for simple transformations.
    
Summary

The map() function applies a given function to all items in an iterable and returns an iterator.

It is commonly used for transforming data, processing numeric data, and performing operations on elements
from multiple iterables.

The result can be easily converted to a list, tuple, or set for further use.


# In[ ]:


# Ques 10

#What is the difference between `map()`, `reduce()`, and `filter()` functions in Python?

In Python, map(), reduce(), and filter() are all higher-order functions that allow you to apply
functions to sequences like lists or tuples. While they may seem similar, they serve distinct 
purposes and behave differently. Here's a breakdown of each, along with the key differences between
them.

1. map() Function

The map() function applies a given function to each item of an iterable (like a list) and
returns an iterator with the results.

Purpose: To transform each element in an iterable by applying a function to it.


# In[13]:


# Syntax:

# map(function, iterable)

# Example:

numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)  # Multiplies each number by 2
print(list(result))  # Output: [2, 4, 6, 8]


# In[ ]:


2. filter() Function

The filter() function applies a function to each item in an iterable and filters out those that 
don't meet a certain condition. It returns an iterator with only the items that return True for
the condition.

Purpose: To filter elements of an iterable based on a condition.



# In[14]:


# Syntax:

# filter(function, iterable)

# Example:

numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 0, numbers)  # Keeps only even numbers
print(list(result))  # Output: [2, 4]


# In[ ]:


3. reduce() Function

The reduce() function, from the functools module, applies a function cumulatively to the items 
of an iterable, from left to right, so as to reduce the iterable to a single value.

Purpose: To reduce an iterable to a single cumulative value by applying a function repeatedl


# In[15]:


# Syntax:

# from functools import reduce
# reduce(function, iterable)

# Example:
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)  # Sums all numbers
print(result)  # Output: 10


# In[ ]:


Use Cases

map(): When you want to apply a transformation (e.g., scaling values, formatting text) to each element
in a sequence.

filter(): When you want to filter elements out of a sequence based on some condition
(e.g., keeping only even numbers, strings that start with a certain letter).

reduce(): When you want to combine elements to produce a single result 
(e.g., summing all numbers, finding the product of elements).


Summary

map() transforms every element in an iterable.

filter() selects elements based on a condition.

reduce() combines elements to return a single value. Each has its own purpose and can be used 
depending on the specific operation you need to perform on the elements of an iterable.


# In[73]:


# Ques 11

#Using pen & Paper write the internal mechanism for sum operation using  reduce function on this given
#list:[47,11,42,13]; 
 

The reduce() function in Python works by applying a function cumulatively to the items of an iterable.
Let's walk through the internal mechanism of the sum operation using reduce() on the given
list [47, 11, 42, 13].

We will use the following steps:

Step 1: Initial Setup

List: [47, 11, 42, 13]
Function: lambda x, y: x + y (This function takes two inputs and returns their sum)
Reduce will start by taking the first two elements and applying the function.

Step 2: First Operation

The first two elements are 47 and 11.
Apply the function: 47 + 11 = 58.
Now the list becomes: [58, 42, 13].
    
Step 3: Second Operation

The next two elements are 58 and 42.
Apply the function: 58 + 42 = 100.
Now the list becomes: [100, 13].
    
Step 4: Final Operation

The next two elements are 100 and 13.
Apply the function: 100 + 13 = 113.
Now we have the final result: 113.
Internal Mechanism of reduce() for Sum
Here’s the internal step-by-step calculation:

reduce(lambda x, y: x + y, [47, 11, 42, 13])
First: 47 + 11 = 58
Second: 58 + 42 = 100
Third: 100 + 13 = 113
    
Final Result:
The sum of the list [47, 11, 42, 13] using reduce() is 113.

This is how reduce() works internally by applying the operation cumulatively to the elements.


# In[ ]:





# In[ ]:


Python Functions Assignment Theory & Practical Questions

            Practical Questions
        
Ques 1. #Write a Python function that takes a list of numbers as input and returns the sum of all even
        #numbers in the list.

Ques 2  #Create a Python function that accepts a string and returns the reverse of that string.


Ques 3  #Implement a Python function that takes a list of integers and returns a new list containing
         #the squares of  each number.      

Ques 4  #Write a Python function that checks if a given number is prime or not from 1 to 200.


Ques 5  #Create an iterator class in Python that generates the Fibonacci sequence up to a specified 
        # number of terms.

Ques 6  #Write a generator function in Python that yields the powers of 2 up to a given exponent.

Ques 7  #Implement a generator function that reads a file line by line and yields each line as a string.

Ques 8  #Use a lambda function in Python to sort a list of tuples based on the second element of each 
        # tuple.

Ques 9 #Write a Python program that uses `map()` to convert a list of temperatures from Celsius to
        #Fahrenheit.

Ques 10 #Create a Python program that uses `filter()` to remove all the vowels from a given string. 

Ques 11

# Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:
    

# Oreder Number      Book Title and Author                        Quantity              Price per Item                    
# 34587              Learning python, mark lutz                     4                     40.95
# 98762              Programimg python, mark lutz                   5                     56.80
# 77226              Head first python, paul barry                  3                     32.95
# 88112              Einfuhrung in python3, bernd klein             3                     24.99


# Write a Python program, which returns a list with 2-tuples. Each tuple consists of the order number and the
# product of the price per item and the quantity. The product should be increased by 10,- € if the value of the
# order is smaller than 100,00 €.

# Write a Python program using lambda and map.


# In[ ]:


# Practical Questions


# In[25]:


# Ques 1

# Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in
# the list.

def sum_of_even_numbers(numbers):
    # Filter out the even numbers using a list comprehension
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    # Sum all the even numbers
    return sum(even_numbers)

# Example usage:
numbers = [47, 11, 42, 13, 8, 10]
result = sum_of_even_numbers(numbers)
print("Sum of even numbers:", result)



# In[46]:


# Ques 2

#Create a Python function that accepts a string and returns the reverse of that string.

def reverse_string(input_string):
    # Reverse the string using slicing
    return input_string[::-1]

# Example usage:
string = "Hello, World!"
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)


# In[58]:


# Ques 3

#Implement a Python function that takes a list of integers and returns a new list containing the
#squares of each number.

def square_numbers(numbers):
    # Using list comprehension to square each number in the list
    return [num ** 2 for num in numbers]

# Example usage:
numbers = [2, 4, 6, 8]
squared_numbers = square_numbers(numbers)
print("Squared numbers:", squared_numbers)


# In[63]:


# Ques 4

# Write a Python function that checks if a given number is prime or not from 1 to 200.

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes_in_range(start, end):
    """Print all prime numbers in a given range."""
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')
    print()  # To add a newline at the end of the output

# Check and print all prime numbers from 1 to 200
print_primes_in_range(1, 200)

  


# In[64]:


# Ques 5

# Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of
# terms.

class FibonacciIterator:
    def __init__(self, num_terms):
        self.num_terms = num_terms
        self.a, self.b = 0, 1
        self.current_term = 0
    
    def __iter__(self):
        # The iterator object itself is returned by __iter__
        return self
    
    def __next__(self):
        # Check if we have more terms to generate
        if self.current_term < self.num_terms:
            # Return the next term in the sequence
            next_value = self.a
            # Update a and b for the next call
            self.a, self.b = self.b, self.a + self.b
            self.current_term += 1
            return next_value
        else:
            # Stop iteration when we reach the specified number of terms
            raise StopIteration

# Example usage
num_terms = 10
fib_iterator = FibonacciIterator(num_terms)

for number in fib_iterator:
    print(number)


# In[65]:


# Ques 6

# Write a generator function in Python that yields the powers of 2 up to a given exponent.

def powers_of_two(max_exponent):
    """Generator function that yields powers of 2 up to 2^max_exponent."""
    exponent = 0
    while exponent <= max_exponent:
        yield 2 ** exponent
        exponent += 1

# Example usage
max_exponent = 5
for power in powers_of_two(max_exponent):
    print(power)


# In[66]:


# Ques 7

# Implement a generator function that reads a file line by line and yields each line as a string.

def read_file_lines(file_path):
    """Generator function that reads a file line by line and yields each line."""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.rstrip('\n')  # Remove trailing newline character
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except IOError as e:
        print(f"Error: An I/O error occurred. Details: {e}")

# Example usage
file_path = 'example.txt'  # Replace with your file path

for line in read_file_lines(file_path):
    print(line)


# In[67]:


# Ques 8

# Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.

# List of tuples
tuples_list = [(1, 3), (2, 1), (3, 2), (4, 4)]

# Sort the list of tuples based on the second element using a lambda function
sorted_list = sorted(tuples_list, key=lambda x: x[1])

# Print the sorted list
print(sorted_list)


# In[68]:


# Ques 9

# Write a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# List of temperatures in Celsius
celsius_temperatures = [0, 20, 37, 100]

# Use map() to apply the conversion function to each temperature
fahrenheit_temperatures = list(map(celsius_to_fahrenheit, celsius_temperatures))

# Print the results
print("Celsius temperatures:", celsius_temperatures)
print("Fahrenheit temperatures:", fahrenheit_temperatures)


# In[70]:


# Ques 10

# Create a Python program that uses `filter()` to remove all the vowels from a given string.

def is_not_vowel(char):
    """Return True if the character is not a vowel."""
    vowels = 'aeiouAEIOU'
    return char not in vowels

def remove_vowels(input_string):
    """Remove all vowels from the input string using filter()."""
    # Use filter() to keep only non-vowel characters
    filtered_chars = filter(is_not_vowel, input_string)
    # Join the filtered characters back into a string
    return ''.join(filtered_chars)

# Example usage
input_string = "Hello, World!"
result_string = remove_vowels(input_string)
print("Original string:", input_string)
print("String without vowels:", result_string)


# In[ ]:


# Ques 11

Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:
    

Oreder Number      Book Title and Author                        Quantity              Price per Item                    
34587              Learning python, mark lutz                     4                     40.95
98762              Programimg python, mark lutz                   5                     56.80
77226              Head first python, paul barry                  3                     32.95
88112              Einfuhrung in python3, bernd klein             3                     24.99


Write a Python program, which returns a list with 2-tuples. Each tuple consists of the order number and the
product of the price per item and the quantity. The product should be increased by 10,- € if the value of the
order is smaller than 100,00 €.

Write a Python program using lambda and map.
    


# In[74]:


# List of orders with [Order Number, Book Title and Author, Quantity, Price per Item]
orders = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

# Use map() and lambda to calculate the total price
order_totals = list(map(lambda order: (order[0], order[2] * order[3] + (10 if order[2] * order[3] < 100 else 0)), orders))

# Print the result
print(order_totals)


# In[ ]:





# In[ ]:




