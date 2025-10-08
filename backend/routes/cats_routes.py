from flask import Blueprint
from controllers.cat_controller import *

cats_routes = Blueprint("cats_routes", __name__)


@cats_routes.route('/cats', methods=['POST'])
def create_cat():
    return add_cat()


@cats_routes.route('/cats', methods=['GET'])
def list_cats():
    return get_cats()


@cats_routes.route('/cats/<int:cat_id>', methods=['GET'])
def list_cat_by_id(cat_id):
    return get_cat_by_id(cat_id)


@cats_routes.route('/cats/<int:cat_id>', methods=['DELETE'])
def remove_cat_by_id(cat_id):
    return delete_cat_by_id(cat_id)