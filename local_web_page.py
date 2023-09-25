from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def home():
    return main.get_top_worldnew()

if __name__ == '__main__':
    app.run(debug=True)
