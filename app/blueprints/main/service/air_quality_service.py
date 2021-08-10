from app.blueprints.main.model.pollutant import Pollutant
from app.blueprints.main.model.town_pollutant import TownPollutant

WEIGHTINGS = {
    3: [.40, .35, .25],
    2: [.60, .40]
}


def calculate_weighted_aq(town_id):
    pollutants = Pollutant.query.all()
    town_weighted_aq = list()

    for pollutant in pollutants:
        town_pollutants = TownPollutant.query.filter_by(town_id=town_id, pollutant_id=pollutant.id).order_by(
            TownPollutant.collection_date.desc()).limit(3).all()

        if not town_pollutants:
            continue

        if len(town_pollutants) == 1:
            town_pollutant = town_pollutants[0]
            town_weighted_aq.append({'name': town_pollutant.pollutant_id, 'value': float(town_pollutant.pollutant_level)})
            continue

        weights = WEIGHTINGS[len(town_pollutants)]
        pollutant_weighted_average = 0

        for index, town_pollutant in enumerate(town_pollutants):
            pollutant_weighted_average += float(town_pollutant.pollutant_level) * weights[index]

        town_weighted_aq.append({'name': pollutant.id, 'value': pollutant_weighted_average})

    return town_weighted_aq
