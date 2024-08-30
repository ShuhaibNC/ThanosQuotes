from flask import Flask, render_template, url_for
from funcs import get_thanosquote, get_img

app = Flask(__name__)

@app.route('/')
def thanos():
    return render_template(
            'index.html', 
            thanos_quote=get_thanosquote(),
            imgg=get_img(), 
            )
if __name__ == '__main__':
    app.run()