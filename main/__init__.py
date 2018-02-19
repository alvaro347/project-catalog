from flask import Flask
app = Flask(__name__)
app.secret_key = 'project-catalog-key'
@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
if __name__ == "__main__":
    app.run()
