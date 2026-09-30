"""Main window: creates the tabs and keeps shared data."""
import tkinter as tk
from tkinter import messagebox, ttk

from .storage import DATA_FILE, PROFILE_FILE, load_data, load_json, save_json
from .tabs.ai_tab import AITab
from .tabs.overview_tab import OverviewTab
from .tabs.profile_tab import ProfileTab
from .tabs.water_tab import WaterTab
from .tabs.weight_tab import WeightTab
from .tabs.workout_tab import WorkoutTab


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI FitBuddy 💪")
        self.geometry("640x580")
        self.p = load_json(PROFILE_FILE, {})
        self.d = load_data()
        self.nb = ttk.Notebook(self)
        self.nb.pack(fill="both", expand=True, padx=8, pady=8)
        self.tabs = {}
        for name, cls in (("Profile", ProfileTab), ("Overview", OverviewTab), ("Workout", WorkoutTab),
                          ("Water", WaterTab), ("Weight", WeightTab), ("AI Coach", AITab)):
            self.tabs[name] = cls(self.nb, self)
            self.nb.add(self.tabs[name], text=name)
        self.refresh_all()
        self.nb.select(1 if self.p else 0)

    def has_profile(self):
        if not self.p:
            messagebox.showinfo("FitBuddy", "Mudhala Profile tab la details save pannunga.")
            self.nb.select(0)
        return bool(self.p)

    def save_profile_data(self):
        save_json(PROFILE_FILE, self.p)
        self.refresh_all()

    def save_data(self):
        save_json(DATA_FILE, self.d)
        self.refresh_all()

    def refresh_all(self):
        for tab in self.tabs.values():
            tab.refresh()
