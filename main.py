# import flask
# print(flask.__version__)
# app = flask(__name__)
# app.run(debug = True)

import flask

app = flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()