from flask import Flask, render_template, url_for
from funcs import get_thanosquote
import os

app = Flask(__name__)

@app.route('/')
def thanos():
    return render_template(
            'index.html', 
            thanos_quote=get_thanosquote(),
            )
if __name__ == '__main__':
    app.run()