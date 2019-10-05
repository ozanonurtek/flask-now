from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route('/')
def hello():
    return '<h1>Hello World</h1>'


def init_db():
    pass
    # from .models import db
    # Initialize db:
    # db.init_app(app)


if __name__ == "__main__":
    # init_db()
    app.run()
