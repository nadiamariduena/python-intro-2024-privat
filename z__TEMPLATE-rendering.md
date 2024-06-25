## 🟡 TEMPLATE rendering

<br>
<br>

### 🌈Purpose of Template Rendering:

<br>

🔸 **Separation of Concerns:** 💅 Templates separate the presentation (HTML structure and styling) from the application logic (Python code). This makes the codebase cleaner and easier to maintain.

🔸 **Dynamic Content:** Templates allow embedding of dynamic content (like variables, conditionals, loops) within static HTML, enabling the server to generate customized responses for different users or situations.

🔸 **Reuse and Consistency**:

- Templates promote reusability of HTML structures across different pages of a web application while maintaining consistency in design.

<br>

### 🟠 Example using Flask:

<br>

Let's consider a simple Flask application that renders a template using ✋ **Jinja2**, a popular <u>templating engine</u> in Python:

#### 💡 If you have already installed your virtual environment [check this: z\_\_ENV_VIRTUALENV%20](./z__ENV_VIRTUALENV%20.md)

```javascript
pip install Flask

```

<br>

### 🟠 Create a Flask App:

```python
from flask import Flask, render_template

app = Flask(__name__)

# Route to render a TEMPLATE
@app.route("/")
def index():

    # Sample data
    user = {"username": "John", "email": "john@example.com"}
    posts = [
        {
            "author": "Jane", "body": "Beautiful day in Portland"
        },

    ]

```
