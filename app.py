from flask import Flask, render_template, request, Response
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def hello_world():
    return '我想放假！！！！!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return Response(f'Register Successfully! \nA user whose name is [{username}] wanna register. His password is [{password}]')
    return render_template('user_registeration.html')


if __name__ == '__main__':
    app.run(port=8080)
