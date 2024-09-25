
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<title> Hello Page </title><p>Hello, World!</p>"

if __name__ == '__main__':
   app.run()
