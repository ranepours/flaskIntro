from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    html ="""
    <html>
        <body>
            <h1>Home Page!</h1>
            <p>reeeaaaalllyyyy didn't want this empty so here's this</p>
        </body>
    </html>
    """
    return html

@app.route('/welcome')
def welcome():
    html ="""
    <html>
        <body>
            <h1>Welcome!</h1>
        </body>
    </html>
    """
    return html

@app.route('/welcome/home')
def welcome_home():
    html = """
    <html>
        <body>
            <h1>Welcome Home!</h1>
        </body>
    </html>
    """
    return html

@app.route('/welcome/back')
def welcome_back():
    html = """
    <html>
        <body>
            <h1>Welcome Back!</h1>
        </body>
    </html>
    """
    return html