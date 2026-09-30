
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from html import escape

app = FastAPI(title="FitBuddy AI")

# Temporary user storage
users = []


@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>FitBuddy AI</title>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: #f0fdf4;
            margin: 0;
            padding: 20px;
            color: #14532d;
        }
        .container {
            max-width: 700px;
            margin: 25px auto;
            background: white;
            padding: 28px;
            border-radius: 18px;
            box-shadow: 0 5px 20px #0001;
        }
        h1 { color: #16a34a; text-align: center; }
        .subtitle { text-align: center; color: #64748b; }
        label {
            display: block;
            margin-top: 15px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 12px;
            margin-top: 7px;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            font-size: 16px;
        }
        button, .link-button {
            display: block;
            width: 100%;
            padding: 14px;
            margin-top: 24px;
            background: #16a34a;
            color: white;
            border: none;
            border-radius: 9px;
            font-size: 17px;
            font-weight: bold;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
        }
        button:hover, .link-button:hover { background: #15803d; }
        #result {
            display: none;
            margin-top: 25px;
            padding: 20px;
            background: #f0fdf4;
            border-radius: 12px;
            line-height: 1.7;
        }
        .note { font-size: 13px; color: #64748b; }
    </style>
</head>
<body>
    <div class="container">
        <h1>💪 FitBuddy AI</h1>
        <p class="subtitle">Your Personal Fitness Planner</p>
        <h2>👤 Your Fitness Profile</h2>
        <p>Enter your details to create a fitness plan.</p>

        <form id="fitnessForm">
            <label>Your Name</label>
            <input name="name" type="text" placeholder="Enter your name" required>

            <label>Age</label>
            <input name="age" type="number" min="13" max="100"
                   placeholder="Enter your age" required>

            <label>Gender</label>
            <select name="gender" required>
                <option value="">Select gender</option>
                <option>Female</option>
                <option>Male</option>
                <option>Other</option>
                <option>Prefer not to say</option>
            </select>

            <label>Height (cm)</label>
            <input name="height" type="number" min="100" max="250"
                   placeholder="e.g. 160" required>

            <label>Weight (kg)</label>
            <input name="weight" type="number" min="25" max="300"
                   step="0.1" placeholder="e.g. 60" required>

            <label>Fitness Goal</label>
            <select name="goal" required>
                <option value="">Select your goal</option>
                <option value="weight_loss">Weight management</option>
                <option value="muscle_gain">Build muscle</option>
                <option value="fitness">Improve fitness</option>
                <option value="healthy">Stay healthy</option>
            </select>

            <label>Activity Level</label>
            <select name="activity" required>
                <option value="">Select activity level</option>
                <option value="beginner">Beginner</option>
                <option value="moderate">Moderately active</option>
                <option value="active">Very active</option>
            </select>

            <button type="submit">🤖 Generate Fitness Plan</button>
        </form>

        <div id="result">
            <h2 id="planTitle"></h2>
            <h3>🏋️ Workout</h3>
            <p id="workout"></p>
            <h3>🥗 Healthy Habits</h3>
            <p id="habits"></p>
            <h3>💧 Water</h3>
            <p id="water"></p>
            <h3>📅 Weekly Goal</h3>
            <p id="weekly"></p>
        </div>

        <a class="link-button" href="/view-all-users">
            👥 View All Users
        </a>

        <p class="note">
            This is a general fitness guide, not medical advice.
            Start gently and consult a healthcare professional if needed.
        </p>
    </div>

    <script>
        const form = document.getElementById("fitnessForm");
        const result = document.getElementById("result");

        form.addEventListener("submit", async function(event) {
            event.preventDefault();

            const data = Object.fromEntries(
                new FormData(form).entries()
            );

            result.style.display = "block";
            document.getElementById("planTitle").textContent =
                "Creating your fitness plan...";

            try {
                const response = await fetch("/generate", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify(data)
                });

                const plan = await response.json();

                if (!response.ok) {
                    throw new Error(plan.detail || "Could not create plan");
                }

                document.getElementById("planTitle").textContent =
                    "🎉 Your Fitness Plan, " + plan.name + "!";
                document.getElementById("workout").textContent = plan.workout;
                document.getElementById("habits").textContent = plan.habits;
                document.getElementById("water").textContent = plan.water;
                document.getElementById("weekly").textContent = plan.weekly;

            } catch (error) {
                document.getElementById("planTitle").textContent =
                    "Error: " + error.message;
            }
        });
    </script>
</body>
</html>
"""


@app.post("/generate")
async def generate_plan(request: Request):
    data = await request.json()

    name = str(data.get("name", "")).strip()
    goal = data.get("goal", "")
    activity = data.get("activity", "")

    try:
        age = int(data.get("age"))
        height = float(data.get("height"))
        weight = float(data.get("weight"))
    except (TypeError, ValueError):
        return JSONResponse(
            {"detail": "Please enter valid age, height and weight."},
            status_code=400
        )

    if not name or not name.replace(" ", "").isalpha():
        return JSONResponse(
            {"detail": "Please enter a valid name using letters."},
            status_code=400
        )

    if not 13 <= age <= 100 or not 100 <= height <= 250 or not 25 <= weight <= 300:
        return JSONResponse(
            {"detail": "Please check your age, height and weight."},
            status_code=400
        )

    if goal == "muscle_gain":
        workout = (
            "Try beginner strength exercises such as wall push-ups, "
            "squats and light resistance exercises, with rest days."
        )
        habits = (
            "Include protein-rich foods, vegetables, fruits "
            "and balanced meals."
        )
    elif goal == "weight_loss":
        workout = (
            "Start with comfortable walking and gentle bodyweight "
            "exercises. Increase activity gradually."
        )
        habits = (
            "Choose balanced meals, vegetables, fruits and appropriate "
            "portions. Avoid crash diets."
        )
    elif goal == "fitness":
        workout = (
            "Combine walking, gentle strength exercises and stretching. "
            "Build up gradually."
        )
        habits = (
            "Eat balanced meals, sleep regularly and take recovery days."
        )
    else:
        workout = (
            "Begin with comfortable walking, light strength exercises "
            "and stretching."
        )
        habits = (
            "Focus on balanced meals, good sleep and consistent "
            "daily movement."
        )

    if activity == "beginner":
        weekly = (
            "Begin with 3 comfortable activity days per week "
            "and rest between strength sessions."
        )
    elif activity == "active":
        weekly = (
            "Plan a varied week with strength, cardio and recovery days. "
            "Avoid overtraining."
        )
    else:
        weekly = (
            "Aim for regular moderate activity across the week, "
            "adjusting to your comfort."
        )

    user_record = {
        "name": name,
        "age": age,
        "gender": str(data.get("gender", "")),
        "height": height,
        "weight": weight,
        "goal": goal,
        "activity": activity
    }

    users.append(user_record)

    return {
        "name": name,
        "workout": workout,
        "habits": habits,
        "water": (
            "Drink water regularly throughout the day, "
            "adjusting for heat and activity."
        ),
        "weekly": weekly
    }


@app.get("/view-all-users", response_class=HTMLResponse)
def view_all_users():
    rows = ""

    for user in users:
        rows += f"""
        <tr>
            <td>{escape(str(user.get('name', '')))}</td>
            <td>{escape(str(user.get('age', '')))}</td>
            <td>{escape(str(user.get('gender', '')))}</td>
            <td>{escape(str(user.get('height', '')))}</td>
            <td>{escape(str(user.get('weight', '')))}</td>
            <td>{escape(str(user.get('goal', '')))}</td>
        </tr>
        """

    if not rows:
        rows = '<tr><td colspan="6">No users found</td></tr>'

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>All FitBuddy Users</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f0fdf4;
                padding: 25px;
                color: #14532d;
            }}
            h1 {{ color: #16a34a; text-align: center; }}
            .container {{
                max-width: 1000px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 15px;
                overflow-x: auto;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: center;
            }}
            th {{ background: #16a34a; color: white; }}
            a {{ color: #15803d; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👥 View All FitBuddy Users</h1>
            <h3>Total Users: {len(users)}</h3>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Height</th>
                    <th>Weight</th>
                    <th>Goal</th>
                </tr>
                {rows}
            </table>
            <p><a href="/">← Back to FitBuddy Home</a></p>
        </div>
    </body>
    </html>
    """