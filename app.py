from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_www():
    return "Hello World Wide Web!"

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
  
