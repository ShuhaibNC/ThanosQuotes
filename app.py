from flask import Flask, render_template, url_for, Response
from funcs import get_thanosquote, get_img
import requests
import random
import string  # Import string module

app = Flask(__name__)

@app.route('/')
def thanos():
    return render_template(
            'index.html', 
            thanos_quote=get_thanosquote(),
            imgg=get_img(), 
            )
            
@app.route('/pass')
def generate_password():  # Renamed function
    adjresp = requests.get("https://gist.githubusercontent.com/hugsy/8910dc78d208e40de42deb29e62df913/raw/eec99c5597a73f6a9240cab26965a8609fa0f6ea/english-adjectives.txt")
    adj = random.choice(adjresp.text.split('\n'))
    nounresp = requests.get("https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-nouns.txt")
    noun = random.choice(nounresp.text.split("\n"))
    num = str(random.randrange(100))
    punct = random.choice(string.punctuation)
    passw = adj + noun + num + punct
    return Response(passw, mimetype='text/plain')

@app.route('/about')
def about():
    return render_template(
            'about.html', 
            )
            
            
if __name__ == '__main__':
    app.run()