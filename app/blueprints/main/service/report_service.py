from app.blueprints.main.model.tree import Tree
from app.blueprints.main.model.pollutant import Pollutant
from app.blueprints.main.model.tree_efficacy import TreeEfficacy
from app.blueprints.main.model.town_pollutant import TownPollutant

### Knapsack Problem

def getSafeLevel(pollutant_id):
    pollutant = Pollutant.query.filter_by(id = pollutant_id).first()
    return pollutant.safe_level

def getTrees(pollutant_list):
    trees = []
    for p in pollutant_list:
        trees.append(TreeEfficacy.query.filter_by(pollutant_id = p.pollutant_id).first())
    return trees

# pollutants - A list of TownPollutant Objects
def get_recommendations(square_footage,pollutants):
    results = {} # key: tree_id; value: amount to plant
    square_footage_left = square_footage
    # Sort pollutants in order of how much they exceed safety limit
    pollutants = sorted(pollutants, key=lambda x: x.pollutant_level - getSafeLevel(x.pollutant_id))
    # Remove any pollutant below safety limit
    pollutants = [x for x in pollutants if x.pollutant_level - getSafeLevel(x.pollutant_id) > 0]

    trees = getTrees(pollutants)

    p = {}
    for pollutant in pollutants:
        p[pollutant.pollutant_id] = pollutant.pollutant_level - getSafeLevel(pollutant.pollutant_id)

    def allSafe():
        for k in p.keys():
            if p[k][0] > p[k][1]:
                return False
        return True

    while square_footage_left > 0 or not allSafe():
        pass

def generate_report():
    pass
