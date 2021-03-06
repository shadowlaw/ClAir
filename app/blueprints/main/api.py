from flask import Blueprint, jsonify

from app.blueprints.main.model.parish import Parish
from app.blueprints.main.model.town import Town
from app.blueprints.main.service.air_quality_service import calculate_weighted_aq

main_api = Blueprint("main_api", __name__)


@main_api.route("/town/<parish_id>")
def get_town_by_parish_id(parish_id):
    parish = Parish.query.filter_by(id=parish_id.upper()).first()
    response_object = {"parish_id": parish_id, "content": []}
    if parish:
        response_object["content"] = [{"id": town.id, "name": town.name} for town in parish.towns]
        return jsonify(response_object), 200 if len(parish.towns) != 0 else 204
    return jsonify(response_object), 404


@main_api.route("/town/<string:parish_id>/<string:town_id>/pollutants")
def get_town_pollutants(parish_id, town_id):
    town = Town.query.filter_by(id=town_id.upper(), parish_id=parish_id.upper()).first()
    response_object = {"parish_id": parish_id, "town_id": town_id, "content": []}

    if town:
        response_object["content"], response_object['date_range'] = calculate_weighted_aq(town_id)
        return jsonify(response_object), 200 if len(town.pollutants) != 0 else 204
    return jsonify(response_object), 404


@main_api.after_request
def add_headers(response):
    response.headers['Content-Type'] = 'application/json'

    return response
