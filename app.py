from flask import Flask
app = Flask(__name__)
#333333333
@app.route('/')
def home():
    return 'Hello World!__1'

@app.route('/test')
def test():
    return 'Hello World!__2'

if __name__ == '__main__':
    app.run()
