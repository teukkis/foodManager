import json
from jsonschema import validate, ValidationError
from flask import Response, request, url_for
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from foodManager.models import Ingredient
from foodManager import db
from foodManager.utils.responsebuilder import ResponseBuilder
from foodManager.utils.masonbuilder import MasonBuilder
from foodManager.constants import *

class IngredientCollection(Resource):

    def get(self):
        body = MasonBuilder(items=[])
        ingredients = Ingredient.query.all()
        for ingr in ingredients:
            body["items"].append({"name": ingr.name, "type": ingr.type, "id": ingr.id})
        return Response(json.dumps(body),status=200)

    def post(self):
        pass

class IngredientItem(Resource):

    def get(self, item):
        pass
    def put(self, item):
        pass
    def delete(self, item):
        pass
