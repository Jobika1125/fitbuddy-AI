"""Health calculations: BMI, BMR, calories, protein, water."""
from .config import ACTIVITY


def calc_targets(p):
    bmi = p["weight"] / (p["height"] / 100) ** 2
    bmr = 10 * p["weight"] + 6.25 * p["height"] - 5 * p["age"] + (5 if p["gender"] == "m" else -161)
    tdee = bmr * ACTIVITY[p["activity"]][1]
    target = tdee - 500 if p["goal"] == "lose weight" else tdee + 300 if p["goal"] == "gain muscle" else tdee
    return bmi, bmr, tdee, target


def bmi_category(bmi):
    return "Underweight" if bmi < 18.5 else "Normal" if bmi < 25 else "Overweight" if bmi < 30 else "Obese"


def protein_goal(p):
    return p["weight"] * (1.6 if p["goal"] == "gain muscle" else 1.2)


def water_goal(p):
    return p["weight"] * 35  # ml/day
