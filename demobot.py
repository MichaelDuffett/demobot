# Import flask
from flask import Flask, request

# Create your app (web server)
app = Flask(__name__)


# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    return 'Hello, World!. This is 2019.'

@app.route('ask')
def hello_world():
    name = request.values.get("text")
    return f"Hello {name}. Welcome to NCSS 2019 Group 1!"

if __name__ == '__main__':
    # Start the web server!
    app.run()