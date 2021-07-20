from app.model.town import Town


def get_towns(parish_id):
    return [(town.id, town.name) for town in Town.query.filter_by(parish_id=parish_id).all()]

