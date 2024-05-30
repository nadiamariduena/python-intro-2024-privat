## Floating

The **.2f** format specifier in Python is used to format floating-point numbers with two decimal places. However, there are various other options you can use with .2f to control the formatting of the floating-point numbers. Here are some common options:

- **.2f**: Format as a floating-point number with two decimal places.

```python
number = 123.45678
formatted_number = f"{number:.2f}"
print(formatted_number)  # Output: 123.46

```

<br>

- **.2e**: Format in scientific notation (exponential format) with two decimal places.

```python
number = 123.45678
formatted_number = f"{number:.2e}"
print(formatted_number)  # Output: 1.23e+02

```

<br>

- **.2%**: Format as a percentage with two decimal places.

```python

```

<br>

- **.2g**: Format using the shorter of .f or .e notation, with two significant digits.

```python

```

<br>

- **.2n**: Format as a floating-point number with two decimal places, but use locale-specific number formatting.

```python

```

<br>
