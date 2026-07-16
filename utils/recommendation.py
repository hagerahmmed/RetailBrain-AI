import joblib
from recommend import recommend

rules = joblib.load("models/rules.pkl")

def get_recommendations(products):

    return recommend(products, rules)
