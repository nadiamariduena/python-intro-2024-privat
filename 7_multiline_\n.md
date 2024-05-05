# MULTILINE, lowercase, uppercase..whitespace

- default

- **\t**, **\n** ...

```python
\a is alert/bell
\b is backspace/rubout
\n is newline
\r is carriage return (return to left margin)
\t is tab
```

https://stackoverflow.com/questions/8657702/what-do-t-and-b-do

https://discuss.python.org/t/python-add-or-insert-tab-t-into-list/27541/2

<br>
<br>

## Default

- first i will show you a basic way to write a text like and use multiline to add a second text, but this is not the common way to do it

```javascript
#
#
# 🟠 Multiple lines

multiline = '''
Hey, how are you?

I was just checking in.
                         All good things
'''
print(multiline)
```

#### result

```javascript
Hey, how are you?

I was just checking in.
                         All good things
```

<br>
<br>

## Using

```python
#
# Escaping special characters
#
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at \\located'
print(sentence)
#
#
# RESULT
Hey, how are you?

I was just checking in.
                         All good things

I'm back at work!       Hey!

Where's this at \located
```

<br>
<br>

## LOWER & UPPER (lower and uppercase)

```python
# String Methods

first = 'Laure'
last = "Blaz"


print(first)
print(first.lower())
print(first.upper())
print(first)
#
# RESULT
Laure
laure
LAURE
Laure
```

### CAPITAL case

```python
multiline = '''
Hey, how are you?

I was just checking in.
                         All good things
'''
print(multiline)


#
#
# the title() will convert it to capital case
print(multiline.title())
# it will replace the word good for ok on the second paragraph
print(multiline.replace("good", "ok"))
print(multiline)
#
#

# has capitalcase on the "How" due to the title()
Hey, How Are You?

I Was Just Checking In.
                         All Good Things


Hey, how are you?

I was just checking in.
                         All ok things

# this below will have the original text
Hey, how are you?

I was just checking in.
                         All good things
```

### White space

```python
multiline = '''
Hey, how are you?

I was just checking in.
                         All good things
'''
print(multiline)
print(len(multiline)) # to see the characters

#
# White space

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))


#
#
#
Hey, How Are You?

I Was Just Checking In.
                         All Good Things


Hey, how are you?

I was just checking in.
                         All ok things


Hey, how are you?

I was just checking in.
                         All good things

85
83
84
84
```

<br>

## 🟡 spaces

#### make spaces between one paragraph and another use this: `print("")` like so

<br>

```javascript
# White space

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
// before text -----
//
//  space
print("")
// space
//
// --- another text
anotherText =  '''
Jelly , hello
'''
print(anotherText)
//---------
//
//
// result

85
83
84
84


Jelly , hello
```
