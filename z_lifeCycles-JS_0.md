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

### Functional Component with Error Boundary (using hooks):

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
