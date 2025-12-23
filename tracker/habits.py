"""Habit tracking logic for AI learning."""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


class HabitTracker:
    """Track learning habits, streaks, and achievements."""

    def __init__(self, data_file: Path):
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self) -> dict:
        """Load data from file or create new."""
        if self.data_file.exists():
            with open(self.data_file) as f:
                return json.load(f)
        return {
            "activities": [],
            "xp": 0,
            "achievements": [],
            "streak_data": {
                "current": 0,
                "longest": 0,
                "last_activity_date": None,
            },
        }

    def _save_data(self):
        """Save data to file."""
        self.data_file.parent.mkdir(exist_ok=True)
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=2, default=str)

    def log_activity(self, description: str, activity_type: str) -> dict:
        """Log a learning activity."""
        today = datetime.now().date().isoformat()

        entry = {
            "description": description,
            "type": activity_type,
            "date": today,
            "timestamp": datetime.now().isoformat(),
        }

        self.data["activities"].append(entry)
        self._update_streak(today)
        self._save_data()

        return entry

    def _update_streak(self, today: str):
        """Update streak based on activity."""
        streak_data = self.data["streak_data"]
        last_date = streak_data["last_activity_date"]

        if last_date is None:
            # First activity ever
            streak_data["current"] = 1
        elif last_date == today:
            # Already logged today, streak unchanged
            pass
        else:
            last = datetime.fromisoformat(last_date).date()
            current = datetime.fromisoformat(today).date()
            diff = (current - last).days

            if diff == 1:
                # Consecutive day - extend streak
                streak_data["current"] += 1
            elif diff > 1:
                # Streak broken
                streak_data["current"] = 1

        streak_data["last_activity_date"] = today

        # Update longest streak
        if streak_data["current"] > streak_data["longest"]:
            streak_data["longest"] = streak_data["current"]

    def get_streak(self) -> int:
        """Get current streak, accounting for today."""
        streak_data = self.data["streak_data"]
        last_date = streak_data["last_activity_date"]

        if last_date is None:
            return 0

        last = datetime.fromisoformat(last_date).date()
        today = datetime.now().date()
        diff = (today - last).days

        if diff == 0:
            # Logged today
            return streak_data["current"]
        elif diff == 1:
            # Yesterday - streak still valid but not extended
            return streak_data["current"]
        else:
            # Streak broken
            return 0

    def get_longest_streak(self) -> int:
        """Get longest streak ever."""
        return self.data["streak_data"]["longest"]

    def add_xp(self, amount: int):
        """Add XP to total."""
        self.data["xp"] += amount
        self._save_data()

    def get_level_info(self) -> tuple[int, int]:
        """Get current level and total XP."""
        xp = self.data["xp"]

        # Level thresholds
        levels = [0, 250, 750, 1500, 3000, 5000, 8000, 12000, 18000, 25000]

        level = 1
        for i, threshold in enumerate(levels):
            if xp >= threshold:
                level = i + 1

        return level, xp

    def get_activities_by_date(self, date: str) -> list:
        """Get activities for a specific date."""
        return [a for a in self.data["activities"] if a["date"] == date]

    def get_activities_by_type(self, activity_type: str) -> list:
        """Get activities by type."""
        return [a for a in self.data["activities"] if a["type"] == activity_type]

    def get_recent_activities(self, days: int = 7) -> list:
        """Get activities from the last N days."""
        cutoff = (datetime.now() - timedelta(days=days)).date().isoformat()
        return [a for a in self.data["activities"] if a["date"] >= cutoff]

    def get_stats(self) -> dict:
        """Get overall statistics."""
        activities = self.data["activities"]

        return {
            "total_readings": len(activities),
            "papers": len([a for a in activities if a["type"] == "paper"]),
            "blogs": len([a for a in activities if a["type"] == "blog"]),
            "videos": len([a for a in activities if a["type"] == "video"]),
            "exercises": len([a for a in activities if a["type"] == "exercise"]),
            "projects": len([a for a in activities if a["type"] == "project"]),
            "total_xp": self.data["xp"],
            "streak": self.get_streak(),
            "longest_streak": self.get_longest_streak(),
            "days_active": len(set(a["date"] for a in activities)),
        }

    def check_achievements(self) -> list[str]:
        """Check for new achievements and return newly unlocked ones."""
        existing = set(self.data["achievements"])
        new_achievements = []

        # First Steps
        if "📖 First Steps" not in existing and len(self.data["activities"]) >= 1:
            new_achievements.append("📖 First Steps")

        # Consistent (3 days in a row)
        if "💪 Consistent" not in existing and self.get_streak() >= 3:
            new_achievements.append("💪 Consistent")

        # Week Warrior
        if "🔥 Week Warrior" not in existing and self.get_streak() >= 7:
            new_achievements.append("🔥 Week Warrior")

        # Month Master
        if "🌟 Month Master" not in existing and self.get_streak() >= 30:
            new_achievements.append("🌟 Month Master")

        # Speed Reader (3 readings in one day)
        today = datetime.now().date().isoformat()
        today_activities = self.get_activities_by_date(today)
        if "🚀 Speed Reader" not in existing and len(today_activities) >= 3:
            new_achievements.append("🚀 Speed Reader")

        # Level achievements
        level, xp = self.get_level_info()
        if "⭐ Level 5" not in existing and level >= 5:
            new_achievements.append("⭐ Level 5")
        if "🏆 Level 10" not in existing and level >= 10:
            new_achievements.append("🏆 Level 10")

        # Add new achievements
        for achievement in new_achievements:
            self.data["achievements"].append(achievement)

        if new_achievements:
            self._save_data()

        return new_achievements

    def get_achievements(self) -> list[str]:
        """Get all unlocked achievements."""
        return self.data["achievements"]

    def get_activity_dates(self) -> set[str]:
        """Get all dates with activity."""
        return set(a["date"] for a in self.data["activities"])

    def reset(self):
        """Reset all data."""
        self.data = {
            "activities": [],
            "xp": 0,
            "achievements": [],
            "streak_data": {
                "current": 0,
                "longest": 0,
                "last_activity_date": None,
            },
        }
        self._save_data()
