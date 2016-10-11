from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home():
    return 'Welcome to home!'

@app.route('/hello')
def hello():
    return 'Hello, Worlsetd python'

@app.route('/imagine')
def imagine():
    return 'I can start now'