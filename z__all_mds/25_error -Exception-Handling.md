## 🟡 Error/Exception Handling

[Python Exception Handling Tutorial for Beginners](https://youtu.be/PHzm_Iox1mE?feature=shared)

- I will be following the examples of the above video at the bottom of this file, first i will ask **chatgpt** some qquestions.

<br>
<br>

### 🙋‍♀️ QUESTION: Explain the purpose and give me some example of Exception Handling

<br>

##### chatgpt:

> 💡 **Exception handling is a programming mechanism designed to handle and manage errors that occur during the execution of a program.**

- It allows developers to anticipate and manage unforeseen circumstances that might disrupt normal program flow.

<!-- #### The primary purposes of exception handling are: -->

<br>
<br>

### 🟣 Difference between Error and Exception:

- In programming, ✋ error and exception are related but **distinct concepts**:

<br>

🚩 **Error:** Typically refers to a mistake made by the programmer that results in a program that cannot run. For example, syntax errors <u>(like a missing parenthesis) or logical errors (where the program does not perform as intended)</u> .

<br>

🏴 **Exception:** An exception is an event that disrupts the normal flow of the program's instructions during execution. Exceptions can occur due to factors **outside the programmer's control**, such as <u>invalid user input, network issues, file I/O errors, etc</u> . Exceptions are typically handled by the program to prevent crashes and manage unexpected situations.

<br>

> 💡 In summary, while errors are mistakes that prevent a program from running correctly due to programming faults, exceptions are events that occur during execution and are managed by exception handling mechanisms to ensure robust and predictable program behavior.

<br>
<br>

### 🙋‍♀️ QUESTION: so its similar to the <u>Try & Catch</u> on react and javascript?

##### chatgpt:

<br>

✅ **Yes**, exception handling in programming languages like Python and error handling in JavaScript (including React) serve similar purposes, although the **syntax** and specific **mechanisms** <u>differ</u> slightly.

<br>

#### 👬 Similarities:

<br>

**Purpose:** Both Python's try-except blocks and JavaScript's try-catch blocks serve the purpose of handling and managing errors or exceptions that occur during program execution.

**Syntax:** While the syntax differs slightly between languages, both mechanisms allow developers to encapsulate potentially error-prone code and provide structured ways to handle different types of errors.

**Handling Unexpected Situations:** Both mechanisms provide a way to gracefully handle unexpected situations that may arise during program execution, preventing crashes and allowing for error recovery or fallback actions.

<br>

🔴 In summary, **while** Python uses try-except blocks for exception handling and JavaScript (including React) uses try-catch blocks for error handling, the core principles and purposes behind these constructs are quite similar across different programming languages and frameworks. They both aim to ensure robust and reliable program execution in the face of unforeseen errors or exceptions.

<br>

#### Here's how they compare:

- Javascript

```javascript
try {
  // Attempt to execute this code block
  let x = parseInt(prompt("Enter a number:"));
  let y = 10 / x; // This may throw a TypeError if x is not a number

  console.log("Result:", y);
} catch (error) {
  if (error instanceof TypeError) {
    console.log("Invalid input. Please enter a valid number.");
  } else if (error instanceof Error && error.name === "RangeError") {
    console.log("Division by zero is not allowed.");
  } else {
    console.log("An unexpected error occurred:", error);
  }
} finally {
  console.log("Execution completed.");
}
```
