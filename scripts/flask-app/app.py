from flask import Flask, g, render_template, request, flash
import keras
import re
import pickle
import numpy as np

app = Flask(__name__)

app.secret_key='dev'

with app.app_context():
    tokenizer = pickle.load(open('k_glo_raw_tok.pickle', 'rb'))
    model = keras.models.load_model('k_glo_raw.h5')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        body = request.form['body']
        error = None
        body = light_cleaning(body)
        lng = len(body.split())
        if len(body) < 20:
            error = "Ce Tweet n'est pas assez long"
        elif lng < 3:
            error = "Ce Tweet ne contient pas assez de mots significatifs"
        if error is not None:
            flash(error)
        else:
            padded = manual_pad(tokenizer, [body])
            pred = model.predict(padded)
            answer = np.rint(pred)[0][0]
            return render_template('tweet/result.html', answer=answer, pred=pred)
    return render_template('tweet/index.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('tweet/index.html')


def light_cleaning(s):
    s = re.sub('\@\w+', '', s) # Enlèvement des références à d'autres utilisateurs
    s = re.sub('http(s)?[:\/\.\w-]+', '', s) # Enlèvement des URL
    return s


def manual_pad(tknizer, tweets):
    sequences = tknizer.texts_to_sequences(tweets)
    padded = []
    for s in sequences:
        if len(s) > 64:
            padded.append(s[:64])
        else:
            while len(s) < 64:
                s.append(0)
            padded.append(s)
    return padded


if __name__ == '__main__':
    app.run()
