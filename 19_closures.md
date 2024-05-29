# Closures

https://www.geeksforgeeks.org/python-closures/

<br>
<br>

### 🍭 What is a Closure?

- Before seeing what a closure is, we have to first **understand** what **nested functions and non-local variables are**.

#### Nested functions in Python

- A function that is defined inside another function is known as a nested function. Nested functions are able to access variables of the enclosing scope.

```python
# Python program to illustrate
# nested functions
def outerFunction(text):

	def innerFunction():
		print(text)

	innerFunction()


if __name__ == '__main__':
	outerFunction('Hey!')
```
