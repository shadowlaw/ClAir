from app import db
from app.blueprints.main.model.tree import Tree
from app.blueprints.main.model.pollutant import Pollutant
from app.blueprints.main.model.tree_efficacy import TreeEfficacy
from app.blueprints.main.model.town_pollutant import TownPollutant

from app.blueprints.report.model.report import Report
from app.blueprints.report.model.targeted_pollutants import TargetedPollutant, TargetedPollutantEnum
from app.blueprints.report.model.report_detail import ReportDetail

from app.blueprints.planning_application.model.planning_application import PlanningApplication

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
    results = {} # key: tree_id; value: [amount to plant, pollutant targeted]
    square_footage_left = square_footage
    # Known pollutants in order of severity
    priority = {"O3" : 6, "PM25" : 5, "PM10": 4, "NO2": 3, "CO": 2, "SO2": 1, "AQI": 0}
    # Sort pollutants in order of severity
    pollutants = sorted(pollutants, key=lambda x: priority[x.pollutant_id], reverse=True)
    # Remove any pollutant below safety limit
    pollutants = [x for x in pollutants if x.pollutant_level - getSafeLevel(x.pollutant_id) > 0 and x.pollutant_id != 'AQI']

    # To keep track of how much pollutant levels exceed safe levels
    p = {}
    for pollutant in pollutants:
        p[pollutant.pollutant_id] = pollutant.pollutant_level - getSafeLevel(pollutant.pollutant_id)

    # All the pollutants present below safe levels
    def allSafe():
        for k in p.keys():
            if p[k] >= 0:
                return False
        return True

    # Return tree with the best efficacy for any pollutant
    def getBestTree(pollutant_id):
        e = TreeEfficacy.query.filter_by(pollutant_id=pollutant_id).all()
        chosen = max(e, key=lambda x: x.effectiveness)
        return Tree.query.filter_by(id=chosen.tree_id).first()

    while square_footage_left > 0 or not allSafe():

        if square_footage_left <= 0:
            break

        for pollutant in pollutants:
            if pollutant.pollutant_id == 'AQI':
                continue

            f = Pollutant.query.filter_by(id=pollutant.pollutant_id).first()
            best_tree = getBestTree(pollutant.pollutant_id)
            square_footage_left -= best_tree.space_required

            # If the tree found exceeds the space requirements STOP
            if square_footage_left < 0:
                square_footage_left = 0
                break

            # Get all the pollutants the tree is effective against
            all_tree_pollutants = TreeEfficacy.query.filter_by(tree_id=best_tree.id).all()

            # Reduce the pollutant levels in the dict
            for x in all_tree_pollutants:
                if x.pollutant_id in p.keys():
                    p[x.pollutant_id] -= x.effectiveness

            if best_tree.id in results:
                results[best_tree.id][0] += 1
            else:
                results[best_tree.id] = [1, f.id]
    return results, [pollutant.pollutant_id for pollutant in pollutants]


def generate_report(application_id):

    appl = PlanningApplication.query.filter_by(id=application_id).first()

    recc, ol_poll = get_recommendations(appl.square_footage,appl.pollutants)

    report = Report(application_id=application_id)
    db.session.add(report)
    db.session.flush()

    for r in recc.keys():
        details = ReportDetail(report_id=report.id,tree_id=r,quantity=recc[r][0],targeted_pollutant=recc[r][1])
        db.session.add(details)
        db.session.flush()

        t = [te for te in TreeEfficacy.query.filter_by(tree_id = r).all() if te.pollutant_id != recc[r][1] and te.pollutant_id in ol_poll]
        t = sorted(t, key=lambda x: x.effectiveness, reverse=True)
        t = t[:3] if len(t) >=3 else t
        for te in t:
            tp = TargetedPollutant(tree_id = r, targeted_pollutant_id = te.pollutant_id, report_id = report.id, target_type = TargetedPollutantEnum.SECONDARY.value)
            db.session.add(tp)

    db.session.commit()

    return report.id
