<h1 align="center">
  <br>
  <img src="https://github.com/1Tatsumaru1/sentiment-analysis/blob/master/img/techno.png" alt="Application technologies">
  <br>
  Sentiment Analysis
  <br>
</h1>

<h4 align="center">
  Based on this 
  <a href="https://www.kaggle.com/kazanova/sentiment140" target="_blank">Kaggle dataset</a>.
</h4>

![screenshot](https://github.com/1Tatsumaru1/sentiment-analysis/blob/master/img/bert.png)

<p align="center">
  <a href="#description">Description</a> •
  <a href="#contents">Contents</a> •
  <a href="#credits">Credits</a> •
  <a href="#links">Links</a>
</p>

## Description

This project was part of my IA Engineering course at OpenClassrooms. 
The aim was to :<br>
* Analyse the <a href="https://www.kaggle.com/kazanova/sentiment140" target="_blank">Kaggle sentiment-140 dataset</a> and find relevant information in showcased tweets in order to set important settings for the latter parts of the study (n-gramms, vocabulary size, normalization pattern, tokenization length)
* Develop a sentiment analysis model (binary classification) by comparing various model architecures (LSTM, GRU, Bert, etc.) as well as several word embedding technics (Word2Vec & GloVe in our case)
* Develop a final Flask application that directly ships the model (.h5 format)

Here is a flux diagram showing the rough functionning of the application :

![screenshot](https://github.com/1Tatsumaru1/sentiment-analysis/blob/master/img/architecture.png)

## Contents

* **Blog_article** (HTML) : A requirement of this project was to write a word-limited article on the suject
* **Scripts** :
  - **P7_Analysis** : A Jupyter notebook analysing the dataset
  - **P7_Model** : A Jupyter notebook where the various model architecture alternatives are compared, and where the final model is developped
  - **Flask-app** : Contains the app itself as well as the model and tokenizer files : ready to deploy !

## Credits

This project makes use of the following packages:

- [Keras](https://keras.io/)
- [Tensorflow](https://www.tensorflow.org/?hl=fr)
- [Flask](https://pypi.org/project/Flask/)
- [NLTK](https://www.nltk.org/)
- [Scikit-learn](https://scikit-learn.org/stable/index.html)
- [Urllib](https://docs.python.org/3/library/urllib.html)
- [Numpy](https://numpy.org/)
- [Contractions](https://pypi.org/project/pycontractions/)
- [Gensim](https://pypi.org/project/gensim/)
- [Huggingface's transformers (Bert)](https://huggingface.co/docs/transformers)

## Links

> <a href="https://anthony.ledouguet.com"><img src="https://github.com/1Tatsumaru1/azure_reco_api/blob/main/img/world.png" alt="website" width="20" /> anthony.ledouguet.com</a><br>
> <a href="https://github.com/1Tatsumaru1"><img src="https://github.com/1Tatsumaru1/azure_reco_api/blob/main/img/github.png" alt="github" width="20" /> GitHub</a><br>
> <a href="https://www.linkedin.com/in/anthony-le-douguet/"><img src="https://github.com/1Tatsumaru1/azure_reco_api/blob/main/img/linkedin.png" alt="linkedin" width="20" />
LinkedIn</a>
