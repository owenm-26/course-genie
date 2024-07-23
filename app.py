# core file for flask app
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Owen! You are my world ;)'

# main driver function
if __name__ == '__main__':
    app.run()