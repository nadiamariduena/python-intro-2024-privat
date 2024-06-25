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
#Flask Route (@app.route('/')): This decorator defines a route for the root URL of the application.

#
#
#
def index():

    # Sample data
    user = {"username": "John", "email": "john@example.com"}
    posts = [
        {
            "author": "Jane", "body": "Beautiful day in Portland"
        },
        {
            "author": "Susan", "body": "The Avengers movie was so cool!"
        }

    ]

    #
    # ✋ RENDER the template with data
    return render_template("index.html", title="Home", user=user, posts=posts)


if __name__ == "__main__":
    app.run(debug=True)

```

<br>

### 🟠 Create a Template:

Save the following HTML as templates/index.html in your project directory:

<br>

```html
<!-- templates/index.html

Jinja2 Templating: Inside index.html, Jinja2 syntax ({{ ... }} and {% ... %}) is used to insert Python variables (title, user.username, user.email, posts) dynamically into the HTML structure. For example, {{ user.username }} inserts the value of user.username into the HTML output.


-->
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>{{title}}</title>
  </head>
  <!--  -->
  <body>
    <h1>Hello, {{ user.username}}</h1>
    <h2>Email: {{ user.email }}</h2>

    <h3>Recent Posts:</h3>
    <ul>
      <!--
🔴
In Jinja2, templating engine used with Python web frameworks like Flask and Django, you write loops using {% for %} and {% endfor %} tags to iterate over lists or other iterable objects like dictionaries.

 -->
      {% for post in posts %}
      <li><strong>{{ post.author }}</strong>: {{ post.body }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```
