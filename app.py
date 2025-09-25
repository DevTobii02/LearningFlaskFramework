from flask import Flask, render_template

app = Flask(__name__)
posts = [  #Dictionary to store post details in key and value pair
    {
        'author': 'Tobii Dev',
        'title': 'My first post',
        'content': 'My first post content',
        'date_posted': 'April 5, 2018'
    },
    {
        'author': 'Tobi Dev',
        'title': 'My first post 1',
        'content': 'My first post content 1',
        'date_posted': 'April 5, 2020'
    }
]
@app.route('/')
def startflask():
    # return 'Hello World!, I Am LearningFlaskFramework'
    # Changed 'post=posts' to 'posts=posts' to match the variable used in the template
    return  render_template("index.html", posts=posts) #renders the index.html page

@app.route("/about")
def aboutpage():
    return render_template("about.html")
if __name__ == '__main__':
    app.run(debug=True)