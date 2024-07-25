# 🟡 ASCII:

<br>

### [what-is-ascii-a-complete-guide-to-generating-ascii-cod](https://www.geeksforgeeks.org/what-is-ascii-a-complete-guide-to-generating-ascii-code/?ref=lbp)


 <br>
 <br


### 🟦 ASCII stands for American Standard Code for Information Interchange.

<br>

- - 🟠 It is a **character encoding standard** for **electronic communication**.

- - ASCII defines **codes** for **128 characters:** 33 are non-printing control characters, and 95 are printable characters.


<br>





<br>
<br>
<br>

### 🟢 Related to the hangman exercise [LESSON_19_PPROJECTS/random_Hangman/README](./LESSON_19_PPROJECTS/random_Hangman/README.md)

#### excerpt of the code from the above link ⤴️

<br>

### 🟠 The `ascii_uppercase`



```python
import string # import the string at the top of the page,  to use it below
#
alphabet = set(string.ascii_uppercase)  # This line creates a set of all uppercase letters in the alphabet
```

<br>


The `ascii_uppercase`  is a constant defined in the Python string module. It represents a string containing all uppercase letters of the **ASCII** character set.


<br>

### Here’s some more detail:

<br>

🟪 **string Module:** In Python, the string module contains a collection of constants and functions related to ASCII strings.

- - These include various sets of ASCII characters (ascii_letters, ascii_lowercase, ascii_uppercase), digits (digits), punctuation (punctuation), and printable characters (printable).

<br>

🟪 **ascii_uppercase:**

- - This constant specifically contains all uppercase letters from 'A' to 'Z' in ASCII encoding. Therefore, ascii_**uppercase** is a **string** `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

<br>

### 🟠  Basic ASCII table showing the character, its decimal value, and its hexadecimal value:

<br>

 ```python
Dec  Hex  Char   Dec  Hex  Char   Dec  Hex  Char   Dec  Hex  Char
---------------------------------------------------------------
  0  00   NUL    32  20        64  40   @      96  60   `
  1  01   SOH    33  21   !     65  41   A      97  61   a
  2  02   STX    34  22   "     66  42   B      98  62   b
  3  03   ETX    35  23   #     67  43   C      99  63   c
  4  04   EOT    36  24   $     68  44   D     100  64   d
  5  05   ENQ    37  25   %     69  45   E     101  65   e
  6  06   ACK    38  26   &     70  46   F     102  66   f
  7  07   BEL    39  27   '     71  47   G     103  67   g
  8  08   BS     40  28   (     72  48   H     104  68   h
  9  09   TAB    41  29   )     73  49   I     105  69   i
 10  0A   LF     42  2A   *     74  4A   J     106  6A   j
 11  0B   VT     43  2B   +     75  4B   K     107  6B   k
 12  0C   FF     44  2C   ,     76  4C   L     108  6C   l
 13  0D   CR     45  2D   -     77  4D   M     109  6D   m
 14  0E   SO     46  2E   .     78  4E   N     110  6E   n
 15  0F   SI     47  2F   /     79  4F   O     111  6F   o
 16  10   DLE    48  30   0     80  50   P     112  70   p
 17  11   DC1    49  31   1     81  51   Q     113  71   q
 18  12   DC2    50  32   2     82  52   R     114  72   r
 19  13   DC3    51  33   3     83  53   S     115  73   s
 20  14   DC4    52  34   4     84  54   T     116  74   t
 21  15   NAK    53  35   5     85  55   U     117  75   u
 22

 ```

 <br>

 ### 🟠 Example:

 - - **Suppose** you have a **list of words** and **you want** to **sort** them **alphabetically**:

 ```python
words = ["apple", "Banana", "car", "Dog"]
sorted_words = sorted(words)
print(sorted_words)
#
# ✋ OUTPUT
# ['Banana', 'Dog', 'apple', 'car']
 ```

 <br>

### 🟣 QUESTION: so its getting only the uppercase from THE table:
`'Apple' (65), 'Banana' (66), 'Cat' (67), and 'Dog' (68).`

#### ✅ chatgpt:

- - Yes, that's correct. In your previous example, you mentioned strings like 'Apple', 'Banana', 'Cat', and 'Dog'. Each character in these strings corresponds to a specific ASCII value:

<br>

**'A'** corresponds to ASCII value **65**

**'B'** corresponds to ASCII value **66**

**'C'** corresponds to ASCII value **67**

**'D'** corresponds to ASCII value **68**

<br>

### 🫐 When you refer to `string.ascii_uppercase` in Python, it specifically provides a string containing all uppercase letters from 'A' to 'Z'. This is directly related to their ASCII values:

```python

import string

ascii_uppercase = string.ascii_uppercase
print(ascii_uppercase)
# Output: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

```
<br>

- This string **ascii_uppercase** consists of all uppercase letters in the ASCII character set, which are exactly the characters you mentioned ('A', 'B', 'C', 'D').

- These characters have consecutive ASCII values from 65 to 68, respectively.

<br>
<br>

##  🟦 Another ascii table

- This table covers the basic ASCII characters from 0 to 127. Each character has a unique decimal and hexadecimal representation, allowing computers to understand and process textual data universally across different systems and programming languages that adhere to the ASCII standard.

```python
Dec  Hex  Char   Dec  Hex  Char   Dec  Hex  Char   Dec  Hex  Char
---------------------------------------------------------------
 23  17   ETB    55  37   7     87  57   W     119  77   w
 24  18   CAN    56  38   8     88  58   X     120  78   x
 25  19   EM     57  39   9     89  59   Y     121  79   y
 26  1A   SUB    58  3A   :     90  5A   Z     122  7A   z
 27  1B   ESC    59  3B   ;     91  5B   [     123  7B   {
 28  1C   FS     60  3C   <     92  5C   \     124  7C   |
 29  1D   GS     61  3D   =     93  5D   ]     125  7D   }
 30  1E   RS     62  3E   >     94  5E   ^     126  7E   ~
 31  1F   US     63  3F   ?     95  5F   _     127  7F  DEL

```

<br>

**Dec:**  Decimal value of the ASCII character.

**Hex:**  Hexadecimal value of the ASCII character.

**Char:**  Corresponding character represented by the ASCII code.

<br>
<br>


#### 🟣 QUESTION: Can you give me an example where you include "text" converted to `uppercase, lowercase and symbols`? Use the right methods, similar to the first example "where is used" the: `set(string.ascii`


#### ✅ chatgpt:

- Let's work with a sample text that includes uppercase letters, lowercase letters, and symbols. We’ll use Python to manipulate and analyze this text using methods similar to those shown in the first example, focusing on ASCII values.

```python
"Hello, World! 123 @#"

```

<br>

- 🟠 **Extracting** `uppercase letters, lowercase letters, and symbols`

- -  we'll use **sets** to **demonstrate** how these **characters can be categorized**.


- - We’ll **use** `string.ascii_uppercase`, `string.ascii_lowercase`, `string.ascii_letters`, `string.digits`, and `string.punctuation` to achieve this.

<br>

```python
import string

# Example text
text = "Hello, World! 123 @#"

# ✋ Convert text to sets of different character types
uppercase_letters = set(char for char in text if char in string.ascii_uppercase)


# ✋ lowercase
lowercase_letters = set(char for char in text if char in string.ascii_lowercase)

# ✋ Digits
digits = set(char for char in text if char in string.digits)

# ✋ Punctuation
punctuation = set(char for char in text if char in string.punctuation)

# Print results
print("Uppercase Letters:", uppercase_letters)
print("Lowercase Letters:", lowercase_letters)
print("Digits:", digits)
print("Punctuation:", punctuation)

```

<br>

```bash
Uppercase Letters: {'W', 'H'}
Lowercase Letters: {'l', 'o', 'e', 'r', 'd'}
Digits: {'2', '1', '3'}
Punctuation: {'@', '!', ',', '#', ' '}
```

#### output acsii

```bash
ASCII values for Uppercase Letters: {'W': 87, 'H': 72}
ASCII values for Lowercase Letters: {'l': 108, 'o': 111, 'e': 101, 'r': 114, 'd': 100}
ASCII values for Digits: {'2': 50, '1': 49, '3': 51}
ASCII values for Punctuation: {'@': 64, '!': 33, ',': 44, '#': 35, ' ': 32}

```

<br>
<br>


#### 🟣 QUESTION: I see that the current method of choosing letters seems a bit random. Can you show me how to make the 'H' in 'Hello' and the 'O' in 'World' uppercase? Also, could you explain how to use symbols like {, which I think is '123' in the table?

<br>