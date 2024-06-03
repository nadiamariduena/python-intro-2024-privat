## Python lambda, map, filter, & reduce - Higher Order Functions for Beginners

https://youtu.be/YIOYJgLQYiY?feature=shared

<br>
<br>

### 🍭 Lambda

- [LAMBDA functions](https://youtu.be/KR22jigJLok?feature=shared)

##### chatgpt

- Lambda typically refers to the lambda function in Python, which is a small anonymous function defined using the lambda keyword. Lambda functions can take any number of arguments, but can only have one expression.

```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
# 3 +5 = 8
```

<br>

### 🍭 In Python, a lambda function is a way to create small, anonymous functions. They are similar to regular functions defined using the def keyword, but with a few key differences:

- **Anonymous:** Lambda functions are anonymous, meaning they don't have a name like regular functions do. They are defined using the lambda keyword followed by parameters and an expression.

```python
# Anonymous lambda function to calculate the square of a number
square = lambda x: x**2
print(square(5))  # Output: 25

```

<br>

**Small:** Lambda functions are typically used for small tasks and simple operations. They are often used where a function is needed for a short period of time and creating a named function would be overkill.

```python
# Using lambda function to add two numbers
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

```

<br>

**Expression-based:** Lambda functions can only contain a single expression. This means they are limited in what they can do compared to regular functions, which can contain multiple statements and have more complex logic.

```python
# Using lambda function to check if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True
# Examples of odd numbers are 3, 5, 7, 9, 11, 13, 15,…
# Examples of even numbers are 2, 4, 6, 8, 10, 12, 14,…
```

#### Lambda functions are often used in Python in situations where a function is required as an argument to higher-order functions (functions that take other functions as arguments), such as `map()`, `filter()`, and `sorted()`.

They are a convenient way to define simple functions inline without the need for a full function definition.

<br>
<br>

## ALSO:

-In mathematics, lambda (λ) often denotes a parameter or variable in functions or calculus.

- ✋ In computer science and distributed systems, ["Lambda"](https://aws.amazon.com/pm/lambda/?gclid=Cj0KCQjwsPCyBhD4ARIsAPaaRf3S1nW6pAbjQs9UkM1QB0OQYXuuzn5CBnmUqHWFRJDXD2KDAMC5msYaAvVVEALw_wcB&trk=c8019b8a-d2f2-4ec8-ac50-7bdc0dbe1996&sc_channel=ps&ef_id=Cj0KCQjwsPCyBhD4ARIsAPaaRf3S1nW6pAbjQs9UkM1QB0OQYXuuzn5CBnmUqHWFRJDXD2KDAMC5msYaAvVVEALw_wcB:G:s&s_kwcid=AL!4422!3!651612391322!e!!g!!lambda%20aws!19828205892!147081379877) can refer to AWS Lambda, which is a serverless computing service provided by Amazon Web Services.

- courses [AWS Lambda y Python | Guía PRÁCTICA aprende con un EXPERTO](https://www.udemy.com/course/aws-lambda-y-python-el-futuro-es-serverless/?utm_source=adwords&utm_medium=udemyads&utm_campaign=DSA-WebIndex_la.ES_cc.LATAM&campaigntype=Search&portfolio=LATAM&language=ES&product=Course&test=&audience=DSA&topic=&priority=&utm_content=deal4584&utm_term=_._ag_120316893258_._ad_504879908808_._kw__._de_c_._dm__._pl__._ti_dsa-93451758763_._li_9077251_._pd__._&matchtype=&gad_source=1&gclid=Cj0KCQjwsPCyBhD4ARIsAPaaRf1aMPZkWxqBwRmqiRF6xZCnNpGTxjewd0wr389S8o2rJFYA7buTV-kaAtISEALw_wcB)

[Intro to AWS Lambda with Python | AWS Lambda Python Tutorial](https://www.youtube.com/watch?v=-8L4OxotXlE)

<br>
<br>

- In functional programming languages like Lisp, lambda denotes an anonymous function.

<br>
<br>

## examples 1

```python
def squared(num): return num + num
print(squared(2))
#result
#4 // num + num or 2 + 2 = 4
```
