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
number = 0.45678
formatted_number = f"{number:.2%}"
print(formatted_number)  # Output: 45.68%

```

<br>

- **.2g**: Format using the shorter of .f or .e notation, with two significant digits.

```python
number = 123.45678
formatted_number = f"{number:.2g}"
print(formatted_number)  # Output: 1.2e+02

```

<br>

- **.2n**: Format as a floating-point number with two decimal places, but use locale-specific number formatting.

```python
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Set locale to English (United States)
number = 123456.789
formatted_number = f"{number:.2n}"
print(formatted_number)  # Output: 123,456.79

```

<br>

**locale.LC_ALL** specifies that the locale settings should be applied to all categories, including numbers, dates, times, and currency.

So, when you use `"{number:.2n}"` to format a number with .2n, it will format the number with two decimal places and use locale-specific number formatting, adhering to the conventions of the English (United States) locale set by locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

<br>
