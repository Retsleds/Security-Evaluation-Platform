from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def hello_world():
    return 'Welcome to Flask world!'


if __name__ == '__main__':
    app.run(port=8080)
