# AI FitBuddy 💪

Desktop fitness app: Profile, BMI/calories/diet, workout plan + streak, water tracker,
weight chart, and an AI coach (Claude).

## VS Code la run panra vidham
1. Zip ah **Extract** pannunga.
2. VS Code -> File -> Open Folder -> `fitbuddy_project` folder select pannunga.
3. Python extension install aagalana, VS Code suggest pannum -> Install.
4. `main.py` open pannunga -> top-right la **▶ Run Python File** click pannunga
   (illana Terminal la: `python main.py`, Mac/Linux la `python3 main.py`).

Extra `pip install` thevai illa.

## Requirements
- Python 3.9+ (python.org). Windows/Mac installer la tkinter irukkum.
- Linux la tkinter illana: `sudo apt install python3-tk`

## AI Coach setup (optional)
API key: https://console.anthropic.com. AI Coach tab la paste panni **Save key** click pannunga
(illana `.env.example` ah `.env` nu rename panni key add pannunga).

## Structure
```
main.py                  <- run this
fitbuddy/
  app.py                 main window
  config.py              plans, meals, constants
  storage.py             save/load data, streak
  calculator.py          BMI, BMR, calories, protein, water
  ai_client.py           Claude API call
  tabs/                  profile, overview, workout, water, weight, ai tabs
data/                    your saved data (auto-created)
```
