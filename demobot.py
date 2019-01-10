# Import flask
from flask import Flask

# Create your app (web server)
app = Flask(__name__)


# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    return 'Hello, World!. This is 2019. sd s d'

if __name__ == '__main__':
    # Start the web server!
    app.run()