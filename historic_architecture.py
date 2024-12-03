# Let's create a simple web app that showcases some historic Friendly Society architecture.
# We'll use Flask, a popular web framework for Python, to create a simple website.

from flask import Flask, render_template_string

# First, we create a list of buildings with basic information about them.
# This is our data that we will display to the user.

buildings = [
    {"name": "Mission to Seafarers Building", "location": "Melbourne, Victoria", "year": 1917, "description": "A heritage building offering support to seafarers since the early 20th century."},
    {"name": "Manchester Unity Building", "location": "Melbourne, Victoria", "year": 1932, "description": "An iconic building created by the Manchester Unity Independent Order of Oddfellows."},
    {"name": "Ancient Order of Foresters Hall", "location": "Sydney, New South Wales", "year": 1880, "description": "Used by the Foresters society, offering social aid and community support."},
]

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    # HTML template for displaying the buildings
    template = '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Historic Friendly Society Architecture</title>
      </head>
      <body>
        <h1>Historic Friendly Society Architecture</h1>
        <ul>
          {% for building in buildings %}
            <li>
              <strong>{{ building.name }}</strong> - Located in {{ building.location }} (Year Built: {{ building.year }})<br>
              Description: {{ building.description }}
            </li>
          {% endfor %}
        </ul>
      </body>
    </html>
    '''
    # Render the HTML template with the buildings data
    return render_template_string(template, buildings=buildings)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
