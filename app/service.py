# service.py
from flask import jsonify, request, abort
from app import app
from flask_sqlalchemy import SQLAlchemy

import uuid
import enum

db = SQLAlchemy(app)

# INGREDIENT CLASS
# class IngredientType(enum.Enum):
#     SYRUP = "Syrup Ingredient"
#     MIXER = "Mixer Ingredient"

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column('ingredient_id', db.String(60), primary_key=True)
    title = db.Column(db.String(60))
    type = db.Column(db.Integer)
    sugar_content = db.Column(db.Integer)

    def __init__(self, title, type, sugarContent):
        self.id = str(uuid.uuid4())
        self.title = title
        self.type = type
        self.sugar_content = sugarContent

    def get_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'type': self.type,
            'sugarContent': self.sugar_content,
        }
    def get_id(self):
        return self.id

# RECIPE CLASS


# Test Route
@app.route('/api/test')
def test():
    return "Hello World!"

def initialize_database():
    app.logger.info('Database is not created, exec create_all() here.')
    db.create_all()
    data1 = Ingredient('Default Soda', 0, 44)
    db.session.add(data1)
    db.session.commit()

@app.route('/api/ingredient/all', methods=['GET'])
def ingredient_get_all():
    try:
        ingredients = Ingredient.query.all()
    except:
        initialize_database()
    return jsonify(ingredients=[ingredient.get_dict() for ingredient in ingredients])

@app.route('/api/ingredient/get', methods=['GET'])
def ingredient_get():
    if request.args:
        ingredient = Ingredient.query.get(request.args.get('id'));
        return jsonify(ingredient.get_dict());
    return abort(422);

# TODO: reject wrong request params
@app.route('/api/ingredient/new',  methods=['POST'])
def ingredient_new():
    if request.json:
        title = request.json['title'];
        type = int(request.json['type']);
        sugarContent = int(request.json['sugarContent'])
        ingredient = Ingredient(title, type, sugarContent)
        db.session.add(ingredient)
        db.session.commit()
        return jsonify(message='success', id=ingredient.get_id())
    return abort(422);