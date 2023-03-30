from flask import Flask,request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from wtforms import validators
import string
from random import choice
import os


app=Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db = SQLAlchemy(app)
Migrate(app, db)


class URL(db.Model):
    __tablename__='links'
    id= db.Column(db.Integer, primary_key= True)
    long= db.Column(db.Text)
    short= db.Column(db.Text)

    def __init__(self,long,short):
        self.long= long
        self.short= short


def shortURL(char):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(char))




@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        long_url= request.form.get('url') 
        current = URL.query.filter_by(long=long_url).first()
        if current:
            return render_template('index.html', error=0, final=current.short)
        else:
            if validators.url(long_url):
                while True:
                    shortLink = shortURL(3)
                    short = URL.query.filter_by(short=shortLink).first()
                    if not short:
                        link=URL(long_url,shortLink)
                        db.session.add(link)
                        db.session.commit()
                        return render_template('index.html',error=0,final=shortLink)
            else:
                return render_template('index.html',error=1)
    return render_template("index.html")


@app.route('/history',methods=["GET","POST"])
def history():
    link=URL.query.all()
    return render_template("history.html", history=link)


@app.route('/<final>')
def redirection(final):
    full_URL = URL.query.filter_by(short=final).first()
    if full_URL:
        return redirect(full_URL.long)
    else:
        return f'<h1>URL does not Exists</h1>'


@app.route('/delete/<int:id>')
def delete(id):
    item = URL.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/history')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)