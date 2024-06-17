## Life Cycles

- While learning about the [ERROR & Exception Handling](./z__all_mds/25_error%20-Exception-Handling.md) i had to review the Life Cycles from javascript & react

<br>
<br>

---

<br>

### Using functional components with hooks (like useState) is considered the modern way to write React components. It provides a more concise and readable syntax compared to class components, while still allowing for the same error handling capabilities using error boundaries.

<br>

#### State Handling:

In functional components, state is managed using the useState hook, unlike class components where state is managed via this.state.

#### Lifecycle Methods:

Error boundaries in functional components do not use lifecycle methods like getDerivedStateFromError. Instead, you directly handle errors within the component's function body.

<br>

#### Example: Error Handling in React

- Class Component with Error Boundary (using lifecycle methods):

```javascript
import React, { Component } from "react";

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = {
      hasError: false,
      error: null,
      errorInfo: null,
    };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Error caught in ErrorBoundary:", error, errorInfo);
    this.setState({
      hasError: true,
      error: error,
      errorInfo: errorInfo,
    });
  }

  render() {
    if (this.state.hasError) {
      return (
        <div>
          <h1>Something went wrong.</h1>
          <p>{this.state.error && this.state.error.toString()}</p>
          <p>{this.state.errorInfo && this.state.errorInfo.componentStack}</p>
        </div>
      );
    }

    return this.props.children;
  }
}

// Example usage:
class MyComponent extends Component {
  render() {
    // Example of causing an error
    const handleClick = () => {
      throw new Error("An error occurred.");
    };

    return (
      <div>
        <button onClick={handleClick}>Click Me</button>
      </div>
    );
  }
}

class App extends Component {
  render() {
    return (
      <ErrorBoundary>
        <MyComponent />
      </ErrorBoundary>
    );
  }
}

export default App;
```

<br>

## Explanation and Differences:

## 🟠 Class Component (using lifecycle methods):

✋ Lifecycle Method `(componentDidCatch)`: In the class component **ErrorBoundary**, componentDidCatch is used to catch any error thrown by its children components.

```javascript

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = {
      hasError: false,
      error: null,
      errorInfo: null,
    };
  }

```

- It sets the `hasError`, `error`, and `errorInfo` **state** variables to manage and display the error information.

```javascript
//  STATE (before, when there is not issue)
this.state = {
  hasError: false,
  error: null,
  errorInfo: null,
};
```

**State Management:** The state (hasError, error, errorInfo) is managed within the class component using this.state and this.setState.

```javascript
// SETSTATE (when there is issue, so it s TRUE)
this.setState({
  hasError: true,
  error: error,
  errorInfo: errorInfo,
});
```

**Usage of Lifecycle Hooks:** Class components utilize lifecycle hooks (componentDidCatch in this case) to handle errors and manage state changes accordingly.

```javascript
  componentDidCatch(error, errorInfo) {
    console.error("Error caught in ErrorBoundary:", error, errorInfo);
    this.setState({
      hasError: true,
      error: error,
      errorInfo: errorInfo,
    });
  }
```

<br>
<br>

## 🟠 Functional Component with Error Boundary (using hooks):

```javascript
import React, { useState } from "react";

const ErrorBoundary = ({ children }) => {
  const [hasError, setHasError] = useState(false);
  const [error, setError] = useState(null);
  const [errorInfo, setErrorInfo] = useState(null);

  const componentDidCatch = (error, errorInfo) => {
    console.error("Error caught in ErrorBoundary:", error, errorInfo);
    setHasError(true);
    setError(error);
    setErrorInfo(errorInfo);
  };

  if (hasError) {
    return (
      <div>
        <h1>Something went wrong.</h1>
        <p>{error && error.toString()}</p>
        <p>{errorInfo && errorInfo.componentStack}</p>
      </div>
    );
  }

  return children;
};

// Example usage:
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
```

### Functional Component (using hooks):

#### Hook `(useState)`:

- In the functional component ErrorBoundary, useState hooks (**useState** for `hasError`, `error`, and `errorInfo`) are used to manage component state.

<br>

**Direct Error Handling:** Errors are handled directly within the function body of the component.

- 🔺 There are **no lifecycle** methods like `componentDidCatch`.

- **Instead**, errors are caught where they occur (e.g., in event handlers or function bodies).

<br>

**State Management:** State is managed using useState hooks, which provide a more concise and functional approach to managing component state compared to class components.

<br>
<br>

## 🟡 Key Differences:

#### Lifecycle Methods vs Direct Handling:

- Class components with error boundaries use lifecycle methods (componentDidCatch) to catch errors, whereas functional components handle errors directly within the component's function body or via custom error handling logic.

**State Management:** Class components use this.state and this.setState to manage state changes, while functional components use useState and potentially other hooks (useEffect, etc.) to manage state and side effects.

**Component Syntax:** Functional components with hooks offer a more streamlined and modern approach to writing React components, avoiding the use of class syntax and lifecycle methods in favor of functional programming techniques.

<br>
<br>

🌈 In summary, while both approaches achieve error handling in React, functional components with hooks provide a more modern and concise way to handle state and manage component logic, including error handling, compared to traditional class components with lifecycle methods.
