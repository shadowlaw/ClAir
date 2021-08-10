from flask import current_app
from app.blueprints.main.model.pollutant import Pollutant
from app.blueprints.main.model.town_pollutant import TownPollutant

WEIGHTINGS = {
    3: [.40, .35, .25],
    2: [.60, .40]
}


def calculate_weighted_aq(town_id):
    pollutants = Pollutant.query.all()
    town_weighted_aq = list()
    min_date, max_date = None, None

    for pollutant in pollutants:
        town_pollutants = TownPollutant.query.filter_by(town_id=town_id, pollutant_id=pollutant.id).order_by(
            TownPollutant.collection_date.desc()).limit(3).all()

        if not town_pollutants:
            continue

        min_date = earlier_date(min_date, town_pollutants[len(town_pollutants) - 1])
        max_date = later_date(max_date, town_pollutants[0])

        if len(town_pollutants) == 1:
            town_pollutant = town_pollutants[0]
            town_weighted_aq.append({'name': town_pollutant.pollutant_id, 'value': float(town_pollutant.pollutant_level)})
            continue

        weights = WEIGHTINGS[len(town_pollutants)]
        pollutant_weighted_average = 0

        for index, town_pollutant in enumerate(town_pollutants):
            pollutant_weighted_average += float(town_pollutant.pollutant_level) * weights[index]

        town_weighted_aq.append({'name': pollutant.id, 'value': pollutant_weighted_average})

    return town_weighted_aq, get_date_range(min_date, max_date) if len(town_weighted_aq) > 0 else ''


def earlier_date(min_date, town_pollutant):
    if min_date is None:
        min_date = town_pollutant.collection_date
    else:
        min_date = town_pollutant.collection_date if town_pollutant.collection_date < min_date else min_date

    return min_date


def later_date(max_date, town_pollutant):
    if max_date is None:
        max_date = town_pollutant.collection_date
    else:
        max_date = town_pollutant.collection_date if town_pollutant.collection_date > max_date else max_date
    return max_date


def get_date_range(min_date, max_date):

    if max_date == min_date:
        return str(min_date.strftime(current_app.config['DISPLAY_DATE_FORMAT']))

    return str(max_date.strftime(current_app.config['DISPLAY_DATE_FORMAT'])) + ' - ' + str(min_date.strftime(
        current_app.config['DISPLAY_DATE_FORMAT']))
