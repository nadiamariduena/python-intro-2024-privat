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
<br>

### Here's how they compare:

<br>

```python
#
# ---- CONDITION
#
try:
    # Step 1: Attempt to execute this code block
    x = int(input("Enter a number: "))  # Step 2: Prompt user for input and convert to integer
    y = 10 / x  # Step 3: Perform division, which may raise a ZeroDivisionError if x is 0
    print("Result:", y)  # Step 4: Print the result of the division


#
#
#
#  EXCEPTIONS *--------------
except ValueError:
    # Step 5: Handle ValueError if user input cannot be converted to an integer
    print("Invalid input. Please enter a valid number.") # you will get an error if you type something other than a number

# ✋ WHEN YOU run the code, you will be asked to type something,  typed g:
# Enter a number: g
# OUTPUT:
# Invalid input. Please enter a valid number.
# Execution completed.

    #
    #
    #


except ZeroDivisionError:
    # Step 6: Handle ZeroDivisionError if division by zero occurs
    print("Division by zero is not allowed.")

# ✋ WHEN YOU run the code, you will be asked to type something,  typed 0:
# Enter a number: 0
# OUTPUT:
# Division by zero is not allowed.
# Execution completed.

#
#
#

except Exception as e:
    # Step 7: Handle any other unexpected exceptions
    print("An unexpected error occurred:", e)

#
#
# IF ALL IS OK, then show the 2 last messages
#
#
# ✋ If you enter a correct value, then it will perform the logic, and if everthing is fine, it will give you the calculation and the success messages
# OUTPUT
# Enter a number: 5
# Result: 2.0
# success
# No exceptions occurred.
# Execution completed.
#
else:
    # Step 8: Execute if no exceptions occurred in the try block
    print(" ✅ No exceptions occurred.")

finally:
    # Step 9: Always execute, regardless of whether exceptions occurred or not
    print("  ✅ Execution completed.")

```

<br>

#### ✋ javascript

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

<br>
<br>

### ✋ react

#### class & arrow function

> **State Handling:** In functional components, state is managed using the useState hook, unlike class components where state is managed via this.state.

> **Lifecycle Methods:** Error boundaries in functional components do not use lifecycle methods like getDerivedStateFromError. Instead, you directly handle errors within the component's function body [read more HERE / z_lifeCycles-JS_0](../z_lifeCycles-JS_0.md)

```javascript
// CLASS example
//
import React, { Component } from "react";

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Error caught in ErrorBoundary:", error, errorInfo);
    // You can also log the error to a service here
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children;
  }
}

// Usage example:
<ErrorBoundary>
  <MyComponent />
</ErrorBoundary>;
/*


The ErrorBoundary component uses getDerivedStateFromError and componentDidCatch to handle errors thrown in its children components.

If an error occurs, it renders a fallback UI (e.g., "Something went wrong.").


The finally equivalent in React is represented by the regular rendering of this.props.children, which will be rendered regardless of whether an error occurred or not.

*/
//
//
// --------------------
//
// ARROW function
import React, { useState } from "react";

const ErrorBoundary = ({ children }) => {
  //
  //  This functional component uses useState to manage the hasError state.
  const [hasError, setHasError] = useState(false);

  //
  //
  // This arrow function handles errors thrown by its children components. It updates the state hasError to true when an error is caught.
  const componentDidCatch = (error, errorInfo) => {
    console.error("Error caught in ErrorBoundary:", error, errorInfo);
    // You can also log the error to a service here
    setHasError(true);
  };

  //
  //
  //  If hasError is true, it renders a fallback UI (e.g., "Something went wrong."). Otherwise, it renders its children.
  if (hasError) {
    return <h1>Something went wrong.</h1>;
  }

  return children;
};

// Usage example:
const MyComponent = () => {
  // Example of causing an error
  const handleClick = () => {
    throw new Error("An error occurred.");
  };

  return (
    <div>
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
};

const App = () => {
  return (
    <ErrorBoundary>
      <MyComponent />
    </ErrorBoundary>
  );
};

export default App;

/*

ErrorBoundary: This functional component uses useState to manage the hasError state.

componentDidCatch: This arrow function handles errors thrown by its children components. It updates the state hasError to true when an error is caught.

Render logic: If hasError is true, it renders a fallback UI (e.g., "Something went wrong."). Otherwise, it renders its children.




*/
```
