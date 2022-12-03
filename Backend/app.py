from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/hacker/VUE App/Backend/flasktodo.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    listd = db.Column(db.Text())
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self,title,listd):
        self.title = title
        self.listd = listd
######################################################################

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id','title','listd','date')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

#####################################################################
# initial page
@app.route('/',methods = ['GET'])
def index():
    all_artciles = Articles.query.all()
    results = articles_schema.dump(all_artciles)
    return jsonify(results)

@app.route('/get/<id>/',methods = ['GET'])
def post_details(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)
######################################################################
# updating

@app.route('/update/<id>/',methods = ['PUT'])
def update_article(id):
    article = Articles.query.get(id)
    title = request.json['title']
    listd = request.json['listd'] 

    
    article.title = title
    article.listd = listd
    
    
    db.session.commit()
    return article_schema.jsonify(article)
#####################################################################
# Deleting

@app.route('/delete/<id>/',methods = ['DELETE'])
def delete_article(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()

    return article_schema.jsonify(article)

#####################################################################

# adding 
@app.route('/add',methods = ['GET','POST'])
def add_articles():
    title = request.json['title']
    listd = request.json['listd']
    
    articles = Articles(title,listd)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)

#####################################################################

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 