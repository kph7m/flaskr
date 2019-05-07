from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello_world():
    return "Hello World!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return str(post_id)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080)
