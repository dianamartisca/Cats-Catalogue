from models import Cat, db


def create_cat(data):
    name = data.get("name")

    if not name:
        raise ValueError("Name cannot be empty")
    if len(name) < 2:
        raise ValueError("Name must be at least 2 characters long.")

    cat = Cat(name=name)
    db.session.add(cat)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

    return {
        "id": cat.id,
        "name": cat.name,
        "created_at": cat.created_at
    }

def get_cat(cat_id):
    cat = db.session.get(Cat, cat_id)
    if not cat:
        return None

    return {
        "id": cat.id,
        "name": cat.name,
        "created_at": cat.created_at
    }


def get_all_cats():
    cats = Cat.query.all()
    if not cats:
        return []

    return [{
        "id": cat.id,
        "name": cat.name,
        "created_at": cat.created_at
    } for cat in cats]


def delete_cat(cat_id):
    cat = db.session.get(Cat, cat_id)

    if not cat:
        return {"message": "Cat not found"}

    db.session.delete(cat)

    try:
        db.session.commit()
        return {"message": "Cat deleted successfully"}
    except Exception as e:
        db.session.rollback()
        raise e