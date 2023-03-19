from flask import Flask, render_template, url_for
from funcs import get_thanosquote
import os

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

@app.route('/')
def thanos():
    return render_template(
            'index.html', 
            thanos_quote=get_thanosquote(),
            )
app.run()