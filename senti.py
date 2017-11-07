from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///senti.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/language')
def language():
    return render_template('language.html')

@app.route('/annotate')
def annotate():
    return render_template('annotate.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

class Sentence(db.Model):
    """model for one of your table"""
    __tablename__ = 'sentence'
    # define your model
    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.String)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'))

class Language(db.Model):
    __tablename__ = 'language'
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String)

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentence.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sentiment_id = db.Column(db.Integer, db.ForeignKey('sentiment.id'))

class Sentiment(db.Model):
    __tablename__ = 'sentiment'
    id = db.Column(db.Integer, primary_key=True)
    sentiment = db.Column(db.String, index=True, unique=True)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

class Source(db.Model):
    __tablename__ = 'source'
    id = db.Column(db.Integer, primary_key=True)

class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True)

if __name__ == '__main__':
    app.run()
