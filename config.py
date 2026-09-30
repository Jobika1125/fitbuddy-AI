"""Constants: model settings, activity levels, workout plans, meals."""
MODEL = "claude-sonnet-5-5"
API_URL = "https://api.anthropic.com/v1/messages"

ACTIVITY = {"1": ("Sedentary", 1.2), "2": ("Light", 1.375), "3": ("Moderate", 1.55), "4": ("Very active", 1.725)}
GOALS = ["lose weight", "maintain", "gain muscle"]
PLANS = {
    "lose weight": ["Mon: 30 min brisk walk + core", "Tue: Full-body circuit (squats, pushups, planks)",
                    "Wed: Rest / stretching", "Thu: 30 min cycling or jog", "Fri: Full-body circuit",
                    "Sat: Long walk or swim (45 min)", "Sun: Rest"],
    "maintain": ["Mon: Upper body", "Tue: 30 min cardio", "Wed: Lower body", "Thu: Rest / yoga",
                 "Fri: Full-body", "Sat: Sports / walk", "Sun: Rest"],
    "gain muscle": ["Mon: Chest + triceps", "Tue: Back + biceps", "Wed: Legs + core", "Thu: Rest",
                    "Fri: Shoulders + arms", "Sat: Full-body strength", "Sun: Rest"],
}
MEALS = {
    "veg": {"Breakfast": ["Idli/dosa (3) + sambar + chutney", "Vegetable upma + sprouts", "Oats + banana + nuts"],
            "Lunch": ["Rice/chapati + dal + poriyal + curd", "Millet rice + sambar + keerai", "Paneer/soya curry + chapati + salad"],
            "Snack": ["Sundal / roasted chana", "Fruit + almonds", "Buttermilk + peanuts"],
            "Dinner": ["2 chapati + veg kurma", "Ragi dosa + chutney", "Veg soup + paneer/tofu stir-fry"]},
    "nonveg": {"Breakfast": ["Egg omelette + 2 toast", "Idli (3) + egg + sambar", "Oats + milk + banana"],
               "Lunch": ["Rice + lean chicken curry + poriyal", "Fish curry + rice + keerai", "Chapati + egg curry + salad"],
               "Snack": ["Boiled eggs (2)", "Sundal / roasted chana", "Fruit + nuts"],
               "Dinner": ["Grilled chicken + veg + 1 chapati", "Fish fry + salad + soup", "Egg bhurji + 2 chapati"]},
}
SPLIT = {"Breakfast": 0.25, "Lunch": 0.35, "Snack": 0.10, "Dinner": 0.30}
