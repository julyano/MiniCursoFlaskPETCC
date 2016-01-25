from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index new page'

@app.route('/hello')
def hello():
    return 'hello world!!!!!!!!!!!!!!!!111'

@app.route('/user/<var>')
def show_user_profile(var):
    return 'User %s' %var

if __name__ == '__main__':
   app.run(debug=True)
