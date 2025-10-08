from flask import jsonify, request
from services.cat_services import (
    create_cat, get_cat, get_all_cats,
    delete_cat)


def add_cat():
    try:
        data = request.get_json()
        new_cat = create_cat(data)
        return jsonify(new_cat), 201
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def get_cat_by_id(cat_id):
    cat = get_cat(cat_id)
    if cat:
        return jsonify(cat), 200
    return jsonify({"message": "Cat not found"}), 404


def get_cats():
    cats = get_all_cats()
    if not cats:
        return jsonify([]), 200
    return jsonify(cats), 200


def delete_cat_by_id(cat_id):
    try:
        result = delete_cat(cat_id)
        if result.get("message") == "Cat not found":
            return jsonify(result), 404
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500