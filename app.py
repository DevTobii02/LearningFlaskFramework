from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def startflask():
    # return 'Hello World!, I Am LearningFlaskFramework'
    return  render_template("index.html") #renders the index.html page
if __name__ == '__main__':
    app.run(debug=True)